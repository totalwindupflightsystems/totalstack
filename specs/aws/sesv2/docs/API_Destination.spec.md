---
id: "@specs/aws/sesv2/docs/API_Destination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Destination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Destination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Destination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Destination
<a name="API_Destination"></a>

An object that describes the recipients for an email.

**Note**  
Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the *local part* of a destination email address (the part of the email address that precedes the @ sign) may only contain [7-bit ASCII characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the *domain part* of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in [RFC3492](https://tools.ietf.org/html/rfc3492.html).

## Contents
<a name="API_Destination_Contents"></a>

 ** BccAddresses **   <a name="SES-Type-Destination-BccAddresses"></a>
An array that contains the email addresses of the "BCC" (blind carbon copy) recipients for the email.  
Type: Array of strings  
Required: No

 ** CcAddresses **   <a name="SES-Type-Destination-CcAddresses"></a>
An array that contains the email addresses of the "CC" (carbon copy) recipients for the email.  
Type: Array of strings  
Required: No

 ** ToAddresses **   <a name="SES-Type-Destination-ToAddresses"></a>
An array that contains the email addresses of the "To" recipients for the email.  
Type: Array of strings  
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Destination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Destination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Destination) 