---
id: "@specs/aws/cloudfront/docs/API_CloudFrontOriginAccessIdentitySummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudFrontOriginAccessIdentitySummary"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CloudFrontOriginAccessIdentitySummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CloudFrontOriginAccessIdentitySummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudFrontOriginAccessIdentitySummary
<a name="API_CloudFrontOriginAccessIdentitySummary"></a>

Summary of the information about a CloudFront origin access identity.

## Contents
<a name="API_CloudFrontOriginAccessIdentitySummary_Contents"></a>

 ** Comment **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentitySummary-Comment"></a>
The comment for this origin access identity, as originally specified when created.  
Type: String  
Required: Yes

 ** Id **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentitySummary-Id"></a>
The ID for the origin access identity. For example: `E74FTE3AJFJ256A`.  
Type: String  
Required: Yes

 ** S3CanonicalUserId **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentitySummary-S3CanonicalUserId"></a>
The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.  
Type: String  
Required: Yes

## See Also
<a name="API_CloudFrontOriginAccessIdentitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CloudFrontOriginAccessIdentitySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CloudFrontOriginAccessIdentitySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CloudFrontOriginAccessIdentitySummary) 