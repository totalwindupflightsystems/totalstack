---
id: "@specs/aws/bedrock-agent/docs/API_GetPromptRouter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPromptRouter"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetPromptRouter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetPromptRouter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPromptRouter
<a name="API_GetPromptRouter"></a>

Retrieves details about a prompt router.

## Request Syntax
<a name="API_GetPromptRouter_RequestSyntax"></a>

```
GET /prompt-routers/{{promptRouterArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPromptRouter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [promptRouterArn](#API_GetPromptRouter_RequestSyntax) **   <a name="bedrock-GetPromptRouter-request-uri-promptRouterArn"></a>
The prompt router's ARN  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+`   
Required: Yes

## Request Body
<a name="API_GetPromptRouter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPromptRouter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "fallbackModel": { 
      "modelArn": "string"
   },
   "models": [ 
      { 
         "modelArn": "string"
      }
   ],
   "promptRouterArn": "string",
   "promptRouterName": "string",
   "routingCriteria": { 
      "responseQualityDifference": number
   },
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetPromptRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-createdAt"></a>
When the router was created.  
Type: Timestamp

 ** [description](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-description"></a>
The router's description.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `([0-9a-zA-Z:.][ _-]?)+` 

 ** [fallbackModel](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-fallbackModel"></a>
The router's fallback model.  
Type: [PromptRouterTargetModel](API_PromptRouterTargetModel.md) object

 ** [models](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-models"></a>
The router's models.  
Type: Array of [PromptRouterTargetModel](API_PromptRouterTargetModel.md) objects

 ** [promptRouterArn](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-promptRouterArn"></a>
The prompt router's ARN  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+` 

 ** [promptRouterName](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-promptRouterName"></a>
The router's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `([0-9a-zA-Z][ _-]?)+` 

 ** [routingCriteria](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-routingCriteria"></a>
The router's routing criteria.  
Type: [RoutingCriteria](API_RoutingCriteria.md) object

 ** [status](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-status"></a>
The router's status.  
Type: String  
Valid Values: `AVAILABLE` 

 ** [type](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-type"></a>
The router's type.  
Type: String  
Valid Values: `custom | default` 

 ** [updatedAt](#API_GetPromptRouter_ResponseSyntax) **   <a name="bedrock-GetPromptRouter-response-updatedAt"></a>
When the router was updated.  
Type: Timestamp

## Errors
<a name="API_GetPromptRouter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_GetPromptRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetPromptRouter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetPromptRouter) 