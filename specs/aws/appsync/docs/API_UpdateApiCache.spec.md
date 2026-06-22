---
id: "@specs/aws/appsync/docs/API_UpdateApiCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateApiCache"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# UpdateApiCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_UpdateApiCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateApiCache
<a name="API_UpdateApiCache"></a>

Updates the cache for the GraphQL API.

## Request Syntax
<a name="API_UpdateApiCache_RequestSyntax"></a>

```
POST /v1/apis/{{apiId}}/ApiCaches/update HTTP/1.1
Content-type: application/json

{
   "apiCachingBehavior": "{{string}}",
   "healthMetricsConfig": "{{string}}",
   "ttl": {{number}},
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApiCache_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_UpdateApiCache_RequestSyntax) **   <a name="appsync-UpdateApiCache-request-uri-apiId"></a>
The GraphQL API ID.  
Required: Yes

## Request Body
<a name="API_UpdateApiCache_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiCachingBehavior](#API_UpdateApiCache_RequestSyntax) **   <a name="appsync-UpdateApiCache-request-apiCachingBehavior"></a>
Caching behavior.  
+  **FULL\_REQUEST\_CACHING**: All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.
+  **PER\_RESOLVER\_CACHING**: Individual resolvers that you specify are cached.
+  **OPERATION\_LEVEL\_CACHING**: Full requests are cached together and returned without executing resolvers.
Type: String  
Valid Values: `FULL_REQUEST_CACHING | PER_RESOLVER_CACHING | OPERATION_LEVEL_CACHING`   
Required: Yes

 ** [healthMetricsConfig](#API_UpdateApiCache_RequestSyntax) **   <a name="appsync-UpdateApiCache-request-healthMetricsConfig"></a>
Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:  
+ NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.
+ EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.
Metrics will be recorded by API ID. You can set the value to `ENABLED` or `DISABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [ttl](#API_UpdateApiCache_RequestSyntax) **   <a name="appsync-UpdateApiCache-request-ttl"></a>
TTL in seconds for cache entries.  
Valid values are 1–3,600 seconds.  
Type: Long  
Required: Yes

 ** [type](#API_UpdateApiCache_RequestSyntax) **   <a name="appsync-UpdateApiCache-request-type"></a>
The cache instance type. Valid values are   
+  `SMALL` 
+  `MEDIUM` 
+  `LARGE` 
+  `XLARGE` 
+  `LARGE_2X` 
+  `LARGE_4X` 
+  `LARGE_8X` (not available in all regions)
+  `LARGE_12X` 
Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.  
The following legacy instance types are available, but their use is discouraged:  
+  **T2\_SMALL**: A t2.small instance type.
+  **T2\_MEDIUM**: A t2.medium instance type.
+  **R4\_LARGE**: A r4.large instance type.
+  **R4\_XLARGE**: A r4.xlarge instance type.
+  **R4\_2XLARGE**: A r4.2xlarge instance type.
+  **R4\_4XLARGE**: A r4.4xlarge instance type.
+  **R4\_8XLARGE**: A r4.8xlarge instance type.
Type: String  
Valid Values: `T2_SMALL | T2_MEDIUM | R4_LARGE | R4_XLARGE | R4_2XLARGE | R4_4XLARGE | R4_8XLARGE | SMALL | MEDIUM | LARGE | XLARGE | LARGE_2X | LARGE_4X | LARGE_8X | LARGE_12X`   
Required: Yes

## Response Syntax
<a name="API_UpdateApiCache_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiCache": { 
      "apiCachingBehavior": "string",
      "atRestEncryptionEnabled": boolean,
      "healthMetricsConfig": "string",
      "status": "string",
      "transitEncryptionEnabled": boolean,
      "ttl": number,
      "type": "string"
   }
}
```

## Response Elements
<a name="API_UpdateApiCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiCache](#API_UpdateApiCache_ResponseSyntax) **   <a name="appsync-UpdateApiCache-response-apiCache"></a>
The `ApiCache` object.  
Type: [ApiCache](API_ApiCache.md) object

## Errors
<a name="API_UpdateApiCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** ConcurrentModificationException **   
Another modification is in progress at this time and it must complete before you can make your change.  
HTTP Status Code: 409

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_UpdateApiCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/UpdateApiCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/UpdateApiCache) 