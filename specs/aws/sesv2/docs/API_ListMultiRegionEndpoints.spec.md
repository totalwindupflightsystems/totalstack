---
id: "@specs/aws/sesv2/docs/API_ListMultiRegionEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListMultiRegionEndpoints"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListMultiRegionEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListMultiRegionEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListMultiRegionEndpoints
<a name="API_ListMultiRegionEndpoints"></a>

List the multi-region endpoints (global-endpoints).

Only multi-region endpoints (global-endpoints) whose primary region is the AWS-Region where operation is executed will be listed.

## Request Syntax
<a name="API_ListMultiRegionEndpoints_RequestSyntax"></a>

```
GET /v2/email/multi-region-endpoints?NextToken={{NextToken}}&PageSize={{PageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMultiRegionEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_ListMultiRegionEndpoints_RequestSyntax) **   <a name="SES-ListMultiRegionEndpoints-request-uri-NextToken"></a>
A token returned from a previous call to `ListMultiRegionEndpoints` to indicate the position in the list of multi-region endpoints (global-endpoints).  
Length Constraints: Minimum length of 1. Maximum length of 5000.  
Pattern: `^^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$` 

 ** [PageSize](#API_ListMultiRegionEndpoints_RequestSyntax) **   <a name="SES-ListMultiRegionEndpoints-request-uri-PageSize"></a>
The number of results to show in a single call to `ListMultiRegionEndpoints`. If the number of results is larger than the number you specified in this parameter, the response includes a `NextToken` element that you can use to retrieve the next page of results.   
Valid Range: Minimum value of 1. Maximum value of 1000.

## Request Body
<a name="API_ListMultiRegionEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMultiRegionEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MultiRegionEndpoints": [ 
      { 
         "CreatedTimestamp": number,
         "EndpointId": "string",
         "EndpointName": "string",
         "LastUpdatedTimestamp": number,
         "Regions": [ "string" ],
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMultiRegionEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MultiRegionEndpoints](#API_ListMultiRegionEndpoints_ResponseSyntax) **   <a name="SES-ListMultiRegionEndpoints-response-MultiRegionEndpoints"></a>
An array that contains key multi-region endpoint (global-endpoint) properties.  
Type: Array of [MultiRegionEndpoint](API_MultiRegionEndpoint.md) objects

 ** [NextToken](#API_ListMultiRegionEndpoints_ResponseSyntax) **   <a name="SES-ListMultiRegionEndpoints-response-NextToken"></a>
A token indicating that there are additional multi-region endpoints (global-endpoints) available to be listed. Pass this token to a subsequent `ListMultiRegionEndpoints` call to retrieve the next page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5000.  
Pattern: `^^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$` 

## Errors
<a name="API_ListMultiRegionEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListMultiRegionEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListMultiRegionEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListMultiRegionEndpoints) 