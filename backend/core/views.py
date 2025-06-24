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
            
            # Build proper URLs for PayFast - MATCH HTML TEST EXACTLY
            base_url = getattr(settings, 'FRONTEND_URL', 'https://fletcraft.co.za')
            return_url = f'{base_url}/payment/success'
            cancel_url = f'{base_url}/payment/cancel'
            # CRITICAL: Use exact same notify_url as working HTML test
            notify_url = f'{request.build_absolute_uri("/").rstrip("/")}/api/payfast/itn/'
            
            # Split customer name properly with validation
            name_parts = order.customer_name.strip().split(' ') if order.customer_name else ['Customer']
            first_name = name_parts[0][:50]  # PayFast limit: 50 chars
            last_name = (' '.join(name_parts[1:]) if len(name_parts) > 1 else 'Customer')[:50]  # PayFast limit: 50 chars
            
            # Build payment data in EXACT FORM FIELD ORDER (Byron Adams working solution)
            # This is the EXACT order that Byron used successfully: merchant_id, merchant_key, return_url, etc.
            from collections import OrderedDict
            payment_data = OrderedDict([
                ('merchant_id', MERCHANT_ID),
                ('merchant_key', MERCHANT_KEY),
                ('return_url', return_url),
                ('cancel_url', cancel_url),
                ('notify_url', notify_url),
                ('name_first', first_name),
                ('name_last', last_name),
                ('email_address', order.customer_email[:100]),
                ('m_payment_id', str(order.order_id)[:100]),
                ('amount', f'{float(order.amount):.2f}'),
                ('item_name', order.service.title[:100]),
                ('item_description', (order.service.description[:200] if order.service.description else order.service.title[:200])),
            ])
            
            # Add optional fields in Byron's order if they exist
            if order.customer_phone:
                clean_phone = ''.join(filter(str.isdigit, order.customer_phone))
                if len(clean_phone) >= 10:
                    payment_data['cell_number'] = clean_phone[-10:]
            
            # Add custom fields using Byron's EXACT format with real order data
            payment_data['custom_int1'] = '1'  # Keep Byron's exact format
            # Use Byron's proven format but with real order identifiers
            payment_data['custom_str1'] = f'order_reference_{order.order_id}'[:255]  # Byron's format: "order_reference_XXX"
            payment_data['custom_str2'] = 'fletcraft_service'[:255]                  # Keep Byron's exact working value
            payment_data['custom_str3'] = 'web_development'[:255]                    # Keep Byron's exact working value
            
            # Remove empty values while preserving order
            payment_data = OrderedDict([(k, v) for k, v in payment_data.items() if v])
            
            # Generate signature using Byron's EXACT method (form field order + merchant_key included)
            # This matches Byron's working signature string exactly
            signature_params = []
            for key, value in payment_data.items():
                if key != 'signature':  # Exclude only signature field (include merchant_key like Byron)
                    # PayFast requires URL encoding for signature generation
                    encoded_value = urllib.parse.quote_plus(str(value))
                    signature_params.append(f'{key}={encoded_value}')
            
            # Create signature string exactly like Byron's working example
            signature_string = '&'.join(signature_params)
            if PASSPHRASE:
                # Add passphrase exactly as Byron did
                signature_string += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
            
            # Generate MD5 hash in lowercase exactly like Byron's method
            signature_string = signature_string.strip()
            signature = hashlib.md5(signature_string.encode()).hexdigest().lower()
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
            
            # Remove signature from data for verification 
            data_for_signature = {k: v for k, v in payment_data.items() if k not in ['signature']}
            
            # Use Byron's EXACT signature verification method (same as payment creation)
            # Must match the exact method that generated the original signature
            signature_params = []
            # Use the same field order as Byron's working example
            for key, value in data_for_signature.items():
                # PayFast requires URL encoding for signature verification
                encoded_value = urllib.parse.quote_plus(str(value))
                signature_params.append(f'{key}={encoded_value}')
            
            signature_string = '&'.join(signature_params)
            
            # Add passphrase to signature string if provided
            if PASSPHRASE:
                signature_string += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
            
            # Ensure signature string is trimmed and generate MD5 hash in lowercase
            signature_string = signature_string.strip()
            calculated_signature = hashlib.md5(signature_string.encode()).hexdigest().lower()
            
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
