---
id: "@specs/aws/appsync/docs/API_DataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSource"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSource
<a name="API_DataSource"></a>

Describes a data source.

## Contents
<a name="API_DataSource_Contents"></a>

 ** dataSourceArn **   <a name="appsync-Type-DataSource-dataSourceArn"></a>
The data source Amazon Resource Name (ARN).  
Type: String  
Required: No

 ** description **   <a name="appsync-Type-DataSource-description"></a>
The description of the data source.  
Type: String  
Required: No

 ** dynamodbConfig **   <a name="appsync-Type-DataSource-dynamodbConfig"></a>
DynamoDB settings.  
Type: [DynamodbDataSourceConfig](API_DynamodbDataSourceConfig.md) object  
Required: No

 ** elasticsearchConfig **   <a name="appsync-Type-DataSource-elasticsearchConfig"></a>
Amazon OpenSearch Service settings.  
Type: [ElasticsearchDataSourceConfig](API_ElasticsearchDataSourceConfig.md) object  
Required: No

 ** eventBridgeConfig **   <a name="appsync-Type-DataSource-eventBridgeConfig"></a>
Amazon EventBridge settings.  
Type: [EventBridgeDataSourceConfig](API_EventBridgeDataSourceConfig.md) object  
Required: No

 ** httpConfig **   <a name="appsync-Type-DataSource-httpConfig"></a>
HTTP endpoint settings.  
Type: [HttpDataSourceConfig](API_HttpDataSourceConfig.md) object  
Required: No

 ** lambdaConfig **   <a name="appsync-Type-DataSource-lambdaConfig"></a>
Lambda settings.  
Type: [LambdaDataSourceConfig](API_LambdaDataSourceConfig.md) object  
Required: No

 ** metricsConfig **   <a name="appsync-Type-DataSource-metricsConfig"></a>
Enables or disables enhanced data source metrics for specified data sources. Note that `metricsConfig` won't be used unless the `dataSourceLevelMetricsBehavior` value is set to `PER_DATA_SOURCE_METRICS`. If the `dataSourceLevelMetricsBehavior` is set to `FULL_REQUEST_DATA_SOURCE_METRICS` instead, `metricsConfig` will be ignored. However, you can still set its value.  
 `metricsConfig` can be `ENABLED` or `DISABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** name **   <a name="appsync-Type-DataSource-name"></a>
The name of the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

 ** openSearchServiceConfig **   <a name="appsync-Type-DataSource-openSearchServiceConfig"></a>
Amazon OpenSearch Service settings.  
Type: [OpenSearchServiceDataSourceConfig](API_OpenSearchServiceDataSourceConfig.md) object  
Required: No

 ** relationalDatabaseConfig **   <a name="appsync-Type-DataSource-relationalDatabaseConfig"></a>
Relational database settings.  
Type: [RelationalDatabaseDataSourceConfig](API_RelationalDatabaseDataSourceConfig.md) object  
Required: No

 ** serviceRoleArn **   <a name="appsync-Type-DataSource-serviceRoleArn"></a>
The AWS Identity and Access Management (IAM) service role Amazon Resource Name (ARN) for the data source. The system assumes this role when accessing the data source.  
Type: String  
Required: No

 ** type **   <a name="appsync-Type-DataSource-type"></a>
The type of the data source.  
+  **AWS\_LAMBDA**: The data source is an AWS Lambda function.
+  **AMAZON\_DYNAMODB**: The data source is an Amazon DynamoDB table.
+  **AMAZON\_ELASTICSEARCH**: The data source is an Amazon OpenSearch Service domain.
+  **AMAZON\_OPENSEARCH\_SERVICE**: The data source is an Amazon OpenSearch Service domain.
+  **AMAZON\_EVENTBRIDGE**: The data source is an Amazon EventBridge configuration.
+  **AMAZON\_BEDROCK\_RUNTIME**: The data source is the Amazon Bedrock runtime.
+  **NONE**: There is no data source. Use this type when you want to invoke a GraphQL operation without connecting to a data source, such as when you're performing data transformation with resolvers or invoking a subscription from a mutation.
+  **HTTP**: The data source is an HTTP endpoint.
+  **RELATIONAL\_DATABASE**: The data source is a relational database.
Type: String  
Valid Values: `AWS_LAMBDA | AMAZON_DYNAMODB | AMAZON_ELASTICSEARCH | NONE | HTTP | RELATIONAL_DATABASE | AMAZON_OPENSEARCH_SERVICE | AMAZON_EVENTBRIDGE | AMAZON_BEDROCK_RUNTIME`   
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DataSource) 