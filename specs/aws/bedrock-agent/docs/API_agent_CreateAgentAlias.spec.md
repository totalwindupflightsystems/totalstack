---
id: "@specs/aws/bedrock-agent/docs/API_agent_CreateAgentAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAgentAlias"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateAgentAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_CreateAgentAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAgentAlias
<a name="API_agent_CreateAgentAlias"></a>

Creates an alias of an agent that can be used to deploy the agent.

## Request Syntax
<a name="API_agent_CreateAgentAlias_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/agentaliases/ HTTP/1.1
Content-type: application/json

{
   "agentAliasName": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "routingConfiguration": [ 
      { 
         "agentVersion": "{{string}}",
         "provisionedThroughput": "{{string}}"
      }
   ],
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateAgentAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_CreateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_CreateAgentAlias-request-uri-agentId"></a>
The unique identifier of the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_CreateAgentAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentAliasName](#API_agent_CreateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_CreateAgentAlias-request-agentAliasName"></a>
The name of the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [clientToken](#API_agent_CreateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_CreateAgentAlias-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_agent_CreateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_CreateAgentAlias-request-description"></a>
A description of the alias of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [routingConfiguration](#API_agent_CreateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_CreateAgentAlias-request-routingConfiguration"></a>
Contains details about the routing configuration of the alias.  
Type: Array of [AgentAliasRoutingConfigurationListItem](API_agent_AgentAliasRoutingConfigurationListItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

 ** [tags](#API_agent_CreateAgentAlias_RequestSyntax) **   <a name="bedrock-agent_CreateAgentAlias-request-tags"></a>
Any tags that you want to attach to the alias of the agent.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_agent_CreateAgentAlias_ResponseSyntax"></a>

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
<a name="API_agent_CreateAgentAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentAlias](#API_agent_CreateAgentAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateAgentAlias-response-agentAlias"></a>
Contains details about the alias that was created.  
Type: [AgentAlias](API_agent_AgentAlias.md) object

## Errors
<a name="API_agent_CreateAgentAlias_Errors"></a>

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
<a name="API_agent_CreateAgentAlias_Examples"></a>

### Example request
<a name="API_agent_CreateAgentAlias_Example_1"></a>

This example illustrates one usage of CreateAgentAlias.

```
PUT /agents/ABCDEFGHIJ/agentaliases/ HTTP/1.1
Content-type: application/json

{
 "agentAliasName": "TestName",
 "description": "Alias is test"
}
```

## See Also
<a name="API_agent_CreateAgentAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateAgentAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateAgentAlias) 