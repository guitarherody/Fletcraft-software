#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PayFast Live Debug Script - Test exact payload being sent
"""
import hashlib
import urllib.parse
from collections import OrderedDict

# Your LIVE PayFast credentials
MERCHANT_ID = "13245841"
MERCHANT_KEY = "kzyobsh5zlvrw"
PASSPHRASE = "Redeclip5e-8298"
PAYFAST_URL = "https://www.payfast.co.za/eng/process"

def create_test_payload():
    """Create test payload exactly like our Django backend"""
    
    # Build payment data in EXACT order PayFast form expects
    payment_data = OrderedDict([
        ('merchant_id', MERCHANT_ID),
        ('merchant_key', MERCHANT_KEY),
        ('return_url', 'https://fletcraft.co.za/payment/success'),
        ('cancel_url', 'https://fletcraft.co.za/payment/cancel'),
        ('notify_url', 'https://fletcraft.co.za/api/payment/notify/'),
        ('name_first', 'Test'),
        ('name_last', 'Customer'),
        ('email_address', 'test@fletcraft.co.za'),
        ('m_payment_id', 'TEST123456'),
        ('amount', '100.00'),
        ('item_name', 'Web Applications'),
        ('item_description', 'Professional web application development services'),
        ('custom_str1', '1'),
        ('custom_str2', 'Web Applications'),
        ('custom_str3', 'Fletcraft Software'),
    ])
    
    # Remove empty values while preserving order
    payment_data = OrderedDict([(k, v) for k, v in payment_data.items() if v])
    
    # Generate signature using exact field order
    encoded_params = []
    for key, value in payment_data.items():
        if key != 'merchant_key':  # Exclude merchant_key from signature
            encoded_params.append(key + '=' + urllib.parse.quote_plus(str(value)))
    
    signature_string = '&'.join(encoded_params)
    
    # Add passphrase to signature string
    signature_string += '&passphrase=' + urllib.parse.quote_plus(PASSPHRASE)
    
    signature = hashlib.md5(signature_string.encode()).hexdigest()
    payment_data['signature'] = signature
    
    return payment_data, signature_string

def generate_html_form(payment_data):
    """Generate HTML form for manual testing"""
    html = f'''<!DOCTYPE html>
<html>
<head>
    <title>PayFast Debug Test</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .debug {{ background: #f5f5f5; padding: 20px; margin: 20px 0; }}
        .form {{ background: #e8f4fd; padding: 20px; margin: 20px 0; }}
        input {{ margin: 5px 0; padding: 8px; width: 300px; }}
        button {{ background: #007cba; color: white; padding: 12px 24px; border: none; cursor: pointer; }}
    </style>
</head>
<body>
    <h1>PayFast Live Debug Test</h1>
    
    <div class="debug">
        <h3>🔍 Debug Information:</h3>
        <p><strong>Merchant ID:</strong> {payment_data['merchant_id']}</p>
        <p><strong>Amount:</strong> R{payment_data['amount']}</p>
        <p><strong>Signature:</strong> {payment_data['signature']}</p>
        <p><strong>PayFast URL:</strong> {PAYFAST_URL}</p>
    </div>
    
    <div class="form">
        <h3>🚀 Test Form (Auto-submits in 3 seconds):</h3>
        <form action="{PAYFAST_URL}" method="post" id="payfast_form">
'''
    
    for key, value in payment_data.items():
        html += f'            <input type="hidden" name="{key}" value="{value}">\n'
    
    html += '''        </form>
        
        <button onclick="document.getElementById('payfast_form').submit();">
            🔥 Submit to PayFast NOW
        </button>
    </div>
    
    <script>
        // Auto-submit after 3 seconds
        setTimeout(function() {
            console.log('Auto-submitting to PayFast...');
            document.getElementById('payfast_form').submit();
        }, 3000);
    </script>
</body>
</html>'''
    
    return html

if __name__ == "__main__":
    print("🔥 PayFast Live Debug Test")
    print("=" * 50)
    
    # Create test payload
    payment_data, signature_string = create_test_payload()
    
    print("\n📦 PAYMENT DATA:")
    for key, value in payment_data.items():
        print(f"  {key}: {value}")
    
    print(f"\n🔐 SIGNATURE STRING:")
    print(f"  {signature_string}")
    
    print(f"\n✅ SIGNATURE HASH:")
    print(f"  {payment_data['signature']}")
    
    # Generate HTML test file
    html_content = generate_html_form(payment_data)
    
    with open('payfast_live_test.html', 'w') as f:
        f.write(html_content)
    
    print(f"\n🌐 HTML Test File Created: payfast_live_test.html")
    print(f"📋 Open this file in your browser to test PayFast directly!")
    print(f"🎯 This will submit the EXACT same payload as your Django backend")
    
    print("\n" + "=" * 50)
    print("🚨 CRITICAL: If this HTML form also gives 500 error,")
    print("   then the issue is with PayFast account setup or credentials!")
    print("=" * 50) 