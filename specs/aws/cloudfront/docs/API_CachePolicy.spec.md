---
id: "@specs/aws/cloudfront/docs/API_CachePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachePolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CachePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CachePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachePolicy
<a name="API_CachePolicy"></a>

A cache policy.

When it's attached to a cache behavior, the cache policy determines the following:
+ The values that CloudFront includes in the cache key. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.
+ The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.

The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find a valid object in its cache that matches the request's cache key. If you want to send values to the origin but *not* include them in the cache key, use `OriginRequestPolicy`.

## Contents
<a name="API_CachePolicy_Contents"></a>

 ** CachePolicyConfig **   <a name="cloudfront-Type-CachePolicy-CachePolicyConfig"></a>
The cache policy configuration.  
Type: [CachePolicyConfig](API_CachePolicyConfig.md) object  
Required: Yes

 ** Id **   <a name="cloudfront-Type-CachePolicy-Id"></a>
The unique identifier for the cache policy.  
Type: String  
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-CachePolicy-LastModifiedTime"></a>
The date and time when the cache policy was last modified.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_CachePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicy) 