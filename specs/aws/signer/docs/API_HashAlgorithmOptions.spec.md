---
id: "@specs/aws/signer/docs/API_HashAlgorithmOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HashAlgorithmOptions"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# HashAlgorithmOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_HashAlgorithmOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HashAlgorithmOptions
<a name="API_HashAlgorithmOptions"></a>

The hash algorithms that are available to a code-signing job.

## Contents
<a name="API_HashAlgorithmOptions_Contents"></a>

 ** allowedValues **   <a name="signer-Type-HashAlgorithmOptions-allowedValues"></a>
The set of accepted hash algorithms allowed in a code-signing job.  
Type: Array of strings  
Valid Values: `SHA1 | SHA256`   
Required: Yes

 ** defaultValue **   <a name="signer-Type-HashAlgorithmOptions-defaultValue"></a>
The default hash algorithm that is used in a code-signing job.  
Type: String  
Valid Values: `SHA1 | SHA256`   
Required: Yes

## See Also
<a name="API_HashAlgorithmOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/HashAlgorithmOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/HashAlgorithmOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/HashAlgorithmOptions) 