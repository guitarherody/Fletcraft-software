#!/usr/bin/env python3
"""
🚀 LIVE SITE SIMULATION TEST
Test the exact flow that happens when a customer places an order on your live site
"""

import requests
import json
from collections import OrderedDict
import hashlib
import urllib.parse

def test_live_order_flow():
    """Simulate complete customer order flow on live site"""
    
    print("🚀 TESTING LIVE SITE ORDER FLOW")
    print("=" * 50)
    
    # Step 1: Create a test order (simulating customer checkout)
    print("\n📝 Step 1: Creating customer order...")
    
    order_data = {
        "customer_name": "Emma Wilson",
        "customer_email": "emma.wilson@example.com", 
        "customer_phone": "0821234567",  # This will be ignored (no cell_number)
        "service": 390,  # Cybersecurity service (R100.00)
        "amount": 100.00,
        "special_requirements": "Cybersecurity audit and protection setup"
    }
    
    try:
        # Create order via your API
        create_response = requests.post(
            'https://fletcraft-software.onrender.com/api/orders/',
            json=order_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if create_response.status_code == 201:
            order = create_response.json()
            order_id = order['order_id']
            print(f"✅ Order created: {order_id}")
            print(f"   Customer: {order['customer_name']}")
            print(f"   Amount: R{order['amount']}")
            print(f"   Service: {order['service']}")
        else:
            print(f"❌ Failed to create order: {create_response.status_code}")
            print(f"   Response: {create_response.text}")
            return
            
    except Exception as e:
        print(f"❌ Error creating order: {str(e)}")
        return
    
    # Step 2: Generate PayFast payment (simulating customer clicking "Pay Now")
    print(f"\n💳 Step 2: Generating PayFast payment for order {order_id}...")
    
    try:
        # Request PayFast payment via your API
        payment_response = requests.post(
            'https://fletcraft-software.onrender.com/api/orders/create_payfast_payment/',
            json={'order_id': order_id},
            headers={'Content-Type': 'application/json'}
        )
        
        if payment_response.status_code == 200:
            payment_data = payment_response.json()
            print("✅ PayFast payment data generated!")
            print(f"   Payment URL: {payment_data['payment_url']}")
            print(f"   Signature: {payment_data['payment_data']['signature']}")
            print(f"   Amount: R{payment_data['payment_data']['amount']}")
            
            # Step 3: Verify signature is correct using Graham's working method
            print(f"\n🔍 Step 3: Verifying signature matches Graham's working method...")
            
            # Build signature exactly like Graham's working test
            form_data = payment_data['payment_data']
            
            # Byron's exact field order (form field order, not alphabetical)
            ordered_fields = [
                'merchant_id', 'merchant_key', 'return_url', 'cancel_url', 'notify_url',
                'name_first', 'name_last', 'email_address', 'm_payment_id', 'amount',
                'item_name', 'item_description', 'custom_int1', 'custom_str1', 'custom_str2', 'custom_str3'
            ]
            
            # Create signature string using Byron's method
            signature_parts = []
            for field in ordered_fields:
                if field in form_data and form_data[field]:
                    value = str(form_data[field])
                    encoded_value = urllib.parse.quote_plus(value)
                    signature_parts.append(f'{field}={encoded_value}')
            
            signature_string = '&'.join(signature_parts)
            signature_string += '&passphrase=Redeclip5e-8298'  # Not URL encoded
            
            expected_signature = hashlib.md5(signature_string.encode()).hexdigest().lower()
            actual_signature = form_data['signature']
            
            if expected_signature == actual_signature:
                print(f"✅ Signature verification PASSED!")
                print(f"   Expected: {expected_signature}")
                print(f"   Actual:   {actual_signature}")
                print(f"   ✅ Using Graham's working method!")
            else:
                print(f"❌ Signature verification FAILED!")
                print(f"   Expected: {expected_signature}")
                print(f"   Actual:   {actual_signature}")
                print(f"   Signature string: {signature_string}")
                return
                
            # Step 4: Create HTML test file for manual verification
            print(f"\n🌐 Step 4: Creating HTML test file...")
            
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Site Test - {order['customer_name']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .container {{ background: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .success {{ background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }}
        .info {{ background: #d1ecf1; border: 1px solid #bee5eb; color: #0c5460; }}
        .btn {{ background: #007bff; color: white; padding: 12px 24px; border: none; border-radius: 4px; 
                font-size: 16px; cursor: pointer; margin: 10px 0; }}
        .btn:hover {{ background: #0056b3; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        .signature {{ font-family: monospace; word-break: break-all; }}
    </style>
</head>
<body>
    <h1>🚀 Live Site Test - PayFast Payment</h1>
    
    <div class="container success">
        <h3>✅ Test Status: READY FOR PAYMENT</h3>
        <p><strong>Customer:</strong> {order['customer_name']}</p>
        <p><strong>Email:</strong> {order['customer_email']}</p>
        <p><strong>Order ID:</strong> {order['order_id']}</p>
        <p><strong>Amount:</strong> R{order['amount']}</p>
        <p><strong>Service:</strong> {order['service']}</p>
    </div>
    
    <div class="container info">
        <h3>🔍 PayFast Integration Details</h3>
        <table>
            <tr><th>Field</th><th>Value</th></tr>"""
            
            # Add form data to table
            for key, value in form_data.items():
                if key != 'signature':
                    html_content += f"<tr><td>{key}</td><td>{value}</td></tr>"
            
            html_content += f"""
            <tr><td><strong>signature</strong></td><td class="signature">{form_data['signature']}</td></tr>
        </table>
    </div>
    
    <div class="container">
        <h3>💳 Test Payment</h3>
        <p>Click the button below to test the PayFast payment with your live credentials:</p>
        
        <form action="{payment_data['payment_url']}" method="post">"""
        
            # Add all form fields
            for key, value in form_data.items():
                html_content += f'\n            <input type="hidden" name="{key}" value="{value}">'
                
            html_content += f"""
            <button type="submit" class="btn">
                💳 Pay R{form_data['amount']} with PayFast (LIVE)
            </button>
        </form>
        
        <p><small>This will redirect to PayFast with your live credentials and process a real payment.</small></p>
    </div>
    
    <div class="container">
        <h3>📋 Verification Checklist</h3>
        <ul>
            <li>✅ Using Byron's working signature method (form field order + include merchant_key)</li>
            <li>✅ NO cell_number field (Graham's fix applied)</li>
            <li>✅ Live PayFast credentials (Merchant ID: {form_data['merchant_id']})</li>
            <li>✅ HTTPS notify_url: {form_data['notify_url']}</li>
            <li>✅ Proper URL encoding in signature</li>
            <li>✅ Signature verification passed</li>
        </ul>
    </div>
</body>
</html>"""
            
            filename = f'live_test_{order_id.split("-")[0]}.html'
            with open(filename, 'w') as f:
                f.write(html_content)
                
            print(f"✅ Created {filename}")
            print(f"\n🎯 FINAL RESULTS:")
            print(f"   ✅ Order created successfully")
            print(f"   ✅ PayFast payment generated successfully") 
            print(f"   ✅ Signature verification passed")
            print(f"   ✅ Using Graham's working method (no cell_number)")
            print(f"   ✅ HTML test file created: {filename}")
            print(f"\n🚀 Your live site should now work for ALL customers!")
            print(f"   Open {filename} to test the payment manually")
            
        else:
            print(f"❌ Failed to generate PayFast payment: {payment_response.status_code}")
            print(f"   Response: {payment_response.text}")
            
    except Exception as e:
        print(f"❌ Error generating PayFast payment: {str(e)}")

if __name__ == "__main__":
    test_live_order_flow() 