---
id: "@specs/aws/bedrock/docs/API_agent-runtime_InvokeAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InvokeAgent"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# InvokeAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_InvokeAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InvokeAgent
<a name="API_agent-runtime_InvokeAgent"></a>

**Note**  
The AWS CLI doesn't support streaming operations in Amazon Bedrock, including `InvokeAgent`.

Sends a prompt for the agent to process and respond to. Note the following fields for the request:
+ To continue the same conversation with an agent, use the same `sessionId` value in the request.
+ To activate trace enablement, turn `enableTrace` to `true`. Trace enablement helps you follow the agent's reasoning process that led it to the information it processed, the actions it took, and the final result it yielded. For more information, see [Trace enablement](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events).
+ End a conversation by setting `endSession` to `true`.
+ In the `sessionState` object, you can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group.

The response contains both **chunk** and **trace** attributes.

The final response is returned in the `bytes` field of the `chunk` object. The `InvokeAgent` returns one chunk for the entire interaction.
+ The `attribution` object contains citations for parts of the response.
+ If you set `enableTrace` to `true` in the request, you can trace the agent's steps and reasoning process that led it to the response.
+ If the action predicted was configured to return control, the response returns parameters for the action, elicited from the user, in the `returnControl` field.
+ Errors are also surfaced in the response.

## Request Syntax
<a name="API_agent-runtime_InvokeAgent_RequestSyntax"></a>

```
POST /agents/{{agentId}}/agentAliases/{{agentAliasId}}/sessions/{{sessionId}}/text HTTP/1.1
x-amz-source-arn: {{sourceArn}}
Content-type: application/json

{
   "bedrockModelConfigurations": { 
      "performanceConfig": { 
         "latency": "{{string}}"
      }
   },
   "enableTrace": {{boolean}},
   "endSession": {{boolean}},
   "inputText": "{{string}}",
   "memoryId": "{{string}}",
   "promptCreationConfigurations": { 
      "excludePreviousThinkingSteps": {{boolean}},
      "previousConversationTurnsToInclude": {{number}}
   },
   "sessionState": { 
      "conversationHistory": { 
         "messages": [ 
            { 
               "content": [ 
                  { ... }
               ],
               "role": "{{string}}"
            }
         ]
      },
      "files": [ 
         { 
            "name": "{{string}}",
            "source": { 
               "byteContent": { 
                  "data": {{blob}},
                  "mediaType": "{{string}}"
               },
               "s3Location": { 
                  "uri": "{{string}}"
               },
               "sourceType": "{{string}}"
            },
            "useCase": "{{string}}"
         }
      ],
      "invocationId": "{{string}}",
      "knowledgeBaseConfigurations": [ 
         { 
            "knowledgeBaseId": "{{string}}",
            "retrievalConfiguration": { 
               "managedSearchConfiguration": { 
                  "filter": { ... },
                  "numberOfResults": {{number}},
                  "rerankingConfiguration": { 
                     "bedrockRerankingConfiguration": { 
                        "metadataConfiguration": { 
                           "selectionMode": "{{string}}",
                           "selectiveModeConfiguration": { ... }
                        },
                        "modelConfiguration": { 
                           "additionalModelRequestFields": { 
                              "{{string}}" : {{JSON value}} 
                           },
                           "modelArn": "{{string}}"
                        },
                        "numberOfRerankedResults": {{number}}
                     },
                     "type": "{{string}}"
                  },
                  "rerankingModelType": "{{string}}"
               },
               "vectorSearchConfiguration": { 
                  "filter": { ... },
                  "implicitFilterConfiguration": { 
                     "metadataAttributes": [ 
                        { 
                           "description": "{{string}}",
                           "key": "{{string}}",
                           "type": "{{string}}"
                        }
                     ],
                     "modelArn": "{{string}}"
                  },
                  "numberOfResults": {{number}},
                  "overrideSearchType": "{{string}}",
                  "rerankingConfiguration": { 
                     "bedrockRerankingConfiguration": { 
                        "metadataConfiguration": { 
                           "selectionMode": "{{string}}",
                           "selectiveModeConfiguration": { ... }
                        },
                        "modelConfiguration": { 
                           "additionalModelRequestFields": { 
                              "{{string}}" : {{JSON value}} 
                           },
                           "modelArn": "{{string}}"
                        },
                        "numberOfRerankedResults": {{number}}
                     },
                     "type": "{{string}}"
                  }
               }
            }
         }
      ],
      "promptSessionAttributes": { 
         "{{string}}" : "{{string}}" 
      },
      "returnControlInvocationResults": [ 
         { ... }
      ],
      "sessionAttributes": { 
         "{{string}}" : "{{string}}" 
      }
   },
   "streamingConfigurations": { 
      "applyGuardrailInterval": {{number}},
      "streamFinalResponse": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_InvokeAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentAliasId](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-uri-agentAliasId"></a>
The alias of the agent to use.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [agentId](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-uri-agentId"></a>
The unique identifier of the agent to use.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [sessionId](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-uri-sessionId"></a>
The unique identifier of the session. Use the same value across requests to continue the same conversation.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: Yes

 ** [sourceArn](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-sourceArn"></a>
The ARN of the resource making the request.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent/[0-9a-zA-Z]{10}` 

