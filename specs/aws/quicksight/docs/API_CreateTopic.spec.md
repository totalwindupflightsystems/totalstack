---
id: "@specs/aws/quicksight/docs/API_CreateTopic"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTopic"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateTopic

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateTopic
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTopic
<a name="API_CreateTopic"></a>

Creates a new Q topic.

## Request Syntax
<a name="API_CreateTopic_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/topics HTTP/1.1
Content-type: application/json

{
   "CustomInstructions": { 
      "CustomInstructionsString": "{{string}}"
   },
   "FolderArns": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Topic": { 
      "ConfigOptions": { 
         "QBusinessInsightsEnabled": {{boolean}}
      },
      "DataSets": [ 
         { 
            "CalculatedFields": [ 
               { 
                  "Aggregation": "{{string}}",
                  "AllowedAggregations": [ "{{string}}" ],
                  "CalculatedFieldDescription": "{{string}}",
                  "CalculatedFieldName": "{{string}}",
                  "CalculatedFieldSynonyms": [ "{{string}}" ],
                  "CellValueSynonyms": [ 
                     { 
                        "CellValue": "{{string}}",
                        "Synonyms": [ "{{string}}" ]
                     }
                  ],
                  "ColumnDataRole": "{{string}}",
                  "ComparativeOrder": { 
                     "SpecifedOrder": [ "{{string}}" ],
                     "TreatUndefinedSpecifiedValues": "{{string}}",
                     "UseOrdering": "{{string}}"
                  },
                  "DefaultFormatting": { 
                     "DisplayFormat": "{{string}}",
                     "DisplayFormatOptions": { 
                        "BlankCellFormat": "{{string}}",
                        "CurrencySymbol": "{{string}}",
                        "DateFormat": "{{string}}",
                        "DecimalSeparator": "{{string}}",
                        "FractionDigits": {{number}},
                        "GroupingSeparator": "{{string}}",
                        "NegativeFormat": { 
                           "Prefix": "{{string}}",
                           "Suffix": "{{string}}"
                        },
                        "Prefix": "{{string}}",
                        "Suffix": "{{string}}",
                        "UnitScaler": "{{string}}",
                        "UseBlankCellFormat": {{boolean}},
                        "UseGrouping": {{boolean}}
                     }
                  },
                  "DisableIndexing": {{boolean}},
                  "Expression": "{{string}}",
                  "IsIncludedInTopic": {{boolean}},
                  "NeverAggregateInFilter": {{boolean}},
                  "NonAdditive": {{boolean}},
                  "NotAllowedAggregations": [ "{{string}}" ],
                  "SemanticType": { 
                     "FalseyCellValue": "{{string}}",
                     "FalseyCellValueSynonyms": [ "{{string}}" ],
                     "SubTypeName": "{{string}}",
                     "TruthyCellValue": "{{string}}",
                     "TruthyCellValueSynonyms": [ "{{string}}" ],
                     "TypeName": "{{string}}",
                     "TypeParameters": { 
                        "{{string}}" : "{{string}}" 
                     }
                  },
                  "TimeGranularity": "{{string}}"
               }
            ],
            "Columns": [ 
               { 
                  "Aggregation": "{{string}}",
                  "AllowedAggregations": [ "{{string}}" ],
                  "CellValueSynonyms": [ 
                     { 
                        "CellValue": "{{string}}",
                        "Synonyms": [ "{{string}}" ]
                     }
                  ],
                  "ColumnDataRole": "{{string}}",
                  "ColumnDescription": "{{string}}",
                  "ColumnFriendlyName": "{{string}}",
                  "ColumnName": "{{string}}",
                  "ColumnSynonyms": [ "{{string}}" ],
                  "ComparativeOrder": { 
                     "SpecifedOrder": [ "{{string}}" ],
                     "TreatUndefinedSpecifiedValues": "{{string}}",
                     "UseOrdering": "{{string}}"
                  },
                  "DefaultFormatting": { 
                     "DisplayFormat": "{{string}}",
                     "DisplayFormatOptions": { 
                        "BlankCellFormat": "{{string}}",
                        "CurrencySymbol": "{{string}}",
                        "DateFormat": "{{string}}",
                        "DecimalSeparator": "{{string}}",
                        "FractionDigits": {{number}},
                        "GroupingSeparator": "{{string}}",
                        "NegativeFormat": { 
                           "Prefix": "{{string}}",
                           "Suffix": "{{string}}"
                        },
                        "Prefix": "{{string}}",
                        "Suffix": "{{string}}",
                        "UnitScaler": "{{string}}",
                        "UseBlankCellFormat": {{boolean}},
                        "UseGrouping": {{boolean}}
                     }
                  },
                  "DisableIndexing": {{boolean}},
                  "IsIncludedInTopic": {{boolean}},
                  "NeverAggregateInFilter": {{boolean}},
                  "NonAdditive": {{boolean}},
                  "NotAllowedAggregations": [ "{{string}}" ],
                  "SemanticType": { 
                     "FalseyCellValue": "{{string}}",
                     "FalseyCellValueSynonyms": [ "{{string}}" ],
                     "SubTypeName": "{{string}}",
                     "TruthyCellValue": "{{string}}",
                     "TruthyCellValueSynonyms": [ "{{string}}" ],
                     "TypeName": "{{string}}",
                     "TypeParameters": { 
                        "{{string}}" : "{{string}}" 
                     }
                  },
                  "TimeGranularity": "{{string}}"
               }
            ],
            "DataAggregation": { 
               "DatasetRowDateGranularity": "{{string}}",
               "DefaultDateColumnName": "{{string}}"
            },
            "DatasetArn": "{{string}}",
            "DatasetDescription": "{{string}}",
            "DatasetName": "{{string}}",
            "Filters": [ 
               { 
                  "CategoryFilter": { 
                     "CategoryFilterFunction": "{{string}}",
                     "CategoryFilterType": "{{string}}",
                     "Constant": { 
                        "CollectiveConstant": { 
                           "ValueList": [ "{{string}}" ]
                        },
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "Inverse": {{boolean}}
                  },
                  "DateRangeFilter": { 
                     "Constant": { 
                        "ConstantType": "{{string}}",
                        "RangeConstant": { 
                           "Maximum": "{{string}}",
                           "Minimum": "{{string}}"
                        }
                     },
                     "Inclusive": {{boolean}}
                  },
                  "FilterClass": "{{string}}",
                  "FilterDescription": "{{string}}",
                  "FilterName": "{{string}}",
                  "FilterSynonyms": [ "{{string}}" ],
                  "FilterType": "{{string}}",
                  "NullFilter": { 
                     "Constant": { 
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "Inverse": {{boolean}},
                     "NullFilterType": "{{string}}"
                  },
                  "NumericEqualityFilter": { 
                     "Aggregation": "{{string}}",
                     "Constant": { 
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     }
                  },
                  "NumericRangeFilter": { 
                     "Aggregation": "{{string}}",
                     "Constant": { 
                        "ConstantType": "{{string}}",
                        "RangeConstant": { 
                           "Maximum": "{{string}}",
                           "Minimum": "{{string}}"
                        }
                     },
                     "Inclusive": {{boolean}}
                  },
                  "OperandFieldName": "{{string}}",
                  "RelativeDateFilter": { 
                     "Constant": { 
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "RelativeDateFilterFunction": "{{string}}",
                     "TimeGranularity": "{{string}}"
                  }
               }
            ],
            "NamedEntities": [ 
               { 
                  "Definition": [ 
                     { 
                        "FieldName": "{{string}}",
                        "Metric": { 
                           "Aggregation": "{{string}}",
                           "AggregationFunctionParameters": { 
                              "{{string}}" : "{{string}}" 
                           }
                        },
                        "PropertyName": "{{string}}",
                        "PropertyRole": "{{string}}",
                        "PropertyUsage": "{{string}}"
                     }
                  ],
                  "EntityDescription": "{{string}}",
                  "EntityName": "{{string}}",
                  "EntitySynonyms": [ "{{string}}" ],
                  "SemanticEntityType": { 
                     "SubTypeName": "{{string}}",
                     "TypeName": "{{string}}",
                     "TypeParameters": { 
                        "{{string}}" : "{{string}}" 
                     }
                  }
               }
            ]
         }
      ],
      "Description": "{{string}}",
      "Name": "{{string}}",
      "UserExperienceVersion": "{{string}}"
   },
   "TopicId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTopic_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateTopic_RequestSyntax) **   <a name="QS-CreateTopic-request-uri-AwsAccountId"></a>
The ID of the AWS account that you want to create a topic in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateTopic_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Topic](#API_CreateTopic_RequestSyntax) **   <a name="QS-CreateTopic-request-Topic"></a>
The definition of a topic to create.  
Type: [TopicDetails](API_TopicDetails.md) object  
Required: Yes

 ** [TopicId](#API_CreateTopic_RequestSyntax) **   <a name="QS-CreateTopic-request-TopicId"></a>
The ID for the topic that you want to create. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

 ** [CustomInstructions](#API_CreateTopic_RequestSyntax) **   <a name="QS-CreateTopic-request-CustomInstructions"></a>
Custom instructions for the topic.  
Type: [CustomInstructions](API_CustomInstructions.md) object  
Required: No

 ** [FolderArns](#API_CreateTopic_RequestSyntax) **   <a name="QS-CreateTopic-request-FolderArns"></a>
The Folder ARN of the folder that you want the topic to reside in.  
Type: Array of strings  
Array Members: Maximum number of 1 item.  
Required: No

 ** [Tags](#API_CreateTopic_RequestSyntax) **   <a name="QS-CreateTopic-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags that are assigned to the dataset.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateTopic_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RefreshArn": "string",
   "RequestId": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_CreateTopic_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateTopic_ResponseSyntax) **   <a name="QS-CreateTopic-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateTopic_ResponseSyntax) **   <a name="QS-CreateTopic-response-Arn"></a>
The Amazon Resource Name (ARN) of the topic.  
Type: String

 ** [RefreshArn](#API_CreateTopic_ResponseSyntax) **   <a name="QS-CreateTopic-response-RefreshArn"></a>
The Amazon Resource Name (ARN) of the topic refresh.  
Type: String

 ** [RequestId](#API_CreateTopic_ResponseSyntax) **   <a name="QS-CreateTopic-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TopicId](#API_CreateTopic_ResponseSyntax) **   <a name="QS-CreateTopic-response-TopicId"></a>
The ID for the topic that you want to create. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$` 

## Errors
<a name="API_CreateTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_CreateTopic_Examples"></a>

### Example
<a name="API_CreateTopic_Example_1"></a>

This example illustrates one usage of CreateTopic.

#### Sample Request
<a name="API_CreateTopic_Example_1_Request"></a>

```
POST /accounts/{AwsAccountId}/topics HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_CreateTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateTopic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateTopic) 