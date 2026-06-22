---
id: "@specs/aws/bedrock/docs/API_agent_UpdateKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_UpdateKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateKnowledgeBase
<a name="API_agent_UpdateKnowledgeBase"></a>

Updates the configuration of a knowledge base with the fields that you specify. Because all fields will be overwritten, you must include the same values for fields that you want to keep the same.

You can change the following fields:
+  `name` 
+  `description` 
+  `roleArn` 

You can't change the `knowledgeBaseConfiguration` or `storageConfiguration` fields, so you must specify the same configurations as when you created the knowledge base. You can send a [GetKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html) request and copy the same configurations.

## Request Syntax
<a name="API_agent_UpdateKnowledgeBase_RequestSyntax"></a>

```
PUT /knowledgebases/{{knowledgeBaseId}} HTTP/1.1
Content-type: application/json

{
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
   }
}
```

## URI Request Parameters
<a name="API_agent_UpdateKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_agent_UpdateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base to update.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_UpdateKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_agent_UpdateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-request-description"></a>
Specifies a new description for the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [knowledgeBaseConfiguration](#API_agent_UpdateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-request-knowledgeBaseConfiguration"></a>
Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.  
Type: [KnowledgeBaseConfiguration](API_agent_KnowledgeBaseConfiguration.md) object  
Required: Yes

 ** [name](#API_agent_UpdateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-request-name"></a>
Specifies a new name for the knowledge base.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [roleArn](#API_agent_UpdateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-request-roleArn"></a>
Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [storageConfiguration](#API_agent_UpdateKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-request-storageConfiguration"></a>
Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.  
Type: [StorageConfiguration](API_agent_StorageConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_agent_UpdateKnowledgeBase_ResponseSyntax"></a>

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
<a name="API_agent_UpdateKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBase](#API_agent_UpdateKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_UpdateKnowledgeBase-response-knowledgeBase"></a>
Contains details about the knowledge base.  
Type: [KnowledgeBase](API_agent_KnowledgeBase.md) object

## Errors
<a name="API_agent_UpdateKnowledgeBase_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_UpdateKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateKnowledgeBase) 