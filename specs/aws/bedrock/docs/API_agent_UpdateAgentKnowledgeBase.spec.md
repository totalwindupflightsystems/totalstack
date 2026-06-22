---
id: "@specs/aws/bedrock/docs/API_agent_UpdateAgentKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAgentKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateAgentKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_UpdateAgentKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAgentKnowledgeBase
<a name="API_agent_UpdateAgentKnowledgeBase"></a>

Updates the configuration for a knowledge base that has been associated with an agent.

## Request Syntax
<a name="API_agent_UpdateAgentKnowledgeBase_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/agentversions/{{agentVersion}}/knowledgebases/{{knowledgeBaseId}}/ HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "knowledgeBaseState": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_UpdateAgentKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_UpdateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentKnowledgeBase-request-uri-agentId"></a>
The unique identifier of the agent associated with the knowledge base that you want to update.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_UpdateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentKnowledgeBase-request-uri-agentVersion"></a>
The version of the agent associated with the knowledge base that you want to update.  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_UpdateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentKnowledgeBase-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that has been associated with an agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_UpdateAgentKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_agent_UpdateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentKnowledgeBase-request-description"></a>
Specifies a new description for the knowledge base associated with an agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [knowledgeBaseState](#API_agent_UpdateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentKnowledgeBase-request-knowledgeBaseState"></a>
Specifies whether the agent uses the knowledge base or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## Response Syntax
<a name="API_agent_UpdateAgentKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentKnowledgeBase": { 
      "agentId": "string",
      "agentVersion": "string",
      "createdAt": "string",
      "description": "string",
      "knowledgeBaseId": "string",
      "knowledgeBaseState": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_UpdateAgentKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentKnowledgeBase](#API_agent_UpdateAgentKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_UpdateAgentKnowledgeBase-response-agentKnowledgeBase"></a>
Contains details about the knowledge base that has been associated with an agent.  
Type: [AgentKnowledgeBase](API_agent_AgentKnowledgeBase.md) object

## Errors
<a name="API_agent_UpdateAgentKnowledgeBase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation.  
HTTP Status Code: 409

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
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_UpdateAgentKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateAgentKnowledgeBase) 