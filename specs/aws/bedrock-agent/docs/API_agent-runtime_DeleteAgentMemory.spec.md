---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_DeleteAgentMemory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAgentMemory"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteAgentMemory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_DeleteAgentMemory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAgentMemory
<a name="API_agent-runtime_DeleteAgentMemory"></a>

Deletes memory from the specified memory identifier.

## Request Syntax
<a name="API_agent-runtime_DeleteAgentMemory_RequestSyntax"></a>

```
DELETE /agents/{{agentId}}/agentAliases/{{agentAliasId}}/memories?memoryId={{memoryId}}&sessionId={{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_DeleteAgentMemory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentAliasId](#API_agent-runtime_DeleteAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_DeleteAgentMemory-request-uri-agentAliasId"></a>
The unique identifier of an alias of an agent.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [agentId](#API_agent-runtime_DeleteAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_DeleteAgentMemory-request-uri-agentId"></a>
The unique identifier of the agent to which the alias belongs.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [memoryId](#API_agent-runtime_DeleteAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_DeleteAgentMemory-request-uri-memoryId"></a>
The unique identifier of the memory.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

 ** [sessionId](#API_agent-runtime_DeleteAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_DeleteAgentMemory-request-uri-sessionId"></a>
The unique session identifier of the memory.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

## Request Body
<a name="API_agent-runtime_DeleteAgentMemory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_DeleteAgentMemory_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_agent-runtime_DeleteAgentMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_agent-runtime_DeleteAgentMemory_Errors"></a>

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
<a name="API_agent-runtime_DeleteAgentMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/DeleteAgentMemory) 