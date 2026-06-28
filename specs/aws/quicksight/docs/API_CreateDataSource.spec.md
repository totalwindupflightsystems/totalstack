---
id: "@specs/aws/quicksight/docs/API_CreateDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDataSource"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDataSource
<a name="API_CreateDataSource"></a>

Creates a data source.

## Request Syntax
<a name="API_CreateDataSource_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/data-sources HTTP/1.1
Content-type: application/json

{
   "Credentials": { 
      "CopySourceArn": "{{string}}",
      "CredentialPair": { 
         "AlternateDataSourceParameters": [ 
            { 
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
            }
         ],
         "Password": "{{string}}",
         "Username": "{{string}}"
      },
      "KeyPairCredentials": { 
         "KeyPairUsername": "{{string}}",
         "PrivateKey": "{{string}}",
         "PrivateKeyPassphrase": "{{string}}"
      },
      "OAuthClientCredentials": { 
         "ClientId": "{{string}}",
         "ClientSecret": "{{string}}",
         "Username": "{{string}}"
      },
      "SecretArn": "{{string}}",
      "WebProxyCredentials": { 
         "WebProxyPassword": "{{string}}",
         "WebProxyUsername": "{{string}}"
      }
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
   "FolderArns": [ "{{string}}" ],
   "Name": "{{string}}",
   "Permissions": [ 
      { 
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "SslProperties": { 
      "DisableSsl": {{boolean}}
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}",
   "VpcConnectionProperties": { 
      "VpcConnectionArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSourceId](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-DataSourceId"></a>
An ID for the data source. This ID is unique per AWS Region for each AWS account.   
Type: String  
Required: Yes

 ** [Name](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-Name"></a>
A display name for the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [Type](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-Type"></a>
The type of the data source. To return a list of all data sources, use `ListDataSources`.  
Use `AMAZON_ELASTICSEARCH` for Amazon OpenSearch Service.  
Type: String  
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`   
Required: Yes

 ** [Credentials](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-Credentials"></a>
The credentials Amazon Quick Sight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.  
Type: [DataSourceCredentials](API_DataSourceCredentials.md) object  
Required: No

 ** [DataSourceParameters](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-DataSourceParameters"></a>
The parameters that Amazon Quick Sight uses to connect to your underlying source.  
Type: [DataSourceParameters](API_DataSourceParameters.md) object  
Required: No

 ** [FolderArns](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-FolderArns"></a>
When you create the data source, Amazon Quick Sight adds the data source to these folders.  
Type: Array of strings  
Array Members: Maximum number of 1 item.  
Required: No

 ** [Permissions](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-Permissions"></a>
A list of resource permissions on the data source.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [SslProperties](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-SslProperties"></a>
Secure Socket Layer (SSL) properties that apply when Amazon Quick Sight connects to your underlying source.  
Type: [SslProperties](API_SslProperties.md) object  
Required: No

 ** [Tags](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [VpcConnectionProperties](#API_CreateDataSource_RequestSyntax) **   <a name="QS-CreateDataSource-request-VpcConnectionProperties"></a>
Use this parameter only when you want Amazon Quick Sight to use a VPC connection when connecting to your underlying source.  
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object  
Required: No

## Response Syntax
<a name="API_CreateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "DataSourceId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateDataSource_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateDataSource_ResponseSyntax) **   <a name="QS-CreateDataSource-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDataSource_ResponseSyntax) **   <a name="QS-CreateDataSource-response-Arn"></a>
The Amazon Resource Name (ARN) of the data source.  
Type: String

 ** [CreationStatus](#API_CreateDataSource_ResponseSyntax) **   <a name="QS-CreateDataSource-response-CreationStatus"></a>
The status of creating the data source.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [DataSourceId](#API_CreateDataSource_ResponseSyntax) **   <a name="QS-CreateDataSource-response-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.  
Type: String

 ** [RequestId](#API_CreateDataSource_ResponseSyntax) **   <a name="QS-CreateDataSource-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateDataSource_Errors"></a>

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

 ** CustomerManagedKeyUnavailableException **   
The customer managed key that is registered to your Amazon Quick Sight account is unavailable.    
 ** RequestId **   
The AWS request ID for this operation.
HTTP Status Code: 400

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
<a name="API_CreateDataSource_Examples"></a>

### Example
<a name="API_CreateDataSource_Example_1"></a>

This example illustrates one usage of CreateDataSource.

#### Sample Request
<a name="API_CreateDataSource_Example_1_Request"></a>

```
POST /accounts/{AwsAccountId}/data-sources HTTP/1.1 Content-type: application/json
```

## See Also
<a name="API_CreateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateDataSource) 