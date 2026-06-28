---
id: "@specs/aws/quicksight/docs/API_DescribeTopic"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTopic"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeTopic

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeTopic
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTopic
<a name="API_DescribeTopic"></a>

Describes a topic.

## Request Syntax
<a name="API_DescribeTopic_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/topics/{{TopicId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTopic_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeTopic_RequestSyntax) **   <a name="QS-DescribeTopic-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TopicId](#API_DescribeTopic_RequestSyntax) **   <a name="QS-DescribeTopic-request-uri-TopicId"></a>
The ID of the topic that you want to describe. This ID is unique per AWS Region for each AWS account.  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

## Request Body
<a name="API_DescribeTopic_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTopic_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CustomInstructions": { 
      "CustomInstructionsString": "string"
   },
   "RequestId": "string",
   "Topic": { 
      "ConfigOptions": { 
         "QBusinessInsightsEnabled": boolean
      },
      "DataSets": [ 
         { 
            "CalculatedFields": [ 
               { 
                  "Aggregation": "string",
                  "AllowedAggregations": [ "string" ],
                  "CalculatedFieldDescription": "string",
                  "CalculatedFieldName": "string",
                  "CalculatedFieldSynonyms": [ "string" ],
                  "CellValueSynonyms": [ 
                     { 
                        "CellValue": "string",
                        "Synonyms": [ "string" ]
                     }
                  ],
                  "ColumnDataRole": "string",
                  "ComparativeOrder": { 
                     "SpecifedOrder": [ "string" ],
                     "TreatUndefinedSpecifiedValues": "string",
                     "UseOrdering": "string"
                  },
                  "DefaultFormatting": { 
                     "DisplayFormat": "string",
                     "DisplayFormatOptions": { 
                        "BlankCellFormat": "string",
                        "CurrencySymbol": "string",
                        "DateFormat": "string",
                        "DecimalSeparator": "string",
                        "FractionDigits": number,
                        "GroupingSeparator": "string",
                        "NegativeFormat": { 
                           "Prefix": "string",
                           "Suffix": "string"
                        },
                        "Prefix": "string",
                        "Suffix": "string",
                        "UnitScaler": "string",
                        "UseBlankCellFormat": boolean,
                        "UseGrouping": boolean
                     }
                  },
                  "DisableIndexing": boolean,
                  "Expression": "string",
                  "IsIncludedInTopic": boolean,
                  "NeverAggregateInFilter": boolean,
                  "NonAdditive": boolean,
                  "NotAllowedAggregations": [ "string" ],
                  "SemanticType": { 
                     "FalseyCellValue": "string",
                     "FalseyCellValueSynonyms": [ "string" ],
                     "SubTypeName": "string",
                     "TruthyCellValue": "string",
                     "TruthyCellValueSynonyms": [ "string" ],
                     "TypeName": "string",
                     "TypeParameters": { 
                        "string" : "string" 
                     }
                  },
                  "TimeGranularity": "string"
               }
            ],
            "Columns": [ 
               { 
                  "Aggregation": "string",
                  "AllowedAggregations": [ "string" ],
                  "CellValueSynonyms": [ 
                     { 
                        "CellValue": "string",
                        "Synonyms": [ "string" ]
                     }
                  ],
                  "ColumnDataRole": "string",
                  "ColumnDescription": "string",
                  "ColumnFriendlyName": "string",
                  "ColumnName": "string",
                  "ColumnSynonyms": [ "string" ],
                  "ComparativeOrder": { 
                     "SpecifedOrder": [ "string" ],
                     "TreatUndefinedSpecifiedValues": "string",
                     "UseOrdering": "string"
                  },
                  "DefaultFormatting": { 
                     "DisplayFormat": "string",
                     "DisplayFormatOptions": { 
                        "BlankCellFormat": "string",
                        "CurrencySymbol": "string",
                        "DateFormat": "string",
                        "DecimalSeparator": "string",
                        "FractionDigits": number,
                        "GroupingSeparator": "string",
                        "NegativeFormat": { 
                           "Prefix": "string",
                           "Suffix": "string"
                        },
                        "Prefix": "string",
                        "Suffix": "string",
                        "UnitScaler": "string",
                        "UseBlankCellFormat": boolean,
                        "UseGrouping": boolean
                     }
                  },
                  "DisableIndexing": boolean,
                  "IsIncludedInTopic": boolean,
                  "NeverAggregateInFilter": boolean,
                  "NonAdditive": boolean,
                  "NotAllowedAggregations": [ "string" ],
                  "SemanticType": { 
                     "FalseyCellValue": "string",
                     "FalseyCellValueSynonyms": [ "string" ],
                     "SubTypeName": "string",
                     "TruthyCellValue": "string",
                     "TruthyCellValueSynonyms": [ "string" ],
                     "TypeName": "string",
                     "TypeParameters": { 
                        "string" : "string" 
                     }
                  },
                  "TimeGranularity": "string"
               }
            ],
            "DataAggregation": { 
               "DatasetRowDateGranularity": "string",
               "DefaultDateColumnName": "string"
            },
            "DatasetArn": "string",
            "DatasetDescription": "string",
            "DatasetName": "string",
            "Filters": [ 
               { 
                  "CategoryFilter": { 
                     "CategoryFilterFunction": "string",
                     "CategoryFilterType": "string",
                     "Constant": { 
                        "CollectiveConstant": { 
                           "ValueList": [ "string" ]
                        },
                        "ConstantType": "string",
                        "SingularConstant": "string"
                     },
                     "Inverse": boolean
                  },
                  "DateRangeFilter": { 
                     "Constant": { 
                        "ConstantType": "string",
                        "RangeConstant": { 
                           "Maximum": "string",
                           "Minimum": "string"
                        }
                     },
                     "Inclusive": boolean
                  },
                  "FilterClass": "string",
                  "FilterDescription": "string",
                  "FilterName": "string",
                  "FilterSynonyms": [ "string" ],
                  "FilterType": "string",
                  "NullFilter": { 
                     "Constant": { 
                        "ConstantType": "string",
                        "SingularConstant": "string"
                     },
                     "Inverse": boolean,
                     "NullFilterType": "string"
                  },
                  "NumericEqualityFilter": { 
                     "Aggregation": "string",
                     "Constant": { 
                        "ConstantType": "string",
                        "SingularConstant": "string"
                     }
                  },
                  "NumericRangeFilter": { 
                     "Aggregation": "string",
                     "Constant": { 
                        "ConstantType": "string",
                        "RangeConstant": { 
                           "Maximum": "string",
                           "Minimum": "string"
                        }
                     },
                     "Inclusive": boolean
                  },
                  "OperandFieldName": "string",
                  "RelativeDateFilter": { 
                     "Constant": { 
                        "ConstantType": "string",
                        "SingularConstant": "string"
                     },
                     "RelativeDateFilterFunction": "string",
                     "TimeGranularity": "string"
                  }
               }
            ],
            "NamedEntities": [ 
               { 
                  "Definition": [ 
                     { 
                        "FieldName": "string",
                        "Metric": { 
                           "Aggregation": "string",
                           "AggregationFunctionParameters": { 
                              "string" : "string" 
                           }
                        },
                        "PropertyName": "string",
                        "PropertyRole": "string",
                        "PropertyUsage": "string"
                     }
                  ],
                  "EntityDescription": "string",
                  "EntityName": "string",
                  "EntitySynonyms": [ "string" ],
                  "SemanticEntityType": { 
                     "SubTypeName": "string",
                     "TypeName": "string",
                     "TypeParameters": { 
                        "string" : "string" 
                     }
                  }
               }
            ]
         }
      ],
      "Description": "string",
      "Name": "string",
      "UserExperienceVersion": "string"
   },
   "TopicId": "string"
}
```

## Response Elements
<a name="API_DescribeTopic_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeTopic_ResponseSyntax) **   <a name="QS-DescribeTopic-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeTopic_ResponseSyntax) **   <a name="QS-DescribeTopic-response-Arn"></a>
The Amazon Resource Name (ARN) of the topic.  
Type: String

 ** [CustomInstructions](#API_DescribeTopic_ResponseSyntax) **   <a name="QS-DescribeTopic-response-CustomInstructions"></a>
Custom instructions for the topic.  
Type: [CustomInstructions](API_CustomInstructions.md) object

 ** [RequestId](#API_DescribeTopic_ResponseSyntax) **   <a name="QS-DescribeTopic-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Topic](#API_DescribeTopic_ResponseSyntax) **   <a name="QS-DescribeTopic-response-Topic"></a>
The definition of a topic.  
Type: [TopicDetails](API_TopicDetails.md) object

 ** [TopicId](#API_DescribeTopic_ResponseSyntax) **   <a name="QS-DescribeTopic-response-TopicId"></a>
The ID of the topic that you want to describe. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$` 

## Errors
<a name="API_DescribeTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_DescribeTopic_Examples"></a>

### Example
<a name="API_DescribeTopic_Example_1"></a>

This example illustrates one usage of DescribeTopic.

#### Sample Request
<a name="API_DescribeTopic_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/topics/{TopicId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_DescribeTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeTopic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeTopic) 