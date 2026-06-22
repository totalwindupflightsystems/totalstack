---
id: "@specs/aws/bedrock/docs/API_agent-runtime_InvokeInlineAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InvokeInlineAgent"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# InvokeInlineAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_InvokeInlineAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InvokeInlineAgent
<a name="API_agent-runtime_InvokeInlineAgent"></a>

 Invokes an inline Amazon Bedrock agent using the configurations you provide with the request. 
+ Specify the following fields for security purposes.
  + (Optional) `customerEncryptionKeyArn` – The Amazon Resource Name (ARN) of a AWS KMS key to encrypt the creation of the agent.
  + (Optional) `idleSessionTTLinSeconds` – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent `InvokeInlineAgent` request begins a new session.
+ To override the default prompt behavior for agent orchestration and to use advanced prompts, include a `promptOverrideConfiguration` object. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).
+ The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.

**Note**  
The AWS CLI doesn't support streaming operations in Amazon Bedrock, including `InvokeInlineAgent`.

## Request Syntax
<a name="API_agent-runtime_InvokeInlineAgent_RequestSyntax"></a>

```
POST /agents/{{sessionId}} HTTP/1.1
Content-type: application/json

{
   "actionGroups": [ 
      { 
         "actionGroupExecutor": { ... },
         "actionGroupName": "{{string}}",
         "apiSchema": { ... },
         "description": "{{string}}",
         "functionSchema": { ... },
         "parentActionGroupSignature": "{{string}}",
         "parentActionGroupSignatureParams": { 
            "{{string}}" : "{{string}}" 
         }
      }
   ],
   "agentCollaboration": "{{string}}",
   "agentName": "{{string}}",
   "bedrockModelConfigurations": { 
      "performanceConfig": { 
         "latency": "{{string}}"
      }
   },
   "collaboratorConfigurations": [ 
      { 
         "agentAliasArn": "{{string}}",
         "collaboratorInstruction": "{{string}}",
         "collaboratorName": "{{string}}",
         "relayConversationHistory": "{{string}}"
      }
   ],
   "collaborators": [ 
      { 
         "actionGroups": [ 
            { 
               "actionGroupExecutor": { ... },
               "actionGroupName": "{{string}}",
               "apiSchema": { ... },
               "description": "{{string}}",
               "functionSchema": { ... },
               "parentActionGroupSignature": "{{string}}",
               "parentActionGroupSignatureParams": { 
                  "{{string}}" : "{{string}}" 
               }
            }
         ],
         "agentCollaboration": "{{string}}",
         "agentName": "{{string}}",
         "collaboratorConfigurations": [ 
            { 
               "agentAliasArn": "{{string}}",
               "collaboratorInstruction": "{{string}}",
               "collaboratorName": "{{string}}",
               "relayConversationHistory": "{{string}}"
            }
         ],
         "customerEncryptionKeyArn": "{{string}}",
         "foundationModel": "{{string}}",
         "guardrailConfiguration": { 
            "guardrailIdentifier": "{{string}}",
            "guardrailVersion": "{{string}}"
         },
         "idleSessionTTLInSeconds": {{number}},
         "instruction": "{{string}}",
         "knowledgeBases": [ 
            { 
               "description": "{{string}}",
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
   ],
   "customerEncryptionKeyArn": "{{string}}",
   "customOrchestration": { 
      "executor": { ... }
   },
   "enableTrace": {{boolean}},
   "endSession": {{boolean}},
   "foundationModel": "{{string}}",
   "guardrailConfiguration": { 
      "guardrailIdentifier": "{{string}}",
      "guardrailVersion": "{{string}}"
   },
   "idleSessionTTLInSeconds": {{number}},
   "inlineSessionState": { 
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
   "inputText": "{{string}}",
   "instruction": "{{string}}",
   "knowledgeBases": [ 
      { 
         "description": "{{string}}",
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
   "orchestrationType": "{{string}}",
   "promptCreationConfigurations": { 
      "excludePreviousThinkingSteps": {{boolean}},
      "previousConversationTurnsToInclude": {{number}}
   },
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
   },
   "streamingConfigurations": { 
      "applyGuardrailInterval": {{number}},
      "streamFinalResponse": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_InvokeInlineAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionId](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-uri-sessionId"></a>
 The unique identifier of the session. Use the same value across requests to continue the same conversation.   
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: Yes

## Request Body
<a name="API_agent-runtime_InvokeInlineAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionGroups](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-actionGroups"></a>
 A list of action groups with each action group defining the action the inline agent needs to carry out.   
Type: Array of [AgentActionGroup](API_agent-runtime_AgentActionGroup.md) objects  
Required: No

 ** [agentCollaboration](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-agentCollaboration"></a>
 Defines how the inline collaborator agent handles information across multiple collaborator agents to coordinate a final response. The inline collaborator agent can also be the supervisor.   
Type: String  
Valid Values: `SUPERVISOR | SUPERVISOR_ROUTER | DISABLED`   
Required: No

 ** [agentName](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-agentName"></a>
The name for the agent.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** [bedrockModelConfigurations](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-bedrockModelConfigurations"></a>
Model settings for the request.  
Type: [InlineBedrockModelConfigurations](API_agent-runtime_InlineBedrockModelConfigurations.md) object  
Required: No

 ** [collaboratorConfigurations](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-collaboratorConfigurations"></a>
 Settings for an inline agent collaborator called with [InvokeInlineAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeInlineAgent.html).   
Type: Array of [CollaboratorConfiguration](API_agent-runtime_CollaboratorConfiguration.md) objects  
Required: No

 ** [collaborators](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-collaborators"></a>
 List of collaborator inline agents.   
Type: Array of [Collaborator](API_agent-runtime_Collaborator.md) objects  
Required: No

 ** [customerEncryptionKeyArn](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-customerEncryptionKeyArn"></a>
 The Amazon Resource Name (ARN) of the AWS KMS key to use to encrypt your inline agent.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [customOrchestration](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-customOrchestration"></a>
Contains details of the custom orchestration configured for the agent.   
Type: [CustomOrchestration](API_agent-runtime_CustomOrchestration.md) object  
Required: No

 ** [enableTrace](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-enableTrace"></a>
 Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see [Using trace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html).   
Type: Boolean  
Required: No

 ** [endSession](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-endSession"></a>
 Specifies whether to end the session with the inline agent or not.   
Type: Boolean  
Required: No

 ** [foundationModel](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-foundationModel"></a>
 The [model identifier (ID)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns) of the model to use for orchestration by the inline agent. For example, `meta.llama3-1-70b-instruct-v1:0`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+))$|(^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{1,20}):(|[0-9]{12}):inference-profile/[a-zA-Z0-9-:.]+)`   
