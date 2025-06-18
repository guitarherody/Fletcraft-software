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
            
            # PayFast configuration - TEMPORARILY USE SANDBOX FOR TESTING
            MERCHANT_ID = '10000100'  # PayFast test merchant ID
            MERCHANT_KEY = '46f0cd694581a'  # PayFast test merchant key
            PAYFAST_URL = 'https://sandbox.payfast.co.za/eng/process'  # Sandbox URL
            PASSPHRASE = 'jt7NOE43FZPn'  # PayFast test passphrase
            
            # Build proper URLs for PayFast
            base_url = 'https://fletcraft.co.za'  # Use your actual domain
            return_url = f'{base_url}/payment/success'
            cancel_url = f'{base_url}/payment/cancel'
            notify_url = 'https://fletcraft-software.onrender.com/api/payment/notify/'
            
            # Split customer name properly
            name_parts = order.customer_name.strip().split(' ') if order.customer_name else ['Customer']
            first_name = name_parts[0]
            last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
            
            # Prepare payment data with all required fields
            payment_data = {
                'merchant_id': MERCHANT_ID,
                'merchant_key': MERCHANT_KEY,
                'return_url': return_url,
                'cancel_url': cancel_url,
                'notify_url': notify_url,
                'name_first': first_name[:50],  # Limit to 50 chars
                'name_last': last_name[:50] if last_name else 'Customer',  # Ensure last name exists
                'email_address': order.customer_email,
                'm_payment_id': str(order.order_id),
                'amount': f'{float(order.amount):.2f}',
                'item_name': order.service.title[:100],  # Limit to 100 chars
                'item_description': (order.service.description[:200] if order.service.description else order.service.title)[:200],
                'custom_str1': str(order.id),
                'custom_str2': order.service.title[:255],
                'custom_str3': 'Fletcraft Software',
                'custom_str4': '',
                'custom_str5': '',
            }
            
            # Add optional fields if available
            if order.customer_phone:
                # Clean phone number (remove spaces, dashes, etc.)
                clean_phone = ''.join(filter(str.isdigit, order.customer_phone))
                if len(clean_phone) >= 10:
                    payment_data['cell_number'] = clean_phone[-10:]  # Last 10 digits
            
            # Remove empty values
            payment_data = {k: v for k, v in payment_data.items() if v}
            
            # Generate signature (EXCLUDE merchant_key from signature calculation)
            signature_data = {k: v for k, v in payment_data.items() if k != 'merchant_key'}
            signature_string = '&'.join([f'{key}={value}' for key, value in sorted(signature_data.items())])
            
            # Add passphrase to signature string if provided
            if PASSPHRASE:
                signature_string += f'&passphrase={PASSPHRASE}'
            
            signature = hashlib.md5(signature_string.encode()).hexdigest()
            payment_data['signature'] = signature
            
            return Response({
                'payment_url': PAYFAST_URL,
                'payment_data': payment_data,
                'order_id': order.order_id,
                'debug_info': {
                    'merchant_id': MERCHANT_ID,
                    'amount': str(order.amount),
                    'signature_string': signature_string,
                    'signature': signature,
                    'first_name': first_name,
                    'last_name': last_name,
                    'return_url': return_url,
                    'notify_url': notify_url
                }
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
            
            # Verify signature - USE SANDBOX CREDENTIALS FOR TESTING
            MERCHANT_KEY = '46f0cd694581a'  # PayFast test merchant key
            PASSPHRASE = 'jt7NOE43FZPn'  # PayFast test passphrase
            signature = payment_data.get('signature', '')
            
            # Remove signature from data for verification (and merchant_key if present)
            data_for_signature = {k: v for k, v in payment_data.items() if k not in ['signature', 'merchant_key']}
            signature_string = '&'.join([f'{key}={value}' for key, value in sorted(data_for_signature.items())])
            
            # Add passphrase to signature string if provided
            if PASSPHRASE:
                signature_string += f'&passphrase={PASSPHRASE}'
            
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
