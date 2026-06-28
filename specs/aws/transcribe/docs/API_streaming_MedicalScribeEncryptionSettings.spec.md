---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeEncryptionSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeEncryptionSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeEncryptionSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeEncryptionSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeEncryptionSettings
<a name="API_streaming_MedicalScribeEncryptionSettings"></a>

Contains encryption related settings to be used for data encryption with AWS Key Management Service, including KmsEncryptionContext and KmsKeyId. The KmsKeyId is required, while KmsEncryptionContext is optional for additional layer of security. 

By default, AWS HealthScribe provides encryption at rest to protect sensitive customer data using Amazon S3-managed keys. HealthScribe uses the KMS key you specify as a second layer of encryption.

 Your `ResourceAccessRoleArn` must permission to use your KMS key. For more information, see [Data Encryption at rest for AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-encryption.html). 

## Contents
<a name="API_streaming_MedicalScribeEncryptionSettings_Contents"></a>

 ** KmsKeyId **   <a name="transcribe-Type-streaming_MedicalScribeEncryptionSettings-KmsKeyId"></a>
The ID of the KMS key you want to use for your streaming session. You can specify its KMS key ID, key Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with `"alias/"`. To specify a KMS key in a different AWS account, you must use the key ARN or alias ARN.  
For example:  
+ Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
+ Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
+  Alias name: alias/ExampleAlias
+  Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias 
 To get the key ID and key ARN for a KMS key, use the [ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) or [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) KMS API operations. To get the alias name and alias ARN, use [ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html) API operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`   
Required: Yes

 ** KmsEncryptionContext **   <a name="transcribe-Type-streaming_MedicalScribeEncryptionSettings-KmsEncryptionContext"></a>
A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see [AWS KMSencryption context ](https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context) and [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html).   
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

## See Also
<a name="API_streaming_MedicalScribeEncryptionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeEncryptionSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeEncryptionSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeEncryptionSettings) 