Required: Yes

 ** [guardrailConfiguration](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-guardrailConfiguration"></a>
 The [guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to assign to the inline agent.   
Type: [GuardrailConfigurationWithArn](API_agent-runtime_GuardrailConfigurationWithArn.md) object  
Required: No

 ** [idleSessionTTLInSeconds](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-idleSessionTTLInSeconds"></a>
 The number of seconds for which the inline agent should maintain session information. After this time expires, the subsequent `InvokeInlineAgent` request begins a new session.   
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and the data provided before the timeout is deleted.  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 3600.  
Required: No

 ** [inlineSessionState](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-inlineSessionState"></a>
 Parameters that specify the various attributes of a sessions. You can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group. For more information, see [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html).   
If you include `returnControlInvocationResults` in the `sessionState` field, the `inputText` field will be ignored.
Type: [InlineSessionState](API_agent-runtime_InlineSessionState.md) object  
Required: No

 ** [inputText](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-inputText"></a>
 The prompt text to send to the agent.   
If you include `returnControlInvocationResults` in the `sessionState` field, the `inputText` field will be ignored.
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 25000000.  
Required: No

 ** [instruction](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-instruction"></a>
 The instructions that tell the inline agent what it should do and how it should interact with users.   
Type: String  
Length Constraints: Minimum length of 40.  
Required: Yes

 ** [knowledgeBases](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-knowledgeBases"></a>
 Contains information of the knowledge bases to associate with.   
Type: Array of [KnowledgeBase](API_agent-runtime_KnowledgeBase.md) objects  
Required: No

 ** [orchestrationType](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-orchestrationType"></a>
Specifies the type of orchestration strategy for the agent. This is set to DEFAULT orchestration type, by default.   
Type: String  
Valid Values: `DEFAULT | CUSTOM_ORCHESTRATION`   
Required: No

 ** [promptCreationConfigurations](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-promptCreationConfigurations"></a>
Specifies parameters that control how the service populates the agent prompt for an `InvokeInlineAgent` request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.  
Type: [PromptCreationConfigurations](API_agent-runtime_PromptCreationConfigurations.md) object  
Required: No

 ** [promptOverrideConfiguration](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-promptOverrideConfiguration"></a>
 Configurations for advanced prompts used to override the default prompts to enhance the accuracy of the inline agent.   
Type: [PromptOverrideConfiguration](API_agent-runtime_PromptOverrideConfiguration.md) object  
Required: No

 ** [streamingConfigurations](#API_agent-runtime_InvokeInlineAgent_RequestSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-request-streamingConfigurations"></a>
 Specifies the configurations for streaming.   
To use agent streaming, you need permissions to perform the `bedrock:InvokeModelWithResponseStream` action.
Type: [StreamingConfigurations](API_agent-runtime_StreamingConfigurations.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_InvokeInlineAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-bedrock-agent-content-type: {{contentType}}
x-amz-bedrock-agent-session-id: {{sessionId}}
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
<a name="API_agent-runtime_InvokeInlineAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentType](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-contentType"></a>
 The MIME type of the input data in the request. The default value is application/json. 

 ** [sessionId](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-sessionId"></a>
 The unique identifier of the session with the agent.   
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403

 ** [badGatewayException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.   
Type: Exception  
HTTP Status Code: 502

 ** [chunk](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-chunk"></a>
Contains a part of an agent response and citations for it.  
Type: [InlineAgentPayloadPart](API_agent-runtime_InlineAgentPayloadPart.md) object

 ** [conflictException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-conflictException"></a>
There was a conflict performing an operation. Resolve the conflict and retry your request.   
Type: Exception  
HTTP Status Code: 409

 ** [dependencyFailedException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424

 ** [files](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-files"></a>
Contains intermediate response for code interpreter if any files have been generated.  
Type: [InlineAgentFilePart](API_agent-runtime_InlineAgentFilePart.md) object

 ** [internalServerException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-resourceNotFoundException"></a>
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.   
Type: Exception  
HTTP Status Code: 404

 ** [returnControl](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-returnControl"></a>
Contains the parameters and information that the agent elicited from the customer to carry out an action. This information is returned to the system and can be used in your own setup for fulfilling the action.  
Type: [InlineAgentReturnControlPayload](API_agent-runtime_InlineAgentReturnControlPayload.md) object

 ** [serviceQuotaExceededException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-serviceQuotaExceededException"></a>
The number of requests exceeds the service quota. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 400

 ** [throttlingException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-throttlingException"></a>
The number of requests exceeds the limit. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 429

 ** [trace](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-trace"></a>
Contains information about the agent and session, alongside the agent's reasoning process and results from calling actions and querying knowledge bases and metadata about the trace. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see [Trace events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html).   
Type: [InlineAgentTracePart](API_agent-runtime_InlineAgentTracePart.md) object

 ** [validationException](#API_agent-runtime_InvokeInlineAgent_ResponseSyntax) **   <a name="bedrock-agent-runtime_InvokeInlineAgent-response-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_agent-runtime_InvokeInlineAgent_Errors"></a>

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

## See Also
<a name="API_agent-runtime_InvokeInlineAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvokeInlineAgent) 