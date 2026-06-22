---
id: "@specs/aws/bedrock/docs/API_agent_UpdateAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAgent"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_UpdateAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAgent
<a name="API_agent_UpdateAgent"></a>

Updates the configuration of an agent.

## Request Syntax
<a name="API_agent_UpdateAgent_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/ HTTP/1.1
Content-type: application/json

{
   "agentCollaboration": "{{string}}",
   "agentName": "{{string}}",
   "agentResourceRoleArn": "{{string}}",
   "customerEncryptionKeyArn": "{{string}}",
   "customOrchestration": { 
      "executor": { ... }
   },
   "description": "{{string}}",
   "foundationModel": "{{string}}",
   "guardrailConfiguration": { 
      "guardrailIdentifier": "{{string}}",
      "guardrailVersion": "{{string}}"
   },
   "idleSessionTTLInSeconds": {{number}},
   "instruction": "{{string}}",
   "memoryConfiguration": { 
      "enabledMemoryTypes": [ "{{string}}" ],
      "sessionSummaryConfiguration": { 
         "maxRecentSessions": {{number}}
      },
      "storageDays": {{number}}
   },
   "orchestrationType": "{{string}}",
   "promptOverrideConfiguration": { 
      "overrideLambda": "{{string}}",
      "promptConfigurations": [ 
         { 
            "additionalModelRequestFields": {{JSON value}},
            "basePromptTemplate": "{{string}}",
            "foundationModel": "{{string}}",
            "inferenceConfiguration": { 
               "maximumLength": {{number}},
               "stopSequences": [ "{{string}}" ],
               "temperature": {{number}},
               "topK": {{number}},
               "topP": {{number}}
            },
            "parserMode": "{{string}}",
            "promptCreationMode": "{{string}}",
            "promptState": "{{string}}",
            "promptType": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_agent_UpdateAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-uri-agentId"></a>
The unique identifier of the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_UpdateAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentCollaboration](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-agentCollaboration"></a>
The agent's collaboration role.  
Type: String  
Valid Values: `SUPERVISOR | SUPERVISOR_ROUTER | DISABLED`   
Required: No

 ** [agentName](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-agentName"></a>
Specifies a new name for the agent.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [agentResourceRoleArn](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-agentResourceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [customerEncryptionKeyArn](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key with which to encrypt the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [customOrchestration](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-customOrchestration"></a>
 Contains details of the custom orchestration configured for the agent.   
Type: [CustomOrchestration](API_agent_CustomOrchestration.md) object  
Required: No

 ** [description](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-description"></a>
Specifies a new description of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [foundationModel](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-foundationModel"></a>
The identifier for the model that you want to be used for orchestration by the agent you create.  
The `modelId` to provide depends on the type of model or throughput that you use:  
+ If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see [Amazon Bedrock base model IDs (on-demand throughput)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns) in the Amazon Bedrock User Guide.
+ If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see [Supported Regions and models for cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html) in the Amazon Bedrock User Guide.
+ If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see [Run inference using a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html) in the Amazon Bedrock User Guide.
+ If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see [Use a custom model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html) in the Amazon Bedrock User Guide.
+ If you use an [imported model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), specify the ARN of the imported model. You can get the model ARN from a successful call to [CreateModelImportJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html) or from the Imported models page in the Amazon Bedrock console.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** [guardrailConfiguration](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-guardrailConfiguration"></a>
The unique Guardrail configuration assigned to the agent when it is updated.  
Type: [GuardrailConfiguration](API_agent_GuardrailConfiguration.md) object  
Required: No

 ** [idleSessionTTLInSeconds](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-idleSessionTTLInSeconds"></a>
The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.  
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 5400.  
Required: No

 ** [instruction](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-instruction"></a>
Specifies new instructions that tell the agent what it should do and how it should interact with users.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 4000.  
Required: No

 ** [memoryConfiguration](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-memoryConfiguration"></a>
Specifies the new memory configuration for the agent.   
Type: [MemoryConfiguration](API_agent_MemoryConfiguration.md) object  
Required: No

 ** [orchestrationType](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-orchestrationType"></a>
 Specifies the type of orchestration strategy for the agent. This is set to `DEFAULT` orchestration type, by default.   
Type: String  
Valid Values: `DEFAULT | CUSTOM_ORCHESTRATION`   
Required: No

 ** [promptOverrideConfiguration](#API_agent_UpdateAgent_RequestSyntax) **   <a name="bedrock-agent_UpdateAgent-request-promptOverrideConfiguration"></a>
Contains configurations to override prompts in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).  
Type: [PromptOverrideConfiguration](API_agent_PromptOverrideConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_agent_UpdateAgent_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_agent_UpdateAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agent](#API_agent_UpdateAgent_ResponseSyntax) **   <a name="bedrock-agent_UpdateAgent-response-agent"></a>
Contains details about the agent that was updated.  
Type: [Agent](API_agent_Agent.md) object

## Errors
<a name="API_agent_UpdateAgent_Errors"></a>

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
<a name="API_agent_UpdateAgent_Examples"></a>

### Example request
<a name="API_agent_UpdateAgent_Example_1"></a>

This example illustrates one usage of UpdateAgent.

```
PUT /agents/ABCDEFGHIJ/ HTTP/1.1
Content-type: application/json

{
  "agentName": "TestName",
  "agentResourceRoleArn": "arn:aws:iam::123456789012:role/AmazonBedrockExecutionRoleForAgents_user",
  "instruction": "You are an IT agent who solves customer's problems",
  "description": "Description is here",
  "idleSessionTTLInSeconds": 900,
  "foundationModel": "anthropic.claude-v2"
}
```

## See Also
<a name="API_agent_UpdateAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateAgent) 