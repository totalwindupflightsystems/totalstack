---
id: "@specs/aws/kendra/docs/API_AccessControlListConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccessControlListConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# AccessControlListConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_AccessControlListConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccessControlListConfiguration
<a name="API_AccessControlListConfiguration"></a>

Access Control List files for the documents in a data source. For the format of the file, see [Access control for S3 data sources](https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html).

## Contents
<a name="API_AccessControlListConfiguration_Contents"></a>

 ** KeyPath **   <a name="kendra-Type-AccessControlListConfiguration-KeyPath"></a>
Path to the Amazon S3 bucket that contains the ACL files.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

## See Also
<a name="API_AccessControlListConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/AccessControlListConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/AccessControlListConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/AccessControlListConfiguration) 