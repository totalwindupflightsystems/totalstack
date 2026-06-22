---
id: "@specs/aws/bedrock/docs/API_agent_UpdateAgentAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAgentAlias"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateAgentAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_UpdateAgentAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAgentAlias
<a name="API_agent_UpdateAgentAlias"></a>

Updates configurations for an alias of an agent.

## Request Syntax
<a name="API_agent_UpdateAgentAlias_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/agentaliases/{{agentAliasId}}/ HTTP/1.1
Content-type: application/json

{
   "agentAliasName": "{{string}}",
   "aliasInvocationState": "{{string}}",
   "description": "{{string}}",
   "routingConfiguration": [ 
      { 
         "agentVersion": "{{string}}",
         "provisionedThroughput": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_agent_UpdateAgentAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentAliasId](#API_agent_UpdateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-request-uri-agentAliasId"></a>
The unique identifier of the alias.  
Length Constraints: Fixed length of 10.  
Pattern: `(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [agentId](#API_agent_UpdateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-request-uri-agentId"></a>
The unique identifier of the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_UpdateAgentAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentAliasName](#API_agent_UpdateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-request-agentAliasName"></a>
Specifies a new name for the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [aliasInvocationState](#API_agent_UpdateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-request-aliasInvocationState"></a>
The invocation state for the agent alias. To pause the agent alias, set the value to `REJECT_INVOCATIONS`. To start the agent alias running again, set the value to `ACCEPT_INVOCATIONS`. Use the `GetAgentAlias`, or `ListAgentAliases`, operation to get the invocation state of an agent alias.  
Type: String  
Valid Values: `ACCEPT_INVOCATIONS | REJECT_INVOCATIONS`   
Required: No

 ** [description](#API_agent_UpdateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-request-description"></a>
Specifies a new description for the alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [routingConfiguration](#API_agent_UpdateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-request-routingConfiguration"></a>
Contains details about the routing configuration of the alias.  
Type: Array of [AgentAliasRoutingConfigurationListItem](API_agent_AgentAliasRoutingConfigurationListItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

## Response Syntax
<a name="API_agent_UpdateAgentAlias_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_agent_UpdateAgentAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentAlias](#API_agent_UpdateAgentAlias_ResponseSyntax) **   <a name="bedrock-agent_UpdateAgentAlias-response-agentAlias"></a>
Contains details about the alias that was updated.  
Type: [AgentAlias](API_agent_AgentAlias.md) object

## Errors
<a name="API_agent_UpdateAgentAlias_Errors"></a>

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

## Examples
<a name="API_agent_UpdateAgentAlias_Examples"></a>

### Example request
<a name="API_agent_UpdateAgentAlias_Example_1"></a>

This example illustrates one usage of UpdateAgentAlias.

```
PUT /agents/ABCDEFGHIJ/agentaliases/ABCDEFGHIJ/ HTTP/1.1
Content-type: application/json

{
    "agentAliasName": "TestName",
    "description": "Updated description",
    "routingConfiguration": [ 
       { 
          "agentVersion": "2"
       }
    ]
}
```

## See Also
<a name="API_agent_UpdateAgentAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateAgentAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateAgentAlias) 