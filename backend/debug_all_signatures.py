#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive PayFast Signature Debugging
Test ALL possible signature combinations
"""

import hashlib
import urllib.parse

def test_all_signature_methods():
    """Test every possible PayFast signature combination"""
    
    # Your exact PayFast credentials
    MERCHANT_ID = '13245841'
    MERCHANT_KEY = 'kzyobsh5zlvrw'
    PASSPHRASE = 'Redeclip5e-8298'
    
    # Base payment data
    base_data = {
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
    
    print("=" * 80)
    print("COMPREHENSIVE PAYFAST SIGNATURE DEBUG")
    print("=" * 80)
    
    signatures = []
    
    # Method 1: Standard with URL encoding
    print(f"\n🔍 Method 1: Standard + URL Encoding")
    data1 = base_data.copy()
    params1 = []
    for key, value in sorted(data1.items()):
        params1.append(f'{key}={urllib.parse.quote_plus(str(value))}')
    sig_string1 = '&'.join(params1) + f'&passphrase={urllib.parse.quote_plus(PASSPHRASE)}'
    sig1 = hashlib.md5(sig_string1.encode()).hexdigest()
    signatures.append(('Method 1 (URL encoded)', sig1))
    print(f"Signature: {sig1}")
    
    # Method 2: No URL encoding
    print(f"\n🔍 Method 2: No URL Encoding")
    data2 = base_data.copy()
    params2 = []
    for key, value in sorted(data2.items()):
        params2.append(f'{key}={value}')
    sig_string2 = '&'.join(params2) + f'&passphrase={PASSPHRASE}'
    sig2 = hashlib.md5(sig_string2.encode()).hexdigest()
    signatures.append(('Method 2 (No encoding)', sig2))
    print(f"Signature: {sig2}")
    
    # Method 3: Include merchant_key in data
    print(f"\n🔍 Method 3: Include merchant_key")
    data3 = base_data.copy()
    data3['merchant_key'] = MERCHANT_KEY
    # Remove merchant_key from signature calculation
    sig_data3 = {k: v for k, v in data3.items() if k != 'merchant_key'}
    params3 = []
    for key, value in sorted(sig_data3.items()):
        params3.append(f'{key}={value}')
    sig_string3 = '&'.join(params3) + f'&passphrase={PASSPHRASE}'
    sig3 = hashlib.md5(sig_string3.encode()).hexdigest()
    signatures.append(('Method 3 (With merchant_key)', sig3))
    print(f"Signature: {sig3}")
    
    # Method 4: Exclude custom fields
    print(f"\n🔍 Method 4: Exclude Custom Fields")
    data4 = {k: v for k, v in base_data.items() if not k.startswith('custom_')}
    params4 = []
    for key, value in sorted(data4.items()):
        params4.append(f'{key}={value}')
    sig_string4 = '&'.join(params4) + f'&passphrase={PASSPHRASE}'
    sig4 = hashlib.md5(sig_string4.encode()).hexdigest()
    signatures.append(('Method 4 (No custom fields)', sig4))
    print(f"Signature: {sig4}")
    
    # Method 5: Only required fields
    print(f"\n🔍 Method 5: Only Required Fields")
    required_data = {
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
    }
    params5 = []
    for key, value in sorted(required_data.items()):
        params5.append(f'{key}={value}')
    sig_string5 = '&'.join(params5) + f'&passphrase={PASSPHRASE}'
    sig5 = hashlib.md5(sig_string5.encode()).hexdigest()
    signatures.append(('Method 5 (Required only)', sig5))
    print(f"Signature: {sig5}")
    
    # Method 6: No passphrase
    print(f"\n🔍 Method 6: No Passphrase")
    params6 = []
    for key, value in sorted(base_data.items()):
        params6.append(f'{key}={value}')
    sig_string6 = '&'.join(params6)  # No passphrase
    sig6 = hashlib.md5(sig_string6.encode()).hexdigest()
    signatures.append(('Method 6 (No passphrase)', sig6))
    print(f"Signature: {sig6}")
    
    # Method 7: Passphrase first
    print(f"\n🔍 Method 7: Passphrase First")
    sig_string7 = f'passphrase={PASSPHRASE}&' + '&'.join(params2)
    sig7 = hashlib.md5(sig_string7.encode()).hexdigest()
    signatures.append(('Method 7 (Passphrase first)', sig7))
    print(f"Signature: {sig7}")
    
    # Method 8: Different field order (PayFast docs order)
    print(f"\n🔍 Method 8: PayFast Documentation Order")
    ordered_data = [
        ('merchant_id', MERCHANT_ID),
        ('merchant_key', MERCHANT_KEY),
        ('return_url', 'https://fletcraft.co.za/payment/success'),
        ('cancel_url', 'https://fletcraft.co.za/payment/cancel'),
        ('notify_url', 'https://fletcraft-software.onrender.com/api/payment/notify/'),
        ('name_first', 'Test'),
        ('name_last', 'Customer'),
        ('email_address', 'test@fletcraft.co.za'),
        ('m_payment_id', 'TEST-123'),
        ('amount', '5.00'),
        ('item_name', 'Test Service'),
        ('item_description', 'Test payment for debugging'),
    ]
    # Remove merchant_key for signature
    sig_data8 = [item for item in ordered_data if item[0] != 'merchant_key']
    params8 = [f'{key}={value}' for key, value in sig_data8]
    sig_string8 = '&'.join(params8) + f'&passphrase={PASSPHRASE}'
    sig8 = hashlib.md5(sig_string8.encode()).hexdigest()
    signatures.append(('Method 8 (Doc order)', sig8))
    print(f"Signature: {sig8}")
    
    print(f"\n" + "=" * 80)
    print("ALL SIGNATURE VARIATIONS:")
    print("=" * 80)
    for i, (method, sig) in enumerate(signatures, 1):
        print(f"{i:2d}. {method:<25} : {sig}")
    
    return signatures

def create_test_html_all():
    """Create HTML test forms for all methods"""
    signatures = test_all_signature_methods()
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PayFast - ALL Signature Methods</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 20px auto; padding: 20px; }
        .method { background: #f8f9fa; padding: 20px; margin: 15px 0; border-radius: 8px; border: 1px solid #ddd; }
        .btn { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin: 5px; }
        .btn:hover { background: #0056b3; }
        h1 { text-align: center; color: #333; }
        .signature { font-family: monospace; background: #e9ecef; padding: 5px; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>🧪 PayFast Signature Testing - ALL METHODS</h1>
    <p><strong>Instructions:</strong> Try each method until one works!</p>
"""
    
    for i, (method, signature) in enumerate(signatures, 1):
        html_content += f"""
    <div class="method">
        <h3>Method {i}: {method}</h3>
        <p>Signature: <span class="signature">{signature}</span></p>
        
        <form action="https://www.payfast.co.za/eng/process" method="post" style="display: inline;">
            <input type="hidden" name="merchant_id" value="13245841">
            <input type="hidden" name="merchant_key" value="kzyobsh5zlvrw">
            <input type="hidden" name="return_url" value="https://fletcraft.co.za/payment/success">
            <input type="hidden" name="cancel_url" value="https://fletcraft.co.za/payment/cancel">
            <input type="hidden" name="notify_url" value="https://fletcraft-software.onrender.com/api/payment/notify/">
            <input type="hidden" name="name_first" value="Test">
            <input type="hidden" name="name_last" value="Customer">
            <input type="hidden" name="email_address" value="test@fletcraft.co.za">
            <input type="hidden" name="m_payment_id" value="TEST-{i}">
            <input type="hidden" name="amount" value="5.00">
            <input type="hidden" name="item_name" value="Test Service">
            <input type="hidden" name="item_description" value="Test payment for debugging">
            <input type="hidden" name="custom_str1" value="test">
            <input type="hidden" name="custom_str2" value="debug">
            <input type="hidden" name="custom_str3" value="Fletcraft">
            <input type="hidden" name="signature" value="{signature}">
            <button type="submit" class="btn">🚀 Test Method {i}</button>
        </form>
    </div>"""
    
    html_content += """
</body>
</html>"""
    
    with open('test_all_payfast_methods.html', 'w') as f:
        f.write(html_content)
    
    print(f"\n✅ Created test_all_payfast_methods.html with {len(signatures)} methods to test!")

if __name__ == "__main__":
    create_test_html_all() 