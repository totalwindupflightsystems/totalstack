---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgent"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgent
<a name="API_agent_GetAgent"></a>

Gets information about an agent.

## Request Syntax
<a name="API_agent_GetAgent_RequestSyntax"></a>

```
GET /agents/{{agentId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_GetAgent_RequestSyntax) **   <a name="bedrock-agent_GetAgent-request-uri-agentId"></a>
The unique identifier of the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_GetAgent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agent": { 
      "agentArn": "string",
      "agentCollaboration": "string",
      "agentId": "string",
      "agentName": "string",
      "agentResourceRoleArn": "string",
      "agentStatus": "string",
      "agentVersion": "string",
      "clientToken": "string",
      "createdAt": "string",
      "customerEncryptionKeyArn": "string",
      "customOrchestration": { 
         "executor": { ... }
      },
      "description": "string",
      "failureReasons": [ "string" ],
      "foundationModel": "string",
      "guardrailConfiguration": { 
         "guardrailIdentifier": "string",
         "guardrailVersion": "string"
      },
      "idleSessionTTLInSeconds": number,
      "instruction": "string",
      "memoryConfiguration": { 
         "enabledMemoryTypes": [ "string" ],
         "sessionSummaryConfiguration": { 
            "maxRecentSessions": number
         },
         "storageDays": number
      },
      "orchestrationType": "string",
      "preparedAt": "string",
      "promptOverrideConfiguration": { 
         "overrideLambda": "string",
         "promptConfigurations": [ 
            { 
               "additionalModelRequestFields": JSON value,
               "basePromptTemplate": "string",
               "foundationModel": "string",
               "inferenceConfiguration": { 
                  "maximumLength": number,
                  "stopSequences": [ "string" ],
                  "temperature": number,
                  "topK": number,
                  "topP": number
               },
               "parserMode": "string",
               "promptCreationMode": "string",
               "promptState": "string",
               "promptType": "string"
            }
         ]
      },
      "recommendedActions": [ "string" ],
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_GetAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agent](#API_agent_GetAgent_ResponseSyntax) **   <a name="bedrock-agent_GetAgent-response-agent"></a>
Contains details about the agent.  
Type: [Agent](API_agent_Agent.md) object

## Errors
<a name="API_agent_GetAgent_Errors"></a>

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
<a name="API_agent_GetAgent_Examples"></a>

### Example request
<a name="API_agent_GetAgent_Example_1"></a>

This example illustrates one usage of GetAgent.

```
GET /agents/ABCDEFGHIJ/ HTTP/1.1
```

## See Also
<a name="API_agent_GetAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetAgent) 