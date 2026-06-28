---
id: "@specs/aws/quicksight/docs/API_StartAssetBundleImportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartAssetBundleImportJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# StartAssetBundleImportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_StartAssetBundleImportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartAssetBundleImportJob
<a name="API_StartAssetBundleImportJob"></a>

Starts an Asset Bundle import job.

An Asset Bundle import job imports specified Amazon Quick Sight assets into an Amazon Quick Sight account. You can also choose to import a naming prefix and specified configuration overrides. The assets that are contained in the bundle file that you provide are used to create or update a new or existing asset in your Amazon Quick Sight account. Each Amazon Quick Sight account can run up to 5 import jobs concurrently.

The API caller must have the necessary `"create"`, `"describe"`, and `"update"` permissions in their IAM role to access each resource type that is contained in the bundle file before the resources can be imported.

## Request Syntax
<a name="API_StartAssetBundleImportJob_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/asset-bundle-import-jobs/import HTTP/1.1
Content-type: application/json

{
   "AssetBundleImportJobId": "{{string}}",
   "AssetBundleImportSource": { 
      "Body": {{blob}},
      "S3Uri": "{{string}}"
   },
   "FailureAction": "{{string}}",
   "OverrideParameters": { 
      "Analyses": [ 
         { 
            "AnalysisId": "{{string}}",
            "Name": "{{string}}"
         }
      ],
      "Dashboards": [ 
         { 
            "DashboardId": "{{string}}",
            "Name": "{{string}}"
         }
      ],
      "DataSets": [ 
         { 
            "DataSetId": "{{string}}",
            "DataSetRefreshProperties": { 
               "FailureConfiguration": { 
                  "EmailAlert": { 
                     "AlertStatus": "{{string}}"
                  }
               },
               "RefreshConfiguration": { 
                  "IncrementalRefresh": { 
                     "LookbackWindow": { 
                        "ColumnName": "{{string}}",
                        "Size": {{number}},
                        "SizeUnit": "{{string}}"
                     }
                  }
               }
            },
            "Name": "{{string}}"
         }
      ],
      "DataSources": [ 
         { 
            "Credentials": { 
               "CredentialPair": { 
                  "Password": "{{string}}",
                  "Username": "{{string}}"
               },
               "SecretArn": "{{string}}"
            },
            "DataSourceId": "{{string}}",
            "DataSourceParameters": { 
               "AmazonElasticsearchParameters": { 
                  "Domain": "{{string}}"
               },
               "AmazonOpenSearchParameters": { 
                  "Domain": "{{string}}"
               },
               "AthenaParameters": { 
                  "ConsumerAccountRoleArn": "{{string}}",
                  "IdentityCenterConfiguration": { 
                     "EnableIdentityPropagation": {{boolean}}
                  },
                  "RoleArn": "{{string}}",
                  "WorkGroup": "{{string}}"
               },
               "AuroraParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "AuroraPostgreSqlParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "AwsIotAnalyticsParameters": { 
                  "DataSetName": "{{string}}"
               },
               "BigQueryParameters": { 
                  "DataSetRegion": "{{string}}",
                  "ProjectId": "{{string}}"
               },
               "ConfluenceParameters": { 
                  "ConfluenceUrl": "{{string}}"
               },
               "CustomConnectionParameters": { 
                  "ConnectionType": "{{string}}"
               },
               "DatabricksParameters": { 
                  "Host": "{{string}}",
                  "Port": {{number}},
                  "SqlEndpointPath": "{{string}}"
               },
               "ExasolParameters": { 
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "ImpalaParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}},
                  "SqlEndpointPath": "{{string}}"
               },
               "JiraParameters": { 
                  "SiteBaseUrl": "{{string}}"
               },
               "MariaDbParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "MySqlParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "OracleParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}},
                  "UseServiceName": {{boolean}}
               },
               "PostgreSqlParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "PrestoParameters": { 
                  "Catalog": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "QBusinessParameters": { 
                  "ApplicationArn": "{{string}}"
               },
               "RdsParameters": { 
                  "Database": "{{string}}",
                  "InstanceId": "{{string}}"
               },
               "RedshiftParameters": { 
                  "ClusterId": "{{string}}",
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "IAMParameters": { 
                     "AutoCreateDatabaseUser": {{boolean}},
                     "DatabaseGroups": [ "{{string}}" ],
                     "DatabaseUser": "{{string}}",
                     "RoleArn": "{{string}}"
                  },
                  "IdentityCenterConfiguration": { 
                     "EnableIdentityPropagation": {{boolean}}
                  },
                  "Port": {{number}}
               },
               "S3KnowledgeBaseParameters": { 
                  "BucketUrl": "{{string}}",
                  "MetadataFilesLocation": "{{string}}",
                  "RoleArn": "{{string}}"
               },
               "S3Parameters": { 
                  "ManifestFileLocation": { 
                     "Bucket": "{{string}}",
                     "Key": "{{string}}"
                  },
                  "RoleArn": "{{string}}"
               },
               "S3TablesParameters": { 
                  "TableBucketArn": "{{string}}"
               },
               "ServiceNowParameters": { 
                  "SiteBaseUrl": "{{string}}"
               },
               "SnowflakeParameters": { 
                  "AuthenticationType": "{{string}}",
                  "Database": "{{string}}",
                  "DatabaseAccessControlRole": "{{string}}",
                  "Host": "{{string}}",
                  "OAuthParameters": { 
                     "IdentityProviderCACertificatesBundleS3Uri": "{{string}}",
                     "IdentityProviderResourceUri": "{{string}}",
                     "IdentityProviderVpcConnectionProperties": { 
                        "VpcConnectionArn": "{{string}}"
                     },
                     "OAuthScope": "{{string}}",
                     "TokenProviderUrl": "{{string}}"
                  },
                  "Warehouse": "{{string}}"
               },
               "SparkParameters": { 
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "SqlServerParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "StarburstParameters": { 
                  "AuthenticationType": "{{string}}",
                  "Catalog": "{{string}}",
                  "DatabaseAccessControlRole": "{{string}}",
                  "Host": "{{string}}",
                  "OAuthParameters": { 
                     "IdentityProviderCACertificatesBundleS3Uri": "{{string}}",
                     "IdentityProviderResourceUri": "{{string}}",
                     "IdentityProviderVpcConnectionProperties": { 
                        "VpcConnectionArn": "{{string}}"
                     },
                     "OAuthScope": "{{string}}",
                     "TokenProviderUrl": "{{string}}"
                  },
                  "Port": {{number}},
                  "ProductType": "{{string}}"
               },
               "TeradataParameters": { 
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "TrinoParameters": { 
                  "Catalog": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "TwitterParameters": { 
                  "MaxRows": {{number}},
                  "Query": "{{string}}"
               },
               "WebCrawlerParameters": { 
                  "LoginPageUrl": "{{string}}",
                  "PasswordButtonXpath": "{{string}}",
                  "PasswordFieldXpath": "{{string}}",
                  "UsernameButtonXpath": "{{string}}",
                  "UsernameFieldXpath": "{{string}}",
                  "WebCrawlerAuthType": "{{string}}",
                  "WebProxyHostName": "{{string}}",
                  "WebProxyPortNumber": {{number}}
               }
            },
            "Name": "{{string}}",
            "SslProperties": { 
               "DisableSsl": {{boolean}}
            },
            "VpcConnectionProperties": { 
               "VpcConnectionArn": "{{string}}"
            }
         }
      ],
      "Folders": [ 
         { 
            "FolderId": "{{string}}",
            "Name": "{{string}}",
            "ParentFolderArn": "{{string}}"
         }
      ],
      "RefreshSchedules": [ 
         { 
            "DataSetId": "{{string}}",
            "ScheduleId": "{{string}}",
            "StartAfterDateTime": {{number}}
         }
      ],
      "ResourceIdOverrideConfiguration": { 
         "PrefixForAllResources": "{{string}}"
      },
      "Themes": [ 
         { 
            "Name": "{{string}}",
            "ThemeId": "{{string}}"
         }
      ],
      "VPCConnections": [ 
         { 
            "DnsResolvers": [ "{{string}}" ],
            "Name": "{{string}}",
            "RoleArn": "{{string}}",
            "SecurityGroupIds": [ "{{string}}" ],
            "SubnetIds": [ "{{string}}" ],
            "VPCConnectionId": "{{string}}"
         }
      ]
   },
   "OverridePermissions": { 
      "Analyses": [ 
         { 
            "AnalysisIds": [ "{{string}}" ],
            "Permissions": { 
               "Actions": [ "{{string}}" ],
               "Principals": [ "{{string}}" ]
            }
         }
      ],
      "Dashboards": [ 
         { 
            "DashboardIds": [ "{{string}}" ],
            "LinkSharingConfiguration": { 
               "Permissions": { 
                  "Actions": [ "{{string}}" ],
                  "Principals": [ "{{string}}" ]
               }
            },
            "Permissions": { 
               "Actions": [ "{{string}}" ],
               "Principals": [ "{{string}}" ]
            }
         }
      ],
      "DataSets": [ 
         { 
            "DataSetIds": [ "{{string}}" ],
            "Permissions": { 
               "Actions": [ "{{string}}" ],
               "Principals": [ "{{string}}" ]
            }
         }
      ],
      "DataSources": [ 
         { 
            "DataSourceIds": [ "{{string}}" ],
            "Permissions": { 
               "Actions": [ "{{string}}" ],
               "Principals": [ "{{string}}" ]
            }
         }
      ],
      "Folders": [ 
         { 
            "FolderIds": [ "{{string}}" ],
            "Permissions": { 
               "Actions": [ "{{string}}" ],
               "Principals": [ "{{string}}" ]
            }
         }
      ],
      "Themes": [ 
         { 
            "Permissions": { 
               "Actions": [ "{{string}}" ],
               "Principals": [ "{{string}}" ]
            },
            "ThemeIds": [ "{{string}}" ]
         }
      ]
   },
   "OverrideTags": { 
      "Analyses": [ 
         { 
            "AnalysisIds": [ "{{string}}" ],
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "Dashboards": [ 
         { 
            "DashboardIds": [ "{{string}}" ],
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "DataSets": [ 
         { 
            "DataSetIds": [ "{{string}}" ],
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "DataSources": [ 
         { 
            "DataSourceIds": [ "{{string}}" ],
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "Folders": [ 
         { 
            "FolderIds": [ "{{string}}" ],
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "Themes": [ 
         { 
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "ThemeIds": [ "{{string}}" ]
         }
      ],
      "VPCConnections": [ 
         { 
            "Tags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "VPCConnectionIds": [ "{{string}}" ]
         }
      ]
   },
   "OverrideValidationStrategy": { 
      "StrictModeForAllResources": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_StartAssetBundleImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-uri-AwsAccountId"></a>
The ID of the AWS account to import assets into.   
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_StartAssetBundleImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssetBundleImportJobId](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-AssetBundleImportJobId"></a>
The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AssetBundleImportSource](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-AssetBundleImportSource"></a>
The source of the asset bundle zip file that contains the data that you want to import. The file must be in `QUICKSIGHT_JSON` format.   
Type: [AssetBundleImportSource](API_AssetBundleImportSource.md) object  
Required: Yes

 ** [FailureAction](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-FailureAction"></a>
The failure action for the import job.  
If you choose `ROLLBACK`, failed import jobs will attempt to undo any asset changes caused by the failed job.  
If you choose `DO_NOTHING`, failed import jobs will not attempt to roll back any asset changes caused by the failed job, possibly keeping the Amazon Quick Sight account in an inconsistent state.  
Type: String  
Valid Values: `DO_NOTHING | ROLLBACK`   
Required: No

 ** [OverrideParameters](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-OverrideParameters"></a>
Optional overrides that are applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverrideParameters](API_AssetBundleImportJobOverrideParameters.md) object  
Required: No

 ** [OverridePermissions](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-OverridePermissions"></a>
Optional permission overrides that are applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverridePermissions](API_AssetBundleImportJobOverridePermissions.md) object  
Required: No

 ** [OverrideTags](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-OverrideTags"></a>
Optional tag overrides that are applied to the resource configuration before import.  
Type: [AssetBundleImportJobOverrideTags](API_AssetBundleImportJobOverrideTags.md) object  
Required: No

 ** [OverrideValidationStrategy](#API_StartAssetBundleImportJob_RequestSyntax) **   <a name="QS-StartAssetBundleImportJob-request-OverrideValidationStrategy"></a>
An optional validation strategy override for all analyses and dashboards that is applied to the resource configuration before import.   
Type: [AssetBundleImportJobOverrideValidationStrategy](API_AssetBundleImportJobOverrideValidationStrategy.md) object  
Required: No

## Response Syntax
<a name="API_StartAssetBundleImportJob_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AssetBundleImportJobId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_StartAssetBundleImportJob_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_StartAssetBundleImportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleImportJob-response-Status"></a>
The HTTP status of the response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_StartAssetBundleImportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleImportJob-response-Arn"></a>
The Amazon Resource Name (ARN) for the import job.  
Type: String

 ** [AssetBundleImportJobId](#API_StartAssetBundleImportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleImportJob-response-AssetBundleImportJobId"></a>
The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [RequestId](#API_StartAssetBundleImportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleImportJob-response-RequestId"></a>
The AWS response ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

## Errors
<a name="API_StartAssetBundleImportJob_Errors"></a>

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
<a name="API_StartAssetBundleImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/StartAssetBundleImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StartAssetBundleImportJob) 