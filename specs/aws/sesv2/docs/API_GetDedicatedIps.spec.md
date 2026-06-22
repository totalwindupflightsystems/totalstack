---
id: "@specs/aws/sesv2/docs/API_GetDedicatedIps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDedicatedIps"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetDedicatedIps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetDedicatedIps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDedicatedIps
<a name="API_GetDedicatedIps"></a>

List the dedicated IP addresses that are associated with your AWS account.

## Request Syntax
<a name="API_GetDedicatedIps_RequestSyntax"></a>

```
GET /v2/email/dedicated-ips?NextToken={{NextToken}}&PageSize={{PageSize}}&PoolName={{PoolName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDedicatedIps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_GetDedicatedIps_RequestSyntax) **   <a name="SES-GetDedicatedIps-request-uri-NextToken"></a>
A token returned from a previous call to `GetDedicatedIps` to indicate the position of the dedicated IP pool in the list of IP pools.

 ** [PageSize](#API_GetDedicatedIps_RequestSyntax) **   <a name="SES-GetDedicatedIps-request-uri-PageSize"></a>
The number of results to show in a single call to `GetDedicatedIpsRequest`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.

 ** [PoolName](#API_GetDedicatedIps_RequestSyntax) **   <a name="SES-GetDedicatedIps-request-uri-PoolName"></a>
The name of the IP pool that the dedicated IP address is associated with.

## Request Body
<a name="API_GetDedicatedIps_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDedicatedIps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DedicatedIps": [ 
      { 
         "Ip": "string",
         "PoolName": "string",
         "WarmupPercentage": number,
         "WarmupStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetDedicatedIps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DedicatedIps](#API_GetDedicatedIps_ResponseSyntax) **   <a name="SES-GetDedicatedIps-response-DedicatedIps"></a>
A list of dedicated IP addresses that are associated with your AWS account.  
Type: Array of [DedicatedIp](API_DedicatedIp.md) objects

 ** [NextToken](#API_GetDedicatedIps_ResponseSyntax) **   <a name="SES-GetDedicatedIps-response-NextToken"></a>
A token that indicates that there are additional dedicated IP addresses to list. To view additional addresses, issue another request to `GetDedicatedIps`, passing this token in the `NextToken` parameter.  
Type: String

## Errors
<a name="API_GetDedicatedIps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetDedicatedIps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetDedicatedIps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetDedicatedIps) 