## Request Body
<a name="API_agent-runtime_InvokeAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [bedrockModelConfigurations](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-bedrockModelConfigurations"></a>
Model performance settings for the request.  
Type: [BedrockModelConfigurations](API_agent-runtime_BedrockModelConfigurations.md) object  
Required: No

 ** [enableTrace](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-enableTrace"></a>
Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see [Trace enablement](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events).  
Type: Boolean  
Required: No

 ** [endSession](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-endSession"></a>
Specifies whether to end the session with the agent or not.  
Type: Boolean  
Required: No

 ** [inputText](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-inputText"></a>
The prompt text to send the agent.  
If you include `returnControlInvocationResults` in the `sessionState` field, the `inputText` field will be ignored.
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 25000000.  
Required: No

 ** [memoryId](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-memoryId"></a>
The unique identifier of the agent memory.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: No

 ** [promptCreationConfigurations](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-promptCreationConfigurations"></a>
Specifies parameters that control how the service populates the agent prompt for an `InvokeAgent` request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.  
Type: [PromptCreationConfigurations](API_agent-runtime_PromptCreationConfigurations.md) object  
Required: No

 ** [sessionState](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-sessionState"></a>
Contains parameters that specify various attributes of the session. For more information, see [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html).  
If you include `returnControlInvocationResults` in the `sessionState` field, the `inputText` field will be ignored.
Type: [SessionState](API_agent-runtime_SessionState.md) object  
Required: No

 ** [streamingConfigurations](#API_agent-runtime_InvokeAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-request-streamingConfigurations"></a>
 Specifies the configurations for streaming.   
To use agent streaming, you need permissions to perform the `bedrock:InvokeModelWithResponseStream` action.
Type: [StreamingConfigurations](API_agent-runtime_StreamingConfigurations.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_InvokeAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-bedrock-agent-content-type: {{contentType}}
x-amz-bedrock-agent-session-id: {{sessionId}}
x-amz-bedrock-agent-memory-id: {{memoryId}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "badGatewayException": { 
   },
   "chunk": { 
      "attribution": { 
         "citations": [ 
            { 
               "generatedResponsePart": { 
                  "textResponsePart": { 
                     "span": { 
                        "end": number,
                        "start": number
                     },
                     "text": "string"
                  }
               },
               "retrievedReferences": [ 
                  { 
                     "content": { 
                        "audio": { 
                           "s3Uri": "string",
                           "transcription": "string"
                        },
                        "byteContent": "string",
                        "row": [ 
                           { 
                              "columnName": "string",
                              "columnValue": "string",
                              "type": "string"
                           }
                        ],
                        "text": "string",
                        "type": "string",
                        "video": { 
                           "s3Uri": "string",
                           "summary": "string"
                        }
                     },
                     "location": { 
                        "confluenceLocation": { 
                           "url": "string"
                        },
                        "customDocumentLocation": { 
                           "id": "string"
                        },
                        "googleDriveLocation": { 
                           "url": "string"
                        },
                        "kendraDocumentLocation": { 
                           "uri": "string"
                        },
                        "oneDriveLocation": { 
                           "url": "string"
                        },
                        "s3Location": { 
                           "uri": "string"
                        },
                        "salesforceLocation": { 
                           "url": "string"
                        },
                        "sharePointLocation": { 
                           "url": "string"
                        },
                        "sqlLocation": { 
                           "query": "string"
                        },
                        "type": "string",
                        "webLocation": { 
                           "url": "string"
                        }
                     },
                     "metadata": { 
                        "string" : JSON value 
                     }
                  }
               ]
            }
         ]
      },
      "bytes": blob
   },
   "conflictException": { 
   },
   "dependencyFailedException": { 
   },
   "files": { 
      "files": [ 
         { 
            "bytes": blob,
            "name": "string",
            "type": "string"
         }
      ]
   },
   "internalServerException": { 
   },
   "modelNotReadyException": { 
   },
   "resourceNotFoundException": { 
   },
   "returnControl": { 
      "invocationId": "string",
      "invocationInputs": [ 
         { ... }
      ]
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "trace": { 
      "agentAliasId": "string",
      "agentId": "string",
      "agentVersion": "string",
      "callerChain": [ 
         { ... }
      ],
      "collaboratorName": "string",
      "eventTime": "string",
      "sessionId": "string",
      "trace": { ... }
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_agent-runtime_InvokeAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentType](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-contentType"></a>
The MIME type of the input data in the request. The default value is `application/json`.

 ** [memoryId](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-memoryId"></a>
The unique identifier of the agent memory.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

 ** [sessionId](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-sessionId"></a>
The unique identifier of the session with the agent.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403

 ** [badGatewayException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.  
Type: Exception  
HTTP Status Code: 502

 ** [chunk](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-chunk"></a>
Contains a part of an agent response and citations for it.  
Type: [PayloadPart](API_agent-runtime_PayloadPart.md) object

 ** [conflictException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-conflictException"></a>
There was a conflict performing an operation. Resolve the conflict and retry your request.  
Type: Exception  
HTTP Status Code: 409

 ** [dependencyFailedException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424

 ** [files](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-files"></a>
Contains intermediate response for code interpreter if any files have been generated.  
Type: [FilePart](API_agent-runtime_FilePart.md) object

 ** [internalServerException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500

 ** [modelNotReadyException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-modelNotReadyException"></a>
 The model specified in the request is not ready to serve Inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools* reference guide.   
Type: Exception  
HTTP Status Code: 424

 ** [resourceNotFoundException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-resourceNotFoundException"></a>
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
Type: Exception  
HTTP Status Code: 404

 ** [returnControl](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-returnControl"></a>
Contains the parameters and information that the agent elicited from the customer to carry out an action. This information is returned to the system and can be used in your own setup for fulfilling the action.  
Type: [ReturnControlPayload](API_agent-runtime_ReturnControlPayload.md) object

 ** [serviceQuotaExceededException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-serviceQuotaExceededException"></a>
The number of requests exceeds the service quota. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 400

 ** [throttlingException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-throttlingException"></a>
The number of requests exceeds the limit. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 429

 ** [trace](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-trace"></a>
Contains information about the agent and session, alongside the agent's reasoning process and results from calling actions and querying knowledge bases and metadata about the trace. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see [Trace events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html).  
Type: [TracePart](API_agent-runtime_TracePart.md) object

 ** [validationException](#API_agent-runtime_InvokeAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeAgent-response-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_agent-runtime_InvokeAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ModelNotReadyException **   
 The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools* reference guide.   
HTTP Status Code: 424

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_InvokeAgent_Examples"></a>

### Example simple request
<a name="API_agent-runtime_InvokeAgent_Example_1"></a>

The following example inquires the agent to get the weather for Seattle.

```
POST https://bedrock-agent-runtime.us-east-1.amazonaws.com/agents/AGENT12345/agentAliases/TSTALIASID/sessions/abb/text

{
    "inputText": "give me the weather for seattle",
    "enableTrace": true
}
```

### Example response (action group defined with OpenAPI schema, control returned)
<a name="API_agent-runtime_InvokeAgent_Example_2"></a>

The following example shows a response from an agent that has invoked an action group that was configured as follows:
+ Defined with an OpenAPI schema
+ Configured to return control to the agent developer

```
HTTP/1.1 200
x-amzn-bedrock-agent-content-type: application/json
x-amz-bedrock-agent-session-id: session0
Content-type: application/json

{
    "invocationInputs": [{
        "apiInvocationInput": {
            "actionGroup": "WeatherAPIs",
            "apiPath": "/get-weather",
            "httpMethod": "get",
            "parameters": [
                {
                    "name": "location",
                    "type": "string",
                    "value": "seattle"
                },
                {
                    "name": "date",
                    "type": "string",
                    "value": "2024-09-15"
                }
            ]
        }
    }],
    "invocationId": "337cb2f6-ec74-4b49-8141-00b8091498ad"
}
```

### Example request using results from returned control (action group defined with OpenAPI schema)
<a name="API_agent-runtime_InvokeAgent_Example_3"></a>

The following example shows a request in which the results returned in the `InvokeAgent` response from an agent are passed to the `sessionState` of a new request. The results were returned from an agent that has invoked an action group that was configured as follows:
+ Defined with an OpenAPI schema
+ Configured to return control to the agent developer

The `invocationId` must match the `invocationId` that was returned in the response.

```
POST https: //bedrock-agent-runtime.us-east-1.amazonaws.com/agents/AGENT12345/agentAliases/TSTALIASID/sessions/abb/text
 
{
    "enableTrace": true,
    "sessionState": {
        "invocationId": "337cb2f6-ec74-4b49-8141-00b8091498ad",
        "returnControlInvocationResults": [{
            "apiResult": {
                "actionGroup": "WeatherAPIs",
                "httpMethod": "get",
                "apiPath": "/get-weather",
                "responseBody": {
                    "application/json": {
                        "body": "It's rainy in Seattle today."
                    }
                }
            }
        }]
    }
}
```

### Example response (action group defined with function details, control returned)
<a name="API_agent-runtime_InvokeAgent_Example_4"></a>

The following example shows a response from an agent that has invoked an action group that was configured as follows:
+ Defined with function details
+ Configured to return control to the agent developer

```
HTTP/1.1 200
x-amzn-bedrock-agent-content-type: application/json
x-amz-bedrock-agent-session-id: session0
Content-type: application/json
 
{
    "invocationInputs": [{
        "functionInvocationInput": {
            "actionGroup": "WeatherAPIs",
            "function": "getWeather",
            "parameters": [
                {
                    "name": "location",
                    "type": "string",
                    "value": "seattle"
                },
                {
                    "name": "date",
                    "type": "string",
                    "value": "2024-09-15"
                }
            ]
        }
    }],
    "invocationId": "79e0feaa-c6f7-49bf-814d-b7c498505172"
}
```

### Example request using results from returned control (action group defined with function details)
<a name="API_agent-runtime_InvokeAgent_Example_5"></a>

The following example shows a request in which the results returned in the `InvokeAgent` response from an agent are passed to the `sessionState` of a new request. The results were returned from an agent that has invoked an action group that was configured as follows:
+ Defined with function details
+ Configured to return control to the agent developer

The `invocationId` must match the `invocationId` that was returned in the response.

```
POST https://bedrock-agent-runtime.us-east-1.amazonaws.com/agents/AGENT12345/agentAliases/TSTALIASID/sessions/abb/text
            
{
    "enableTrace": true,
    "sessionState": {
        "invocationId": "79e0feaa-c6f7-49bf-814d-b7c498505172",
        "returnControlInvocationResults": [{
            "functionResult": {
                "actionGroup": "WeatherAPIs",
                "function": "getWeather",
                "responseBody": {
                    "TEXT": {
                        "body": "It's rainy in Seattle today."
                    }
                }
            }
        }]
    }
}
```

## See Also
<a name="API_agent-runtime_InvokeAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/InvokeAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvokeAgent) 