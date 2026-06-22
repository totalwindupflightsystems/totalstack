---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetAgentCollaborator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgentCollaborator"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAgentCollaborator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetAgentCollaborator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgentCollaborator
<a name="API_agent_GetAgentCollaborator"></a>

Retrieves information about an agent's collaborator.

## Request Syntax
<a name="API_agent_GetAgentCollaborator_RequestSyntax"></a>

```
GET /agents/{{agentId}}/agentversions/{{agentVersion}}/agentcollaborators/{{collaboratorId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetAgentCollaborator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_GetAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_GetAgentCollaborator-request-uri-agentId"></a>
The agent's ID.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_GetAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_GetAgentCollaborator-request-uri-agentVersion"></a>
The agent's version.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** [collaboratorId](#API_agent_GetAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_GetAgentCollaborator-request-uri-collaboratorId"></a>
The collaborator's ID.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_GetAgentCollaborator_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetAgentCollaborator_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentCollaborator": { 
      "agentDescriptor": { 
         "aliasArn": "string"
      },
      "agentId": "string",
      "agentVersion": "string",
      "clientToken": "string",
      "collaborationInstruction": "string",
      "collaboratorId": "string",
      "collaboratorName": "string",
      "createdAt": "string",
      "lastUpdatedAt": "string",
      "relayConversationHistory": "string"
   }
}
```

## Response Elements
<a name="API_agent_GetAgentCollaborator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentCollaborator](#API_agent_GetAgentCollaborator_ResponseSyntax) **   <a name="bedrock-agent_GetAgentCollaborator-response-agentCollaborator"></a>
Details about the collaborator.  
Type: [AgentCollaborator](API_agent_AgentCollaborator.md) object

## Errors
<a name="API_agent_GetAgentCollaborator_Errors"></a>

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
<a name="API_agent_GetAgentCollaborator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetAgentCollaborator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetAgentCollaborator) 