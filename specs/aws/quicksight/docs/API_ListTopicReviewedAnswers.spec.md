---
id: "@specs/aws/quicksight/docs/API_ListTopicReviewedAnswers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTopicReviewedAnswers"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListTopicReviewedAnswers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListTopicReviewedAnswers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTopicReviewedAnswers
<a name="API_ListTopicReviewedAnswers"></a>

Lists all reviewed answers for a Q Topic.

## Request Syntax
<a name="API_ListTopicReviewedAnswers_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/topics/{{TopicId}}/reviewed-answers HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTopicReviewedAnswers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListTopicReviewedAnswers_RequestSyntax) **   <a name="QS-ListTopicReviewedAnswers-request-uri-AwsAccountId"></a>
The ID of the AWS account that containd the reviewed answers that you want listed.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TopicId](#API_ListTopicReviewedAnswers_RequestSyntax) **   <a name="QS-ListTopicReviewedAnswers-request-uri-TopicId"></a>
The ID for the topic that contains the reviewed answer that you want to list. This ID is unique per AWS Region for each AWS account.  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

## Request Body
<a name="API_ListTopicReviewedAnswers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTopicReviewedAnswers_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Answers": [ 
      { 
         "AnswerId": "string",
         "Arn": "string",
         "DatasetArn": "string",
         "Mir": { 
            "ContributionAnalysis": { 
               "Direction": "string",
               "Factors": [ 
                  { 
                     "FieldName": "string"
                  }
               ],
               "SortType": "string",
               "TimeRanges": { 
                  "EndRange": { 
                     "AggMetrics": [ 
                        { 
                           "Function": "string",
                           "MetricOperand": { 
                              "Identity": "string"
                           },
                           "SortDirection": "string"
                        }
                     ],
                     "Aggregation": "string",
                     "AggregationFunctionParameters": { 
                        "string" : "string" 
                     },
                     "AggregationPartitionBy": [ 
                        { 
                           "FieldName": "string",
                           "TimeGranularity": "string"
                        }
                     ],
                     "Anchor": { 
                        "AnchorType": "string",
                        "Offset": number,
                        "TimeGranularity": "string"
                     },
                     "Constant": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "FilterClass": "string",
                     "FilterType": "string",
                     "Function": "string",
                     "Inclusive": boolean,
                     "Inverse": boolean,
                     "LastNextOffset": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "NullFilter": "string",
                     "OperandField": { 
                        "Identity": "string"
                     },
                     "Range": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "SortDirection": "string",
                     "TimeGranularity": "string",
                     "TopBottomLimit": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     }
                  },
                  "StartRange": { 
                     "AggMetrics": [ 
                        { 
                           "Function": "string",
                           "MetricOperand": { 
                              "Identity": "string"
                           },
                           "SortDirection": "string"
                        }
                     ],
                     "Aggregation": "string",
                     "AggregationFunctionParameters": { 
                        "string" : "string" 
                     },
                     "AggregationPartitionBy": [ 
                        { 
                           "FieldName": "string",
                           "TimeGranularity": "string"
                        }
                     ],
                     "Anchor": { 
                        "AnchorType": "string",
                        "Offset": number,
                        "TimeGranularity": "string"
                     },
                     "Constant": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "FilterClass": "string",
                     "FilterType": "string",
                     "Function": "string",
                     "Inclusive": boolean,
                     "Inverse": boolean,
                     "LastNextOffset": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "NullFilter": "string",
                     "OperandField": { 
                        "Identity": "string"
                     },
                     "Range": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "SortDirection": "string",
                     "TimeGranularity": "string",
                     "TopBottomLimit": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     }
                  }
               }
            },
            "Filters": [ 
               [ 
                  { 
                     "AggMetrics": [ 
                        { 
                           "Function": "string",
                           "MetricOperand": { 
                              "Identity": "string"
                           },
                           "SortDirection": "string"
                        }
                     ],
                     "Aggregation": "string",
                     "AggregationFunctionParameters": { 
                        "string" : "string" 
                     },
                     "AggregationPartitionBy": [ 
                        { 
                           "FieldName": "string",
                           "TimeGranularity": "string"
                        }
                     ],
                     "Anchor": { 
                        "AnchorType": "string",
                        "Offset": number,
                        "TimeGranularity": "string"
                     },
                     "Constant": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "FilterClass": "string",
                     "FilterType": "string",
                     "Function": "string",
                     "Inclusive": boolean,
                     "Inverse": boolean,
                     "LastNextOffset": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "NullFilter": "string",
                     "OperandField": { 
                        "Identity": "string"
                     },
                     "Range": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     },
                     "SortDirection": "string",
                     "TimeGranularity": "string",
                     "TopBottomLimit": { 
                        "ConstantType": "string",
                        "Maximum": "string",
                        "Minimum": "string",
                        "Value": "string",
                        "ValueList": [ 
                           { 
                              "ConstantType": "string",
                              "Value": "string"
                           }
                        ]
                     }
                  }
               ]
            ],
            "GroupByList": [ 
               { 
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
                  },
                  "FieldName": { 
                     "Identity": "string"
                  },
                  "NamedEntity": { 
                     "NamedEntityName": "string"
                  },
                  "Sort": { 
                     "Operand": { 
                        "Identity": "string"
                     },
                     "SortDirection": "string"
                  },
                  "TimeGranularity": "string"
               }
            ],
            "Metrics": [ 
               { 
                  "CalculatedFieldReferences": [ 
                     { 
                        "Identity": "string"
                     }
                  ],
                  "ComparisonMethod": { 
                     "Period": "string",
                     "Type": "string",
                     "WindowSize": number
                  },
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
                  },
                  "Expression": "string",
                  "Function": { 
                     "Aggregation": "string",
                     "AggregationFunctionParameters": { 
                        "string" : "string" 
                     },
                     "Period": "string",
                     "PeriodField": "string"
                  },
                  "MetricId": { 
                     "Identity": "string"
                  },
                  "NamedEntity": { 
                     "NamedEntityName": "string"
                  },
                  "Operands": [ 
                     { 
                        "Identity": "string"
                     }
                  ]
               }
            ],
            "Sort": { 
               "Operand": { 
                  "Identity": "string"
               },
               "SortDirection": "string"
            },
            "Visual": { 
               "type": "string"
            }
         },
         "PrimaryVisual": { 
            "Ir": { 
               "ContributionAnalysis": { 
                  "Direction": "string",
                  "Factors": [ 
                     { 
                        "FieldName": "string"
                     }
                  ],
                  "SortType": "string",
                  "TimeRanges": { 
                     "EndRange": { 
                        "AggMetrics": [ 
                           { 
                              "Function": "string",
                              "MetricOperand": { 
                                 "Identity": "string"
                              },
                              "SortDirection": "string"
                           }
                        ],
                        "Aggregation": "string",
                        "AggregationFunctionParameters": { 
                           "string" : "string" 
                        },
                        "AggregationPartitionBy": [ 
                           { 
                              "FieldName": "string",
                              "TimeGranularity": "string"
                           }
                        ],
                        "Anchor": { 
                           "AnchorType": "string",
                           "Offset": number,
                           "TimeGranularity": "string"
                        },
                        "Constant": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "FilterClass": "string",
                        "FilterType": "string",
                        "Function": "string",
                        "Inclusive": boolean,
                        "Inverse": boolean,
                        "LastNextOffset": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "NullFilter": "string",
                        "OperandField": { 
                           "Identity": "string"
                        },
                        "Range": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "SortDirection": "string",
                        "TimeGranularity": "string",
                        "TopBottomLimit": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        }
                     },
                     "StartRange": { 
                        "AggMetrics": [ 
                           { 
                              "Function": "string",
                              "MetricOperand": { 
                                 "Identity": "string"
                              },
                              "SortDirection": "string"
                           }
                        ],
                        "Aggregation": "string",
                        "AggregationFunctionParameters": { 
                           "string" : "string" 
                        },
                        "AggregationPartitionBy": [ 
                           { 
                              "FieldName": "string",
                              "TimeGranularity": "string"
                           }
                        ],
                        "Anchor": { 
                           "AnchorType": "string",
                           "Offset": number,
                           "TimeGranularity": "string"
                        },
                        "Constant": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "FilterClass": "string",
                        "FilterType": "string",
                        "Function": "string",
                        "Inclusive": boolean,
                        "Inverse": boolean,
                        "LastNextOffset": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "NullFilter": "string",
                        "OperandField": { 
                           "Identity": "string"
                        },
                        "Range": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "SortDirection": "string",
                        "TimeGranularity": "string",
                        "TopBottomLimit": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        }
                     }
                  }
               },
               "Filters": [ 
                  [ 
                     { 
                        "AggMetrics": [ 
                           { 
                              "Function": "string",
                              "MetricOperand": { 
                                 "Identity": "string"
                              },
                              "SortDirection": "string"
                           }
                        ],
                        "Aggregation": "string",
                        "AggregationFunctionParameters": { 
                           "string" : "string" 
                        },
                        "AggregationPartitionBy": [ 
                           { 
                              "FieldName": "string",
                              "TimeGranularity": "string"
                           }
                        ],
                        "Anchor": { 
                           "AnchorType": "string",
                           "Offset": number,
                           "TimeGranularity": "string"
                        },
                        "Constant": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "FilterClass": "string",
                        "FilterType": "string",
                        "Function": "string",
                        "Inclusive": boolean,
                        "Inverse": boolean,
                        "LastNextOffset": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "NullFilter": "string",
                        "OperandField": { 
                           "Identity": "string"
                        },
                        "Range": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "SortDirection": "string",
                        "TimeGranularity": "string",
                        "TopBottomLimit": { 
                           "ConstantType": "string",
                           "Maximum": "string",
                           "Minimum": "string",
                           "Value": "string",
                           "ValueList": [ 
                              { 
                                 "ConstantType": "string",
                                 "Value": "string"
                              }
                           ]
                        }
                     }
                  ]
               ],
               "GroupByList": [ 
                  { 
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
                     },
                     "FieldName": { 
                        "Identity": "string"
                     },
                     "NamedEntity": { 
                        "NamedEntityName": "string"
                     },
                     "Sort": { 
                        "Operand": { 
                           "Identity": "string"
                        },
                        "SortDirection": "string"
                     },
                     "TimeGranularity": "string"
                  }
               ],
               "Metrics": [ 
                  { 
                     "CalculatedFieldReferences": [ 
                        { 
                           "Identity": "string"
                        }
                     ],
                     "ComparisonMethod": { 
                        "Period": "string",
                        "Type": "string",
                        "WindowSize": number
                     },
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
                     },
                     "Expression": "string",
                     "Function": { 
                        "Aggregation": "string",
                        "AggregationFunctionParameters": { 
                           "string" : "string" 
                        },
                        "Period": "string",
                        "PeriodField": "string"
                     },
                     "MetricId": { 
                        "Identity": "string"
                     },
                     "NamedEntity": { 
                        "NamedEntityName": "string"
                     },
                     "Operands": [ 
                        { 
                           "Identity": "string"
                        }
                     ]
                  }
               ],
               "Sort": { 
                  "Operand": { 
                     "Identity": "string"
                  },
                  "SortDirection": "string"
               },
               "Visual": { 
                  "type": "string"
               }
            },
            "Role": "string",
            "SupportingVisuals": [ 
               "TopicVisual"
            ],
            "VisualId": "string"
         },
         "Question": "string",
         "Template": { 
            "Slots": [ 
               { 
                  "SlotId": "string",
                  "VisualId": "string"
               }
            ],
            "TemplateType": "string"
         }
      }
   ],
   "RequestId": "string",
   "TopicArn": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_ListTopicReviewedAnswers_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListTopicReviewedAnswers_ResponseSyntax) **   <a name="QS-ListTopicReviewedAnswers-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Answers](#API_ListTopicReviewedAnswers_ResponseSyntax) **   <a name="QS-ListTopicReviewedAnswers-response-Answers"></a>
The definition of all Answers in the topic.  
Type: Array of [TopicReviewedAnswer](API_TopicReviewedAnswer.md) objects

 ** [RequestId](#API_ListTopicReviewedAnswers_ResponseSyntax) **   <a name="QS-ListTopicReviewedAnswers-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TopicArn](#API_ListTopicReviewedAnswers_ResponseSyntax) **   <a name="QS-ListTopicReviewedAnswers-response-TopicArn"></a>
The Amazon Resource Name (ARN) of the topic.  
Type: String

 ** [TopicId](#API_ListTopicReviewedAnswers_ResponseSyntax) **   <a name="QS-ListTopicReviewedAnswers-response-TopicId"></a>
The ID for the topic that contains the reviewed answer that you want to list. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$` 

## Errors
<a name="API_ListTopicReviewedAnswers_Errors"></a>

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

## See Also
<a name="API_ListTopicReviewedAnswers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListTopicReviewedAnswers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListTopicReviewedAnswers) 