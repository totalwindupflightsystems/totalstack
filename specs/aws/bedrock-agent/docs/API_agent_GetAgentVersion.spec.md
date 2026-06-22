---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetAgentVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAgentVersion"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAgentVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetAgentVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAgentVersion
<a name="API_agent_GetAgentVersion"></a>

Gets details about a version of an agent.

## Request Syntax
<a name="API_agent_GetAgentVersion_RequestSyntax"></a>

```
GET /agents/{{agentId}}/agentversions/{{agentVersion}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetAgentVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_GetAgentVersion_RequestSyntax) **   <a name="bedrock-agent_GetAgentVersion-request-uri-agentId"></a>
The unique identifier of the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_GetAgentVersion_RequestSyntax) **   <a name="bedrock-agent_GetAgentVersion-request-uri-agentVersion"></a>
The version of the agent.  
Pattern: `[0-9]{1,5}`   
Required: Yes

## Request Body
<a name="API_agent_GetAgentVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetAgentVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentVersion": { 
      "agentArn": "string",
      "agentCollaboration": "string",
      "agentId": "string",
      "agentName": "string",
      "agentResourceRoleArn": "string",
      "agentStatus": "string",
      "createdAt": "string",
      "customerEncryptionKeyArn": "string",
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
      "updatedAt": "string",
      "version": "string"
   }
}
```

## Response Elements
<a name="API_agent_GetAgentVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentVersion](#API_agent_GetAgentVersion_ResponseSyntax) **   <a name="bedrock-agent_GetAgentVersion-response-agentVersion"></a>
Contains details about the version of the agent.  
Type: [AgentVersion](API_agent_AgentVersion.md) object

## Errors
<a name="API_agent_GetAgentVersion_Errors"></a>

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
<a name="API_agent_GetAgentVersion_Examples"></a>

### Example request
<a name="API_agent_GetAgentVersion_Example_1"></a>

This example illustrates one usage of GetAgentVersion.

```
GET /agents/agentId/agentversions/agentVersion/ HTTP/1.1
```

## See Also
<a name="API_agent_GetAgentVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetAgentVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetAgentVersion) 