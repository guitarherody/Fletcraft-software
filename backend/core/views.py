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
import urllib.parse
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
            
            # PayFast configuration - Use environment variables for security
            MERCHANT_ID = getattr(settings, 'PAYFAST_MERCHANT_ID', '10000100')  # Fallback to test ID
            MERCHANT_KEY = getattr(settings, 'PAYFAST_MERCHANT_KEY', '46f0cd694581a')  # Fallback to test key
            PAYFAST_URL = getattr(settings, 'PAYFAST_URL', 'https://sandbox.payfast.co.za/eng/process')
            PASSPHRASE = getattr(settings, 'PAYFAST_PASSPHRASE', 'jt7NOE43FZPn')  # Fallback to test passphrase
            
            # Build proper URLs for PayFast
            base_url = getattr(settings, 'FRONTEND_URL', 'https://fletcraft.co.za')
            return_url = f'{base_url}/payment/success'
            cancel_url = f'{base_url}/payment/cancel'
            notify_url = f'{request.build_absolute_uri("/").rstrip("/")}/api/payment/notify/'
            
            # Split customer name properly with validation
            name_parts = order.customer_name.strip().split(' ') if order.customer_name else ['Customer']
            first_name = name_parts[0][:50]  # PayFast limit: 50 chars
            last_name = (' '.join(name_parts[1:]) if len(name_parts) > 1 else 'Customer')[:50]  # PayFast limit: 50 chars
            
            # Prepare payment data with proper field length validation
            payment_data = {
                'merchant_id': MERCHANT_ID,
                'merchant_key': MERCHANT_KEY,
                'return_url': return_url,
                'cancel_url': cancel_url,
                'notify_url': notify_url,
                'name_first': first_name,
                'name_last': last_name,
                'email_address': order.customer_email[:100],  # PayFast limit: 100 chars
                'm_payment_id': str(order.order_id)[:100],  # PayFast limit: 100 chars
                'amount': f'{float(order.amount):.2f}',
                'item_name': order.service.title[:100],  # PayFast limit: 100 chars
                'item_description': (order.service.description[:200] if order.service.description else order.service.title[:200]),  # PayFast limit: 200 chars
                'custom_str1': str(order.id)[:255],  # PayFast limit: 255 chars
                'custom_str2': order.service.title[:255],  # PayFast limit: 255 chars
                'custom_str3': 'Fletcraft Software'[:255],  # PayFast limit: 255 chars
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
            
            # Generate signature using FORM field order (NOT alphabetical as per Byron Adams)
            # Order must match the PayFast form documentation exactly
            signature_data = {k: v for k, v in payment_data.items() if k != 'merchant_key'}
            
            # Use the exact field order from PayFast form documentation
            field_order = [
                'merchant_id', 'merchant_key', 'return_url', 'cancel_url', 'notify_url',
                'name_first', 'name_last', 'email_address', 'm_payment_id', 'amount',
                'item_name', 'item_description', 'custom_str1', 'custom_str2', 'custom_str3',
                'custom_str4', 'custom_str5', 'custom_int1', 'custom_int2', 'custom_int3',
                'custom_int4', 'custom_int5', 'cell_number'
            ]
            
            # Build signature string in proper field order (not alphabetical)
            encoded_params = []
            for field in field_order:
                if field in signature_data and signature_data[field]:
                    encoded_params.append(f'{field}={urllib.parse.quote_plus(str(signature_data[field]))}')
            
            signature_string = '&'.join(encoded_params)
            
            # Add passphrase to signature string if provided
            if PASSPHRASE:
                signature_string += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
            
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
        """Handle PayFast payment notifications (ITN)"""
        try:
            # Get payment data from PayFast
            payment_data = request.POST.dict()
            
            # PayFast configuration - Use environment variables for security
            MERCHANT_KEY = getattr(settings, 'PAYFAST_MERCHANT_KEY', '46f0cd694581a')
            PASSPHRASE = getattr(settings, 'PAYFAST_PASSPHRASE', 'jt7NOE43FZPn')
            
            signature = payment_data.get('signature', '')
            
            # Validate required fields
            required_fields = ['m_payment_id', 'payment_status', 'amount_gross']
            missing_fields = [field for field in required_fields if field not in payment_data]
            if missing_fields:
                return HttpResponse(f'MISSING_FIELDS: {", ".join(missing_fields)}', status=400)
            
            # Remove signature from data for verification (and merchant_key if present)
            data_for_signature = {k: v for k, v in payment_data.items() if k not in ['signature', 'merchant_key']}
            
            # URL encode the values properly for signature verification
            encoded_params = []
            for key, value in sorted(data_for_signature.items()):
                encoded_params.append(f'{key}={urllib.parse.quote_plus(str(value))}')
            
            signature_string = '&'.join(encoded_params)
            
            # Add passphrase to signature string if provided
            if PASSPHRASE:
                signature_string += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
            
            calculated_signature = hashlib.md5(signature_string.encode()).hexdigest()
            
            if signature != calculated_signature:
                return HttpResponse('INVALID_SIGNATURE', status=400)
            
            # Process payment
            order_id = payment_data.get('m_payment_id')
            payment_status = payment_data.get('payment_status')
            payfast_payment_id = payment_data.get('pf_payment_id')
            amount_paid = float(payment_data.get('amount_gross', 0))
            
            try:
                order = Order.objects.get(order_id=order_id)
                
                # Validate amount matches order amount
                if abs(float(order.amount) - amount_paid) > 0.01:  # Allow for small floating point differences
                    return HttpResponse('AMOUNT_MISMATCH', status=400)
                
                # Update order status based on PayFast payment status
                status_mapping = {
                    'COMPLETE': 'paid',
                    'FAILED': 'failed',
                    'CANCELLED': 'cancelled',
                    'PENDING': 'pending'
                }
                
                if payment_status in status_mapping:
                    order.payment_status = status_mapping[payment_status]
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
                else:
                    return HttpResponse(f'UNKNOWN_STATUS: {payment_status}', status=400)
                
            except Order.DoesNotExist:
                return HttpResponse('ORDER_NOT_FOUND', status=404)
                
        except Exception as e:
            # Log the error for debugging
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f'PayFast ITN Error: {str(e)}', exc_info=True)
            return HttpResponse('ERROR', status=500)
