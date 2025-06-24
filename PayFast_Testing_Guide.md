# PayFast Testing Guide

## Important: Email Address Issue (Solved!)

**Problem**: PayFast was rejecting transactions with "Generated signature does not match submitted signature" error.

**Root Cause**: Byron Adams from PayFast identified that we were using the merchant account email for testing transactions.

**Solution**: Use a **different email address** for testing transactions.

## ⚠️ DO NOT USE These Merchant Account Emails for Testing:
- `dylan@fletcraft.co.za`
- `guitarherody@gmail.com`

## Test Email Addresses to Use

Instead of your merchant emails, use any of these for testing:

- `test@example.com`
- `customer@test.com`
- `buyer@gmail.com`
- `testuser@outlook.com`
- Or any other email that's NOT your PayFast merchant account email

## Testing Steps

1. **Visit**: https://fletcraft.co.za/pricing
2. **Select a service** and click "Purchase Now"
3. **Fill in test details**:
   - Name: `Test Customer`
   - Email: `test@example.com` (NOT your merchant email!)
   - Phone: `0123456789` (optional)
4. **Click "Pay with PayFast"**
5. **Check result** - should now work without signature errors

## Recent Fixes Applied

1. **Simplified signature generation** - removed complex URL encoding
2. **Added helpful UI note** - reminds users about email requirement
3. **Updated backend** - uses cleaner signature method

## What to Watch For

- **Backend logs** should show successful 200/201 responses
- **PayFast** should accept the transaction instead of 400 errors
- **Payment flow** should redirect to PayFast payment page

The combination of the simplified signature generation + using a different email address should resolve the PayFast integration issues completely! 