---
id: "@specs/aws/network-firewall/docs/API_EncryptionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EncryptionConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# EncryptionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_EncryptionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

A complex type that contains optional AWS Key Management Service (KMS) encryption settings for your Network Firewall resources. Your data is encrypted by default with an AWS owned key that AWS owns and manages for you. You can use either the AWS owned key, or provide your own customer managed key. To learn more about KMS encryption of your Network Firewall resources, see [Encryption at rest with AWS Key Managment Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-encryption-at-rest.html) in the *Network Firewall Developer Guide*.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** Type **   <a name="networkfirewall-Type-EncryptionConfiguration-Type"></a>
The type of AWS KMS key to use for encryption of your Network Firewall resources.  
Type: String  
Valid Values: `CUSTOMER_KMS | AWS_OWNED_KMS_KEY`   
Required: Yes

 ** KeyId **   <a name="networkfirewall-Type-EncryptionConfiguration-KeyId"></a>
The ID of the AWS Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless you're using a key that's managed by another account. If you're using a key managed by another account, then specify the key ARN. For more information, see [Key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the * AWS KMS Developer Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/EncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/EncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/EncryptionConfiguration) 