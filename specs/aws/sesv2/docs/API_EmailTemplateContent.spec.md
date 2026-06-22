---
id: "@specs/aws/sesv2/docs/API_EmailTemplateContent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EmailTemplateContent"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EmailTemplateContent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EmailTemplateContent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EmailTemplateContent
<a name="API_EmailTemplateContent"></a>

The content of the email, composed of a subject line, an HTML part, and a text-only part.

## Contents
<a name="API_EmailTemplateContent_Contents"></a>

 ** Html **   <a name="SES-Type-EmailTemplateContent-Html"></a>
The HTML body of the email.  
Type: String  
Required: No

 ** Subject **   <a name="SES-Type-EmailTemplateContent-Subject"></a>
The subject line of the email.  
Type: String  
Required: No

 ** Text **   <a name="SES-Type-EmailTemplateContent-Text"></a>
The email body that will be visible to recipients whose email clients do not display HTML.  
Type: String  
Required: No

## See Also
<a name="API_EmailTemplateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EmailTemplateContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EmailTemplateContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EmailTemplateContent) 