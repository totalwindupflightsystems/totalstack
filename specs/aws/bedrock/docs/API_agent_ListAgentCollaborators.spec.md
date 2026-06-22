---
id: "@specs/aws/bedrock/docs/API_agent_ListAgentCollaborators"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAgentCollaborators"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListAgentCollaborators

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_ListAgentCollaborators
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAgentCollaborators
<a name="API_agent_ListAgentCollaborators"></a>

Retrieve a list of an agent's collaborators.

## Request Syntax
<a name="API_agent_ListAgentCollaborators_RequestSyntax"></a>

```
POST /agents/{{agentId}}/agentversions/{{agentVersion}}/agentcollaborators/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_ListAgentCollaborators_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_ListAgentCollaborators_RequestSyntax) **   <a name="bedrock-agent_ListAgentCollaborators-request-uri-agentId"></a>
The agent's ID.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_ListAgentCollaborators_RequestSyntax) **   <a name="bedrock-agent_ListAgentCollaborators-request-uri-agentVersion"></a>
The agent's version.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

## Request Body
<a name="API_agent_ListAgentCollaborators_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_agent_ListAgentCollaborators_RequestSyntax) **   <a name="bedrock-agent_ListAgentCollaborators-request-maxResults"></a>
The maximum number of agent collaborators to return in one page of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_agent_ListAgentCollaborators_RequestSyntax) **   <a name="bedrock-agent_ListAgentCollaborators-request-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

## Response Syntax
<a name="API_agent_ListAgentCollaborators_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentCollaboratorSummaries": [ 
      { 
         "agentDescriptor": { 
            "aliasArn": "string"
         },
         "agentId": "string",
         "agentVersion": "string",
         "collaborationInstruction": "string",
         "collaboratorId": "string",
         "collaboratorName": "string",
         "createdAt": "string",
         "lastUpdatedAt": "string",
         "relayConversationHistory": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListAgentCollaborators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentCollaboratorSummaries](#API_agent_ListAgentCollaborators_ResponseSyntax) **   <a name="bedrock-agent_ListAgentCollaborators-response-agentCollaboratorSummaries"></a>
A list of collaborator summaries.  
Type: Array of [AgentCollaboratorSummary](API_agent_AgentCollaboratorSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [nextToken](#API_agent_ListAgentCollaborators_ResponseSyntax) **   <a name="bedrock-agent_ListAgentCollaborators-response-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent_ListAgentCollaborators_Errors"></a>

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
<a name="API_agent_ListAgentCollaborators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListAgentCollaborators) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListAgentCollaborators) 