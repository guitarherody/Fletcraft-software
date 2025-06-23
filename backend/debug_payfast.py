#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PayFast Debug Script - Check what data is being sent to PayFast
"""

import os
import sys
import django
import hashlib
import urllib.parse

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
from core.models import Order, Service

def debug_payfast_data():
    """Debug the exact data being sent to PayFast"""
    
    print("=" * 60)
    print("PayFast Debug - Data Being Sent to PayFast")
    print("=" * 60)
    
    # Check recent orders
    print("\n=== Recent Orders ===")
    orders = Order.objects.all().order_by('-created_at')[:3]
    if orders:
        for order in orders:
            print(f"Order {order.order_id}: {order.customer_name} - R{order.amount} - Status: {order.payment_status}")
        
        # Use the most recent order for testing
        test_order = orders[0]
        print(f"\n=== Using Order {test_order.order_id} for Debug ===")
        
        # Generate the exact same data that would be sent to PayFast
        MERCHANT_ID = settings.PAYFAST_MERCHANT_ID
        MERCHANT_KEY = settings.PAYFAST_MERCHANT_KEY
        PAYFAST_URL = settings.PAYFAST_URL
        PASSPHRASE = settings.PAYFAST_PASSPHRASE
        
        # Build URLs
        base_url = settings.FRONTEND_URL
        return_url = f'{base_url}/payment/success'
        cancel_url = f'{base_url}/payment/cancel'
        notify_url = 'https://fletcraft-software.onrender.com/api/payment/notify/'
        
        # Split customer name
        name_parts = test_order.customer_name.strip().split(' ') if test_order.customer_name else ['Customer']
        first_name = name_parts[0][:50]
        last_name = (' '.join(name_parts[1:]) if len(name_parts) > 1 else 'Customer')[:50]
        
        # Build payment data exactly like the view does
        payment_data = {
            'merchant_id': MERCHANT_ID,
            'merchant_key': MERCHANT_KEY,
            'return_url': return_url,
            'cancel_url': cancel_url,
            'notify_url': notify_url,
            'name_first': first_name,
            'name_last': last_name,
            'email_address': test_order.customer_email[:100],
            'm_payment_id': str(test_order.order_id)[:100],
            'amount': f'{float(test_order.amount):.2f}',
            'item_name': test_order.service.title[:100],
            'item_description': (test_order.service.description[:200] if test_order.service.description else test_order.service.title[:200]),
            'custom_str1': str(test_order.id)[:255],
            'custom_str2': test_order.service.title[:255],
            'custom_str3': 'Fletcraft Software'[:255],
            'custom_str4': '',
            'custom_str5': '',
        }
        
        # Add phone if available
        if test_order.customer_phone:
            clean_phone = ''.join(filter(str.isdigit, test_order.customer_phone))
            if len(clean_phone) >= 10:
                payment_data['cell_number'] = clean_phone[-10:]
        
        # Remove empty values
        payment_data = {k: v for k, v in payment_data.items() if v}
        
        print(f"\n=== PayFast Configuration ===")
        print(f"Merchant ID: {MERCHANT_ID}")
        print(f"Merchant Key: {MERCHANT_KEY[:5]}...{MERCHANT_KEY[-3:]}")
        print(f"PayFast URL: {PAYFAST_URL}")
        print(f"Passphrase: {PASSPHRASE[:5]}...{PASSPHRASE[-3:]}")
        
        print(f"\n=== Payment Data Being Sent ===")
        for key, value in payment_data.items():
            if key == 'merchant_key':
                print(f"{key}: {value[:5]}...{value[-3:]}")
            else:
                print(f"{key}: {value}")
        
        # Generate signature
        signature_data = {k: v for k, v in payment_data.items() if k != 'merchant_key'}
        
        # URL encode the values properly
        encoded_params = []
        for key, value in sorted(signature_data.items()):
            encoded_params.append(f'{key}={urllib.parse.quote_plus(str(value))}')
        
        signature_string = '&'.join(encoded_params)
        
        # Add passphrase to signature string if provided
        if PASSPHRASE:
            signature_string += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
        
        signature = hashlib.md5(signature_string.encode()).hexdigest()
        
        print(f"\n=== Signature Generation ===")
        print(f"Signature String Length: {len(signature_string)} characters")
        print(f"Signature String (first 100 chars): {signature_string[:100]}...")
        print(f"Generated Signature: {signature}")
        
        # Check for potential issues
        print(f"\n=== Potential Issues Check ===")
        
        issues = []
        
        # Check merchant ID format
        if not MERCHANT_ID.isdigit():
            issues.append("Merchant ID should be numeric")
        
        # Check amount format
        try:
            amount = float(payment_data['amount'])
            if amount <= 0:
                issues.append("Amount must be greater than 0")
        except:
            issues.append("Invalid amount format")
        
        # Check required fields
        required_fields = ['merchant_id', 'return_url', 'cancel_url', 'notify_url', 'name_first', 'name_last', 'email_address', 'm_payment_id', 'amount', 'item_name']
        for field in required_fields:
            if field not in payment_data or not payment_data[field]:
                issues.append(f"Missing required field: {field}")
        
        # Check email format
        if '@' not in payment_data.get('email_address', ''):
            issues.append("Invalid email format")
        
        if issues:
            print("ISSUES FOUND:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("No obvious issues found with the data")
        
        print(f"\n=== PayFast Account Check ===")
        print("Make sure your PayFast account has:")
        print("1. Correct merchant ID and key configured")
        print("2. ITN URL set to: https://fletcraft-software.onrender.com/api/payment/notify/")
        print("3. Account is verified and active")
        print("4. Payment methods enabled (credit card, etc.)")
        
    else:
        print("No orders found. Please create a test order first.")

if __name__ == "__main__":
    try:
        debug_payfast_data()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc() 