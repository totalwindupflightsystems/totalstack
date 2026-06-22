---
id: "@specs/aws/codepipeline/docs/API_S3Location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3Location"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# S3Location

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_S3Location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3Location
<a name="API_S3Location"></a>

The Amazon S3 artifact location for an action's artifacts.

## Contents
<a name="API_S3Location_Contents"></a>

 ** bucket **   <a name="CodePipeline-Type-S3Location-bucket"></a>
The Amazon S3 artifact bucket for an action's artifacts.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Required: No

 ** key **   <a name="CodePipeline-Type-S3Location-key"></a>
The artifact name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/S3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/S3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/S3Location) 