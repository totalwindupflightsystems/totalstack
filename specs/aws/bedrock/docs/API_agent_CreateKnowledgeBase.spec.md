---
id: "@specs/aws/bedrock/docs/API_agent_CreateKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_CreateKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateKnowledgeBase
<a name="API_agent_CreateKnowledgeBase"></a>

Creates a knowledge base. A knowledge base contains your data sources so that Large Language Models (LLMs) can use your data. To create a knowledge base, you must first set up your data sources and configure a supported vector store. For more information, see [Set up a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowlege-base-prereq.html).

**Note**  
To create a managed knowledge base, provide a `managedKnowledgeBaseConfiguration` during creation. For more information, see [Build a managed knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html).
+ Provide the `name` and an optional `description`.
+ Provide the Amazon Resource Name (ARN) with permissions to create a knowledge base in the `roleArn` field.
+ For managed knowledge bases, set `embeddingModelType` to `MANAGED` to use the service-managed embedding model, or `CUSTOM` with an `embeddingModelArn` to use your own. To use your own KMS key for encryption, provide the ARN in `serverSideEncryptionConfiguration`. No vector store configuration is required for managed knowledge bases.
+ For self-managed knowledge bases, provide the embedding model to use in the `embeddingModelArn` field in the `knowledgeBaseConfiguration` object.
+ For self-managed knowledge bases, provide the configuration for your vector store in the `storageConfiguration` object.
  + For an Amazon OpenSearch Service database, use the `opensearchServerlessConfiguration` object. For more information, see [Create a vector store in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html).
  + For an Amazon Aurora database, use the `RdsConfiguration` object. For more information, see [Create a vector store in Amazon Aurora](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html).
  + For a Pinecone database, use the `pineconeConfiguration` object. For more information, see [Create a vector store in Pinecone](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-pinecone.html).
  + For a Redis Enterprise Cloud database, use the `redisEnterpriseCloudConfiguration` object. For more information, see [Create a vector store in Redis Enterprise Cloud](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-redis.html).

## Request Syntax
<a name="API_agent_CreateKnowledgeBase_RequestSyntax"></a>

