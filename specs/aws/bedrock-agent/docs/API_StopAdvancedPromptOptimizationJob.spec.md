---
id: "@specs/aws/bedrock-agent/docs/API_StopAdvancedPromptOptimizationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopAdvancedPromptOptimizationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# StopAdvancedPromptOptimizationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_StopAdvancedPromptOptimizationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopAdvancedPromptOptimizationJob
<a name="API_StopAdvancedPromptOptimizationJob"></a>

Stops an advanced prompt optimization job that is in progress.

## Request Syntax
<a name="API_StopAdvancedPromptOptimizationJob_RequestSyntax"></a>

```
POST /advanced-prompt-optimization-jobs/{{jobIdentifier}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_StopAdvancedPromptOptimizationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobIdentifier](#API_StopAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-StopAdvancedPromptOptimizationJob-request-uri-jobIdentifier"></a>
The ARN or ID of the advanced prompt optimization job to stop.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/)?[a-z0-9]{12})`   
Required: Yes

## Request Body
<a name="API_StopAdvancedPromptOptimizationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopAdvancedPromptOptimizationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopAdvancedPromptOptimizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopAdvancedPromptOptimizationJob_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_StopAdvancedPromptOptimizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/StopAdvancedPromptOptimizationJob) 