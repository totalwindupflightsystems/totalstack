---
id: "@specs/aws/bedrock/docs/API_agent_AssociateAgentCollaborator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateAgentCollaborator"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# AssociateAgentCollaborator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_AssociateAgentCollaborator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateAgentCollaborator
<a name="API_agent_AssociateAgentCollaborator"></a>

Makes an agent a collaborator for another agent.

## Request Syntax
<a name="API_agent_AssociateAgentCollaborator_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/agentversions/{{agentVersion}}/agentcollaborators/ HTTP/1.1
Content-type: application/json

{
   "agentDescriptor": { 
      "aliasArn": "{{string}}"
   },
   "clientToken": "{{string}}",
   "collaborationInstruction": "{{string}}",
   "collaboratorName": "{{string}}",
   "relayConversationHistory": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_AssociateAgentCollaborator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-uri-agentId"></a>
The agent's ID.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-uri-agentVersion"></a>
An agent version.  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

## Request Body
<a name="API_agent_AssociateAgentCollaborator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentDescriptor](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-agentDescriptor"></a>
The alias of the collaborator agent.  
Type: [AgentDescriptor](API_agent_AgentDescriptor.md) object  
Required: Yes

 ** [clientToken](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-clientToken"></a>
A client token.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [collaborationInstruction](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-collaborationInstruction"></a>
Instruction for the collaborator.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4000.  
Required: Yes

 ** [collaboratorName](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-collaboratorName"></a>
A name for the collaborator.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [relayConversationHistory](#API_agent_AssociateAgentCollaborator_RequestSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-request-relayConversationHistory"></a>
A relay conversation history for the collaborator.  
Type: String  
Valid Values: `TO_COLLABORATOR | DISABLED`   
Required: No

## Response Syntax
<a name="API_agent_AssociateAgentCollaborator_ResponseSyntax"></a>

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
<a name="API_agent_AssociateAgentCollaborator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentCollaborator](#API_agent_AssociateAgentCollaborator_ResponseSyntax) **   <a name="bedrock-agent_AssociateAgentCollaborator-response-agentCollaborator"></a>
Details about the collaborator.  
Type: [AgentCollaborator](API_agent_AgentCollaborator.md) object

## Errors
<a name="API_agent_AssociateAgentCollaborator_Errors"></a>

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
<a name="API_agent_AssociateAgentCollaborator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AssociateAgentCollaborator) 