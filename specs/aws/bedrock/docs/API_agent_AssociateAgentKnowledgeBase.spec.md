---
id: "@specs/aws/bedrock/docs/API_agent_AssociateAgentKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateAgentKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# AssociateAgentKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_AssociateAgentKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateAgentKnowledgeBase
<a name="API_agent_AssociateAgentKnowledgeBase"></a>

Associates a knowledge base with an agent. If a knowledge base is associated and its `indexState` is set to `Enabled`, the agent queries the knowledge base for information to augment its response to the user.

## Request Syntax
<a name="API_agent_AssociateAgentKnowledgeBase_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/agentversions/{{agentVersion}}/knowledgebases/ HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "knowledgeBaseId": "{{string}}",
   "knowledgeBaseState": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_AssociateAgentKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_AssociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentKnowledgeBase-request-uri-agentId"></a>
The unique identifier of the agent with which you want to associate the knowledge base.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_AssociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentKnowledgeBase-request-uri-agentVersion"></a>
The version of the agent with which you want to associate the knowledge base.  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

## Request Body
<a name="API_agent_AssociateAgentKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_agent_AssociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentKnowledgeBase-request-description"></a>
A description of what the agent should use the knowledge base for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: Yes

 ** [knowledgeBaseId](#API_agent_AssociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentKnowledgeBase-request-knowledgeBaseId"></a>
The unique identifier of the knowledge base to associate with the agent.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseState](#API_agent_AssociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentKnowledgeBase-request-knowledgeBaseState"></a>
Specifies whether to use the knowledge base or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## Response Syntax
<a name="API_agent_AssociateAgentKnowledgeBase_ResponseSyntax"></a>

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
<a name="API_agent_AssociateAgentKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentKnowledgeBase](#API_agent_AssociateAgentKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_AssociateAgentKnowledgeBase-response-agentKnowledgeBase"></a>
Contains details about the knowledge base that has been associated with the agent.  
Type: [AgentKnowledgeBase](API_agent_AgentKnowledgeBase.md) object

## Errors
<a name="API_agent_AssociateAgentKnowledgeBase_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 402

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_AssociateAgentKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AssociateAgentKnowledgeBase) 