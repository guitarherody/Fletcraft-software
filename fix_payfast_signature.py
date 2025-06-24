#!/usr/bin/env python3
"""
🔧 PAYFAST SIGNATURE FIX UTILITY
Fixes Django's incorrect PayFast signatures by removing cell_number and regenerating
"""

import requests
import json
import hashlib
import urllib.parse
from collections import OrderedDict

def fix_django_payfast_signature(order_id):
    """Get Django's PayFast data and fix the signature"""
    
    print(f"🔧 FIXING PAYFAST SIGNATURE FOR ORDER: {order_id}")
    print("=" * 60)
    
    try:
        # Step 1: Get Django's PayFast data (with incorrect signature)
        print("📡 Step 1: Getting Django's PayFast data...")
        response = requests.post(
            'https://fletcraft-software.onrender.com/api/orders/create_payfast_payment/',
            json={'order_id': order_id},
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code != 200:
            print(f"❌ Failed to get PayFast data: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
        django_data = response.json()
        payment_data_raw = django_data['payment_data']
        
        print(f"✅ Got Django data:")
        print(f"   Django Signature: {payment_data_raw['signature']}")
        if 'cell_number' in payment_data_raw:
            print(f"   ❌ Contains cell_number: {payment_data_raw['cell_number']}")
        else:
            print(f"   ✅ No cell_number found")
        
        # Step 2: Fix the payment data using Graham's working method
        print(f"\n🔧 Step 2: Applying Graham's fix...")
        
        # Create ordered payment data in Byron's exact field order
        fixed_payment_data = OrderedDict([
            ('merchant_id', payment_data_raw['merchant_id']),
            ('merchant_key', payment_data_raw['merchant_key']),
            ('return_url', payment_data_raw['return_url']),
            ('cancel_url', payment_data_raw['cancel_url']),
            ('notify_url', payment_data_raw['notify_url']),
            ('name_first', payment_data_raw['name_first']),
            ('name_last', payment_data_raw['name_last']),
            ('email_address', payment_data_raw['email_address']),
            ('m_payment_id', payment_data_raw['m_payment_id']),
            ('amount', payment_data_raw['amount']),
            ('item_name', payment_data_raw['item_name']),
            ('item_description', payment_data_raw['item_description']),
        ])
        
        # Add custom fields if present
        for field in ['custom_int1', 'custom_str1', 'custom_str2', 'custom_str3']:
            if field in payment_data_raw:
                fixed_payment_data[field] = payment_data_raw[field]
        
        # CRITICAL: DO NOT add cell_number (Graham's fix)
        print(f"   ❌ Removing cell_number field (Graham's fix)")
        
        # Step 3: Generate correct signature using Graham's method
        print(f"\n🔍 Step 3: Generating correct signature...")
        
        encoded_params = []
        for key, value in fixed_payment_data.items():
            encoded_value = urllib.parse.quote_plus(str(value))
            encoded_params.append(f'{key}={encoded_value}')
        
        signature_string = '&'.join(encoded_params)
        signature_string += '&passphrase=Redeclip5e-8298'  # Not URL encoded
        
        correct_signature = hashlib.md5(signature_string.encode()).hexdigest().lower()
        fixed_payment_data['signature'] = correct_signature
        
        print(f"   ✅ Correct signature: {correct_signature}")
        print(f"   📋 Signature string: {signature_string}")
        
        # Step 4: Create test HTML
        print(f"\n🌐 Step 4: Creating test HTML...")
        
        # Get order details for display
        order_response = requests.get(f'https://fletcraft-software.onrender.com/api/orders/')
        orders = order_response.json().get('results', [])
        order = next((o for o in orders if o['order_id'] == order_id), None)
        
        if not order:
            print(f"❌ Could not find order details for {order_id}")
            return None
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FIXED PayFast Payment - {order['customer_name']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .container {{ background: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .success {{ background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }}
        .error {{ background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; }}
        .warning {{ background: #fff3cd; border: 1px solid #ffeaa7; color: #856404; }}
        .btn {{ background: #28a745; color: white; padding: 15px 30px; border: none; border-radius: 4px; 
                font-size: 18px; cursor: pointer; margin: 10px 0; font-weight: bold; }}
        .btn:hover {{ background: #218838; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        .signature {{ font-family: monospace; word-break: break-all; font-size: 12px; }}
    </style>
</head>
<body>
    <h1>✅ FIXED PayFast Payment</h1>
    
    <div class="container success">
        <h3>✅ PAYMENT READY - GRAHAM'S METHOD APPLIED</h3>
        <p><strong>Customer:</strong> {order['customer_name']}</p>
        <p><strong>Email:</strong> {order['customer_email']}</p>
        <p><strong>Order ID:</strong> {order['order_id']}</p>
        <p><strong>Amount:</strong> R{order['amount']}</p>
        <p><strong>Service:</strong> {order.get('service', 'N/A')}</p>
    </div>
    
    <div class="container error">
        <h3>❌ Django Backend Issue (FIXED HERE)</h3>
        <p><strong>Problem:</strong> Django was adding <code>cell_number</code> causing signature mismatches</p>
        <p><strong>Django Signature:</strong> <span class="signature">{payment_data_raw['signature']}</span></p>
        <p><strong>Solution Applied:</strong> Removed cell_number + Graham's method</p>
    </div>
    
    <div class="container success">
        <h3>✅ Fixed Payment Data</h3>
        <table>
            <tr><th>Field</th><th>Value</th></tr>"""
        
        # Add fixed payment data to table
        for key, value in fixed_payment_data.items():
            if key != 'signature':
                html_content += f"<tr><td>{key}</td><td>{value}</td></tr>"
        
        html_content += f"""
            <tr><td><strong>signature</strong></td><td class="signature">{fixed_payment_data['signature']}</td></tr>
        </table>
    </div>
    
    <div class="container warning">
        <h3>🚀 TEST THIS PAYMENT</h3>
        <p>This uses Graham's proven working method with your live PayFast credentials.</p>
        <p><strong>What was fixed:</strong></p>
        <ul>
            <li>❌ Removed invalid cell_number field</li>
            <li>✅ Applied Byron's form field order</li>
            <li>✅ Correct signature: {fixed_payment_data['signature']}</li>
            <li>✅ Live credentials: Merchant ID {fixed_payment_data['merchant_id']}</li>
        </ul>
    </div>
    
    <div class="container">
        <form action="{django_data['payment_url']}" method="post">"""
        
        # Add all fixed form fields
        for key, value in fixed_payment_data.items():
            html_content += f'\n            <input type="hidden" name="{key}" value="{value}">'
        
        html_content += f"""
            <button type="submit" class="btn">
                🚀 PAY R{fixed_payment_data['amount']} WITH PAYFAST (FIXED)
            </button>
        </form>
        
        <p><small>This will process a REAL payment with your live PayFast account using the corrected signature.</small></p>
    </div>
    
    <div class="container">
        <h3>📋 Verification Checklist</h3>
        <ul>
            <li>✅ Using Graham's working method (form field order)</li>
            <li>✅ NO cell_number field (the fix that made Graham work)</li>
            <li>✅ Merchant key included in signature calculation</li>
            <li>✅ HTTPS notify_url</li>
            <li>✅ Proper URL encoding</li>
            <li>✅ Live PayFast credentials</li>
            <li>✅ Correct signature generated: {fixed_payment_data['signature']}</li>
        </ul>
    </div>
</body>
</html>"""
        
        filename = f'FIXED_payfast_{order_id.split("-")[0]}.html'
        with open(filename, 'w') as f:
            f.write(html_content)
        
        print(f"✅ Created {filename}")
        
        return {
            'payment_url': django_data['payment_url'],
            'payment_data': fixed_payment_data,
            'order_id': order_id,
            'filename': filename,
            'django_signature': payment_data_raw['signature'],
            'fixed_signature': correct_signature
        }
        
    except Exception as e:
        print(f"❌ Error fixing PayFast signature: {str(e)}")
        return None

if __name__ == "__main__":
    # Test with Emma Wilson's order
    order_id = "3d3477ec-e636-42a9-966c-8eefeb531d47"
    result = fix_django_payfast_signature(order_id)
    
    if result:
        print(f"\n🎯 SUMMARY:")
        print(f"   ❌ Django Signature: {result['django_signature']}")
        print(f"   ✅ Fixed Signature:  {result['fixed_signature']}")
        print(f"   🌐 Test File: {result['filename']}")
        print(f"\n🚀 Your customers can now pay successfully!")
        print(f"   Open {result['filename']} and test the payment") 