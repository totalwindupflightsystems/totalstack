---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_AgenticRetrieveStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AgenticRetrieveStream"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# AgenticRetrieveStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_AgenticRetrieveStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AgenticRetrieveStream
<a name="API_agent-runtime_AgenticRetrieveStream"></a>

Retrieves information from one or more knowledge bases using an agentic approach. Agentic retrieval uses a foundation model to intelligently decompose complex queries into sub-queries and iteratively retrieve relevant information from your knowledge bases. This approach improves retrieval accuracy for complex, multi-step questions that a single retrieval pass might not fully address.

The operation returns results through a stream that includes retrieval results, trace events for visibility into the process, and a generated response synthesized from the results by default, which can be turned off.

## Request Syntax
<a name="API_agent-runtime_AgenticRetrieveStream_RequestSyntax"></a>

```
POST /agenticRetrieveStream HTTP/1.1
Content-type: application/json

{
   "agenticRetrieveConfiguration": { 
      "foundationModelConfiguration": { 
         "bedrockFoundationModelConfiguration": { 
            "modelConfiguration": { 
               "modelArn": "{{string}}"
            }
         },
         "type": "{{string}}"
      },
      "foundationModelType": "{{string}}",
      "maxAgentIteration": {{number}},
      "rerankingConfiguration": { 
         "bedrockRerankingConfiguration": { 
            "modelConfiguration": { 
               "modelArn": "{{string}}"
            }
         },
         "type": "{{string}}"
      },
      "rerankingModelType": "{{string}}"
   },
   "generateResponse": {{boolean}},
   "messages": [ 
      { 
         "content": { 
            "text": "{{string}}"
         },
         "role": "{{string}}"
      }
   ],
   "nextToken": "{{string}}",
   "policyConfiguration": { 
      "bedrockGuardrailConfiguration": { 
         "guardrailId": "{{string}}",
         "guardrailVersion": "{{string}}"
      }
   },
   "retrievers": [ 
      { 
         "configuration": { ... },
         "description": "{{string}}"
      }
   ],
   "userContext": { 
      "userId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_AgenticRetrieveStream_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent-runtime_AgenticRetrieveStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agenticRetrieveConfiguration](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-agenticRetrieveConfiguration"></a>
Configuration settings for the agentic retrieval operation.  
Type: [AgenticRetrieveConfiguration](API_agent-runtime_AgenticRetrieveConfiguration.md) object  
Required: Yes

 ** [generateResponse](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-generateResponse"></a>
Whether to generate a response based on the retrieved results.  
Type: Boolean  
Required: No

 ** [messages](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-messages"></a>
The list of messages for the agentic retrieval conversation.  
Type: Array of [AgenticRetrieveMessage](API_agent-runtime_AgenticRetrieveMessage.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

 ** [nextToken](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-nextToken"></a>
Opaque continuation token for paginated results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [policyConfiguration](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-policyConfiguration"></a>
Policy configuration for guardrails and content filtering.  
Type: [AgenticRetrievePolicyConfiguration](API_agent-runtime_AgenticRetrievePolicyConfiguration.md) object  
Required: No

 ** [retrievers](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-retrievers"></a>
The list of retrievers to use for agentic retrieval.  
Type: Array of [AgenticRetriever](API_agent-runtime_AgenticRetriever.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

 ** [userContext](#API_agent-runtime_AgenticRetrieveStream_RequestSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-request-userContext"></a>
Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.  
Type: [UserContext](API_agent-runtime_UserContext.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_AgenticRetrieveStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "badGatewayException": { 
   },
   "conflictException": { 
   },
   "dependencyFailedException": { 
   },
   "internalServerException": { 
   },
   "resourceNotFoundException": { 
   },
   "responseEvent": { 
      "text": "string"
   },
   "result": { 
      "generatedResponse": { 
         "answer": "string",
         "citations": [ 
            { 
               "endIndex": number,
               "references": [ 
                  { 
                     "resultIndex": number
                  }
               ],
               "startIndex": number
            }
         ]
      },
      "nextToken": "string",
      "results": [ 
         { 
            "content": { 
               "byteContent": blob,
               "mimeType": "string",
               "text": "string"
            },
            "metadata": { 
               "string" : JSON value 
            },
            "sourceRetriever": { 
               "identifier": "string"
            }
         }
      ]
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "traceEvent": { 
      "attributes": { 
         "actions": [ 
            { 
               "fullDocumentExpansion": { 
                  "documentId": "string",
                  "sourceRetriever": { 
                     "identifier": "string"
                  }
               },
               "retrieve": { 
                  "inputQuery": { 
                     "text": "string"
                  },
                  "sourceRetrievers": [ 
                     { 
                        "identifier": "string"
                     }
                  ]
               }
            }
         ],
         "failures": [ 
            { 
               "message": "string"
            }
         ],
         "message": "string",
         "retrievalMetadata": [ 
            { 
               "identifier": "string",
               "retrievalType": "string"
            }
         ],
         "retrievalResponse": [ 
            { 
               "content": { 
                  "byteContent": blob,
                  "mimeType": "string",
                  "text": "string"
               },
               "metadata": { 
                  "string" : JSON value 
               },
               "sourceRetriever": { 
                  "identifier": "string"
               }
            }
         ],
         "status": "string",
         "step": "string",
         "warnings": [ 
            { ... }
         ]
      },
      "id": "string",
      "timestamp": number
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_agent-runtime_AgenticRetrieveStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-accessDeniedException"></a>
Access to the resource was denied.  
Type: Exception  
HTTP Status Code: 403

 ** [badGatewayException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-badGatewayException"></a>
A bad gateway error occurred.  
Type: Exception  
HTTP Status Code: 502

 ** [conflictException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-conflictException"></a>
A conflict occurred with the current state of the resource.  
Type: Exception  
HTTP Status Code: 409

 ** [dependencyFailedException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-dependencyFailedException"></a>
A dependency failed during the operation.  
Type: Exception  
HTTP Status Code: 424

 ** [internalServerException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-internalServerException"></a>
An internal server error occurred.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-resourceNotFoundException"></a>
The specified resource was not found.  
Type: Exception  
HTTP Status Code: 404

 ** [responseEvent](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-responseEvent"></a>
A chunk of the generated answer. Emitted only when generateResponse is true.  
Type: [AgenticRetrieveResponseEvent](API_agent-runtime_AgenticRetrieveResponseEvent.md) object

 ** [result](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-result"></a>
A retrieval result event containing the retrieved items.  
Type: [AgenticRetrieveResultEvent](API_agent-runtime_AgenticRetrieveResultEvent.md) object

 ** [serviceQuotaExceededException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-serviceQuotaExceededException"></a>
The service quota has been exceeded.  
Type: Exception  
HTTP Status Code: 400

 ** [throttlingException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-throttlingException"></a>
The request was throttled.  
Type: Exception  
HTTP Status Code: 429

 ** [traceEvent](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-traceEvent"></a>
A trace event providing visibility into the retrieval process.  
Type: [AgenticRetrieveTraceEvent](API_agent-runtime_AgenticRetrieveTraceEvent.md) object

 ** [validationException](#API_agent-runtime_AgenticRetrieveStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_AgenticRetrieveStream-response-validationException"></a>
The request validation failed.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_agent-runtime_AgenticRetrieveStream_Errors"></a>

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

## Examples
<a name="API_agent-runtime_AgenticRetrieveStream_Examples"></a>

### Send a basic query using a managed model
<a name="API_agent-runtime_AgenticRetrieveStream_Example_1"></a>

The following example uses the managed foundation model type to query a knowledge base with agentic retrieval. When you set `foundationModelType` to `MANAGED`, the service selects the optimal model for you.

#### Sample Request
<a name="API_agent-runtime_AgenticRetrieveStream_Example_1_Request"></a>

```
POST /agenticRetrieveStream HTTP/1.1
Content-type: application/json

{
    "messages": [
        {
            "content": {
                "text": "What are the main benefits of using Amazon Bedrock?"
            },
            "role": "user"
        }
    ],
    "retrievers": [
        {
            "description": "Knowledge base about Amazon Bedrock documentation",
            "configuration": {
                "knowledgeBase": {
                    "knowledgeBaseId": "KB12345678"
                }
            }
        }
    ],
    "agenticRetrieveConfiguration": {
        "foundationModelType": "MANAGED",
        "rerankingModelType": "MANAGED"
    }
}
```

## See Also
<a name="API_agent-runtime_AgenticRetrieveStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStream) 