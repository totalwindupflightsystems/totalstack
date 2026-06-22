---
id: "@specs/aws/bedrock-agent/docs/API_DeletePromptRouter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeletePromptRouter"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeletePromptRouter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_DeletePromptRouter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeletePromptRouter
<a name="API_DeletePromptRouter"></a>

Deletes a specified prompt router. This action cannot be undone.

## Request Syntax
<a name="API_DeletePromptRouter_RequestSyntax"></a>

```
DELETE /prompt-routers/{{promptRouterArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePromptRouter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [promptRouterArn](#API_DeletePromptRouter_RequestSyntax) **   <a name="bedrock-DeletePromptRouter-request-uri-promptRouterArn"></a>
The Amazon Resource Name (ARN) of the prompt router to delete.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+`   
Required: Yes

## Request Body
<a name="API_DeletePromptRouter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePromptRouter_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeletePromptRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePromptRouter_Errors"></a>

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
<a name="API_DeletePromptRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeletePromptRouter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeletePromptRouter) 