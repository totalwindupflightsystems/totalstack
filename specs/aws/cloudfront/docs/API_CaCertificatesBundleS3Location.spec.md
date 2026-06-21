---
id: "@specs/aws/cloudfront/docs/API_CaCertificatesBundleS3Location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CaCertificatesBundleS3Location"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CaCertificatesBundleS3Location

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CaCertificatesBundleS3Location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CaCertificatesBundleS3Location
<a name="API_CaCertificatesBundleS3Location"></a>

The CA certificates bundle location in Amazon S3.

## Contents
<a name="API_CaCertificatesBundleS3Location_Contents"></a>

 ** Bucket **   <a name="cloudfront-Type-CaCertificatesBundleS3Location-Bucket"></a>
The S3 bucket.  
Type: String  
Required: Yes

 ** Key **   <a name="cloudfront-Type-CaCertificatesBundleS3Location-Key"></a>
The location's key.  
Type: String  
Required: Yes

 ** Region **   <a name="cloudfront-Type-CaCertificatesBundleS3Location-Region"></a>
The location's Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `[a-z]{2}-[a-z]+-\d`   
Required: Yes

 ** Version **   <a name="cloudfront-Type-CaCertificatesBundleS3Location-Version"></a>
The location's version.  
Type: String  
Required: No

## See Also
<a name="API_CaCertificatesBundleS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CaCertificatesBundleS3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CaCertificatesBundleS3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CaCertificatesBundleS3Location) 