---
id: "@specs/aws/transcribe/docs/API_InputDataConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InputDataConfig"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# InputDataConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_InputDataConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InputDataConfig
<a name="API_InputDataConfig"></a>

Contains the Amazon S3 location of the training data you want to use to create a new custom language model, and permissions to access this location.

When using `InputDataConfig`, you must include these sub-parameters: `S3Uri` and `DataAccessRoleArn`. You can optionally include `TuningDataS3Uri`.

## Contents
<a name="API_InputDataConfig_Contents"></a>

 ** DataAccessRoleArn **   <a name="transcribe-Type-InputDataConfig-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.  
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.  
For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: Yes

 ** S3Uri **   <a name="transcribe-Type-InputDataConfig-S3Uri"></a>
The Amazon S3 location (URI) of the text files you want to use to train your custom language model.  
Here's an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-model-training-data/`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: Yes

 ** TuningDataS3Uri **   <a name="transcribe-Type-InputDataConfig-TuningDataS3Uri"></a>
The Amazon S3 location (URI) of the text files you want to use to tune your custom language model.  
Here's an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-model-tuning-data/`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

## See Also
<a name="API_InputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/InputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/InputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/InputDataConfig) 