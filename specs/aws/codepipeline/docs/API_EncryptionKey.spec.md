---
id: "@specs/aws/codepipeline/docs/API_EncryptionKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EncryptionKey"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# EncryptionKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_EncryptionKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EncryptionKey
<a name="API_EncryptionKey"></a>

Represents information about the key used to encrypt data in the artifact store, such as an AWS Key Management Service (AWS Key Management Service) key.

## Contents
<a name="API_EncryptionKey_Contents"></a>

 ** id **   <a name="CodePipeline-Type-EncryptionKey-id"></a>
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.  
Aliases are recognized only in the account that created the AWS KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 400.  
Required: Yes

 ** type **   <a name="CodePipeline-Type-EncryptionKey-type"></a>
The type of encryption key, such as an AWS KMS key. When creating or updating a pipeline, the value must be set to 'KMS'.  
Type: String  
Valid Values: `KMS`   
Required: Yes

## See Also
<a name="API_EncryptionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/EncryptionKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/EncryptionKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/EncryptionKey) 