# PayFast Implementation Guide

## Overview
This document outlines the PayFast payment integration implemented in the Fletcraft Software project and how it complies with PayFast's official developer documentation.

## ✅ PayFast Compliance Summary

### What We're Doing Right:

1. **Proper Form Submission**: Using POST form to submit payment data
2. **Required Fields**: All mandatory PayFast fields are included
3. **Signature Generation**: Following correct signature process
4. **ITN Handling**: Proper Instant Transaction Notification endpoint

### 🔄 Improvements Made:

1. **Environment Variables**: Moved credentials to Django settings
2. **Field Validation**: Added proper field length validation
3. **URL Encoding**: Proper URL encoding for signature generation
4. **Error Handling**: Enhanced error handling in ITN endpoint
5. **Amount Validation**: Validates payment amounts match order amounts

## PayFast Integration Flow

### 1. Payment Creation (Frontend → Backend)
```
POST /api/orders/create_payfast_payment/
{
  "order_id": "uuid-string"
}
```

### 2. PayFast Form Submission (Backend → PayFast)
```
POST https://sandbox.payfast.co.za/eng/process
{
  "merchant_id": "...",
  "merchant_key": "...",
  "signature": "...",
  ...
}
```

### 3. Payment Notification (PayFast → Backend)
```
POST /api/payment/notify/
{
  "payment_status": "COMPLETE",
  "pf_payment_id": "...",
  "amount_gross": "...",
  ...
}
```

## Environment Variables Required

Add these to your production environment:

```bash
# PayFast Live Credentials (replace with your actual credentials)
PAYFAST_MERCHANT_ID=your-live-merchant-id
PAYFAST_MERCHANT_KEY=your-live-merchant-key
PAYFAST_PASSPHRASE=your-live-passphrase
PAYFAST_URL=https://www.payfast.co.za/eng/process
FRONTEND_URL=https://yourdomain.com
```

## PayFast Developer Documentation Compliance

### ✅ Required Fields (All Implemented)
- `merchant_id` - Your PayFast merchant ID
- `merchant_key` - Your PayFast merchant key  
- `return_url` - Where to redirect after successful payment
- `cancel_url` - Where to redirect after cancelled payment
- `notify_url` - ITN endpoint for payment notifications
- `name_first` - Customer first name (max 50 chars)
- `name_last` - Customer last name (max 50 chars)
- `email_address` - Customer email (max 100 chars)
- `m_payment_id` - Unique payment reference (max 100 chars)
- `amount` - Payment amount in ZAR format
- `item_name` - Service title (max 100 chars)
- `item_description` - Service description (max 200 chars)

### ✅ Optional Fields (Implemented)
- `custom_str1-5` - Custom fields for additional data
- `cell_number` - Customer phone number (10 digits)

### ✅ Signature Generation (Compliant)
1. Exclude `merchant_key` from signature calculation
2. Sort parameters alphabetically
3. URL encode parameter values
4. Add passphrase to signature string
5. Generate MD5 hash in lowercase

### ✅ ITN (Instant Transaction Notification) Handling (Compliant)
1. Verify signature using same process as payment creation
2. Validate required fields are present
3. Check payment amount matches order amount
4. Update order status based on payment status
5. Return appropriate HTTP status codes

## Security Best Practices Implemented

1. **Environment Variables**: Sensitive credentials stored in environment variables
2. **Signature Verification**: All ITN requests verified using signature
3. **Amount Validation**: Payment amounts validated against order amounts
4. **Field Length Validation**: All fields validated against PayFast limits
5. **Error Logging**: Errors logged for debugging and monitoring

## Testing with PayFast Sandbox

The implementation uses PayFast's sandbox environment by default:
- Sandbox URL: `https://sandbox.payfast.co.za/eng/process`
- Test Merchant ID: `10000100`
- Test Merchant Key: `46f0cd694581a`

## Going Live

To switch to production:

1. Update environment variables with live credentials
2. Change `PAYFAST_URL` to `https://www.payfast.co.za/eng/process`
3. Test with small amounts first
4. Monitor ITN notifications for any issues

## Common PayFast Error Messages and Solutions

### "merchant_key invalid"
- **Cause**: Wrong credentials or mixing test/live credentials
- **Solution**: Verify merchant ID and key match your PayFast account

### "signature mismatch"
- **Cause**: Incorrect signature generation
- **Solution**: Our implementation handles this correctly with proper URL encoding

### "amount invalid"
- **Cause**: Amount format incorrect
- **Solution**: We format amounts as `{amount:.2f}` (e.g., "10.00")

## PayFast Field Limits (All Enforced)

| Field | Max Length | Our Implementation |
|-------|------------|-------------------|
| `name_first` | 50 chars | `[:50]` |
| `name_last` | 50 chars | `[:50]` |
| `email_address` | 100 chars | `[:100]` |
| `m_payment_id` | 100 chars | `[:100]` |
| `item_name` | 100 chars | `[:100]` |
| `item_description` | 200 chars | `[:200]` |
| `custom_str1-5` | 255 chars | `[:255]` |

## ITN Status Mapping

| PayFast Status | Our Order Status |
|---------------|------------------|
| `COMPLETE` | `paid` |
| `FAILED` | `failed` |
| `CANCELLED` | `cancelled` |
| `PENDING` | `pending` |

## Monitoring and Debugging

1. **Django Logs**: ITN errors are logged with full stack traces
2. **PayFast Dashboard**: Monitor transactions in your PayFast account
3. **Database**: Transaction records stored in `PaymentTransaction` model

## Support and Resources

- PayFast Developer Documentation: https://developers.payfast.co.za/
- PayFast Support: support@payfast.co.za
- PayFast Phone: 021 300 4455

## Conclusion

Your PayFast implementation is now fully compliant with PayFast's developer documentation requirements. The code follows all best practices for security, field validation, signature generation, and ITN handling. 