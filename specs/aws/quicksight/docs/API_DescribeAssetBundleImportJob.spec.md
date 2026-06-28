---
id: "@specs/aws/quicksight/docs/API_DescribeAssetBundleImportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAssetBundleImportJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAssetBundleImportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAssetBundleImportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAssetBundleImportJob
<a name="API_DescribeAssetBundleImportJob"></a>

Describes an existing import job.

Poll job descriptions after starting a job to know when it has succeeded or failed. Job descriptions are available for 14 days after job starts.

## Request Syntax
<a name="API_DescribeAssetBundleImportJob_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/asset-bundle-import-jobs/{{AssetBundleImportJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAssetBundleImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetBundleImportJobId](#API_DescribeAssetBundleImportJob_RequestSyntax) **   <a name="QS-DescribeAssetBundleImportJob-request-uri-AssetBundleImportJobId"></a>
The ID of the job. The job ID is set when you start a new job with a `StartAssetBundleImportJob` API call.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_DescribeAssetBundleImportJob_RequestSyntax) **   <a name="QS-DescribeAssetBundleImportJob-request-uri-AwsAccountId"></a>
The ID of the AWS account the import job was executed in.   
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAssetBundleImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAssetBundleImportJob_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AssetBundleImportJobId": "string",
   "AssetBundleImportSource": { 
      "Body": "string",
      "S3Uri": "string"
   },
   "AwsAccountId": "string",
   "CreatedTime": number,
   "Errors": [ 
      { 
         "Arn": "string",
         "Message": "string",
         "Type": "string"
      }
   ],
   "FailureAction": "string",
   "JobStatus": "string",
   "OverrideParameters": { 
      "Analyses": [ 
         { 
            "AnalysisId": "string",
            "Name": "string"
         }
      ],
      "Dashboards": [ 
         { 
            "DashboardId": "string",
            "Name": "string"
         }
      ],
      "DataSets": [ 
         { 
            "DataSetId": "string",
            "DataSetRefreshProperties": { 
               "FailureConfiguration": { 
                  "EmailAlert": { 
                     "AlertStatus": "string"
                  }
               },
               "RefreshConfiguration": { 
                  "IncrementalRefresh": { 
                     "LookbackWindow": { 
                        "ColumnName": "string",
                        "Size": number,
                        "SizeUnit": "string"
                     }
                  }
               }
            },
            "Name": "string"
         }
      ],
      "DataSources": [ 
         { 
            "Credentials": { 
               "CredentialPair": { 
                  "Password": "string",
                  "Username": "string"
               },
               "SecretArn": "string"
            },
            "DataSourceId": "string",
            "DataSourceParameters": { 
               "AmazonElasticsearchParameters": { 
                  "Domain": "string"
               },
               "AmazonOpenSearchParameters": { 
                  "Domain": "string"
               },
               "AthenaParameters": { 
                  "ConsumerAccountRoleArn": "string",
                  "IdentityCenterConfiguration": { 
                     "EnableIdentityPropagation": boolean
                  },
                  "RoleArn": "string",
                  "WorkGroup": "string"
               },
               "AuroraParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "AuroraPostgreSqlParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "AwsIotAnalyticsParameters": { 
                  "DataSetName": "string"
               },
               "BigQueryParameters": { 
                  "DataSetRegion": "string",
                  "ProjectId": "string"
               },
               "ConfluenceParameters": { 
                  "ConfluenceUrl": "string"
               },
               "CustomConnectionParameters": { 
                  "ConnectionType": "string"
               },
               "DatabricksParameters": { 
                  "Host": "string",
                  "Port": number,
                  "SqlEndpointPath": "string"
               },
               "ExasolParameters": { 
                  "Host": "string",
                  "Port": number
               },
               "ImpalaParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number,
                  "SqlEndpointPath": "string"
               },
               "JiraParameters": { 
                  "SiteBaseUrl": "string"
               },
               "MariaDbParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "MySqlParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "OracleParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number,
                  "UseServiceName": boolean
               },
               "PostgreSqlParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "PrestoParameters": { 
                  "Catalog": "string",
                  "Host": "string",
                  "Port": number
               },
               "QBusinessParameters": { 
                  "ApplicationArn": "string"
               },
               "RdsParameters": { 
                  "Database": "string",
                  "InstanceId": "string"
               },
               "RedshiftParameters": { 
                  "ClusterId": "string",
                  "Database": "string",
                  "Host": "string",
                  "IAMParameters": { 
                     "AutoCreateDatabaseUser": boolean,
                     "DatabaseGroups": [ "string" ],
                     "DatabaseUser": "string",
                     "RoleArn": "string"
                  },
                  "IdentityCenterConfiguration": { 
                     "EnableIdentityPropagation": boolean
                  },
                  "Port": number
               },
               "S3KnowledgeBaseParameters": { 
                  "BucketUrl": "string",
                  "MetadataFilesLocation": "string",
                  "RoleArn": "string"
               },
               "S3Parameters": { 
                  "ManifestFileLocation": { 
                     "Bucket": "string",
                     "Key": "string"
                  },
                  "RoleArn": "string"
               },
               "S3TablesParameters": { 
                  "TableBucketArn": "string"
               },
               "ServiceNowParameters": { 
                  "SiteBaseUrl": "string"
               },
               "SnowflakeParameters": { 
                  "AuthenticationType": "string",
                  "Database": "string",
                  "DatabaseAccessControlRole": "string",
                  "Host": "string",
                  "OAuthParameters": { 
                     "IdentityProviderCACertificatesBundleS3Uri": "string",
                     "IdentityProviderResourceUri": "string",
                     "IdentityProviderVpcConnectionProperties": { 
                        "VpcConnectionArn": "string"
                     },
                     "OAuthScope": "string",
                     "TokenProviderUrl": "string"
                  },
                  "Warehouse": "string"
               },
               "SparkParameters": { 
                  "Host": "string",
                  "Port": number
               },
               "SqlServerParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "StarburstParameters": { 
                  "AuthenticationType": "string",
                  "Catalog": "string",
                  "DatabaseAccessControlRole": "string",
                  "Host": "string",
                  "OAuthParameters": { 
                     "IdentityProviderCACertificatesBundleS3Uri": "string",
                     "IdentityProviderResourceUri": "string",
                     "IdentityProviderVpcConnectionProperties": { 
                        "VpcConnectionArn": "string"
                     },
                     "OAuthScope": "string",
                     "TokenProviderUrl": "string"
                  },
                  "Port": number,
                  "ProductType": "string"
               },
               "TeradataParameters": { 
                  "Database": "string",
                  "Host": "string",
                  "Port": number
               },
               "TrinoParameters": { 
                  "Catalog": "string",
                  "Host": "string",
                  "Port": number
               },
               "TwitterParameters": { 
                  "MaxRows": number,
                  "Query": "string"
               },
               "WebCrawlerParameters": { 
                  "LoginPageUrl": "string",
                  "PasswordButtonXpath": "string",
                  "PasswordFieldXpath": "string",
                  "UsernameButtonXpath": "string",
                  "UsernameFieldXpath": "string",
                  "WebCrawlerAuthType": "string",
                  "WebProxyHostName": "string",
                  "WebProxyPortNumber": number
               }
            },
            "Name": "string",
            "SslProperties": { 
               "DisableSsl": boolean
            },
            "VpcConnectionProperties": { 
               "VpcConnectionArn": "string"
            }
         }
      ],
      "Folders": [ 
         { 
            "FolderId": "string",
            "Name": "string",
            "ParentFolderArn": "string"
         }
      ],
      "RefreshSchedules": [ 
         { 
            "DataSetId": "string",
            "ScheduleId": "string",
            "StartAfterDateTime": number
         }
      ],
      "ResourceIdOverrideConfiguration": { 
         "PrefixForAllResources": "string"
      },
      "Themes": [ 
         { 
            "Name": "string",
            "ThemeId": "string"
         }
      ],
      "VPCConnections": [ 
         { 
            "DnsResolvers": [ "string" ],
            "Name": "string",
            "RoleArn": "string",
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ],
            "VPCConnectionId": "string"
         }
      ]
   },
   "OverridePermissions": { 
      "Analyses": [ 
         { 
            "AnalysisIds": [ "string" ],
            "Permissions": { 
               "Actions": [ "string" ],
               "Principals": [ "string" ]
            }
         }
      ],
      "Dashboards": [ 
         { 
            "DashboardIds": [ "string" ],
            "LinkSharingConfiguration": { 
               "Permissions": { 
                  "Actions": [ "string" ],
                  "Principals": [ "string" ]
               }
            },
            "Permissions": { 
               "Actions": [ "string" ],
               "Principals": [ "string" ]
            }
         }
      ],
      "DataSets": [ 
         { 
            "DataSetIds": [ "string" ],
            "Permissions": { 
               "Actions": [ "string" ],
               "Principals": [ "string" ]
            }
         }
      ],
      "DataSources": [ 
         { 
            "DataSourceIds": [ "string" ],
            "Permissions": { 
               "Actions": [ "string" ],
               "Principals": [ "string" ]
            }
         }
      ],
      "Folders": [ 
         { 
            "FolderIds": [ "string" ],
            "Permissions": { 
               "Actions": [ "string" ],
               "Principals": [ "string" ]
            }
         }
      ],
      "Themes": [ 
         { 
            "Permissions": { 
               "Actions": [ "string" ],
               "Principals": [ "string" ]
            },
            "ThemeIds": [ "string" ]
         }
      ]
   },
   "OverrideTags": { 
      "Analyses": [ 
         { 
            "AnalysisIds": [ "string" ],
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ]
         }
      ],
      "Dashboards": [ 
         { 
            "DashboardIds": [ "string" ],
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ]
         }
      ],
      "DataSets": [ 
         { 
            "DataSetIds": [ "string" ],
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ]
         }
      ],
      "DataSources": [ 
         { 
            "DataSourceIds": [ "string" ],
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ]
         }
      ],
      "Folders": [ 
         { 
            "FolderIds": [ "string" ],
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ]
         }
      ],
      "Themes": [ 
         { 
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "ThemeIds": [ "string" ]
         }
      ],
      "VPCConnections": [ 
         { 
            "Tags": [ 
               { 
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "VPCConnectionIds": [ "string" ]
         }
      ]
   },
   "OverrideValidationStrategy": { 
      "StrictModeForAllResources": boolean
   },
   "RequestId": "string",
   "RollbackErrors": [ 
      { 
         "Arn": "string",
         "Message": "string",
         "Type": "string"
      }
   ],
   "Warnings": [ 
      { 
         "Arn": "string",
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAssetBundleImportJob_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-Status"></a>
The HTTP status of the response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-Arn"></a>
The Amazon Resource Name (ARN) for the import job.  
Type: String

 ** [AssetBundleImportJobId](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-AssetBundleImportJobId"></a>
The ID of the job. The job ID is set when you start a new job with a `StartAssetBundleImportJob` API call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [AssetBundleImportSource](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-AssetBundleImportSource"></a>
The source of the asset bundle zip file that contains the data that is imported by the job.  
Type: [AssetBundleImportSourceDescription](API_AssetBundleImportSourceDescription.md) object

 ** [AwsAccountId](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-AwsAccountId"></a>
The ID of the AWS account the import job was executed in.   
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [CreatedTime](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-CreatedTime"></a>
The time that the import job was created.  
Type: Timestamp

 ** [Errors](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-Errors"></a>
An array of error records that describes any failures that occurred during the export job processing.  
Error records accumulate while the job is still running. The complete set of error records is available after the job has completed and failed.  
Type: Array of [AssetBundleImportJobError](API_AssetBundleImportJobError.md) objects

 ** [FailureAction](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-FailureAction"></a>
The failure action for the import job.  
Type: String  
Valid Values: `DO_NOTHING | ROLLBACK` 

 ** [JobStatus](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-JobStatus"></a>
Indicates the status of a job through its queuing and execution.  
Poll the `DescribeAssetBundleImport` API until `JobStatus` returns one of the following values:  
+  `SUCCESSFUL` 
+  `FAILED` 
+  `FAILED_ROLLBACK_COMPLETED` 
+  `FAILED_ROLLBACK_ERROR` 
Type: String  
Valid Values: `QUEUED_FOR_IMMEDIATE_EXECUTION | IN_PROGRESS | SUCCESSFUL | FAILED | FAILED_ROLLBACK_IN_PROGRESS | FAILED_ROLLBACK_COMPLETED | FAILED_ROLLBACK_ERROR` 

 ** [OverrideParameters](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-OverrideParameters"></a>
Optional overrides that are applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverrideParameters](API_AssetBundleImportJobOverrideParameters.md) object

 ** [OverridePermissions](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-OverridePermissions"></a>
Optional permission overrides that are applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverridePermissions](API_AssetBundleImportJobOverridePermissions.md) object

 ** [OverrideTags](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-OverrideTags"></a>
Optional tag overrides that are applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverrideTags](API_AssetBundleImportJobOverrideTags.md) object

 ** [OverrideValidationStrategy](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-OverrideValidationStrategy"></a>
An optional validation strategy override for all analyses and dashboards to be applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverrideValidationStrategy](API_AssetBundleImportJobOverrideValidationStrategy.md) object

 ** [RequestId](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

 ** [RollbackErrors](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-RollbackErrors"></a>
An array of error records that describes any failures that occurred while an import job was attempting a rollback.  
Error records accumulate while the job is still running. The complete set of error records is available after the job has completed and failed.  
Type: Array of [AssetBundleImportJobError](API_AssetBundleImportJobError.md) objects

 ** [Warnings](#API_DescribeAssetBundleImportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleImportJob-response-Warnings"></a>
An array of warning records that describe all permitted errors that are encountered during the import job.  
Type: Array of [AssetBundleImportJobWarning](API_AssetBundleImportJobWarning.md) objects

## Errors
<a name="API_DescribeAssetBundleImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_DescribeAssetBundleImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAssetBundleImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAssetBundleImportJob) 