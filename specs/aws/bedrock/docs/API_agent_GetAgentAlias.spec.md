---
id: "@specs/aws/bedrock/docs/API_agent_GetAgentAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgentAlias"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAgentAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_GetAgentAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgentAlias
<a name="API_agent_GetAgentAlias"></a>

Gets information about an alias of an agent.

## Request Syntax
<a name="API_agent_GetAgentAlias_RequestSyntax"></a>

```
GET /agents/{{agentId}}/agentaliases/{{agentAliasId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetAgentAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentAliasId](#API_agent_GetAgentAlias_RequestSyntax) **   <a name="bedrock-agent_GetAgentAlias-request-uri-agentAliasId"></a>
The unique identifier of the alias for which to get information.  
Length Constraints: Fixed length of 10.  
Pattern: `(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [agentId](#API_agent_GetAgentAlias_RequestSyntax) **   <a name="bedrock-agent_GetAgentAlias-request-uri-agentId"></a>
The unique identifier of the agent to which the alias to get information belongs.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_GetAgentAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetAgentAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentAlias": { 
      "agentAliasArn": "string",
      "agentAliasHistoryEvents": [ 
         { 
            "endDate": "string",
            "routingConfiguration": [ 
               { 
                  "agentVersion": "string",
                  "provisionedThroughput": "string"
               }
            ],
            "startDate": "string"
         }
      ],
      "agentAliasId": "string",
      "agentAliasName": "string",
      "agentAliasStatus": "string",
      "agentId": "string",
      "aliasInvocationState": "string",
      "clientToken": "string",
      "createdAt": "string",
      "description": "string",
      "failureReasons": [ "string" ],
      "routingConfiguration": [ 
         { 
            "agentVersion": "string",
            "provisionedThroughput": "string"
         }
      ],
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_GetAgentAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentAlias](#API_agent_GetAgentAlias_ResponseSyntax) **   <a name="bedrock-agent_GetAgentAlias-response-agentAlias"></a>
Contains information about the alias.  
Type: [AgentAlias](API_agent_AgentAlias.md) object

## Errors
<a name="API_agent_GetAgentAlias_Errors"></a>

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
<a name="API_agent_GetAgentAlias_Examples"></a>

### Example request
<a name="API_agent_GetAgentAlias_Example_1"></a>

This example illustrates one usage of GetAgentAlias.

```
GET /agents/ABCDEFGHIJ/agentaliases/ABCDEFGHIJ/ HTTP/1.1
```

## See Also
<a name="API_agent_GetAgentAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetAgentAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetAgentAlias) 