from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
import hashlib
import requests
import json
from .models import Service, TeamMember, Project, Contact, VoiceWork, Order, PaymentTransaction
from .serializers import ServiceSerializer, TeamMemberSerializer, ProjectSerializer, ContactSerializer, VoiceWorkSerializer, OrderSerializer, PaymentTransactionSerializer

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Thank you for your message! We'll get back to you soon."}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoiceWorkViewSet(viewsets.ModelViewSet):
    queryset = VoiceWork.objects.all()
    serializer_class = VoiceWorkSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'])
    def create_payfast_payment(self, request):
        """Create a PayFast payment for an order"""
        try:
            order_id = request.data.get('order_id')
            order = Order.objects.get(order_id=order_id)
            
            # PayFast configuration
            MERCHANT_ID = '13245841'
            MERCHANT_KEY = 'kzyobsh5zlvrw'
            PAYFAST_URL = 'https://www.payfast.co.za/eng/process'  # Use sandbox URL for testing
            
            # Prepare payment data
            payment_data = {
                'merchant_id': MERCHANT_ID,
                'merchant_key': MERCHANT_KEY,
                'return_url': f'{request.build_absolute_uri("/")}payment/success/',
                'cancel_url': f'{request.build_absolute_uri("/")}payment/cancel/',
                'notify_url': f'{request.build_absolute_uri("/")}api/payment/notify/',
                'name_first': order.customer_name.split()[0] if order.customer_name else '',
                'name_last': ' '.join(order.customer_name.split()[1:]) if len(order.customer_name.split()) > 1 else '',
                'email_address': order.customer_email,
                'cell_number': order.customer_phone,
                'm_payment_id': order.order_id,
                'amount': str(order.amount),
                'item_name': order.service.title,
                'item_description': order.service.description[:255],
                'custom_str1': str(order.id),
            }
            
            # Generate signature
            signature_string = '&'.join([f'{key}={value}' for key, value in sorted(payment_data.items())])
            signature = hashlib.md5(signature_string.encode()).hexdigest()
            payment_data['signature'] = signature
            
            return Response({
                'payment_url': PAYFAST_URL,
                'payment_data': payment_data,
                'order_id': order.order_id
            })
            
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PaymentTransactionViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer

    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'])
    def notify(self, request):
        """Handle PayFast payment notifications"""
        try:
            # Get payment data from PayFast
            payment_data = request.POST.dict()
            
            # Verify signature
            MERCHANT_KEY = 'kzyobsh5zlvrw'
            signature = payment_data.get('signature', '')
            
            # Remove signature from data for verification
            data_for_signature = {k: v for k, v in payment_data.items() if k != 'signature'}
            signature_string = '&'.join([f'{key}={value}' for key, value in sorted(data_for_signature.items())])
            calculated_signature = hashlib.md5(signature_string.encode()).hexdigest()
            
            if signature != calculated_signature:
                return HttpResponse('INVALID', status=400)
            
            # Process payment
            order_id = payment_data.get('m_payment_id')
            payment_status = payment_data.get('payment_status')
            payfast_payment_id = payment_data.get('pf_payment_id')
            amount_paid = float(payment_data.get('amount_gross', 0))
            
            try:
                order = Order.objects.get(order_id=order_id)
                
                # Update order status
                if payment_status == 'COMPLETE':
                    order.payment_status = 'paid'
                elif payment_status == 'FAILED':
                    order.payment_status = 'failed'
                elif payment_status == 'CANCELLED':
                    order.payment_status = 'cancelled'
                
                order.payfast_payment_id = payfast_payment_id
                order.save()
                
                # Create payment transaction record
                PaymentTransaction.objects.create(
                    order=order,
                    payfast_payment_id=payfast_payment_id,
                    transaction_status=payment_status,
                    amount_paid=amount_paid,
                    payfast_data=payment_data
                )
                
                return HttpResponse('OK', status=200)
                
            except Order.DoesNotExist:
                return HttpResponse('ORDER_NOT_FOUND', status=404)
                
        except Exception as e:
            return HttpResponse('ERROR', status=500)
