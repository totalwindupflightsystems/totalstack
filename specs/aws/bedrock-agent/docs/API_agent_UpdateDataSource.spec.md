---
id: "@specs/aws/bedrock-agent/docs/API_agent_UpdateDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDataSource"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# UpdateDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_UpdateDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDataSource
<a name="API_agent_UpdateDataSource"></a>

Updates the configurations for a data source connector.

**Important**  
You can't change the `chunkingConfiguration` after you create the data source connector. Specify the existing `chunkingConfiguration`.

## Request Syntax
<a name="API_agent_UpdateDataSource_RequestSyntax"></a>

```
PUT /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}} HTTP/1.1
Content-type: application/json

{
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
<a name="API_agent_UpdateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-uri-dataSourceId"></a>
The unique identifier of the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base for the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_UpdateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataDeletionPolicy](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-dataDeletionPolicy"></a>
The data deletion policy for the data source that you want to update.  
Type: String  
Valid Values: `RETAIN | DELETE`   
Required: No

 ** [dataSourceConfiguration](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-dataSourceConfiguration"></a>
The connection configuration for the data source that you want to update.  
Type: [DataSourceConfiguration](API_agent_DataSourceConfiguration.md) object  
Required: Yes

 ** [description](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-description"></a>
Specifies a new description for the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [name](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-name"></a>
Specifies a new name for the data source.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [serverSideEncryptionConfiguration](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-serverSideEncryptionConfiguration"></a>
Contains details about server-side encryption of the data source.  
Type: [ServerSideEncryptionConfiguration](API_agent_ServerSideEncryptionConfiguration.md) object  
Required: No

 ** [vectorIngestionConfiguration](#API_agent_UpdateDataSource_RequestSyntax) **   <a name="bedrock-agent_UpdateDataSource-request-vectorIngestionConfiguration"></a>
Contains details about how to ingest the documents in the data source.  
Type: [VectorIngestionConfiguration](API_agent_VectorIngestionConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_agent_UpdateDataSource_ResponseSyntax"></a>

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
<a name="API_agent_UpdateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataSource](#API_agent_UpdateDataSource_ResponseSyntax) **   <a name="bedrock-agent_UpdateDataSource-response-dataSource"></a>
Contains details about the data source.  
Type: [DataSource](API_agent_DataSource.md) object

## Errors
<a name="API_agent_UpdateDataSource_Errors"></a>

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
<a name="API_agent_UpdateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateDataSource) 