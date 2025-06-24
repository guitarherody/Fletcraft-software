#!/usr/bin/env python3
"""
Test Graham Smith with Sarah Johnson's WORKING format
"""

import hashlib
import urllib.parse
from collections import OrderedDict

def test_graham_fixed():
    """Test Graham Smith using Sarah Johnson's exact working format"""
    
    MERCHANT_ID = '13245841'
    MERCHANT_KEY = 'kzyobsh5zlvrw'
    PASSPHRASE = 'Redeclip5e-8298'
    
    print("🔧 TESTING GRAHAM SMITH - SARAH JOHNSON'S WORKING FORMAT")
    print("=" * 60)
    
    # Graham's data using Sarah Johnson's EXACT working format
    payment_data = OrderedDict([
        ('merchant_id', MERCHANT_ID),
        ('merchant_key', MERCHANT_KEY),
        ('return_url', 'https://fletcraft.co.za/payment/success'),
        ('cancel_url', 'https://fletcraft.co.za/payment/cancel'),
        ('notify_url', 'https://fletcraft-software.onrender.com/api/payfast/itn/'),
        ('name_first', 'Graham'),
        ('name_last', 'Smith'),
        ('email_address', 'gg@gmail.com'),
        ('m_payment_id', '10a8203b-76c8-4543-96c3-f086a6164188'),
        ('amount', '100.00'),
        ('item_name', 'Cybersecurity'),
        ('item_description', 'Comprehensive cybersecurity assessment and protection'),  # Same as Sarah's
        # NO cell_number field - just like Sarah Johnson!
        ('custom_int1', '1'),
        ('custom_str1', 'order_reference_10a8203b-76c8-4543-96c3-f086a6164188'),
        ('custom_str2', 'fletcraft_service'),
        ('custom_str3', 'web_development'),
    ])
    
    print(f"Graham's FIXED data (Sarah Johnson format):")
    for key, value in payment_data.items():
        print(f"  {key}: {value}")
    
    # Generate signature using Byron's method
    encoded_params = []
    for key, value in payment_data.items():
        encoded_value = urllib.parse.quote_plus(str(value))
        encoded_params.append(f'{key}={encoded_value}')
    
    signature_string = '&'.join(encoded_params)
    signature_string += f'&passphrase={PASSPHRASE}'
    
    signature = hashlib.md5(signature_string.encode()).hexdigest()
    
    print(f"\n✅ Generated signature: {signature}")
    print(f"🎯 Sarah's working sig: cee053490c49471f2c00591102a06ddb")
    print(f"📝 Different signature but same METHOD")
    
    # Create HTML test file
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>PayFast Test - Graham Smith FIXED Format</title>
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
            color: #28a745;
            text-align: center;
            margin-bottom: 30px;
        }}
        .btn {{
            background: #28a745;
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
        <h1>✅ PayFast Test - Graham Smith FIXED</h1>
        
        <p><strong>Customer:</strong> Graham Smith</p>
        <p><strong>Email:</strong> gg@gmail.com</p>
        <p><strong>Order:</strong> 10a8203b-76c8-4543-96c3-f086a6164188</p>
        <p><strong>Amount:</strong> R100.00</p>
        <p><strong>Service:</strong> Cybersecurity</p>
        <p><strong>Format:</strong> Sarah Johnson's WORKING format</p>
        <p><strong>Changes:</strong> ❌ Removed cell_number, ✅ Fixed description</p>
        <p><strong>Signature:</strong> {signature}</p>

        <form action="https://www.payfast.co.za/eng/process" method="post">'''
    
    for key, value in payment_data.items():
        html_content += f'\n            <input type="hidden" name="{key}" value="{value}"/>'
    
    html_content += f'\n            <input type="hidden" name="signature" value="{signature}"/>'
    html_content += '''
            
            <button type="submit" class="btn">🚀 Test Graham Smith FIXED Payment</button>
        </form>
        
        <div style="margin-top: 20px; padding: 15px; background: #d4edda; border-radius: 5px;">
            <h4>✅ Fixed Issues:</h4>
            <ul>
                <li><strong>Removed cell_number:</strong> Invalid format was breaking payment</li>
                <li><strong>Fixed description:</strong> Uses Sarah Johnson's working description</li>
                <li><strong>Same method:</strong> Byron's field order + include merchant_key</li>
                <li><strong>Same format:</strong> Exact structure as Sarah Johnson's working test</li>
            </ul>
        </div>
    </div>
</body>
</html>'''
    
    with open('test_graham_fixed.html', 'w') as f:
        f.write(html_content)
    
    print(f"\n📝 Created test file: test_graham_fixed.html")
    print(f"✅ This should work - matches Sarah Johnson's format exactly!")
    
    return signature

if __name__ == '__main__':
    test_graham_fixed() 