---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_InvokeFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InvokeFlow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# InvokeFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_InvokeFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InvokeFlow
<a name="API_agent-runtime_InvokeFlow"></a>

Invokes an alias of a flow to run the inputs that you specify and return the output of each node as a stream. If there's an error, the error is returned. For more information, see [Test a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

**Note**  
The AWS CLI doesn't support streaming operations in Amazon Bedrock, including `InvokeFlow`.

## Request Syntax
<a name="API_agent-runtime_InvokeFlow_RequestSyntax"></a>

```
POST /flows/{{flowIdentifier}}/aliases/{{flowAliasIdentifier}} HTTP/1.1
Content-type: application/json

{
   "enableTrace": {{boolean}},
   "executionId": "{{string}}",
   "inputs": [ 
      { 
         "content": { ... },
         "nodeInputName": "{{string}}",
         "nodeName": "{{string}}",
         "nodeOutputName": "{{string}}"
      }
   ],
   "modelPerformanceConfiguration": { 
      "performanceConfig": { 
         "latency": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_InvokeFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowAliasIdentifier](#API_agent-runtime_InvokeFlow_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-request-uri-flowAliasIdentifier"></a>
The unique identifier of the flow alias.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [flowIdentifier](#API_agent-runtime_InvokeFlow_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_InvokeFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enableTrace](#API_agent-runtime_InvokeFlow_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-request-enableTrace"></a>
Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see [Track each step in your prompt flow by viewing its trace in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html).  
Type: Boolean  
Required: No

 ** [executionId](#API_agent-runtime_InvokeFlow_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-request-executionId"></a>
The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you.   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: No

 ** [inputs](#API_agent-runtime_InvokeFlow_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-request-inputs"></a>
A list of objects, each containing information about an input into the flow.  
Type: Array of [FlowInput](API_agent-runtime_FlowInput.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [modelPerformanceConfiguration](#API_agent-runtime_InvokeFlow_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-request-modelPerformanceConfiguration"></a>
Model performance settings for the request.  
Type: [ModelPerformanceConfiguration](API_agent-runtime_ModelPerformanceConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_InvokeFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-bedrock-flow-execution-id: {{executionId}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "badGatewayException": { 
   },
   "conflictException": { 
   },
   "dependencyFailedException": { 
   },
   "flowCompletionEvent": { 
      "completionReason": "string"
   },
   "flowMultiTurnInputRequestEvent": { 
      "content": { ... },
      "nodeName": "string",
      "nodeType": "string"
   },
   "flowOutputEvent": { 
      "content": { ... },
      "nodeName": "string",
      "nodeType": "string"
   },
   "flowTraceEvent": { 
      "trace": { ... }
   },
   "internalServerException": { 
   },
   "resourceNotFoundException": { 
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_agent-runtime_InvokeFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [executionId](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-executionId"></a>
The unique identifier for the current flow execution.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403

 ** [badGatewayException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.  
Type: Exception  
HTTP Status Code: 502

 ** [conflictException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-conflictException"></a>
There was a conflict performing an operation. Resolve the conflict and retry your request.  
Type: Exception  
HTTP Status Code: 409

 ** [dependencyFailedException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424

 ** [flowCompletionEvent](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-flowCompletionEvent"></a>
Contains information about why the flow completed.  
Type: [FlowCompletionEvent](API_agent-runtime_FlowCompletionEvent.md) object

 ** [flowMultiTurnInputRequestEvent](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-flowMultiTurnInputRequestEvent"></a>
The event stream containing the multi-turn input request information from the flow.  
Type: [FlowMultiTurnInputRequestEvent](API_agent-runtime_FlowMultiTurnInputRequestEvent.md) object

 ** [flowOutputEvent](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-flowOutputEvent"></a>
Contains information about an output from flow invocation.  
Type: [FlowOutputEvent](API_agent-runtime_FlowOutputEvent.md) object

 ** [flowTraceEvent](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-flowTraceEvent"></a>
Contains information about a trace, which tracks an input or output for a node in the flow.  
Type: [FlowTraceEvent](API_agent-runtime_FlowTraceEvent.md) object

 ** [internalServerException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-resourceNotFoundException"></a>
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
Type: Exception  
HTTP Status Code: 404

 ** [serviceQuotaExceededException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-serviceQuotaExceededException"></a>
The number of requests exceeds the service quota. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 400

 ** [throttlingException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-throttlingException"></a>
The number of requests exceeds the limit. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_agent-runtime_InvokeFlow_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeFlow-response-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_agent-runtime_InvokeFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
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

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_agent-runtime_InvokeFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/InvokeFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvokeFlow) 