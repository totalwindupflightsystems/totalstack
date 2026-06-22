---
id: "@specs/aws/sesv2/docs/API_CreateMultiRegionEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateMultiRegionEndpoint"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateMultiRegionEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateMultiRegionEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateMultiRegionEndpoint
<a name="API_CreateMultiRegionEndpoint"></a>

Creates a multi-region endpoint (global-endpoint).

The primary region is going to be the AWS-Region where the operation is executed. The secondary region has to be provided in request's parameters. From the data flow standpoint there is no difference between primary and secondary regions - sending traffic will be split equally between the two. The primary region is the region where the resource has been created and where it can be managed. 

## Request Syntax
<a name="API_CreateMultiRegionEndpoint_RequestSyntax"></a>

```
POST /v2/email/multi-region-endpoints HTTP/1.1
Content-type: application/json

{
   "Details": { 
      "RoutesDetails": [ 
         { 
            "Region": "{{string}}"
         }
      ]
   },
   "EndpointName": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateMultiRegionEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMultiRegionEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Details](#API_CreateMultiRegionEndpoint_RequestSyntax) **   <a name="SES-CreateMultiRegionEndpoint-request-Details"></a>
Contains details of a multi-region endpoint (global-endpoint) being created.  
Type: [Details](API_Details.md) object  
Required: Yes

 ** [EndpointName](#API_CreateMultiRegionEndpoint_RequestSyntax) **   <a name="SES-CreateMultiRegionEndpoint-request-EndpointName"></a>
The name of the multi-region endpoint (global-endpoint).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w\-_]+$`   
Required: Yes

 ** [Tags](#API_CreateMultiRegionEndpoint_RequestSyntax) **   <a name="SES-CreateMultiRegionEndpoint-request-Tags"></a>
An array of objects that define the tags (keys and values) to associate with the multi-region endpoint (global-endpoint).  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateMultiRegionEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndpointId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateMultiRegionEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointId](#API_CreateMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-CreateMultiRegionEndpoint-response-EndpointId"></a>
The ID of the multi-region endpoint (global-endpoint).  
Type: String

 ** [Status](#API_CreateMultiRegionEndpoint_ResponseSyntax) **   <a name="SES-CreateMultiRegionEndpoint-response-Status"></a>
A status of the multi-region endpoint (global-endpoint) right after the create request.  
+  `CREATING` – The resource is being provisioned.
+  `READY` – The resource is ready to use.
+  `FAILED` – The resource failed to be provisioned.
+  `DELETING` – The resource is being deleted as requested.
Type: String  
Valid Values: `CREATING | READY | FAILED | DELETING` 

## Errors
<a name="API_CreateMultiRegionEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **   
The resource specified in your request already exists.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_CreateMultiRegionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateMultiRegionEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateMultiRegionEndpoint) 