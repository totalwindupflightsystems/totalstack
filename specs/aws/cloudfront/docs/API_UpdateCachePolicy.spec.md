---
id: "@specs/aws/cloudfront/docs/API_UpdateCachePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCachePolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateCachePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateCachePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCachePolicy
<a name="API_UpdateCachePolicy"></a>

Updates a cache policy configuration.

When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:

1. Use `GetCachePolicyConfig` to get the current configuration.

1. Locally modify the fields in the cache policy configuration that you want to update.

1. Call `UpdateCachePolicy` by providing the entire cache policy configuration, including the fields that you modified and those that you didn't.

**Important**  
If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.

## Request Syntax
<a name="API_UpdateCachePolicy_RequestSyntax"></a>

```
PUT /2020-05-31/cache-policy/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CachePolicyConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>{{string}}</Comment>
   <DefaultTTL>{{long}}</DefaultTTL>
   <MaxTTL>{{long}}</MaxTTL>
   <MinTTL>{{long}}</MinTTL>
   <Name>{{string}}</Name>
   <ParametersInCacheKeyAndForwardedToOrigin>
      <CookiesConfig>
         <CookieBehavior>{{string}}</CookieBehavior>
         <Cookies>
            <Items>
               <Name>{{string}}</Name>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </Cookies>
      </CookiesConfig>
      <EnableAcceptEncodingBrotli>{{boolean}}</EnableAcceptEncodingBrotli>
      <EnableAcceptEncodingGzip>{{boolean}}</EnableAcceptEncodingGzip>
      <HeadersConfig>
         <HeaderBehavior>{{string}}</HeaderBehavior>
         <Headers>
            <Items>
               <Name>{{string}}</Name>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </Headers>
      </HeadersConfig>
      <QueryStringsConfig>
         <QueryStringBehavior>{{string}}</QueryStringBehavior>
         <QueryStrings>
            <Items>
               <Name>{{string}}</Name>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </QueryStrings>
      </QueryStringsConfig>
   </ParametersInCacheKeyAndForwardedToOrigin>
</CachePolicyConfig>
```

## URI Request Parameters
<a name="API_UpdateCachePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateCachePolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CachePolicyConfig](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-CachePolicyConfig"></a>
Root level tag for the CachePolicyConfig parameters.  
Required: Yes

 ** [Comment](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-Comment"></a>
A comment to describe the cache policy. The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [DefaultTTL](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-DefaultTTL"></a>
The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value as the object's time to live (TTL) only when the origin does *not* send `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
The default value for this field is 86400 seconds (one day). If the value of `MinTTL` is more than 86400 seconds, then the default value for this field is the same as the value of `MinTTL`.  
Type: Long  
Required: No

 ** [MaxTTL](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-MaxTTL"></a>
The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value only when the origin sends `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
The default value for this field is 31536000 seconds (one year). If the value of `MinTTL` or `DefaultTTL` is more than 31536000 seconds, then the default value for this field is the same as the value of `DefaultTTL`.  
Type: Long  
Required: No

 ** [MinTTL](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-MinTTL"></a>
The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
Type: Long  
Required: Yes

 ** [Name](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-Name"></a>
A unique name to identify the cache policy.  
Type: String  
Required: Yes

 ** [ParametersInCacheKeyAndForwardedToOrigin](#API_UpdateCachePolicy_RequestSyntax) **   <a name="cloudfront-UpdateCachePolicy-request-ParametersInCacheKeyAndForwardedToOrigin"></a>
The HTTP headers, cookies, and URL query strings to include in the cache key. The values included in the cache key are also included in requests that CloudFront sends to the origin.  
Type: [ParametersInCacheKeyAndForwardedToOrigin](API_ParametersInCacheKeyAndForwardedToOrigin.md) object  
Required: No

## Response Syntax
<a name="API_UpdateCachePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CachePolicy>
   <CachePolicyConfig>
      <Comment>string</Comment>
      <DefaultTTL>long</DefaultTTL>
      <MaxTTL>long</MaxTTL>
      <MinTTL>long</MinTTL>
      <Name>string</Name>
      <ParametersInCacheKeyAndForwardedToOrigin>
         <CookiesConfig>
            <CookieBehavior>string</CookieBehavior>
            <Cookies>
               <Items>
                  <Name>string</Name>
               </Items>
               <Quantity>integer</Quantity>
            </Cookies>
         </CookiesConfig>
         <EnableAcceptEncodingBrotli>boolean</EnableAcceptEncodingBrotli>
         <EnableAcceptEncodingGzip>boolean</EnableAcceptEncodingGzip>
         <HeadersConfig>
            <HeaderBehavior>string</HeaderBehavior>
            <Headers>
               <Items>
                  <Name>string</Name>
               </Items>
               <Quantity>integer</Quantity>
            </Headers>
         </HeadersConfig>
         <QueryStringsConfig>
            <QueryStringBehavior>string</QueryStringBehavior>
            <QueryStrings>
               <Items>
                  <Name>string</Name>
               </Items>
               <Quantity>integer</Quantity>
            </QueryStrings>
         </QueryStringsConfig>
      </ParametersInCacheKeyAndForwardedToOrigin>
   </CachePolicyConfig>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
</CachePolicy>
```

## Response Elements
<a name="API_UpdateCachePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [CachePolicy](#API_UpdateCachePolicy_ResponseSyntax) **   <a name="cloudfront-UpdateCachePolicy-response-CachePolicy"></a>
Root level tag for the CachePolicy parameters.  
Required: Yes

 ** [CachePolicyConfig](#API_UpdateCachePolicy_ResponseSyntax) **   <a name="cloudfront-UpdateCachePolicy-response-CachePolicyConfig"></a>
The cache policy configuration.  
Type: [CachePolicyConfig](API_CachePolicyConfig.md) object

 ** [Id](#API_UpdateCachePolicy_ResponseSyntax) **   <a name="cloudfront-UpdateCachePolicy-response-Id"></a>
The unique identifier for the cache policy.  
Type: String

 ** [LastModifiedTime](#API_UpdateCachePolicy_ResponseSyntax) **   <a name="cloudfront-UpdateCachePolicy-response-LastModifiedTime"></a>
The date and time when the cache policy was last modified.  
Type: Timestamp

## Errors
<a name="API_UpdateCachePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CachePolicyAlreadyExists **   
A cache policy with this name already exists. You must provide a unique name. To modify an existing cache policy, use `UpdateCachePolicy`.  
HTTP Status Code: 409

 ** IllegalUpdate **   
The update contains modifications that are not allowed.  
HTTP Status Code: 400

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchCachePolicy **   
The cache policy does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** TooManyCookiesInCachePolicy **   
The number of cookies in the cache policy exceeds the maximum. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyHeadersInCachePolicy **   
The number of headers in the cache policy exceeds the maximum. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyQueryStringsInCachePolicy **   
The number of query strings in the cache policy exceeds the maximum. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateCachePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateCachePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateCachePolicy) 