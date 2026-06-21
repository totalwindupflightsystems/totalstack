---
id: "@specs/aws/cloudfront/docs/API_CachePolicyHeadersConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachePolicyHeadersConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CachePolicyHeadersConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CachePolicyHeadersConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachePolicyHeadersConfig
<a name="API_CachePolicyHeadersConfig"></a>

An object that determines whether any HTTP headers (and if so, which headers) are included in the cache key and in requests that CloudFront sends to the origin.

## Contents
<a name="API_CachePolicyHeadersConfig_Contents"></a>

 ** HeaderBehavior **   <a name="cloudfront-Type-CachePolicyHeadersConfig-HeaderBehavior"></a>
Determines whether any HTTP headers are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:  
+  `none` – No HTTP headers are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none`, any headers that are listed in an `OriginRequestPolicy` *are* included in origin requests.
+  `whitelist` – Only the HTTP headers that are listed in the `Headers` type are included in the cache key and in requests that CloudFront sends to the origin.
Type: String  
Valid Values: `none | whitelist`   
Required: Yes

 ** Headers **   <a name="cloudfront-Type-CachePolicyHeadersConfig-Headers"></a>
Contains a list of HTTP header names.  
Type: [Headers](API_Headers.md) object  
Required: No

## See Also
<a name="API_CachePolicyHeadersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyHeadersConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyHeadersConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyHeadersConfig) 