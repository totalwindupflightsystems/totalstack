---
id: "@specs/aws/eks/docs/API_EncryptionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EncryptionConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# EncryptionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_EncryptionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EncryptionConfig
<a name="API_EncryptionConfig"></a>

The encryption configuration for the cluster.

## Contents
<a name="API_EncryptionConfig_Contents"></a>

 ** provider **   <a name="AmazonEKS-Type-EncryptionConfig-provider"></a>
 AWS Key Management Service (AWS KMS) key. Either the ARN or the alias can be used.  
Type: [Provider](API_Provider.md) object  
Required: No

 ** resources **   <a name="AmazonEKS-Type-EncryptionConfig-resources"></a>
Specifies the resources to be encrypted. The only supported value is `secrets`.  
Type: Array of strings  
Required: No

## See Also
<a name="API_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/EncryptionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/EncryptionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/EncryptionConfig) 