---
id: "@specs/aws/sesv2/docs/API_Content"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Content"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Content

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Content
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Content
<a name="API_Content"></a>

An object that represents the content of the email, and optionally a character set specification.

## Contents
<a name="API_Content_Contents"></a>

 ** Data **   <a name="SES-Type-Content-Data"></a>
The content of the message itself.  
Type: String  
Required: Yes

 ** Charset **   <a name="SES-Type-Content-Charset"></a>
The character set for the content. Because of the constraints of the SMTP protocol, Amazon SES uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8`, `ISO-8859-1`, or `Shift_JIS`.  
Type: String  
Required: No

## See Also
<a name="API_Content_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Content) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Content) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Content) 