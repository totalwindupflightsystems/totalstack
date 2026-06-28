---
id: "@specs/aws/signer/docs/API_SigningConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningConfiguration"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningConfiguration
<a name="API_SigningConfiguration"></a>

The configuration of a signing operation.

## Contents
<a name="API_SigningConfiguration_Contents"></a>

 ** encryptionAlgorithmOptions **   <a name="signer-Type-SigningConfiguration-encryptionAlgorithmOptions"></a>
The encryption algorithm options that are available for a code-signing job.  
Type: [EncryptionAlgorithmOptions](API_EncryptionAlgorithmOptions.md) object  
Required: Yes

 ** hashAlgorithmOptions **   <a name="signer-Type-SigningConfiguration-hashAlgorithmOptions"></a>
The hash algorithm options that are available for a code-signing job.  
Type: [HashAlgorithmOptions](API_HashAlgorithmOptions.md) object  
Required: Yes

## See Also
<a name="API_SigningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningConfiguration) 