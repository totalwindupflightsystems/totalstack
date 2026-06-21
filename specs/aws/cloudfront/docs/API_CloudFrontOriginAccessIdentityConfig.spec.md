---
id: "@specs/aws/cloudfront/docs/API_CloudFrontOriginAccessIdentityConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudFrontOriginAccessIdentityConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CloudFrontOriginAccessIdentityConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CloudFrontOriginAccessIdentityConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudFrontOriginAccessIdentityConfig
<a name="API_CloudFrontOriginAccessIdentityConfig"></a>

Origin access identity configuration. Send a `GET` request to the `/CloudFront API version/CloudFront/identity ID/config` resource.

## Contents
<a name="API_CloudFrontOriginAccessIdentityConfig_Contents"></a>

 ** CallerReference **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityConfig-CallerReference"></a>
A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.  
If the value of `CallerReference` is new (regardless of the content of the `CloudFrontOriginAccessIdentityConfig` object), a new origin access identity is created.  
If the `CallerReference` is a value already sent in a previous identity request, and the content of the `CloudFrontOriginAccessIdentityConfig` is identical to the original request (ignoring white space), the response includes the same information returned to the original request.  
If the `CallerReference` is a value you already sent in a previous request to create an identity, but the content of the `CloudFrontOriginAccessIdentityConfig` is different from the original request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists` error.   
Type: String  
Required: Yes

 ** Comment **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityConfig-Comment"></a>
A comment to describe the origin access identity. The comment cannot be longer than 128 characters.  
Type: String  
Required: Yes

## See Also
<a name="API_CloudFrontOriginAccessIdentityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CloudFrontOriginAccessIdentityConfig) 