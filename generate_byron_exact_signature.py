#!/usr/bin/env python3
"""
Generate Byron's EXACT PayFast Signature Method
This recreates Byron's proven working approach
"""

import hashlib
import urllib.parse
from collections import OrderedDict

def generate_byron_signature():
    """Generate signature using Byron's exact method"""
    
    # Your exact PayFast credentials
    MERCHANT_ID = '13245841'
    MERCHANT_KEY = 'kzyobsh5zlvrw'
    PASSPHRASE = 'Redeclip5e-8298'
    
    print("🔧 GENERATING BYRON'S EXACT PAYFAST SIGNATURE")
    print("=" * 60)
    
    # Byron's EXACT form field order (critical!)
    payment_data = OrderedDict([
        ('merchant_id', MERCHANT_ID),
        ('merchant_key', MERCHANT_KEY),  # Byron INCLUDES this in signature
        ('return_url', 'https://www.fletcraft.co.za/payment/success'),
        ('cancel_url', 'https://www.fletcraft.co.za/payment/cance'),
        ('notify_url', 'https://fletcraft-backend.onrender.com/api/payfast/itn/'),
        ('name_first', 'John'),
        ('name_last', 'Doe'),
        ('email_address', 'test@fletcraft.co.za'),
        ('m_payment_id', 'TEST_ORDER_123456'),
        ('amount', '100.00'),
        ('item_name', 'Web Development Service'),
        ('item_description', 'Custom website development and design'),
        ('custom_int1', '1'),
        ('custom_str1', 'order_reference_123'),
        ('custom_str2', 'fletcraft_service'),
        ('custom_str3', 'web_development'),
    ])
    
    print(f"Using Byron's credentials and data:")
    print(f"Merchant ID: {MERCHANT_ID}")
    print(f"Merchant Key: {MERCHANT_KEY[:5]}...{MERCHANT_KEY[-3:]}")
    print(f"Passphrase: {PASSPHRASE[:5]}...{PASSPHRASE[-3:]}")
    
    # Byron's signature method: FORM FIELD ORDER + INCLUDE merchant_key
    encoded_params = []
    for key, value in payment_data.items():
        # URL encode each value like Byron did
        encoded_value = urllib.parse.quote_plus(str(value))
        encoded_params.append(f'{key}={encoded_value}')
    
    # Create signature string in Byron's exact order
    signature_string = '&'.join(encoded_params)
    signature_string += f'&passphrase={PASSPHRASE}'  # Byron adds passphrase at end
    
    print(f"\nByron's signature string:")
    print(f"{signature_string}")
    
    # Generate MD5 hash exactly like Byron
    signature = hashlib.md5(signature_string.encode()).hexdigest()
    
    print(f"\n✅ Generated signature: {signature}")
    print(f"🎯 Byron's signature:    9e805c7f75733df918e2dfd12e293242")
    
    if signature == '9e805c7f75733df918e2dfd12e293242':
        print("🎉 PERFECT! Signature matches Byron's exactly!")
        return signature_string, signature, payment_data
    else:
        print("❌ Signature doesn't match - debugging...")
        
        # Try with URL encoded passphrase
        signature_string2 = '&'.join(encoded_params)
        signature_string2 += f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
        signature2 = hashlib.md5(signature_string2.encode()).hexdigest()
        
        print(f"\nMethod 2 (URL encoded passphrase): {signature2}")
        
        if signature2 == '9e805c7f75733df918e2dfd12e293242':
            print("🎉 Found it! Method 2 with URL encoded passphrase works!")
            return signature_string2, signature2, payment_data
    
    return signature_string, signature, payment_data

if __name__ == '__main__':
    signature_string, signature, payment_data = generate_byron_signature()
    
    print(f"\n📋 BYRON'S METHOD SUMMARY:")
    print(f"1. Use FORM FIELD ORDER (not alphabetical)")
    print(f"2. INCLUDE merchant_key in signature calculation")
    print(f"3. URL encode all values")
    print(f"4. Add passphrase at the end")
    print(f"5. Generate MD5 hash")
    print(f"\nSignature: {signature}")
    
    if signature == '9e805c7f75733df918e2dfd12e293242':
        print("\n✅ SUCCESS! This is Byron's proven working method!")
    else:
        print("\n❌ Need to debug further") 