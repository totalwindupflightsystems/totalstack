---
id: "@specs/aws/bedrock/docs/API_agent_DisassociateAgentKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateAgentKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DisassociateAgentKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_DisassociateAgentKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateAgentKnowledgeBase
<a name="API_agent_DisassociateAgentKnowledgeBase"></a>

Disassociates a knowledge base from an agent.

## Request Syntax
<a name="API_agent_DisassociateAgentKnowledgeBase_RequestSyntax"></a>

```
DELETE /agents/{{agentId}}/agentversions/{{agentVersion}}/knowledgebases/{{knowledgeBaseId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DisassociateAgentKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_DisassociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_DisassociateAgentKnowledgeBase-request-uri-agentId"></a>
The unique identifier of the agent from which to disassociate the knowledge base.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_DisassociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_DisassociateAgentKnowledgeBase-request-uri-agentVersion"></a>
The version of the agent from which to disassociate the knowledge base.  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_DisassociateAgentKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_DisassociateAgentKnowledgeBase-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base to disassociate.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_DisassociateAgentKnowledgeBase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DisassociateAgentKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_agent_DisassociateAgentKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_agent_DisassociateAgentKnowledgeBase_Errors"></a>

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
<a name="API_agent_DisassociateAgentKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DisassociateAgentKnowledgeBase) 