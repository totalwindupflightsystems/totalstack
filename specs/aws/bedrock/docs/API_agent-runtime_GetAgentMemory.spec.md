---
id: "@specs/aws/bedrock/docs/API_agent-runtime_GetAgentMemory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgentMemory"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAgentMemory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_GetAgentMemory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgentMemory
<a name="API_agent-runtime_GetAgentMemory"></a>

Gets the sessions stored in the memory of the agent.

## Request Syntax
<a name="API_agent-runtime_GetAgentMemory_RequestSyntax"></a>

```
GET /agents/{{agentId}}/agentAliases/{{agentAliasId}}/memories?maxItems={{maxItems}}&memoryId={{memoryId}}&memoryType={{memoryType}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_GetAgentMemory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentAliasId](#API_agent-runtime_GetAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-request-uri-agentAliasId"></a>
The unique identifier of an alias of an agent.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [agentId](#API_agent-runtime_GetAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-request-uri-agentId"></a>
The unique identifier of the agent to which the alias belongs.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [maxItems](#API_agent-runtime_GetAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-request-uri-maxItems"></a>
The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [memoryId](#API_agent-runtime_GetAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-request-uri-memoryId"></a>
The unique identifier of the memory.   
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: Yes

 ** [memoryType](#API_agent-runtime_GetAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-request-uri-memoryType"></a>
The type of memory.  
Valid Values: `SESSION_SUMMARY`   
Required: Yes

 ** [nextToken](#API_agent-runtime_GetAgentMemory_RequestSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-request-uri-nextToken"></a>
If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_agent-runtime_GetAgentMemory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_GetAgentMemory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memoryContents": [ 
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent-runtime_GetAgentMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memoryContents](#API_agent-runtime_GetAgentMemory_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-response-memoryContents"></a>
Contains details of the sessions stored in the memory  
Type: Array of [Memory](API_agent-runtime_Memory.md) objects

 ** [nextToken](#API_agent-runtime_GetAgentMemory_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetAgentMemory-response-nextToken"></a>
If the total number of results is greater than the maxItems value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent-runtime_GetAgentMemory_Errors"></a>

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
<a name="API_agent-runtime_GetAgentMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetAgentMemory) 