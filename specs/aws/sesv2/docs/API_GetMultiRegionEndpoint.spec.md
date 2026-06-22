---
id: "@specs/aws/sesv2/docs/API_GetMultiRegionEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMultiRegionEndpoint"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetMultiRegionEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetMultiRegionEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMultiRegionEndpoint
<a name="API_GetMultiRegionEndpoint"></a>

Displays the multi-region endpoint (global-endpoint) configuration.

Only multi-region endpoints (global-endpoints) whose primary region is the AWS-Region where operation is executed can be displayed.

## Request Syntax
<a name="API_GetMultiRegionEndpoint_RequestSyntax"></a>

```
GET /v2/email/multi-region-endpoints/{{EndpointName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMultiRegionEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndpointName](#API_GetMultiRegionEndpoint_RequestSyntax) **   <a name="SES-GetMultiRegionEndpoint-request-uri-EndpointName"></a>
The name of the multi-region endpoint (global-endpoint).  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w\-_]+$`   
Required: Yes

## Request Body
<a name="API_GetMultiRegionEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMultiRegionEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTimestamp": number,
   "EndpointId": "string",
   "EndpointName": "string",
   "LastUpdatedTimestamp": number,
   "Routes": [ 
      { 
         "Region": "string"
      }
   ],
   "Status": "string"
}
```

## Response Elements
<a name="API_GetMultiRegionEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_GetMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-GetMultiRegionEndpoint-response-CreatedTimestamp"></a>
The time stamp of when the multi-region endpoint (global-endpoint) was created.  
Type: Timestamp

 ** [EndpointId](#API_GetMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-GetMultiRegionEndpoint-response-EndpointId"></a>
The ID of the multi-region endpoint (global-endpoint).  
Type: String

 ** [EndpointName](#API_GetMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-GetMultiRegionEndpoint-response-EndpointName"></a>
The name of the multi-region endpoint (global-endpoint).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w\-_]+$` 

 ** [LastUpdatedTimestamp](#API_GetMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-GetMultiRegionEndpoint-response-LastUpdatedTimestamp"></a>
The time stamp of when the multi-region endpoint (global-endpoint) was last updated.  
Type: Timestamp

 ** [Routes](#API_GetMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-GetMultiRegionEndpoint-response-Routes"></a>
Contains routes information for the multi-region endpoint (global-endpoint).  
Type: Array of [Route](API_Route.md) objects

 ** [Status](#API_GetMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-GetMultiRegionEndpoint-response-Status"></a>
The status of the multi-region endpoint (global-endpoint).  
+  `CREATING` – The resource is being provisioned.
+  `READY` – The resource is ready to use.
+  `FAILED` – The resource failed to be provisioned.
+  `DELETING` – The resource is being deleted as requested.
Type: String  
Valid Values: `CREATING | READY | FAILED | DELETING` 

## Errors
<a name="API_GetMultiRegionEndpoint_Errors"></a>

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
<a name="API_GetMultiRegionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetMultiRegionEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetMultiRegionEndpoint) 