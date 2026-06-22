---
id: "@specs/aws/appsync/docs/API_UpdateDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDataSource"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# UpdateDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_UpdateDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDataSource
<a name="API_UpdateDataSource"></a>

Updates a `DataSource` object.

## Request Syntax
<a name="API_UpdateDataSource_RequestSyntax"></a>

```
POST /v1/apis/{{apiId}}/datasources/{{name}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "dynamodbConfig": { 
      "awsRegion": "{{string}}",
      "deltaSyncConfig": { 
         "baseTableTTL": {{number}},
         "deltaSyncTableName": "{{string}}",
         "deltaSyncTableTTL": {{number}}
      },
      "tableName": "{{string}}",
      "useCallerCredentials": {{boolean}},
      "versioned": {{boolean}}
   },
   "elasticsearchConfig": { 
      "awsRegion": "{{string}}",
      "endpoint": "{{string}}"
   },
   "eventBridgeConfig": { 
      "eventBusArn": "{{string}}"
   },
   "httpConfig": { 
      "authorizationConfig": { 
         "authorizationType": "{{string}}",
         "awsIamConfig": { 
            "signingRegion": "{{string}}",
            "signingServiceName": "{{string}}"
         }
      },
      "endpoint": "{{string}}"
   },
   "lambdaConfig": { 
      "lambdaFunctionArn": "{{string}}"
   },
   "metricsConfig": "{{string}}",
   "openSearchServiceConfig": { 
      "awsRegion": "{{string}}",
      "endpoint": "{{string}}"
   },
   "relationalDatabaseConfig": { 
      "rdsHttpEndpointConfig": { 
         "awsRegion": "{{string}}",
         "awsSecretStoreArn": "{{string}}",
         "databaseName": "{{string}}",
         "dbClusterIdentifier": "{{string}}",
         "schema": "{{string}}"
      },
      "relationalDatabaseSourceType": "{{string}}"
   },
   "serviceRoleArn": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-uri-apiId"></a>
The API ID.  
Required: Yes

 ** [name](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-uri-name"></a>
The new name for the data source.  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: Yes

## Request Body
<a name="API_UpdateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-description"></a>
The new description for the data source.  
Type: String  
Required: No

 ** [dynamodbConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-dynamodbConfig"></a>
The new Amazon DynamoDB configuration.  
Type: [DynamodbDataSourceConfig](API_DynamodbDataSourceConfig.md) object  
Required: No

 ** [elasticsearchConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-elasticsearchConfig"></a>
The new OpenSearch configuration.  
As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch Service. This configuration is deprecated. Instead, use [UpdateDataSource:openSearchServiceConfig](#appsync-UpdateDataSource-request-openSearchServiceConfig) to update an OpenSearch data source.  
Type: [ElasticsearchDataSourceConfig](API_ElasticsearchDataSourceConfig.md) object  
Required: No

 ** [eventBridgeConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-eventBridgeConfig"></a>
The new Amazon EventBridge settings.  
Type: [EventBridgeDataSourceConfig](API_EventBridgeDataSourceConfig.md) object  
Required: No

 ** [httpConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-httpConfig"></a>
The new HTTP endpoint configuration.  
Type: [HttpDataSourceConfig](API_HttpDataSourceConfig.md) object  
Required: No

 ** [lambdaConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-lambdaConfig"></a>
The new AWS Lambda configuration.  
Type: [LambdaDataSourceConfig](API_LambdaDataSourceConfig.md) object  
Required: No

 ** [metricsConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-metricsConfig"></a>
Enables or disables enhanced data source metrics for specified data sources. Note that `metricsConfig` won't be used unless the `dataSourceLevelMetricsBehavior` value is set to `PER_DATA_SOURCE_METRICS`. If the `dataSourceLevelMetricsBehavior` is set to `FULL_REQUEST_DATA_SOURCE_METRICS` instead, `metricsConfig` will be ignored. However, you can still set its value.  
 `metricsConfig` can be `ENABLED` or `DISABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [openSearchServiceConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-openSearchServiceConfig"></a>
The new OpenSearch configuration.  
Type: [OpenSearchServiceDataSourceConfig](API_OpenSearchServiceDataSourceConfig.md) object  
Required: No

 ** [relationalDatabaseConfig](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-relationalDatabaseConfig"></a>
The new relational database configuration.  
Type: [RelationalDatabaseDataSourceConfig](API_RelationalDatabaseDataSourceConfig.md) object  
Required: No

 ** [serviceRoleArn](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-serviceRoleArn"></a>
The new service role Amazon Resource Name (ARN) for the data source.  
Type: String  
Required: No

 ** [type](#API_UpdateDataSource_RequestSyntax) **   <a name="appsync-UpdateDataSource-request-type"></a>
The new data source type.  
Type: String  
Valid Values: `AWS_LAMBDA | AMAZON_DYNAMODB | AMAZON_ELASTICSEARCH | NONE | HTTP | RELATIONAL_DATABASE | AMAZON_OPENSEARCH_SERVICE | AMAZON_EVENTBRIDGE | AMAZON_BEDROCK_RUNTIME`   
Required: Yes

## Response Syntax
<a name="API_UpdateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataSource": { 
      "dataSourceArn": "string",
      "description": "string",
      "dynamodbConfig": { 
         "awsRegion": "string",
         "deltaSyncConfig": { 
            "baseTableTTL": number,
            "deltaSyncTableName": "string",
            "deltaSyncTableTTL": number
         },
         "tableName": "string",
         "useCallerCredentials": boolean,
         "versioned": boolean
      },
      "elasticsearchConfig": { 
         "awsRegion": "string",
         "endpoint": "string"
      },
      "eventBridgeConfig": { 
         "eventBusArn": "string"
      },
      "httpConfig": { 
         "authorizationConfig": { 
            "authorizationType": "string",
            "awsIamConfig": { 
               "signingRegion": "string",
               "signingServiceName": "string"
            }
         },
         "endpoint": "string"
      },
      "lambdaConfig": { 
         "lambdaFunctionArn": "string"
      },
      "metricsConfig": "string",
      "name": "string",
      "openSearchServiceConfig": { 
         "awsRegion": "string",
         "endpoint": "string"
      },
      "relationalDatabaseConfig": { 
         "rdsHttpEndpointConfig": { 
            "awsRegion": "string",
            "awsSecretStoreArn": "string",
            "databaseName": "string",
            "dbClusterIdentifier": "string",
            "schema": "string"
         },
         "relationalDatabaseSourceType": "string"
      },
      "serviceRoleArn": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_UpdateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataSource](#API_UpdateDataSource_ResponseSyntax) **   <a name="appsync-UpdateDataSource-response-dataSource"></a>
The updated `DataSource` object.  
Type: [DataSource](API_DataSource.md) object

## Errors
<a name="API_UpdateDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** ConcurrentModificationException **   
Another modification is in progress at this time and it must complete before you can make your change.  
HTTP Status Code: 409

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_UpdateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/UpdateDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/UpdateDataSource) 