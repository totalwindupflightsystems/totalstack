---
id: "@specs/aws/comprehend/docs/API_UpdateDataSecurityConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDataSecurityConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# UpdateDataSecurityConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_UpdateDataSecurityConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDataSecurityConfig
<a name="API_UpdateDataSecurityConfig"></a>

Data security configuration.

## Contents
<a name="API_UpdateDataSecurityConfig_Contents"></a>

 ** ModelKmsKeyId **   <a name="comprehend-Type-UpdateDataSecurityConfig-ModelKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:  
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"` 
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"` 
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^\p{ASCII}+$`   
Required: No

 ** VolumeKmsKeyId **   <a name="comprehend-Type-UpdateDataSecurityConfig-VolumeKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.  
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^\p{ASCII}+$`   
Required: No

 ** VpcConfig **   <a name="comprehend-Type-UpdateDataSecurityConfig-VpcConfig"></a>
 Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).   
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## See Also
<a name="API_UpdateDataSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/UpdateDataSecurityConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/UpdateDataSecurityConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/UpdateDataSecurityConfig) 