---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetAgentActionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgentActionGroup"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAgentActionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetAgentActionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgentActionGroup
<a name="API_agent_GetAgentActionGroup"></a>

Gets information about an action group for an agent.

## Request Syntax
<a name="API_agent_GetAgentActionGroup_RequestSyntax"></a>

```
GET /agents/{{agentId}}/agentversions/{{agentVersion}}/actiongroups/{{actionGroupId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetAgentActionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionGroupId](#API_agent_GetAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_GetAgentActionGroup-request-uri-actionGroupId"></a>
The unique identifier of the action group for which to get information.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentId](#API_agent_GetAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_GetAgentActionGroup-request-uri-agentId"></a>
The unique identifier of the agent that the action group belongs to.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_GetAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_GetAgentActionGroup-request-uri-agentVersion"></a>
The version of the agent that the action group belongs to.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

## Request Body
<a name="API_agent_GetAgentActionGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetAgentActionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentActionGroup": { 
      "actionGroupExecutor": { ... },
      "actionGroupId": "string",
      "actionGroupName": "string",
      "actionGroupState": "string",
      "agentId": "string",
      "agentVersion": "string",
      "apiSchema": { ... },
      "clientToken": "string",
      "createdAt": "string",
      "description": "string",
      "functionSchema": { ... },
      "parentActionGroupSignatureParams": { 
         "string" : "string" 
      },
      "parentActionSignature": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_GetAgentActionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentActionGroup](#API_agent_GetAgentActionGroup_ResponseSyntax) **   <a name="bedrock-agent_GetAgentActionGroup-response-agentActionGroup"></a>
Contains details about the action group.  
Type: [AgentActionGroup](API_agent_AgentActionGroup.md) object

## Errors
<a name="API_agent_GetAgentActionGroup_Errors"></a>

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

## Examples
<a name="API_agent_GetAgentActionGroup_Examples"></a>

### Example request
<a name="API_agent_GetAgentActionGroup_Example_1"></a>

This example illustrates one usage of GetAgentActionGroup.

```
GET /agents/AGENT12345/agentversions/1/actiongroups/ACTION1234/ HTTP/1.1
```

## See Also
<a name="API_agent_GetAgentActionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetAgentActionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetAgentActionGroup) 