---
id: "@specs/aws/bedrock/docs/API_agent_CreateDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDataSource"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_CreateDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDataSource
<a name="API_agent_CreateDataSource"></a>

Connects a knowledge base to a data source. You specify the configuration for the specific data source service in the `dataSourceConfiguration` field.

**Important**  
You can't change the `chunkingConfiguration` after you create the data source connector.

## Request Syntax
<a name="API_agent_CreateDataSource_RequestSyntax"></a>

```
PUT /knowledgebases/{{knowledgeBaseId}}/datasources/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dataDeletionPolicy": "{{string}}",
   "dataSourceConfiguration": { 
      "confluenceConfiguration": { 
         "crawlerConfiguration": { 
            "filterConfiguration": { 
               "patternObjectFilter": { 
                  "filters": [ 
                     { 
                        "exclusionFilters": [ "{{string}}" ],
                        "inclusionFilters": [ "{{string}}" ],
                        "objectType": "{{string}}"
                     }
                  ]
               },
               "type": "{{string}}"
            }
         },
         "sourceConfiguration": { 
            "authType": "{{string}}",
            "credentialsSecretArn": "{{string}}",
            "hostType": "{{string}}",
            "hostUrl": "{{string}}"
         }
      },
      "managedKnowledgeBaseConnectorConfiguration": { 
         "connectorParameters": {{JSON value}},
         "deletionProtectionConfiguration": { 
            "deletionProtectionStatus": "{{string}}",
            "deletionProtectionThreshold": {{number}}
         },
         "mediaExtractionConfiguration": { 
            "audioExtractionConfiguration": { 
               "audioExtractionStatus": "{{string}}"
            },
            "imageExtractionConfiguration": { 
               "imageExtractionStatus": "{{string}}"
            },
            "videoExtractionConfiguration": { 
               "videoExtractionStatus": "{{string}}"
            }
         }
      },
      "s3Configuration": { 
         "bucketArn": "{{string}}",
         "bucketOwnerAccountId": "{{string}}",
         "inclusionPrefixes": [ "{{string}}" ]
      },
      "salesforceConfiguration": { 
         "crawlerConfiguration": { 
            "filterConfiguration": { 
               "patternObjectFilter": { 
                  "filters": [ 
                     { 
                        "exclusionFilters": [ "{{string}}" ],
                        "inclusionFilters": [ "{{string}}" ],
                        "objectType": "{{string}}"
                     }
                  ]
               },
               "type": "{{string}}"
            }
         },
         "sourceConfiguration": { 
            "authType": "{{string}}",
            "credentialsSecretArn": "{{string}}",
            "hostUrl": "{{string}}"
         }
      },
      "sharePointConfiguration": { 
         "crawlerConfiguration": { 
            "filterConfiguration": { 
               "patternObjectFilter": { 
                  "filters": [ 
                     { 
                        "exclusionFilters": [ "{{string}}" ],
                        "inclusionFilters": [ "{{string}}" ],
                        "objectType": "{{string}}"
                     }
                  ]
               },
               "type": "{{string}}"
            }
         },
         "sourceConfiguration": { 
            "authType": "{{string}}",
            "credentialsSecretArn": "{{string}}",
            "domain": "{{string}}",
            "hostType": "{{string}}",
            "siteUrls": [ "{{string}}" ],
            "tenantId": "{{string}}"
         }
      },
      "type": "{{string}}",
      "webConfiguration": { 
         "crawlerConfiguration": { 
            "crawlerLimits": { 
               "maxPages": {{number}},
               "rateLimit": {{number}}
            },
            "exclusionFilters": [ "{{string}}" ],
            "inclusionFilters": [ "{{string}}" ],
            "scope": "{{string}}",
            "userAgent": "{{string}}",
            "userAgentHeader": "{{string}}"
         },
         "sourceConfiguration": { 
            "urlConfiguration": { 
               "seedUrls": [ 
                  { 
                     "url": "{{string}}"
                  }
               ]
            }
         }
      }
   },
   "description": "{{string}}",
   "name": "{{string}}",
   "serverSideEncryptionConfiguration": { 
      "kmsKeyArn": "{{string}}"
   },
   "vectorIngestionConfiguration": { 
      "chunkingConfiguration": { 
         "chunkingStrategy": "{{string}}",
         "fixedSizeChunkingConfiguration": { 
            "maxTokens": {{number}},
            "overlapPercentage": {{number}}
         },
         "hierarchicalChunkingConfiguration": { 
            "levelConfigurations": [ 
               { 
                  "maxTokens": {{number}}
               }
            ],
            "overlapTokens": {{number}}
         },
         "semanticChunkingConfiguration": { 
            "breakpointPercentileThreshold": {{number}},
            "bufferSize": {{number}},
            "maxTokens": {{number}}
         }
      },
      "contextEnrichmentConfiguration": { 
         "bedrockFoundationModelConfiguration": { 
            "enrichmentStrategyConfiguration": { 
               "method": "{{string}}"
            },
            "modelArn": "{{string}}"
         },
         "type": "{{string}}"
      },
      "customTransformationConfiguration": { 
         "intermediateStorage": { 
            "s3Location": { 
               "uri": "{{string}}"
            }
         },
         "transformations": [ 
            { 
               "stepToApply": "{{string}}",
               "transformationFunction": { 
                  "transformationLambdaConfiguration": { 
                     "lambdaArn": "{{string}}"
                  }
               }
            }
         ]
      },
      "parsingConfiguration": { 
         "bedrockDataAutomationConfiguration": { 
            "parsingModality": "{{string}}"
         },
         "bedrockFoundationModelConfiguration": { 
            "modelArn": "{{string}}",
            "parsingModality": "{{string}}",
            "parsingPrompt": { 
               "parsingPromptText": "{{string}}"
            }
         },
         "parsingStrategy": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base to which to add the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_CreateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [dataDeletionPolicy](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-dataDeletionPolicy"></a>
The data deletion policy for the data source.  
You can set the data deletion policy to:  
+ DELETE: Deletes all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the **vector store itself is not deleted**, only the data. This flag is ignored if an AWS account is deleted.
+ RETAIN: Retains all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the **vector store itself is not deleted** if you delete a knowledge base or data source resource.
For managed knowledge bases, the only supported option is `DELETE`, which is also the default.
Type: String  
Valid Values: `RETAIN | DELETE`   
Required: No

 ** [dataSourceConfiguration](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-dataSourceConfiguration"></a>
The connection configuration for the data source.  
Type: [DataSourceConfiguration](API_agent_DataSourceConfiguration.md) object  
Required: Yes

 ** [description](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-description"></a>
A description of the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [name](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-name"></a>
The name of the data source.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [serverSideEncryptionConfiguration](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-serverSideEncryptionConfiguration"></a>
Contains details about the server-side encryption for the data source.  
Type: [ServerSideEncryptionConfiguration](API_agent_ServerSideEncryptionConfiguration.md) object  
Required: No

 ** [vectorIngestionConfiguration](#API_agent_CreateDataSource_RequestSyntax) **   <a name="bedrock-agent_CreateDataSource-request-vectorIngestionConfiguration"></a>
Contains details about how to ingest the documents in the data source.  
Type: [VectorIngestionConfiguration](API_agent_VectorIngestionConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_agent_CreateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataSource": { 
      "createdAt": "string",
      "dataDeletionPolicy": "string",
      "dataSourceConfiguration": { 
         "confluenceConfiguration": { 
            "crawlerConfiguration": { 
               "filterConfiguration": { 
                  "patternObjectFilter": { 
                     "filters": [ 
                        { 
                           "exclusionFilters": [ "string" ],
                           "inclusionFilters": [ "string" ],
                           "objectType": "string"
                        }
                     ]
                  },
                  "type": "string"
               }
            },
            "sourceConfiguration": { 
               "authType": "string",
               "credentialsSecretArn": "string",
               "hostType": "string",
               "hostUrl": "string"
            }
         },
         "managedKnowledgeBaseConnectorConfiguration": { 
            "connectorParameters": JSON value,
            "deletionProtectionConfiguration": { 
               "deletionProtectionStatus": "string",
               "deletionProtectionThreshold": number
            },
            "mediaExtractionConfiguration": { 
               "audioExtractionConfiguration": { 
                  "audioExtractionStatus": "string"
               },
               "imageExtractionConfiguration": { 
                  "imageExtractionStatus": "string"
               },
               "videoExtractionConfiguration": { 
                  "videoExtractionStatus": "string"
               }
            }
         },
         "s3Configuration": { 
            "bucketArn": "string",
            "bucketOwnerAccountId": "string",
            "inclusionPrefixes": [ "string" ]
         },
         "salesforceConfiguration": { 
            "crawlerConfiguration": { 
               "filterConfiguration": { 
                  "patternObjectFilter": { 
                     "filters": [ 
                        { 
                           "exclusionFilters": [ "string" ],
                           "inclusionFilters": [ "string" ],
                           "objectType": "string"
                        }
                     ]
                  },
                  "type": "string"
               }
            },
            "sourceConfiguration": { 
               "authType": "string",
               "credentialsSecretArn": "string",
               "hostUrl": "string"
            }
         },
         "sharePointConfiguration": { 
            "crawlerConfiguration": { 
               "filterConfiguration": { 
                  "patternObjectFilter": { 
                     "filters": [ 
                        { 
                           "exclusionFilters": [ "string" ],
                           "inclusionFilters": [ "string" ],
                           "objectType": "string"
                        }
                     ]
                  },
                  "type": "string"
               }
            },
            "sourceConfiguration": { 
               "authType": "string",
               "credentialsSecretArn": "string",
               "domain": "string",
               "hostType": "string",
               "siteUrls": [ "string" ],
               "tenantId": "string"
            }
         },
         "type": "string",
         "webConfiguration": { 
            "crawlerConfiguration": { 
               "crawlerLimits": { 
                  "maxPages": number,
                  "rateLimit": number
               },
               "exclusionFilters": [ "string" ],
               "inclusionFilters": [ "string" ],
               "scope": "string",
               "userAgent": "string",
               "userAgentHeader": "string"
            },
            "sourceConfiguration": { 
               "urlConfiguration": { 
                  "seedUrls": [ 
                     { 
                        "url": "string"
                     }
                  ]
               }
            }
         }
      },
      "dataSourceId": "string",
      "description": "string",
      "failureReasons": [ "string" ],
      "knowledgeBaseId": "string",
      "name": "string",
      "serverSideEncryptionConfiguration": { 
         "kmsKeyArn": "string"
      },
      "status": "string",
      "updatedAt": "string",
      "vectorIngestionConfiguration": { 
         "chunkingConfiguration": { 
            "chunkingStrategy": "string",
            "fixedSizeChunkingConfiguration": { 
               "maxTokens": number,
               "overlapPercentage": number
            },
            "hierarchicalChunkingConfiguration": { 
               "levelConfigurations": [ 
                  { 
                     "maxTokens": number
                  }
               ],
               "overlapTokens": number
            },
            "semanticChunkingConfiguration": { 
               "breakpointPercentileThreshold": number,
               "bufferSize": number,
               "maxTokens": number
            }
         },
         "contextEnrichmentConfiguration": { 
            "bedrockFoundationModelConfiguration": { 
               "enrichmentStrategyConfiguration": { 
                  "method": "string"
               },
               "modelArn": "string"
            },
            "type": "string"
         },
         "customTransformationConfiguration": { 
            "intermediateStorage": { 
               "s3Location": { 
                  "uri": "string"
               }
            },
            "transformations": [ 
               { 
                  "stepToApply": "string",
                  "transformationFunction": { 
                     "transformationLambdaConfiguration": { 
                        "lambdaArn": "string"
                     }
                  }
               }
            ]
         },
         "parsingConfiguration": { 
            "bedrockDataAutomationConfiguration": { 
               "parsingModality": "string"
            },
            "bedrockFoundationModelConfiguration": { 
               "modelArn": "string",
               "parsingModality": "string",
               "parsingPrompt": { 
                  "parsingPromptText": "string"
               }
            },
            "parsingStrategy": "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_agent_CreateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataSource](#API_agent_CreateDataSource_ResponseSyntax) **   <a name="bedrock-agent_CreateDataSource-response-dataSource"></a>
Contains details about the data source.  
Type: [DataSource](API_agent_DataSource.md) object

## Errors
<a name="API_agent_CreateDataSource_Errors"></a>

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

## See Also
<a name="API_agent_CreateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateDataSource) 