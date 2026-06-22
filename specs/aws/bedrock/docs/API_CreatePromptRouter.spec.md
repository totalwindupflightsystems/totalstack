---
id: "@specs/aws/bedrock/docs/API_CreatePromptRouter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreatePromptRouter"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreatePromptRouter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreatePromptRouter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreatePromptRouter
<a name="API_CreatePromptRouter"></a>

Creates a prompt router that manages the routing of requests between multiple foundation models based on the routing criteria.

## Request Syntax
<a name="API_CreatePromptRouter_RequestSyntax"></a>

```
POST /prompt-routers HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "description": "{{string}}",
   "fallbackModel": { 
      "modelArn": "{{string}}"
   },
   "models": [ 
      { 
         "modelArn": "{{string}}"
      }
   ],
   "promptRouterName": "{{string}}",
   "routingCriteria": { 
      "responseQualityDifference": {{number}}
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreatePromptRouter_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePromptRouter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the AWS SDK automatically generates one for you.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [description](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-description"></a>
An optional description of the prompt router to help identify its purpose.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `([0-9a-zA-Z:.][ _-]?)+`   
Required: No

 ** [fallbackModel](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-fallbackModel"></a>
The default model to use when the routing criteria is not met.  
Type: [PromptRouterTargetModel](API_PromptRouterTargetModel.md) object  
Required: Yes

 ** [models](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-models"></a>
A list of foundation models that the prompt router can route requests to. At least one model must be specified.  
Type: Array of [PromptRouterTargetModel](API_PromptRouterTargetModel.md) objects  
Required: Yes

 ** [promptRouterName](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-promptRouterName"></a>
The name of the prompt router. The name must be unique within your AWS account in the current region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `([0-9a-zA-Z][ _-]?)+`   
Required: Yes

 ** [routingCriteria](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-routingCriteria"></a>
The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.  
Type: [RoutingCriteria](API_RoutingCriteria.md) object  
Required: Yes

 ** [tags](#API_CreatePromptRouter_RequestSyntax) **   <a name="bedrock-CreatePromptRouter-request-tags"></a>
An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your AWS resources.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreatePromptRouter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "promptRouterArn": "string"
}
```

## Response Elements
<a name="API_CreatePromptRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [promptRouterArn](#API_CreatePromptRouter_ResponseSyntax) **   <a name="bedrock-CreatePromptRouter-response-promptRouterArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the prompt router.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+` 

## Errors
<a name="API_CreatePromptRouter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreatePromptRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreatePromptRouter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreatePromptRouter) 