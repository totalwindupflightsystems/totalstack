---
id: "@specs/aws/cloudfront/docs/API_AllowedMethods"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AllowedMethods"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AllowedMethods

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AllowedMethods
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AllowedMethods
<a name="API_AllowedMethods"></a>

A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
+ CloudFront forwards only `GET` and `HEAD` requests.
+ CloudFront forwards only `GET`, `HEAD`, and `OPTIONS` requests.
+ CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST`, and `DELETE` requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.

## Contents
<a name="API_AllowedMethods_Contents"></a>

 ** Items **   <a name="cloudfront-Type-AllowedMethods-Items"></a>
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.  
Type: Array of strings  
Valid Values: `GET | HEAD | POST | PUT | PATCH | OPTIONS | DELETE`   
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-AllowedMethods-Quantity"></a>
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for `GET` and `HEAD` requests), 3 (for `GET`, `HEAD`, and `OPTIONS` requests) and 7 (for `GET, HEAD, OPTIONS, PUT, PATCH, POST`, and `DELETE` requests).  
Type: Integer  
Required: Yes

 ** CachedMethods **   <a name="cloudfront-Type-AllowedMethods-CachedMethods"></a>
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:  
+ CloudFront caches responses to `GET` and `HEAD` requests.
+ CloudFront caches responses to `GET`, `HEAD`, and `OPTIONS` requests.
If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.  
Type: [CachedMethods](API_CachedMethods.md) object  
Required: No

## See Also
<a name="API_AllowedMethods_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AllowedMethods) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AllowedMethods) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AllowedMethods) 