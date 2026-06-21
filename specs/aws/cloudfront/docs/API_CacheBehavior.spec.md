---
id: "@specs/aws/cloudfront/docs/API_CacheBehavior"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheBehavior"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CacheBehavior

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CacheBehavior
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheBehavior
<a name="API_CacheBehavior"></a>

A complex type that describes how CloudFront processes requests.

You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to serve objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.

For the current quota (formerly known as limit) on the number of cache behaviors that you can add to a distribution, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) in the *Amazon CloudFront Developer Guide*.

If you don't want to specify any cache behaviors, include only an empty `CacheBehaviors` element. Don't specify an empty individual `CacheBehavior` element, because this is invalid. For more information, see [CacheBehaviors](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CacheBehaviors.html). 

To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty `CacheBehaviors` element.

To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.

**Important**  
If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.

For more information about cache behaviors, see [Cache Behavior Settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_CacheBehavior_Contents"></a>

 ** PathPattern **   <a name="cloudfront-Type-CacheBehavior-PathPattern"></a>
The pattern (for example, `images/*.jpg`) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.  
You can optionally include a slash (`/`) at the beginning of the path pattern. For example, `/images/*.jpg`. CloudFront behavior is the same with or without the leading `/`.
The path pattern for the default cache behavior is `*` and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.  
For more information, see [Path Pattern](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern) in the * Amazon CloudFront Developer Guide*.  
Type: String  
Required: Yes

 ** TargetOriginId **   <a name="cloudfront-Type-CacheBehavior-TargetOriginId"></a>
The value of `ID` for the origin that you want CloudFront to route requests to when they match this cache behavior.  
Type: String  
Required: Yes

 ** ViewerProtocolPolicy **   <a name="cloudfront-Type-CacheBehavior-ViewerProtocolPolicy"></a>
The protocol that viewers can use to access the files in the origin specified by `TargetOriginId` when a request matches the path pattern in `PathPattern`. You can specify the following options:  
+  `allow-all`: Viewers can use HTTP or HTTPS.
+  `redirect-to-https`: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
+  `https-only`: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
For more information about requiring the HTTPS protocol, see [Requiring HTTPS Between Viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in the *Amazon CloudFront Developer Guide*.  
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see [Managing Cache Expiration](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.
Type: String  
Valid Values: `allow-all | https-only | redirect-to-https`   
Required: Yes

 ** AllowedMethods **   <a name="cloudfront-Type-CacheBehavior-AllowedMethods"></a>
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:  
+ CloudFront forwards only `GET` and `HEAD` requests.
+ CloudFront forwards only `GET`, `HEAD`, and `OPTIONS` requests.
+ CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST`, and `DELETE` requests.
If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.  
Type: [AllowedMethods](API_AllowedMethods.md) object  
Required: No

 ** CachePolicyId **   <a name="cloudfront-Type-CacheBehavior-CachePolicyId"></a>
The unique identifier of the cache policy that is attached to this cache behavior. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide*.  
A `CacheBehavior` must include either a `CachePolicyId` or `ForwardedValues`. We recommend that you use a `CachePolicyId`.  
Type: String  
Required: No

 ** Compress **   <a name="cloudfront-Type-CacheBehavior-Compress"></a>
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see [Serving Compressed Files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html) in the *Amazon CloudFront Developer Guide*.  
Type: Boolean  
Required: No

 ** DefaultTTL **   <a name="cloudfront-Type-CacheBehavior-DefaultTTL"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
This field is deprecated. We recommend that you use the `DefaultTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide*.  
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as `Cache-Control max-age`, `Cache-Control s-maxage`, and `Expires` to objects. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
Type: Long  
Required: No

 ** FieldLevelEncryptionId **   <a name="cloudfront-Type-CacheBehavior-FieldLevelEncryptionId"></a>
The value of `ID` for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for this cache behavior.  
Type: String  
Required: No

 ** ForwardedValues **   <a name="cloudfront-Type-CacheBehavior-ForwardedValues"></a>
This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field. For more information, see [Working with policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) in the *Amazon CloudFront Developer Guide*.  
If you want to include values in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide*.  
If you want to send values to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) or [Using the managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html) in the *Amazon CloudFront Developer Guide*.  
A `CacheBehavior` must include either a `CachePolicyId` or `ForwardedValues`. We recommend that you use a `CachePolicyId`.  
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.  
Type: [ForwardedValues](API_ForwardedValues.md) object  
Required: No

 ** FunctionAssociations **   <a name="cloudfront-Type-CacheBehavior-FunctionAssociations"></a>
A list of CloudFront functions that are associated with this cache behavior. CloudFront functions must be published to the `LIVE` stage to associate them with a cache behavior.  
Type: [FunctionAssociations](API_FunctionAssociations.md) object  
Required: No

 ** GrpcConfig **   <a name="cloudfront-Type-CacheBehavior-GrpcConfig"></a>
The gRPC configuration for your cache behavior.  
Type: [GrpcConfig](API_GrpcConfig.md) object  
Required: No

 ** LambdaFunctionAssociations **   <a name="cloudfront-Type-CacheBehavior-LambdaFunctionAssociations"></a>
A complex type that contains zero or more Lambda@Edge function associations for a cache behavior.  
Type: [LambdaFunctionAssociations](API_LambdaFunctionAssociations.md) object  
Required: No

 ** MaxTTL **   <a name="cloudfront-Type-CacheBehavior-MaxTTL"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
This field is deprecated. We recommend that you use the `MaxTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide*.  
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as `Cache-Control max-age`, `Cache-Control s-maxage`, and `Expires` to objects. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide*.  
Type: Long  
Required: No

 ** MinTTL **   <a name="cloudfront-Type-CacheBehavior-MinTTL"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
This field is deprecated. We recommend that you use the `MinTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide*.  
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see [ Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the * Amazon CloudFront Developer Guide*.  
You must specify `0` for `MinTTL` if you configure CloudFront to forward all headers to your origin (under `Headers`, if you specify `1` for `Quantity` and `*` for `Name`).  
Type: Long  
Required: No

 ** OriginRequestPolicyId **   <a name="cloudfront-Type-CacheBehavior-OriginRequestPolicyId"></a>
The unique identifier of the origin request policy that is attached to this cache behavior. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) or [Using the managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html) in the *Amazon CloudFront Developer Guide*.  
Type: String  
Required: No

 ** RealtimeLogConfigArn **   <a name="cloudfront-Type-CacheBehavior-RealtimeLogConfigArn"></a>
The Amazon Resource Name (ARN) of the real-time log configuration that is attached to this cache behavior. For more information, see [Real-time logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html) in the *Amazon CloudFront Developer Guide*.  
Type: String  
Required: No

 ** ResponseHeadersPolicyId **   <a name="cloudfront-Type-CacheBehavior-ResponseHeadersPolicyId"></a>
The identifier for a response headers policy.  
Type: String  
Required: No

 ** SmoothStreaming **   <a name="cloudfront-Type-CacheBehavior-SmoothStreaming"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify `true`; if not, specify `false`. If you specify `true` for `SmoothStreaming`, you can still distribute other content using this cache behavior if the content matches the value of `PathPattern`.  
Type: Boolean  
Required: No

 ** TrustedKeyGroups **   <a name="cloudfront-Type-CacheBehavior-TrustedKeyGroups"></a>
A list of key groups that CloudFront can use to validate signed URLs or signed cookies.  
When a cache behavior contains trusted key groups, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.  
Type: [TrustedKeyGroups](API_TrustedKeyGroups.md) object  
Required: No

 ** TrustedSigners **   <a name="cloudfront-Type-CacheBehavior-TrustedSigners"></a>
We recommend using `TrustedKeyGroups` instead of `TrustedSigners`.
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A list of AWS account IDs whose public keys CloudFront can use to validate signed URLs or signed cookies.  
When a cache behavior contains trusted signers, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with the private key of a CloudFront key pair in the trusted signer's AWS account. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.  
Type: [TrustedSigners](API_TrustedSigners.md) object  
Required: No

## See Also
<a name="API_CacheBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheBehavior) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheBehavior) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheBehavior) 