---
id: "@specs/aws/signer/docs/API_S3Destination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3Destination"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# S3Destination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_S3Destination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3Destination
<a name="API_S3Destination"></a>

The name and prefix of the Amazon S3 bucket where AWS Signer saves your signed objects.

## Contents
<a name="API_S3Destination_Contents"></a>

 ** bucketName **   <a name="signer-Type-S3Destination-bucketName"></a>
Name of the S3 bucket.  
Type: String  
Required: No

 ** prefix **   <a name="signer-Type-S3Destination-prefix"></a>
An S3 prefix that you can use to limit responses to those that begin with the specified prefix.  
Type: String  
Required: No

## See Also
<a name="API_S3Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/S3Destination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/S3Destination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/S3Destination) 