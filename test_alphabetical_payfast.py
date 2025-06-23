#!/usr/bin/env python3
import hashlib
import urllib.parse
from collections import OrderedDict

# Your LIVE PayFast credentials
MERCHANT_ID = "13245841"
MERCHANT_KEY = "kzyobsh5zlvrw"
PASSPHRASE = "Redeclip5e-8298"
PAYFAST_URL = "https://www.payfast.co.za/eng/process"

def create_test_payload_alphabetical():
    # Build payment data
    payment_data = {
        'merchant_id': MERCHANT_ID,
        'merchant_key': MERCHANT_KEY,
        'return_url': 'https://fletcraft.co.za/payment/success',
        'cancel_url': 'https://fletcraft.co.za/payment/cancel',
        'notify_url': 'https://fletcraft.co.za/api/payment/notify/',
        'name_first': 'Test',
        'name_last': 'Customer',
        'email_address': 'test@fletcraft.co.za',
        'm_payment_id': 'TEST123456',
        'amount': '100.00',
        'item_name': 'Web Applications',
        'item_description': 'Professional web application development services',
        'custom_str1': '1',
        'custom_str2': 'Web Applications',
        'custom_str3': 'Fletcraft Software',
    }
    
    # Remove empty values
    payment_data = {k: v for k, v in payment_data.items() if v}
    
    # Generate signature using ALPHABETICAL ORDER (standard for most payment gateways)
    signature_data = {k: v for k, v in payment_data.items() if k != 'merchant_key'}
    
    # Sort keys alphabetically
    encoded_params = []
    for key in sorted(signature_data.keys()):
        value = signature_data[key]
        encoded_params.append(key + '=' + urllib.parse.quote_plus(str(value)))
    
    signature_string = '&'.join(encoded_params)
    
    # Add passphrase to signature string
    signature_string += '&passphrase=' + urllib.parse.quote_plus(PASSPHRASE)
    
    signature = hashlib.md5(signature_string.encode()).hexdigest()
    payment_data['signature'] = signature
    
    return payment_data, signature_string

if __name__ == "__main__":
    print("PayFast ALPHABETICAL ORDER Test")
    print("=" * 50)
    
    # Create test payload
    payment_data, signature_string = create_test_payload_alphabetical()
    
    print("\nPAYMENT DATA:")
    for key, value in payment_data.items():
        print("  " + key + ": " + str(value))
    
    print("\nSIGNATURE STRING (ALPHABETICAL ORDER):")
    print("  " + signature_string)
    
    print("\nSIGNATURE HASH:")
    print("  " + payment_data['signature'])
    
    # Create simple HTML form
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>PayFast ALPHABETICAL Test</title>
</head>
<body>
    <h1>PayFast ALPHABETICAL ORDER Test</h1>
    
    <h3>Debug Information:</h3>
    <p><strong>Merchant ID:</strong> ''' + payment_data['merchant_id'] + '''</p>
    <p><strong>Amount:</strong> R''' + payment_data['amount'] + '''</p>
    <p><strong>Signature:</strong> ''' + payment_data['signature'] + '''</p>
    <p><strong>Method:</strong> ALPHABETICAL field ordering</p>
    
    <h3>Test Form:</h3>
    <form action="''' + PAYFAST_URL + '''" method="post" id="payfast_form">
'''
    
    for key, value in payment_data.items():
        html_content += '        <input type="hidden" name="' + key + '" value="' + str(value) + '">\n'
    
    html_content += '''    </form>
    
    <button onclick="document.getElementById('payfast_form').submit();">
        Submit ALPHABETICAL Test to PayFast
    </button>
</body>
</html>'''
    
    with open('payfast_alphabetical_test.html', 'w') as f:
        f.write(html_content)
    
    print("\nHTML Test File Created: payfast_alphabetical_test.html")
    print("This uses ALPHABETICAL field ordering for signature generation")
    print("=" * 50) 