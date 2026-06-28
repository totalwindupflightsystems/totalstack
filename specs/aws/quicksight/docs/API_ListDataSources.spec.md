---
id: "@specs/aws/quicksight/docs/API_ListDataSources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDataSources"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListDataSources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListDataSources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDataSources
<a name="API_ListDataSources"></a>

Lists data sources in current AWS Region that belong to this AWS account.

## Request Syntax
<a name="API_ListDataSources_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-sources?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListDataSources_RequestSyntax) **   <a name="QS-ListDataSources-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListDataSources_RequestSyntax) **   <a name="QS-ListDataSources-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListDataSources_RequestSyntax) **   <a name="QS-ListDataSources-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListDataSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSources_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSources": [ 
      { 
         "AlternateDataSourceParameters": [ 
            { 
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
            }
         ],
         "Arn": "string",
         "CreatedTime": number,
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
         "ErrorInfo": { 
            "Message": "string",
            "Type": "string"
         },
         "LastUpdatedTime": number,
         "Name": "string",
         "SecretArn": "string",
         "SslProperties": { 
            "DisableSsl": boolean
         },
         "Status": "string",
         "Type": "string",
         "VpcConnectionProperties": { 
            "VpcConnectionArn": "string"
         }
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListDataSources_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListDataSources_ResponseSyntax) **   <a name="QS-ListDataSources-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSources](#API_ListDataSources_ResponseSyntax) **   <a name="QS-ListDataSources-response-DataSources"></a>
A list of data sources.  
Type: Array of [DataSource](API_DataSource.md) objects

 ** [NextToken](#API_ListDataSources_ResponseSyntax) **   <a name="QS-ListDataSources-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListDataSources_ResponseSyntax) **   <a name="QS-ListDataSources-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListDataSources_Errors"></a>

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

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_ListDataSources_Examples"></a>

### Example
<a name="API_ListDataSources_Example_1"></a>

This example illustrates one usage of ListDataSources.

#### Sample Request
<a name="API_ListDataSources_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/data-sources?next-token={NextToken};max-results={MaxResults} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_ListDataSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListDataSources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListDataSources) 