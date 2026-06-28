---
id: "@specs/aws/quicksight/docs/API_DescribeDataSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataSet"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDataSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDataSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataSet
<a name="API_DescribeDataSet"></a>

Describes a dataset. This operation doesn't support datasets that include uploaded files as a source.

## Request Syntax
<a name="API_DescribeDataSet_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDataSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeDataSet_RequestSyntax) **   <a name="QS-DescribeDataSet-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DataSetId](#API_DescribeDataSet_RequestSyntax) **   <a name="QS-DescribeDataSet-request-uri-DataSetId"></a>
The ID for the dataset that you want to describe. This ID is unique per AWS Region for each AWS account.  
Required: Yes

## Request Body
<a name="API_DescribeDataSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDataSet_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSet": { 
      "Arn": "string",
      "ColumnGroups": [ 
         { 
            "GeoSpatialColumnGroup": { 
               "Columns": [ "string" ],
               "CountryCode": "string",
               "Name": "string"
            }
         }
      ],
      "ColumnLevelPermissionRules": [ 
         { 
            "ColumnNames": [ "string" ],
            "Principals": [ "string" ]
         }
      ],
      "ConsumedSpiceCapacityInBytes": number,
      "CreatedTime": number,
      "DataPrepConfiguration": { 
         "DestinationTableMap": { 
            "string" : { 
               "Alias": "string",
               "Source": { 
                  "TransformOperationId": "string"
               }
            }
         },
         "SourceTableMap": { 
            "string" : { 
               "DataSet": { 
                  "DataSetArn": "string",
                  "InputColumns": [ 
                     { 
                        "Id": "string",
                        "Name": "string",
                        "SubType": "string",
                        "Type": "string"
                     }
                  ]
               },
               "PhysicalTableId": "string"
            }
         },
         "TransformStepMap": { 
            "string" : { 
               "AggregateStep": { 
                  "Aggregations": [ 
                     { 
                        "AggregationFunction": { 
                           "ListAggregation": { 
                              "Distinct": boolean,
                              "InputColumnName": "string",
                              "Separator": "string"
                           },
                           "SimpleAggregation": { 
                              "FunctionType": "string",
                              "InputColumnName": "string"
                           }
                        },
                        "NewColumnId": "string",
                        "NewColumnName": "string"
                     }
                  ],
                  "Alias": "string",
                  "GroupByColumnNames": [ "string" ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "AppendStep": { 
                  "Alias": "string",
                  "AppendedColumns": [ 
                     { 
                        "ColumnName": "string",
                        "NewColumnId": "string"
                     }
                  ],
                  "FirstSource": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  },
                  "SecondSource": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "CastColumnTypesStep": { 
                  "Alias": "string",
                  "CastColumnTypeOperations": [ 
                     { 
                        "ColumnName": "string",
                        "Format": "string",
                        "NewColumnType": "string",
                        "SubType": "string"
                     }
                  ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "CreateColumnsStep": { 
                  "Alias": "string",
                  "Columns": [ 
                     { 
                        "ColumnId": "string",
                        "ColumnName": "string",
                        "Expression": "string"
                     }
                  ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "FiltersStep": { 
                  "Alias": "string",
                  "FilterOperations": [ 
                     { 
                        "ConditionExpression": "string",
                        "DateFilterCondition": { 
                           "ColumnName": "string",
                           "ComparisonFilterCondition": { 
                              "Operator": "string",
                              "Value": { 
                                 "StaticValue": number
                              }
                           },
                           "RangeFilterCondition": { 
                              "IncludeMaximum": boolean,
                              "IncludeMinimum": boolean,
                              "RangeMaximum": { 
                                 "StaticValue": number
                              },
                              "RangeMinimum": { 
                                 "StaticValue": number
                              }
                           }
                        },
                        "NumericFilterCondition": { 
                           "ColumnName": "string",
                           "ComparisonFilterCondition": { 
                              "Operator": "string",
                              "Value": { 
                                 "StaticValue": number
                              }
                           },
                           "RangeFilterCondition": { 
                              "IncludeMaximum": boolean,
                              "IncludeMinimum": boolean,
                              "RangeMaximum": { 
                                 "StaticValue": number
                              },
                              "RangeMinimum": { 
                                 "StaticValue": number
                              }
                           }
                        },
                        "StringFilterCondition": { 
                           "ColumnName": "string",
                           "ComparisonFilterCondition": { 
                              "Operator": "string",
                              "Value": { 
                                 "StaticValue": "string"
                              }
                           },
                           "ListFilterCondition": { 
                              "Operator": "string",
                              "Values": { 
                                 "StaticValues": [ "string" ]
                              }
                           }
                        }
                     }
                  ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "ImportTableStep": { 
                  "Alias": "string",
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "SourceTableId": "string"
                  }
               },
               "JoinStep": { 
                  "Alias": "string",
                  "LeftOperand": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  },
                  "LeftOperandProperties": { 
                     "OutputColumnNameOverrides": [ 
                        { 
                           "OutputColumnName": "string",
                           "SourceColumnName": "string"
                        }
                     ]
                  },
                  "OnClause": "string",
                  "RightOperand": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  },
                  "RightOperandProperties": { 
                     "OutputColumnNameOverrides": [ 
                        { 
                           "OutputColumnName": "string",
                           "SourceColumnName": "string"
                        }
                     ]
                  },
                  "Type": "string"
               },
               "PivotStep": { 
                  "Alias": "string",
                  "GroupByColumnNames": [ "string" ],
                  "PivotConfiguration": { 
                     "LabelColumnName": "string",
                     "PivotedLabels": [ 
                        { 
                           "LabelName": "string",
                           "NewColumnId": "string",
                           "NewColumnName": "string"
                        }
                     ]
                  },
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  },
                  "ValueColumnConfiguration": { 
                     "AggregationFunction": { 
                        "ListAggregation": { 
                           "Distinct": boolean,
                           "InputColumnName": "string",
                           "Separator": "string"
                        },
                        "SimpleAggregation": { 
                           "FunctionType": "string",
                           "InputColumnName": "string"
                        }
                     }
                  }
               },
               "ProjectStep": { 
                  "Alias": "string",
                  "ProjectedColumns": [ "string" ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "RenameColumnsStep": { 
                  "Alias": "string",
                  "RenameColumnOperations": [ 
                     { 
                        "ColumnName": "string",
                        "NewColumnName": "string"
                     }
                  ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  }
               },
               "UnpivotStep": { 
                  "Alias": "string",
                  "ColumnsToUnpivot": [ 
                     { 
                        "ColumnName": "string",
                        "NewValue": "string"
                     }
                  ],
                  "Source": { 
                     "ColumnIdMappings": [ 
                        { 
                           "SourceColumnId": "string",
                           "TargetColumnId": "string"
                        }
                     ],
                     "TransformOperationId": "string"
                  },
                  "UnpivotedLabelColumnId": "string",
                  "UnpivotedLabelColumnName": "string",
                  "UnpivotedValueColumnId": "string",
                  "UnpivotedValueColumnName": "string"
               }
            }
         }
      },
      "DataSetId": "string",
      "DatasetParameters": [ 
         { 
            "DateTimeDatasetParameter": { 
               "DefaultValues": { 
                  "StaticValues": [ number ]
               },
               "Id": "string",
               "Name": "string",
               "TimeGranularity": "string",
               "ValueType": "string"
            },
            "DecimalDatasetParameter": { 
               "DefaultValues": { 
                  "StaticValues": [ number ]
               },
               "Id": "string",
               "Name": "string",
               "ValueType": "string"
            },
            "IntegerDatasetParameter": { 
               "DefaultValues": { 
                  "StaticValues": [ number ]
               },
               "Id": "string",
               "Name": "string",
               "ValueType": "string"
            },
            "StringDatasetParameter": { 
               "DefaultValues": { 
                  "StaticValues": [ "string" ]
               },
               "Id": "string",
               "Name": "string",
               "ValueType": "string"
            }
         }
      ],
      "DataSetUsageConfiguration": { 
         "DisableUseAsDirectQuerySource": boolean,
         "DisableUseAsImportedSource": boolean
      },
      "FieldFolders": { 
         "string" : { 
            "columns": [ "string" ],
            "description": "string"
         }
      },
      "ImportMode": "string",
      "LastUpdatedTime": number,
      "LogicalTableMap": { 
         "string" : { 
            "Alias": "string",
            "DataTransforms": [ 
               { 
                  "CastColumnTypeOperation": { 
                     "ColumnName": "string",
                     "Format": "string",
                     "NewColumnType": "string",
                     "SubType": "string"
                  },
                  "CreateColumnsOperation": { 
                     "Alias": "string",
                     "Columns": [ 
                        { 
                           "ColumnId": "string",
                           "ColumnName": "string",
                           "Expression": "string"
                        }
                     ],
                     "Source": { 
                        "ColumnIdMappings": [ 
                           { 
                              "SourceColumnId": "string",
                              "TargetColumnId": "string"
                           }
                        ],
                        "TransformOperationId": "string"
                     }
                  },
                  "FilterOperation": { 
                     "ConditionExpression": "string",
                     "DateFilterCondition": { 
                        "ColumnName": "string",
                        "ComparisonFilterCondition": { 
                           "Operator": "string",
                           "Value": { 
                              "StaticValue": number
                           }
                        },
                        "RangeFilterCondition": { 
                           "IncludeMaximum": boolean,
                           "IncludeMinimum": boolean,
                           "RangeMaximum": { 
                              "StaticValue": number
                           },
                           "RangeMinimum": { 
                              "StaticValue": number
                           }
                        }
                     },
                     "NumericFilterCondition": { 
                        "ColumnName": "string",
                        "ComparisonFilterCondition": { 
                           "Operator": "string",
                           "Value": { 
                              "StaticValue": number
                           }
                        },
                        "RangeFilterCondition": { 
                           "IncludeMaximum": boolean,
                           "IncludeMinimum": boolean,
                           "RangeMaximum": { 
                              "StaticValue": number
                           },
                           "RangeMinimum": { 
                              "StaticValue": number
                           }
                        }
                     },
                     "StringFilterCondition": { 
                        "ColumnName": "string",
                        "ComparisonFilterCondition": { 
                           "Operator": "string",
                           "Value": { 
                              "StaticValue": "string"
                           }
                        },
                        "ListFilterCondition": { 
                           "Operator": "string",
                           "Values": { 
                              "StaticValues": [ "string" ]
                           }
                        }
                     }
                  },
                  "OverrideDatasetParameterOperation": { 
                     "NewDefaultValues": { 
                        "DateTimeStaticValues": [ number ],
                        "DecimalStaticValues": [ number ],
                        "IntegerStaticValues": [ number ],
                        "StringStaticValues": [ "string" ]
                     },
                     "NewParameterName": "string",
                     "ParameterName": "string"
                  },
                  "ProjectOperation": { 
                     "Alias": "string",
                     "ProjectedColumns": [ "string" ],
                     "Source": { 
                        "ColumnIdMappings": [ 
                           { 
                              "SourceColumnId": "string",
                              "TargetColumnId": "string"
                           }
                        ],
                        "TransformOperationId": "string"
                     }
                  },
                  "RenameColumnOperation": { 
                     "ColumnName": "string",
                     "NewColumnName": "string"
                  },
                  "TagColumnOperation": { 
                     "ColumnName": "string",
                     "Tags": [ 
                        { 
                           "ColumnDescription": { 
                              "Text": "string"
                           },
                           "ColumnGeographicRole": "string"
                        }
                     ]
                  },
                  "UntagColumnOperation": { 
                     "ColumnName": "string",
                     "TagNames": [ "string" ]
                  }
               }
            ],
            "Source": { 
               "DataSetArn": "string",
               "JoinInstruction": { 
                  "LeftJoinKeyProperties": { 
                     "UniqueKey": boolean
                  },
                  "LeftOperand": "string",
                  "OnClause": "string",
                  "RightJoinKeyProperties": { 
                     "UniqueKey": boolean
                  },
                  "RightOperand": "string",
                  "Type": "string"
               },
               "PhysicalTableId": "string"
            }
         }
      },
      "Name": "string",
      "OutputColumns": [ 
         { 
            "Description": "string",
            "Id": "string",
            "Name": "string",
            "SubType": "string",
            "Type": "string"
         }
      ],
      "PerformanceConfiguration": { 
         "UniqueKeys": [ 
            { 
               "ColumnNames": [ "string" ]
            }
         ]
      },
      "PhysicalTableMap": { 
         "string" : { 
            "CustomSql": { 
               "Columns": [ 
                  { 
                     "Id": "string",
                     "Name": "string",
                     "SubType": "string",
                     "Type": "string"
                  }
               ],
               "DataSourceArn": "string",
               "Name": "string",
               "SqlQuery": "string"
            },
            "RelationalTable": { 
               "Catalog": "string",
               "DataSourceArn": "string",
               "InputColumns": [ 
                  { 
                     "Id": "string",
                     "Name": "string",
                     "SubType": "string",
                     "Type": "string"
                  }
               ],
               "Name": "string",
               "Schema": "string"
            },
            "S3Source": { 
               "DataSourceArn": "string",
               "InputColumns": [ 
                  { 
                     "Id": "string",
                     "Name": "string",
                     "SubType": "string",
                     "Type": "string"
                  }
               ],
               "UploadSettings": { 
                  "ContainsHeader": boolean,
                  "CustomCellAddressRange": "string",
                  "Delimiter": "string",
                  "Format": "string",
                  "StartFromRow": number,
                  "TextQualifier": "string"
               }
            },
            "SaaSTable": { 
               "DataSourceArn": "string",
               "InputColumns": [ 
                  { 
                     "Id": "string",
                     "Name": "string",
                     "SubType": "string",
                     "Type": "string"
                  }
               ],
               "TablePath": [ 
                  { 
                     "Id": "string",
                     "Name": "string"
                  }
               ]
            }
         }
      },
      "RowLevelPermissionDataSet": { 
         "Arn": "string",
         "FormatVersion": "string",
         "Namespace": "string",
         "PermissionPolicy": "string",
         "Status": "string"
      },
      "RowLevelPermissionTagConfiguration": { 
         "Status": "string",
         "TagRuleConfigurations": [ 
            [ "string" ]
         ],
         "TagRules": [ 
            { 
               "ColumnName": "string",
               "MatchAllValue": "string",
               "TagKey": "string",
               "TagMultiValueDelimiter": "string"
            }
         ]
      },
      "SemanticModelConfiguration": { 
         "SemanticMetadata": [ 
            { 
               "CustomInstructions": [ 
                  { 
                     "InlineCustomInstruction": { 
                        "InstructionText": "string",
                        "UploadedDocumentMetadata": { 
                           "Name": "string"
                        }
                     }
                  }
               ],
               "Description": { 
                  "Text": "string"
               }
            }
         ],
         "TableMap": { 
            "string" : { 
               "Alias": "string",
               "DestinationTableId": "string",
               "RowLevelPermissionConfiguration": { 
                  "RowLevelPermissionDataSet": { 
                     "Arn": "string",
                     "FormatVersion": "string",
                     "Namespace": "string",
                     "PermissionPolicy": "string",
                     "Status": "string"
                  },
                  "TagConfiguration": { 
                     "Status": "string",
                     "TagRuleConfigurations": [ 
                        [ "string" ]
                     ],
                     "TagRules": [ 
                        { 
                           "ColumnName": "string",
                           "MatchAllValue": "string",
                           "TagKey": "string",
                           "TagMultiValueDelimiter": "string"
                        }
                     ]
                  }
               },
               "SemanticMetadata": { 
                  "ColumnMetadata": [ 
                     { 
                        "ColumnNames": [ "string" ],
                        "ColumnProperties": [ 
                           { 
                              "AdditionalNotes": { 
                                 "Text": "string"
                              },
                              "Description": { 
                                 "Text": "string"
                              },
                              "SemanticType": { 
                                 "GeographicalRole": "string"
                              }
                           }
                        ]
                     }
                  ]
               }
            }
         }
      },
      "UseAs": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeDataSet_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeDataSet_ResponseSyntax) **   <a name="QS-DescribeDataSet-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSet](#API_DescribeDataSet_ResponseSyntax) **   <a name="QS-DescribeDataSet-response-DataSet"></a>
Information on the dataset.  
Type: [DataSet](API_DataSet.md) object

 ** [RequestId](#API_DescribeDataSet_ResponseSyntax) **   <a name="QS-DescribeDataSet-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeDataSet_Errors"></a>

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
<a name="API_DescribeDataSet_Examples"></a>

### Example
<a name="API_DescribeDataSet_Example_1"></a>

This example illustrates one usage of DescribeDataSet.

#### Sample Request
<a name="API_DescribeDataSet_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/data-sets/{DataSetId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_DescribeDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDataSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDataSet) 