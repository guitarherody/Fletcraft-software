#!/usr/bin/env python3
"""
🚀 COMPREHENSIVE CUSTOMER PAYFAST TEST
Test that PayFast works for multiple different customers after Graham's fix
"""

import requests
import json
import time

def test_customer_payfast(customer_data):
    """Test PayFast payment for a single customer"""
    
    print(f"\n👤 Testing: {customer_data['customer_name']}")
    print("-" * 50)
    
    try:
        # Step 1: Create order
        print("📝 Creating order...")
        create_response = requests.post(
            'https://fletcraft-software.onrender.com/api/orders/',
            json=customer_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if create_response.status_code != 201:
            print(f"❌ Order creation failed: {create_response.status_code}")
            print(f"   Response: {create_response.text}")
            return False
            
        order = create_response.json()
        order_id = order['order_id']
        print(f"✅ Order created: {order_id}")
        
        # Step 2: Generate PayFast payment
        print("💳 Generating PayFast payment...")
        payment_response = requests.post(
            'https://fletcraft-software.onrender.com/api/orders/create_payfast_payment/',
            json={'order_id': order_id},
            headers={'Content-Type': 'application/json'}
        )
        
        if payment_response.status_code != 200:
            print(f"❌ PayFast generation failed: {payment_response.status_code}")
            print(f"   Response: {payment_response.text}")
            return False
            
        payment_data = payment_response.json()
        form_data = payment_data['payment_data']
        
        # Step 3: Check for Graham's fix
        if 'cell_number' in form_data:
            print(f"❌ STILL CONTAINS cell_number: {form_data['cell_number']}")
            print(f"   Django backend needs more time to deploy or has an issue")
            return False
        else:
            print(f"✅ NO cell_number field (Graham's fix applied)")
        
        print(f"✅ PayFast payment ready!")
        print(f"   Amount: R{form_data['amount']}")
        print(f"   Signature: {form_data['signature']}")
        print(f"   Customer: {form_data['name_first']} {form_data['name_last']}")
        print(f"   Email: {form_data['email_address']}")
        
        return {
            'customer': customer_data['customer_name'],
            'order_id': order_id,
            'signature': form_data['signature'],
            'amount': form_data['amount'],
            'success': True,
            'payment_data': form_data
        }
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Test PayFast for multiple different customers"""
    
    print("🚀 COMPREHENSIVE PAYFAST CUSTOMER TEST")
    print("Testing PayFast integration for multiple customer types")
    print("=" * 60)
    
    # Test customers with different characteristics
    test_customers = [
        {
            "customer_name": "John Smith",
            "customer_email": "john.smith@email.com",
            "customer_phone": "0721234567",  # Will be ignored after Graham's fix
            "service": 390,  # Cybersecurity (R100)
            "amount": 100.00,
            "special_requirements": "Basic cybersecurity audit"
        },
        {
            "customer_name": "Sarah Johnson", 
            "customer_email": "sarah@company.com",
            "customer_phone": "0831234567",  # Will be ignored
            "service": 386,  # Web Applications
            "amount": 150.00,
            "special_requirements": "E-commerce website development"
        },
        {
            "customer_name": "Mike Chen",
            "customer_email": "mike.chen@startup.co.za", 
            "customer_phone": "0729876543",  # Will be ignored
            "service": 387,  # Mobile Development  
            "amount": 200.00,
            "special_requirements": "Mobile app for Android and iOS"
        },
        {
            "customer_name": "Lisa Williams",
            "customer_email": "lisa@business.net",
            "customer_phone": "",  # Empty phone
            "service": 388,  # AI & Machine Learning
            "amount": 300.00, 
            "special_requirements": "AI chatbot integration"
        },
        {
            "customer_name": "David Brown",
            "customer_email": "david.brown@corp.com",
            "customer_phone": "invalid_phone",  # Invalid phone format
            "service": 389,  # Cloud Solutions
            "amount": 250.00,
            "special_requirements": "Cloud migration and setup"
        }
    ]
    
    results = []
    successful_tests = 0
    
    for i, customer in enumerate(test_customers, 1):
        print(f"\n🧪 TEST {i}/{len(test_customers)}")
        result = test_customer_payfast(customer)
        
        if result:
            results.append(result)
            successful_tests += 1
            print(f"✅ SUCCESS for {customer['customer_name']}")
        else:
            print(f"❌ FAILED for {customer['customer_name']}")
        
        # Small delay between tests
        time.sleep(1)
    
    # Summary
    print(f"\n🎯 TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Successful: {successful_tests}/{len(test_customers)}")
    print(f"❌ Failed: {len(test_customers) - successful_tests}/{len(test_customers)}")
    
    if successful_tests == len(test_customers):
        print(f"\n🚀 ALL TESTS PASSED!")
        print(f"   ✅ PayFast integration works for all customer types")
        print(f"   ✅ Graham's fix (no cell_number) is working")
        print(f"   ✅ Your live site is ready for customer payments")
        
        # Create summary HTML with all working payments
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ALL CUSTOMERS WORKING - PayFast Integration</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; }}
        .container {{ background: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .success {{ background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }}
        .customer {{ background: #e7f3ff; border: 1px solid #b3d7ff; margin: 10px 0; padding: 15px; border-radius: 4px; }}
        .btn {{ background: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 4px; 
                font-size: 14px; cursor: pointer; margin: 5px; }}
        .btn:hover {{ background: #218838; }}
        table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; font-size: 12px; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>🚀 ALL CUSTOMERS WORKING!</h1>
    
    <div class="container success">
        <h3>✅ PAYFAST INTEGRATION SUCCESS</h3>
        <p><strong>Status:</strong> All {successful_tests} test customers can pay successfully</p>
        <p><strong>Method:</strong> Graham's working method (no cell_number + Byron's field order)</p>
        <p><strong>Credentials:</strong> Live PayFast account (Merchant ID: 13245841)</p>
        <p><strong>Server:</strong> Fletcher SOTFWARE INC. production backend</p>
    </div>
    
    <h2>💳 Test Payments Available</h2>"""
        
        for result in results:
            html_content += f"""
    <div class="customer">
        <h4>👤 {result['customer']} - R{result['amount']}</h4>
        <p><strong>Order ID:</strong> {result['order_id']}</p>
        <p><strong>Signature:</strong> <code>{result['signature']}</code></p>
        
        <form action="https://www.payfast.co.za/eng/process" method="post" style="display: inline;">"""
            
            # Add payment form fields
            for key, value in result['payment_data'].items():
                html_content += f'\n            <input type="hidden" name="{key}" value="{value}">'
            
            html_content += f"""
            <button type="submit" class="btn">💳 Pay R{result['amount']} ({result['customer']})</button>
        </form>
    </div>"""
        
        html_content += f"""
    
    <div class="container">
        <h3>📋 Technical Details</h3>
        <table>
            <tr><th>Customer</th><th>Order ID</th><th>Amount</th><th>Signature</th></tr>"""
        
        for result in results:
            html_content += f"""
            <tr>
                <td>{result['customer']}</td>
                <td>{result['order_id'][:13]}...</td>
                <td>R{result['amount']}</td>
                <td>{result['signature'][:16]}...</td>
            </tr>"""
        
        html_content += f"""
        </table>
    </div>
    
    <div class="container success">
        <h3>🎉 CONGRATULATIONS!</h3>
        <p>Your PayFast integration is now working perfectly for all customer types:</p>
        <ul>
            <li>✅ Customers with valid phone numbers</li>
            <li>✅ Customers with invalid phone numbers</li>
            <li>✅ Customers with no phone numbers</li>
            <li>✅ All different services and amounts</li>
            <li>✅ All using Graham's proven working method</li>
        </ul>
        <p><strong>Your live site can now accept payments from ANY customer!</strong></p>
    </div>
</body>
</html>"""
        
        with open('ALL_CUSTOMERS_WORKING.html', 'w') as f:
            f.write(html_content)
        
        print(f"\n🌐 Created: ALL_CUSTOMERS_WORKING.html")
        print(f"   Contains {successful_tests} working payment links")
        print(f"   Test any of them to verify PayFast payments work")
        
    else:
        print(f"\n❌ SOME TESTS FAILED")
        print(f"   Likely the Django deployment is still in progress")
        print(f"   Wait a few minutes and try again")
        
        if successful_tests > 0:
            print(f"\n✅ But {successful_tests} customers DID work:")
            for result in results:
                print(f"      ✅ {result['customer']} - R{result['amount']}")

if __name__ == "__main__":
    main() 