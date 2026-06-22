---
id: "@specs/aws/bedrock/docs/API_agent-runtime_GetFlowExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFlowExecution"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetFlowExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_GetFlowExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFlowExecution
<a name="API_agent-runtime_GetFlowExecution"></a>

Retrieves details about a specific flow execution, including its status, start and end times, and any errors that occurred during execution.

## Request Syntax
<a name="API_agent-runtime_GetFlowExecution_RequestSyntax"></a>

```
GET /flows/{{flowIdentifier}}/aliases/{{flowAliasIdentifier}}/executions/{{executionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_GetFlowExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionIdentifier](#API_agent-runtime_GetFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-request-uri-executionIdentifier"></a>
The unique identifier of the flow execution to retrieve.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})`   
Required: Yes

 ** [flowAliasIdentifier](#API_agent-runtime_GetFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-request-uri-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [flowIdentifier](#API_agent-runtime_GetFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_GetFlowExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_GetFlowExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endedAt": "string",
   "errors": [ 
      { 
         "error": "string",
         "message": "string",
         "nodeName": "string"
      }
   ],
   "executionArn": "string",
   "flowAliasIdentifier": "string",
   "flowIdentifier": "string",
   "flowVersion": "string",
   "startedAt": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_agent-runtime_GetFlowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endedAt](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-endedAt"></a>
The timestamp when the flow execution ended. This field is only populated when the execution has completed, failed, timed out, or been aborted.  
Type: Timestamp

 ** [errors](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-errors"></a>
A list of errors that occurred during the flow execution. Each error includes an error code, message, and the node where the error occurred, if applicable.  
Type: Array of [FlowExecutionError](API_agent-runtime_FlowExecutionError.md) objects

 ** [executionArn](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-executionArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the flow execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})` 

 ** [flowAliasIdentifier](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)` 

 ** [flowIdentifier](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-flowIdentifier"></a>
The unique identifier of the flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})` 

 ** [flowVersion](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-flowVersion"></a>
The version of the flow used for the execution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [startedAt](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-startedAt"></a>
The timestamp when the flow execution started.  
Type: Timestamp

 ** [status](#API_agent-runtime_GetFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetFlowExecution-response-status"></a>
The current status of the flow execution.  
Flow executions time out after 24 hours.  
Type: String  
Valid Values: `Running | Succeeded | Failed | TimedOut | Aborted` 

## Errors
<a name="API_agent-runtime_GetFlowExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
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
<a name="API_agent-runtime_GetFlowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetFlowExecution) 