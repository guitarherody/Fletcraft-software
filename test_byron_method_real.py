#!/usr/bin/env python3
"""
Generate PayFast Payment Using Byron's Method with Real Order Data
"""

import hashlib
import urllib.parse
from collections import OrderedDict

def create_byron_method_payment():
    """Create PayFast payment using Byron's method with real order data"""
    
    # Your exact PayFast credentials
    MERCHANT_ID = '13245841'
    MERCHANT_KEY = 'kzyobsh5zlvrw'
    PASSPHRASE = 'Redeclip5e-8298'
    
    print("🔧 CREATING PAYFAST PAYMENT - BYRON'S METHOD + REAL DATA")
    print("=" * 60)
    
    # Real customer and order data
    customer_name = "Sarah Johnson"
    customer_email = "sarah.johnson@example.com"
    order_id = "ORD-12345"
    amount = "150.00"  # Cybersecurity service
    service_title = "Cybersecurity"
    service_description = "Comprehensive cybersecurity assessment and protection"
    
    # Split customer name
    name_parts = customer_name.strip().split(' ')
    first_name = name_parts[0][:50]
    last_name = (' '.join(name_parts[1:]) if len(name_parts) > 1 else 'Customer')[:50]
    
    # Byron's EXACT form field order with real data
    payment_data = OrderedDict([
        ('merchant_id', MERCHANT_ID),
        ('merchant_key', MERCHANT_KEY),  # Byron INCLUDES this in signature
        ('return_url', 'https://fletcraft.co.za/payment/success'),
        ('cancel_url', 'https://fletcraft.co.za/payment/cancel'),
        ('notify_url', 'https://fletcraft-software.onrender.com/api/payfast/itn/'),
        ('name_first', first_name),
        ('name_last', last_name),
        ('email_address', customer_email[:100]),
        ('m_payment_id', order_id[:100]),
        ('amount', amount),
        ('item_name', service_title[:100]),
        ('item_description', service_description[:200]),
        ('custom_int1', '1'),
        ('custom_str1', f'order_reference_{order_id}'),
        ('custom_str2', 'fletcraft_service'),
        ('custom_str3', 'web_development'),
    ])
    
    print(f"Real order data:")
    print(f"Customer: {customer_name}")
    print(f"Email: {customer_email}")
    print(f"Order ID: {order_id}")
    print(f"Amount: R{amount}")
    print(f"Service: {service_title}")
    
    # Byron's signature method: FORM FIELD ORDER + INCLUDE merchant_key
    encoded_params = []
    for key, value in payment_data.items():
        # URL encode each value like Byron did
        encoded_value = urllib.parse.quote_plus(str(value))
        encoded_params.append(f'{key}={encoded_value}')
    
    # Create signature string in Byron's exact order
    signature_string = '&'.join(encoded_params)
    signature_string += f'&passphrase={PASSPHRASE}'  # Byron adds passphrase at end (not URL encoded)
    
    # Generate MD5 hash exactly like Byron
    signature = hashlib.md5(signature_string.encode()).hexdigest()
    payment_data['signature'] = signature
    
    print(f"\n✅ Generated signature: {signature}")
    print(f"🎯 Method: Byron's form field order + include merchant_key")
    
    # Create HTML test file
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>PayFast Test - Byron's Method + Real Data</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1a73e8;
            text-align: center;
            margin-bottom: 30px;
        }}
        .btn {{
            background: #1a73e8;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 PayFast Test - Byron's Method + Real Data</h1>
        
        <p><strong>Customer:</strong> {customer_name}</p>
        <p><strong>Order:</strong> {order_id}</p>
        <p><strong>Amount:</strong> R{amount}</p>
        <p><strong>Service:</strong> {service_title}</p>
        <p><strong>Method:</strong> Byron's proven field order + include merchant_key</p>
        <p><strong>Signature:</strong> {signature}</p>

        <form action="https://www.payfast.co.za/eng/process" method="post">'''
    
    # Add all form fields
    for key, value in payment_data.items():
        html_content += f'\n            <input type="hidden" name="{key}" value="{value}"/>'
    
    html_content += '''
            
            <button type="submit" class="btn">🚀 Test PayFast Payment with Byron's Method</button>
        </form>
    </div>
</body>
</html>'''
    
    # Write HTML file
    filename = f'test_byron_real_order_{order_id.replace("-", "_").lower()}.html'
    with open(filename, 'w') as f:
        f.write(html_content)
    
    print(f"\n📝 Created test file: {filename}")
    print(f"✅ This uses Byron's EXACT method with real customer data!")
    
    return filename, signature, payment_data

if __name__ == '__main__':
    filename, signature, payment_data = create_byron_method_payment()
    
    print(f"\n📋 SUMMARY:")
    print(f"🔧 Method: Byron's form field order + include merchant_key")
    print(f"📄 Test file: {filename}")
    print(f"🔐 Signature: {signature}")
    print(f"🎯 This should work with PayFast!")
    print(f"\nOpen the file in your browser to test!") 