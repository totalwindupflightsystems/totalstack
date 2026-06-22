---
id: "@specs/aws/sesv2/docs/API_BulkEmailEntry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BulkEmailEntry"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# BulkEmailEntry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_BulkEmailEntry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BulkEmailEntry
<a name="API_BulkEmailEntry"></a>

## Contents
<a name="API_BulkEmailEntry_Contents"></a>

 ** Destination **   <a name="SES-Type-BulkEmailEntry-Destination"></a>
Represents the destination of the message, consisting of To:, CC:, and BCC: fields.  
Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain [7-bit ASCII characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in [RFC3492](https://tools.ietf.org/html/rfc3492.html).
Type: [Destination](API_Destination.md) object  
Required: Yes

 ** ReplacementEmailContent **   <a name="SES-Type-BulkEmailEntry-ReplacementEmailContent"></a>
The `ReplacementEmailContent` associated with a `BulkEmailEntry`.  
Type: [ReplacementEmailContent](API_ReplacementEmailContent.md) object  
Required: No

 ** ReplacementHeaders **   <a name="SES-Type-BulkEmailEntry-ReplacementHeaders"></a>
The list of message headers associated with the `BulkEmailEntry` data type.  
+ Headers Not Present in `BulkEmailEntry`: If a header is specified in [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html) but not in `BulkEmailEntry`, the header from `Template` will be added to the outgoing email.
+ Headers Present in `BulkEmailEntry`: If a header is specified in `BulkEmailEntry`, it takes precedence over any header of the same name specified in [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html):
  + If the header is also defined within `Template`, the value from `BulkEmailEntry` will replace the header's value in the email.
  + If the header is not defined within `Template`, it will simply be added to the email as specified in `BulkEmailEntry`.
Type: Array of [MessageHeader](API_MessageHeader.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 15 items.  
Required: No

 ** ReplacementTags **   <a name="SES-Type-BulkEmailEntry-ReplacementTags"></a>
A list of tags, in the form of name/value pairs, to apply to an email that you send using the `SendBulkTemplatedEmail` operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.  
Type: Array of [MessageTag](API_MessageTag.md) objects  
Required: No

## See Also
<a name="API_BulkEmailEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/BulkEmailEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/BulkEmailEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/BulkEmailEntry) 