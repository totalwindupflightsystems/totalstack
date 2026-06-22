---
id: "@specs/aws/sesv2/docs/API_ReplacementTemplate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ReplacementTemplate"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ReplacementTemplate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ReplacementTemplate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ReplacementTemplate
<a name="API_ReplacementTemplate"></a>

An object which contains `ReplacementTemplateData` to be used for a specific `BulkEmailEntry`.

## Contents
<a name="API_ReplacementTemplate_Contents"></a>

 ** ReplacementTemplateData **   <a name="SES-Type-ReplacementTemplate-ReplacementTemplateData"></a>
A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.  
Type: String  
Length Constraints: Maximum length of 262144.  
Required: No

## See Also
<a name="API_ReplacementTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ReplacementTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ReplacementTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ReplacementTemplate) 