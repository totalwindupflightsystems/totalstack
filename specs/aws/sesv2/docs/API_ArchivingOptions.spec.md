---
id: "@specs/aws/sesv2/docs/API_ArchivingOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArchivingOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ArchivingOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ArchivingOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArchivingOptions
<a name="API_ArchivingOptions"></a>

Used to associate a configuration set with a MailManager archive.

## Contents
<a name="API_ArchivingOptions_Contents"></a>

 ** ArchiveArn **   <a name="SES-Type-ArchivingOptions-ArchiveArn"></a>
The Amazon Resource Name (ARN) of the MailManager archive where the Amazon SES API v2 will archive sent emails.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:(aws|aws-[a-z-]+):ses:[a-z]{2,4}-[a-z-]+-[0-9]:[0-9]{1,20}:mailmanager-archive/a-[a-z0-9]{24,62}`   
Required: No

## See Also
<a name="API_ArchivingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ArchivingOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ArchivingOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ArchivingOptions) 