```
PUT /knowledgebases/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "knowledgeBaseConfiguration": { 
      "kendraKnowledgeBaseConfiguration": { 
         "kendraIndexArn": "{{string}}"
      },
      "managedKnowledgeBaseConfiguration": { 
         "embeddingModelArn": "{{string}}",
         "embeddingModelConfiguration": { 
            "bedrockEmbeddingModelConfiguration": { 
               "audio": [ 
                  { 
                     "segmentationConfiguration": { 
                        "fixedLengthDuration": {{number}}
                     }
                  }
               ],
               "dimensions": {{number}},
               "embeddingDataType": "{{string}}",
               "video": [ 
                  { 
                     "segmentationConfiguration": { 
                        "fixedLengthDuration": {{number}}
                     }
                  }
               ]
            }
         },
         "embeddingModelType": "{{string}}",
         "serverSideEncryptionConfiguration": { 
            "kmsKeyArn": "{{string}}"
         }
      },
      "sqlKnowledgeBaseConfiguration": { 
         "redshiftConfiguration": { 
            "queryEngineConfiguration": { 
               "provisionedConfiguration": { 
                  "authConfiguration": { 
                     "databaseUser": "{{string}}",
                     "type": "{{string}}",
                     "usernamePasswordSecretArn": "{{string}}"
                  },
                  "clusterIdentifier": "{{string}}"
               },
               "serverlessConfiguration": { 
                  "authConfiguration": { 
                     "type": "{{string}}",
                     "usernamePasswordSecretArn": "{{string}}"
                  },
                  "workgroupArn": "{{string}}"
               },
               "type": "{{string}}"
            },
            "queryGenerationConfiguration": { 
               "executionTimeoutSeconds": {{number}},
               "generationContext": { 
                  "curatedQueries": [ 
                     { 
                        "naturalLanguage": "{{string}}",
                        "sql": "{{string}}"
                     }
                  ],
                  "tables": [ 
                     { 
                        "columns": [ 
                           { 
                              "description": "{{string}}",
                              "inclusion": "{{string}}",
                              "name": "{{string}}"
                           }
                        ],
                        "description": "{{string}}",
                        "inclusion": "{{string}}",
                        "name": "{{string}}"
                     }
                  ]
               }
            },
            "storageConfigurations": [ 
               { 
                  "awsDataCatalogConfiguration": { 
                     "tableNames": [ "{{string}}" ]
                  },
                  "redshiftConfiguration": { 
                     "databaseName": "{{string}}"
                  },
                  "type": "{{string}}"
               }
            ]
         },
         "type": "{{string}}"
      },
      "type": "{{string}}",
      "vectorKnowledgeBaseConfiguration": { 
         "embeddingModelArn": "{{string}}",
         "embeddingModelConfiguration": { 
            "bedrockEmbeddingModelConfiguration": { 
               "audio": [ 
                  { 
                     "segmentationConfiguration": { 
                        "fixedLengthDuration": {{number}}
                     }
                  }
               ],
               "dimensions": {{number}},
               "embeddingDataType": "{{string}}",
               "video": [ 
                  { 
                     "segmentationConfiguration": { 
                        "fixedLengthDuration": {{number}}
                     }
                  }
               ]
            }
         },
         "supplementalDataStorageConfiguration": { 
            "storageLocations": [ 
               { 
                  "s3Location": { 
                     "uri": "{{string}}"
                  },
                  "type": "{{string}}"
               }
            ]
         }
      }
   },
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "storageConfiguration": { 
      "mongoDbAtlasConfiguration": { 
         "collectionName": "{{string}}",
         "credentialsSecretArn": "{{string}}",
         "databaseName": "{{string}}",
         "endpoint": "{{string}}",
         "endpointServiceName": "{{string}}",
         "fieldMapping": { 
            "metadataField": "{{string}}",
            "textField": "{{string}}",
            "vectorField": "{{string}}"
         },
         "textIndexName": "{{string}}",
         "vectorIndexName": "{{string}}"
      },
      "neptuneAnalyticsConfiguration": { 
         "fieldMapping": { 
            "metadataField": "{{string}}",
            "textField": "{{string}}"
         },
         "graphArn": "{{string}}"
      },
      "opensearchManagedClusterConfiguration": { 
         "domainArn": "{{string}}",
         "domainEndpoint": "{{string}}",
         "fieldMapping": { 
            "metadataField": "{{string}}",
            "textField": "{{string}}",
            "vectorField": "{{string}}"
         },
         "vectorIndexName": "{{string}}"
      },
      "opensearchServerlessConfiguration": { 
         "collectionArn": "{{string}}",
         "fieldMapping": { 
            "metadataField": "{{string}}",
            "textField": "{{string}}",
            "vectorField": "{{string}}"
         },
         "vectorIndexName": "{{string}}"
      },
      "pineconeConfiguration": { 
         "connectionString": "{{string}}",
         "credentialsSecretArn": "{{string}}",
         "fieldMapping": { 
            "metadataField": "{{string}}",
            "textField": "{{string}}"
         },
         "namespace": "{{string}}"
      },
      "rdsConfiguration": { 
         "credentialsSecretArn": "{{string}}",
         "databaseName": "{{string}}",
         "fieldMapping": { 
            "customMetadataField": "{{string}}",
            "metadataField": "{{string}}",
            "primaryKeyField": "{{string}}",
            "textField": "{{string}}",
            "vectorField": "{{string}}"
         },
         "resourceArn": "{{string}}",
         "tableName": "{{string}}"
      },
      "redisEnterpriseCloudConfiguration": { 
         "credentialsSecretArn": "{{string}}",
         "endpoint": "{{string}}",
         "fieldMapping": { 
            "metadataField": "{{string}}",
            "textField": "{{string}}",
            "vectorField": "{{string}}"
         },
         "vectorIndexName": "{{string}}"
      },
      "s3VectorsConfiguration": { 
         "indexArn": "{{string}}",
         "indexName": "{{string}}",
         "vectorBucketArn": "{{string}}"
      },
      "type": "{{string}}"
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateKnowledgeBase_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent_CreateKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-description"></a>
A description of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [knowledgeBaseConfiguration](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-knowledgeBaseConfiguration"></a>
Contains details about the embeddings model used for the knowledge base.  
Type: [KnowledgeBaseConfiguration](API_agent_KnowledgeBaseConfiguration.md) object  
Required: Yes

 ** [name](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-name"></a>
A name for the knowledge base.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [roleArn](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [storageConfiguration](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-storageConfiguration"></a>
Contains details about the configuration of the vector database used for the knowledge base.  
Type: [StorageConfiguration](API_agent_StorageConfiguration.md) object  
Required: No

 ** [tags](#API_agent_CreateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-request-tags"></a>
Specify the key-value pairs for the tags that you want to attach to your knowledge base in this object.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_agent_CreateKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "knowledgeBase": { 
      "createdAt": "string",
      "description": "string",
      "failureReasons": [ "string" ],
      "knowledgeBaseArn": "string",
      "knowledgeBaseConfiguration": { 
         "kendraKnowledgeBaseConfiguration": { 
            "kendraIndexArn": "string"
         },
         "managedKnowledgeBaseConfiguration": { 
            "embeddingModelArn": "string",
            "embeddingModelConfiguration": { 
               "bedrockEmbeddingModelConfiguration": { 
                  "audio": [ 
                     { 
                        "segmentationConfiguration": { 
                           "fixedLengthDuration": number
                        }
                     }
                  ],
                  "dimensions": number,
                  "embeddingDataType": "string",
                  "video": [ 
                     { 
                        "segmentationConfiguration": { 
                           "fixedLengthDuration": number
                        }
                     }
                  ]
               }
            },
            "embeddingModelType": "string",
            "serverSideEncryptionConfiguration": { 
               "kmsKeyArn": "string"
            }
         },
         "sqlKnowledgeBaseConfiguration": { 
            "redshiftConfiguration": { 
               "queryEngineConfiguration": { 
                  "provisionedConfiguration": { 
                     "authConfiguration": { 
                        "databaseUser": "string",
                        "type": "string",
                        "usernamePasswordSecretArn": "string"
                     },
                     "clusterIdentifier": "string"
                  },
                  "serverlessConfiguration": { 
                     "authConfiguration": { 
                        "type": "string",
                        "usernamePasswordSecretArn": "string"
                     },
                     "workgroupArn": "string"
                  },
                  "type": "string"
               },
               "queryGenerationConfiguration": { 
                  "executionTimeoutSeconds": number,
                  "generationContext": { 
                     "curatedQueries": [ 
                        { 
                           "naturalLanguage": "string",
                           "sql": "string"
                        }
                     ],
                     "tables": [ 
                        { 
                           "columns": [ 
                              { 
                                 "description": "string",
                                 "inclusion": "string",
                                 "name": "string"
                              }
                           ],
                           "description": "string",
                           "inclusion": "string",
                           "name": "string"
                        }
                     ]
                  }
               },
               "storageConfigurations": [ 
                  { 
                     "awsDataCatalogConfiguration": { 
                        "tableNames": [ "string" ]
                     },
                     "redshiftConfiguration": { 
                        "databaseName": "string"
                     },
                     "type": "string"
                  }
               ]
            },
            "type": "string"
         },
         "type": "string",
         "vectorKnowledgeBaseConfiguration": { 
            "embeddingModelArn": "string",
            "embeddingModelConfiguration": { 
               "bedrockEmbeddingModelConfiguration": { 
                  "audio": [ 
                     { 
                        "segmentationConfiguration": { 
                           "fixedLengthDuration": number
                        }
                     }
                  ],
                  "dimensions": number,
                  "embeddingDataType": "string",
                  "video": [ 
                     { 
                        "segmentationConfiguration": { 
                           "fixedLengthDuration": number
                        }
                     }
                  ]
               }
            },
            "supplementalDataStorageConfiguration": { 
               "storageLocations": [ 
                  { 
                     "s3Location": { 
                        "uri": "string"
                     },
                     "type": "string"
                  }
               ]
            }
         }
      },
      "knowledgeBaseId": "string",
      "name": "string",
      "roleArn": "string",
      "status": "string",
      "storageConfiguration": { 
         "mongoDbAtlasConfiguration": { 
            "collectionName": "string",
            "credentialsSecretArn": "string",
            "databaseName": "string",
            "endpoint": "string",
            "endpointServiceName": "string",
            "fieldMapping": { 
               "metadataField": "string",
               "textField": "string",
               "vectorField": "string"
            },
            "textIndexName": "string",
            "vectorIndexName": "string"
         },
         "neptuneAnalyticsConfiguration": { 
            "fieldMapping": { 
               "metadataField": "string",
               "textField": "string"
            },
            "graphArn": "string"
         },
         "opensearchManagedClusterConfiguration": { 
            "domainArn": "string",
            "domainEndpoint": "string",
            "fieldMapping": { 
               "metadataField": "string",
               "textField": "string",
               "vectorField": "string"
            },
            "vectorIndexName": "string"
         },
         "opensearchServerlessConfiguration": { 
            "collectionArn": "string",
            "fieldMapping": { 
               "metadataField": "string",
               "textField": "string",
               "vectorField": "string"
            },
            "vectorIndexName": "string"
         },
         "pineconeConfiguration": { 
            "connectionString": "string",
            "credentialsSecretArn": "string",
            "fieldMapping": { 
               "metadataField": "string",
               "textField": "string"
            },
            "namespace": "string"
         },
         "rdsConfiguration": { 
            "credentialsSecretArn": "string",
            "databaseName": "string",
            "fieldMapping": { 
               "customMetadataField": "string",
               "metadataField": "string",
               "primaryKeyField": "string",
               "textField": "string",
               "vectorField": "string"
            },
            "resourceArn": "string",
            "tableName": "string"
         },
         "redisEnterpriseCloudConfiguration": { 
            "credentialsSecretArn": "string",
            "endpoint": "string",
            "fieldMapping": { 
               "metadataField": "string",
               "textField": "string",
               "vectorField": "string"
            },
            "vectorIndexName": "string"
         },
         "s3VectorsConfiguration": { 
            "indexArn": "string",
            "indexName": "string",
            "vectorBucketArn": "string"
         },
         "type": "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_CreateKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBase](#API_agent_CreateKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_CreateKnowledgeBase-response-knowledgeBase"></a>
Contains details about the knowledge base.  
Type: [KnowledgeBase](API_agent_KnowledgeBase.md) object

## Errors
<a name="API_agent_CreateKnowledgeBase_Errors"></a>

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
<a name="API_agent_CreateKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateKnowledgeBase) 