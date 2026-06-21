---
id: "@specs/aws/cloudfront/docs/API_CachePolicyCookiesConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachePolicyCookiesConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CachePolicyCookiesConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CachePolicyCookiesConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachePolicyCookiesConfig
<a name="API_CachePolicyCookiesConfig"></a>

An object that determines whether any cookies in viewer requests (and if so, which cookies) are included in the cache key and in requests that CloudFront sends to the origin.

## Contents
<a name="API_CachePolicyCookiesConfig_Contents"></a>

 ** CookieBehavior **   <a name="cloudfront-Type-CachePolicyCookiesConfig-CookieBehavior"></a>
Determines whether any cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:  
+  `none` – No cookies in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none`, any cookies that are listed in an `OriginRequestPolicy` *are* included in origin requests.
+  `whitelist` – Only the cookies in viewer requests that are listed in the `CookieNames` type are included in the cache key and in requests that CloudFront sends to the origin.
+  `allExcept` – All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * for those that are listed in the `CookieNames` type, which are not included.
+  `all` – All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.
Type: String  
Valid Values: `none | whitelist | allExcept | all`   
Required: Yes

 ** Cookies **   <a name="cloudfront-Type-CachePolicyCookiesConfig-Cookies"></a>
Contains a list of cookie names.  
Type: [CookieNames](API_CookieNames.md) object  
Required: No

## See Also
<a name="API_CachePolicyCookiesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyCookiesConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyCookiesConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyCookiesConfig) 