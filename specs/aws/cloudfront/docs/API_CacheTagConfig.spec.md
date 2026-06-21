---
id: "@specs/aws/cloudfront/docs/API_CacheTagConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheTagConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CacheTagConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CacheTagConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheTagConfig
<a name="API_CacheTagConfig"></a>

A complex type that specifies the HTTP header name from which CloudFront extracts cache tags from origin responses. When you add `CacheTagConfig` to a distribution, CloudFront reads the specified header from origin responses, parses the comma-separated tag values, and stores them with the cached object. You can then invalidate cached objects by tag using the `CreateInvalidation` API.

## Contents
<a name="API_CacheTagConfig_Contents"></a>

 ** HeaderName **   <a name="cloudfront-Type-CacheTagConfig-HeaderName"></a>
The name of the HTTP header that your origin includes in responses. CloudFront uses this header to extract cache tags. The header value must contain comma-separated tag values (for example, `product:electronics, category:tv, brand:example`).  
Type: String  
Required: Yes

## See Also
<a name="API_CacheTagConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheTagConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheTagConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheTagConfig) 