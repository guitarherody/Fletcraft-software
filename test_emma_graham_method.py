#!/usr/bin/env python3
"""
Test Emma Wilson's order using Graham's EXACT working method
"""

import hashlib
import urllib.parse
from collections import OrderedDict

def test_emma_graham_method():
    """Generate signature for Emma Wilson using Graham's working method"""
    
    print("🔧 TESTING EMMA WILSON WITH GRAHAM'S EXACT METHOD")
    print("=" * 50)
    
    # Emma Wilson's actual order data
    payment_data = OrderedDict([
        ('merchant_id', '13245841'),
        ('merchant_key', 'kzyobsh5zlvrw'),
        ('return_url', 'https://fletcraft.co.za/payment/success'),
        ('cancel_url', 'https://fletcraft.co.za/payment/cancel'),
        ('notify_url', 'https://fletcraft-software.onrender.com/api/payfast/itn/'),
        ('name_first', 'Emma'),
        ('name_last', 'Wilson'),
        ('email_address', 'emma.wilson@example.com'),
        ('m_payment_id', '3d3477ec-e636-42a9-966c-8eefeb531d47'),
        ('amount', '100.00'),
        ('item_name', 'Cybersecurity'),
        ('item_description', 'Comprehensive security solutions to protect your digital assets and maintain data integrity at all times.'),
        # NO cell_number - this was the fix!
        ('custom_int1', '1'),
        ('custom_str1', 'order_reference_3d3477ec-e636-42a9-966c-8eefeb531d47'),
        ('custom_str2', 'fletcraft_service'),
        ('custom_str3', 'web_development'),
    ])
    
    print(f"📋 Payment Data Fields:")
    for key, value in payment_data.items():
        print(f"   {key}: {value}")
    
    # Generate signature using Graham's working method
    encoded_params = []
    for key, value in payment_data.items():
        encoded_value = urllib.parse.quote_plus(str(value))
        encoded_params.append(f'{key}={encoded_value}')
    
    signature_string = '&'.join(encoded_params)
    signature_string += '&passphrase=Redeclip5e-8298'  # Not URL encoded
    
    signature = hashlib.md5(signature_string.encode()).hexdigest().lower()
    
    print(f"\n🔍 Signature Generation:")
    print(f"   Signature String: {signature_string}")
    print(f"   Generated Signature: {signature}")
    
    # Compare with Django output
    django_signature_string = "merchant_id=13245841&merchant_key=kzyobsh5zlvrw&return_url=https%3A%2F%2Ffletcraft.co.za%2Fpayment%2Fsuccess&cancel_url=https%3A%2F%2Ffletcraft.co.za%2Fpayment%2Fcancel&notify_url=https%3A%2F%2Ffletcraft-software.onrender.com%2Fapi%2Fpayfast%2Fitn%2F&name_first=Emma&name_last=Wilson&email_address=emma.wilson%40example.com&m_payment_id=3d3477ec-e636-42a9-966c-8eefeb531d47&amount=100.00&item_name=Cybersecurity&item_description=Comprehensive+security+solutions+to+protect+your+digital+assets+and+maintain+data+integrity+at+all+times.&cell_number=0821234567&custom_int1=1&custom_str1=order_reference_3d3477ec-e636-42a9-966c-8eefeb531d47&custom_str2=fletcraft_service&custom_str3=web_development&passphrase=Redeclip5e-8298"
    django_signature = "19f10d6a6267f1293680b01c02387545"
    
    print(f"\n❌ Django Backend Output (INCORRECT):")
    print(f"   Signature String: {django_signature_string}")
    print(f"   Generated Signature: {django_signature}")
    print(f"   Problem: Contains cell_number=0821234567")
    
    print(f"\n✅ Graham's Method (CORRECT):")
    print(f"   Signature String: {signature_string}")
    print(f"   Generated Signature: {signature}")
    print(f"   Fix: NO cell_number field")
    
    if signature == django_signature:
        print(f"\n✅ SIGNATURES MATCH!")
    else:
        print(f"\n❌ SIGNATURES DON'T MATCH!")
        print(f"   Django needs to remove cell_number field!")
    
    # Create HTML test file using correct method
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emma Wilson - Graham's Method Test</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .container {{ background: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .success {{ background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }}
        .error {{ background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; }}
        .btn {{ background: #007bff; color: white; padding: 12px 24px; border: none; border-radius: 4px; 
                font-size: 16px; cursor: pointer; margin: 10px 0; }}
        .btn:hover {{ background: #0056b3; }}
    </style>
</head>
<body>
    <h1>✅ Emma Wilson - Graham's Working Method</h1>
    
    <div class="container success">
        <h3>✅ Using Graham's Proven Method</h3>
        <p><strong>Customer:</strong> Emma Wilson</p>
        <p><strong>Amount:</strong> R100.00</p>
        <p><strong>Method:</strong> Form field order + NO cell_number</p>
        <p><strong>Signature:</strong> {signature}</p>
    </div>
    
    <div class="container error">
        <h3>❌ Django Backend Issue</h3>
        <p>Django is still adding <code>cell_number=0821234567</code> to the signature!</p>
        <p>This causes signature mismatch errors.</p>
        <p><strong>Django Signature:</strong> {django_signature}</p>
    </div>
    
    <div class="container">
        <h3>💳 Test Payment (Correct Method)</h3>
        <form action="https://www.payfast.co.za/eng/process" method="post">"""
    
    # Add form fields (without cell_number)
    for key, value in payment_data.items():
        html_content += f'\n            <input type="hidden" name="{key}" value="{value}">'
    
    html_content += f'\n            <input type="hidden" name="signature" value="{signature}">'
    html_content += f"""
            <button type="submit" class="btn">
                💳 Pay R100.00 with PayFast (Graham's Method)
            </button>
        </form>
    </div>
</body>
</html>"""
    
    with open('emma_graham_method.html', 'w') as f:
        f.write(html_content)
    
    print(f"\n🌐 Created emma_graham_method.html")
    print(f"   This uses the CORRECT method (no cell_number)")
    print(f"   Test this to confirm Graham's method works for Emma too")

if __name__ == "__main__":
    test_emma_graham_method() 