---
id: "@specs/aws/appsync/docs/API_DynamodbDataSourceConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DynamodbDataSourceConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DynamodbDataSourceConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DynamodbDataSourceConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DynamodbDataSourceConfig
<a name="API_DynamodbDataSourceConfig"></a>

Describes an Amazon DynamoDB data source configuration.

## Contents
<a name="API_DynamodbDataSourceConfig_Contents"></a>

 ** awsRegion **   <a name="appsync-Type-DynamodbDataSourceConfig-awsRegion"></a>
The AWS Region.  
Type: String  
Required: Yes

 ** tableName **   <a name="appsync-Type-DynamodbDataSourceConfig-tableName"></a>
The table name.  
Type: String  
Required: Yes

 ** deltaSyncConfig **   <a name="appsync-Type-DynamodbDataSourceConfig-deltaSyncConfig"></a>
The `DeltaSyncConfig` for a versioned data source.  
Type: [DeltaSyncConfig](API_DeltaSyncConfig.md) object  
Required: No

 ** useCallerCredentials **   <a name="appsync-Type-DynamodbDataSourceConfig-useCallerCredentials"></a>
Set to TRUE to use Amazon Cognito credentials with this data source.  
Type: Boolean  
Required: No

 ** versioned **   <a name="appsync-Type-DynamodbDataSourceConfig-versioned"></a>
Set to TRUE to use Conflict Detection and Resolution with this data source.  
Type: Boolean  
Required: No

## See Also
<a name="API_DynamodbDataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DynamodbDataSourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DynamodbDataSourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DynamodbDataSourceConfig) 