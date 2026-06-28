---
id: "@specs/aws/signer/docs/API_S3Source"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3Source"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# S3Source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_S3Source
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3Source
<a name="API_S3Source"></a>

Information about the Amazon S3 bucket where you saved your unsigned code.

## Contents
<a name="API_S3Source_Contents"></a>

 ** bucketName **   <a name="signer-Type-S3Source-bucketName"></a>
Name of the S3 bucket.  
Type: String  
Required: Yes

 ** key **   <a name="signer-Type-S3Source-key"></a>
Key name of the bucket object that contains your unsigned code.  
Type: String  
Required: Yes

 ** version **   <a name="signer-Type-S3Source-version"></a>
Version of your source image in your version enabled S3 bucket.  
Type: String  
Required: Yes

## See Also
<a name="API_S3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/S3Source) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/S3Source) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/S3Source) 