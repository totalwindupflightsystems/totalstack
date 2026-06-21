---
id: "@specs/aws/cloudfront/docs/API_CachePolicyConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachePolicyConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CachePolicyConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CachePolicyConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachePolicyConfig
<a name="API_CachePolicyConfig"></a>

A cache policy configuration.

This configuration determines the following:
+ The values that CloudFront includes in the cache key. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.
+ The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.
**Important**  
If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.

The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find a valid object in its cache that matches the request's cache key. If you want to send values to the origin but *not* include them in the cache key, use `OriginRequestPolicy`.

## Contents
<a name="API_CachePolicyConfig_Contents"></a>

 ** MinTTL **   <a name="cloudfront-Type-CachePolicyConfig-MinTTL"></a>
The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
Type: Long  
Required: Yes

 ** Name **   <a name="cloudfront-Type-CachePolicyConfig-Name"></a>
A unique name to identify the cache policy.  
Type: String  
Required: Yes

 ** Comment **   <a name="cloudfront-Type-CachePolicyConfig-Comment"></a>
A comment to describe the cache policy. The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** DefaultTTL **   <a name="cloudfront-Type-CachePolicyConfig-DefaultTTL"></a>
The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value as the object's time to live (TTL) only when the origin does *not* send `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
The default value for this field is 86400 seconds (one day). If the value of `MinTTL` is more than 86400 seconds, then the default value for this field is the same as the value of `MinTTL`.  
Type: Long  
Required: No

 ** MaxTTL **   <a name="cloudfront-Type-CachePolicyConfig-MaxTTL"></a>
The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value only when the origin sends `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
The default value for this field is 31536000 seconds (one year). If the value of `MinTTL` or `DefaultTTL` is more than 31536000 seconds, then the default value for this field is the same as the value of `DefaultTTL`.  
Type: Long  
Required: No

 ** ParametersInCacheKeyAndForwardedToOrigin **   <a name="cloudfront-Type-CachePolicyConfig-ParametersInCacheKeyAndForwardedToOrigin"></a>
The HTTP headers, cookies, and URL query strings to include in the cache key. The values included in the cache key are also included in requests that CloudFront sends to the origin.  
Type: [ParametersInCacheKeyAndForwardedToOrigin](API_ParametersInCacheKeyAndForwardedToOrigin.md) object  
Required: No

## See Also
<a name="API_CachePolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyConfig) 