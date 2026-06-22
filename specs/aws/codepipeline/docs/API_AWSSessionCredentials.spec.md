---
id: "@specs/aws/codepipeline/docs/API_AWSSessionCredentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWSSessionCredentials"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# AWSSessionCredentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_AWSSessionCredentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWSSessionCredentials
<a name="API_AWSSessionCredentials"></a>

Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifact for the pipeline in CodePipeline.

## Contents
<a name="API_AWSSessionCredentials_Contents"></a>

 ** accessKeyId **   <a name="CodePipeline-Type-AWSSessionCredentials-accessKeyId"></a>
The access key for the session.  
Type: String  
Required: Yes

 ** secretAccessKey **   <a name="CodePipeline-Type-AWSSessionCredentials-secretAccessKey"></a>
The secret access key for the session.  
Type: String  
Required: Yes

 ** sessionToken **   <a name="CodePipeline-Type-AWSSessionCredentials-sessionToken"></a>
The token for the session.  
Type: String  
Required: Yes

## See Also
<a name="API_AWSSessionCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/AWSSessionCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/AWSSessionCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/AWSSessionCredentials) 