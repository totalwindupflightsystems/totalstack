---
id: "@specs/aws/sesv2/docs/API_Attachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Attachment"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Attachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Attachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Attachment
<a name="API_Attachment"></a>

 Contains metadata and attachment raw content.

## Contents
<a name="API_Attachment_Contents"></a>

 ** FileName **   <a name="SES-Type-Attachment-FileName"></a>
The file name for the attachment as it will appear in the email. Amazon SES restricts certain file extensions. To ensure attachments are accepted, check the [Unsupported attachment types](https://docs.aws.amazon.com/ses/latest/dg/mime-types.html) in the Amazon SES Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** RawContent **   <a name="SES-Type-Attachment-RawContent"></a>
 The raw data of the attachment. It needs to be base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you.  
Type: Base64-encoded binary data object  
Required: Yes

 ** ContentDescription **   <a name="SES-Type-Attachment-ContentDescription"></a>
 A brief description of the attachment content.  
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** ContentDisposition **   <a name="SES-Type-Attachment-ContentDisposition"></a>
 A standard descriptor indicating how the attachment should be rendered in the email. Supported values: `ATTACHMENT` or `INLINE`.  
Type: String  
Valid Values: `ATTACHMENT | INLINE`   
Required: No

 ** ContentId **   <a name="SES-Type-Attachment-ContentId"></a>
 Unique identifier for the attachment, used for referencing attachments with INLINE disposition in HTML content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 78.  
Required: No

 ** ContentTransferEncoding **   <a name="SES-Type-Attachment-ContentTransferEncoding"></a>
 Specifies how the attachment is encoded. Supported values: `BASE64`, `QUOTED_PRINTABLE`, `SEVEN_BIT`.  
Type: String  
Valid Values: `BASE64 | QUOTED_PRINTABLE | SEVEN_BIT`   
Required: No

 ** ContentType **   <a name="SES-Type-Attachment-ContentType"></a>
 The MIME type of the attachment.  
Example: `application/pdf`, `image/jpeg` 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 78.  
Required: No

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Attachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Attachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Attachment) 