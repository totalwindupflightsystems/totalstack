---
id: "@specs/aws/signer/docs/API_SigningConfigurationOverrides"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningConfigurationOverrides"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningConfigurationOverrides

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningConfigurationOverrides
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningConfigurationOverrides
<a name="API_SigningConfigurationOverrides"></a>

A signing configuration that overrides the default encryption or hash algorithm of a signing job.

## Contents
<a name="API_SigningConfigurationOverrides_Contents"></a>

 ** encryptionAlgorithm **   <a name="signer-Type-SigningConfigurationOverrides-encryptionAlgorithm"></a>
A specified override of the default encryption algorithm that is used in a code-signing job.  
Type: String  
Valid Values: `RSA | ECDSA`   
Required: No

 ** hashAlgorithm **   <a name="signer-Type-SigningConfigurationOverrides-hashAlgorithm"></a>
A specified override of the default hash algorithm that is used in a code-signing job.  
Type: String  
Valid Values: `SHA1 | SHA256`   
Required: No

## See Also
<a name="API_SigningConfigurationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningConfigurationOverrides) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningConfigurationOverrides) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningConfigurationOverrides) 