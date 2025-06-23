#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix PayFast Signature Generation
Generate the correct signature for PayFast
"""

import hashlib
import urllib.parse

def generate_payfast_signature():
    """Generate correct PayFast signature"""
    
    # Your exact PayFast credentials
    MERCHANT_ID = '13245841'
    MERCHANT_KEY = 'kzyobsh5zlvrw'
    PASSPHRASE = 'Redeclip5e-8298'
    
    # Test payment data (matching the HTML form)
    payment_data = {
        'merchant_id': MERCHANT_ID,
        'return_url': 'https://fletcraft.co.za/payment/success',
        'cancel_url': 'https://fletcraft.co.za/payment/cancel',
        'notify_url': 'https://fletcraft-software.onrender.com/api/payment/notify/',
        'name_first': 'Test',
        'name_last': 'Customer',
        'email_address': 'test@fletcraft.co.za',
        'm_payment_id': 'TEST-123',
        'amount': '5.00',
        'item_name': 'Test Service',
        'item_description': 'Test payment for debugging',
        'custom_str1': 'test',
        'custom_str2': 'debug',
        'custom_str3': 'Fletcraft',
    }
    
    print("=" * 60)
    print("PayFast Signature Generation Fix")
    print("=" * 60)
    
    print(f"\nUsing credentials:")
    print(f"Merchant ID: {MERCHANT_ID}")
    print(f"Merchant Key: {MERCHANT_KEY[:5]}...{MERCHANT_KEY[-3:]}")
    print(f"Passphrase: {PASSPHRASE[:5]}...{PASSPHRASE[-3:]}")
    
    # Method 1: PayFast standard method (exclude merchant_key, include passphrase)
    print(f"\n=== Method 1: Standard PayFast Signature ===")
    signature_data = {k: v for k, v in payment_data.items()}  # Don't include merchant_key in signature
    
    # Sort and URL encode
    encoded_params = []
    for key, value in sorted(signature_data.items()):
        encoded_params.append(f'{key}={urllib.parse.quote_plus(str(value))}')
    
    signature_string = '&'.join(encoded_params)
    if PASSPHRASE:
        signature_string += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
    
    signature1 = hashlib.md5(signature_string.encode()).hexdigest()
    print(f"Signature String: {signature_string}")
    print(f"Generated Signature: {signature1}")
    
    # Method 2: Include merchant_key in data, exclude from signature
    print(f"\n=== Method 2: Include merchant_key in data ===")
    data_with_key = payment_data.copy()
    data_with_key['merchant_key'] = MERCHANT_KEY
    
    signature_data2 = {k: v for k, v in data_with_key.items() if k != 'merchant_key'}
    
    encoded_params2 = []
    for key, value in sorted(signature_data2.items()):
        encoded_params2.append(f'{key}={urllib.parse.quote_plus(str(value))}')
    
    signature_string2 = '&'.join(encoded_params2)
    if PASSPHRASE:
        signature_string2 += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
    
    signature2 = hashlib.md5(signature_string2.encode()).hexdigest()
    print(f"Signature String: {signature_string2}")
    print(f"Generated Signature: {signature2}")
    
    # Method 3: No URL encoding (some systems don't encode)
    print(f"\n=== Method 3: No URL Encoding ===")
    simple_params = []
    for key, value in sorted(signature_data.items()):
        simple_params.append(f'{key}={value}')
    
    signature_string3 = '&'.join(simple_params)
    if PASSPHRASE:
        signature_string3 += f'&passphrase={PASSPHRASE}'
    
    signature3 = hashlib.md5(signature_string3.encode()).hexdigest()
    print(f"Signature String: {signature_string3}")
    print(f"Generated Signature: {signature3}")
    
    print(f"\n=== Updated HTML Form ===")
    print("Copy this signature into the HTML form:")
    print(f"Method 1 (Standard): {signature1}")
    print(f"Method 2 (With Key):  {signature2}")
    print(f"Method 3 (No Encode): {signature3}")
    
    return signature1, signature2, signature3

if __name__ == "__main__":
    generate_payfast_signature() 