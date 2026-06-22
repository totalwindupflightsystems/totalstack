---
id: "@specs/aws/sesv2/docs/API_CustomVerificationEmailTemplateMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomVerificationEmailTemplateMetadata"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CustomVerificationEmailTemplateMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CustomVerificationEmailTemplateMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomVerificationEmailTemplateMetadata
<a name="API_CustomVerificationEmailTemplateMetadata"></a>

Contains information about a custom verification email template.

## Contents
<a name="API_CustomVerificationEmailTemplateMetadata_Contents"></a>

 ** FailureRedirectionURL **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-FailureRedirectionURL"></a>
The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.  
Type: String  
Required: No

 ** FromEmailAddress **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-FromEmailAddress"></a>
The email address that the custom verification email is sent from.  
Type: String  
Required: No

 ** SuccessRedirectionURL **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-SuccessRedirectionURL"></a>
The URL that the recipient of the verification email is sent to if his or her address is successfully verified.  
Type: String  
Required: No

 ** TemplateName **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-TemplateName"></a>
The name of the custom verification email template.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** TemplateSubject **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-TemplateSubject"></a>
The subject line of the custom verification email.  
Type: String  
Required: No

## See Also
<a name="API_CustomVerificationEmailTemplateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CustomVerificationEmailTemplateMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CustomVerificationEmailTemplateMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CustomVerificationEmailTemplateMetadata) 