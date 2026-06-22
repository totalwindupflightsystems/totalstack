---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetAgentKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgentKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAgentKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetAgentKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgentKnowledgeBase
<a name="API_agent_GetAgentKnowledgeBase"></a>

Gets information about a knowledge base associated with an agent.

## Request Syntax
<a name="API_agent_GetAgentKnowledgeBase_RequestSyntax"></a>

```
GET /agents/{{agentId}}/agentversions/{{agentVersion}}/knowledgebases/{{knowledgeBaseId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetAgentKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_GetAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_GetAgentKnowledgeBase-request-uri-agentId"></a>
The unique identifier of the agent with which the knowledge base is associated.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_GetAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_GetAgentKnowledgeBase-request-uri-agentVersion"></a>
The version of the agent with which the knowledge base is associated.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_GetAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_GetAgentKnowledgeBase-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base associated with the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_GetAgentKnowledgeBase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetAgentKnowledgeBase_ResponseSyntax"></a>

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
<a name="API_agent_GetAgentKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentKnowledgeBase](#API_agent_GetAgentKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_GetAgentKnowledgeBase-response-agentKnowledgeBase"></a>
Contains details about a knowledge base attached to an agent.  
Type: [AgentKnowledgeBase](API_agent_AgentKnowledgeBase.md) object

## Errors
<a name="API_agent_GetAgentKnowledgeBase_Errors"></a>

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
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_GetAgentKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetAgentKnowledgeBase) 