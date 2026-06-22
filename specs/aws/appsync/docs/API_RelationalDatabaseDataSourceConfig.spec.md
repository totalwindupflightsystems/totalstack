---
id: "@specs/aws/appsync/docs/API_RelationalDatabaseDataSourceConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RelationalDatabaseDataSourceConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# RelationalDatabaseDataSourceConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_RelationalDatabaseDataSourceConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RelationalDatabaseDataSourceConfig
<a name="API_RelationalDatabaseDataSourceConfig"></a>

Describes a relational database data source configuration.

## Contents
<a name="API_RelationalDatabaseDataSourceConfig_Contents"></a>

 ** rdsHttpEndpointConfig **   <a name="appsync-Type-RelationalDatabaseDataSourceConfig-rdsHttpEndpointConfig"></a>
Amazon RDS HTTP endpoint settings.  
Type: [RdsHttpEndpointConfig](API_RdsHttpEndpointConfig.md) object  
Required: No

 ** relationalDatabaseSourceType **   <a name="appsync-Type-RelationalDatabaseDataSourceConfig-relationalDatabaseSourceType"></a>
Source type for the relational database.  
+  **RDS\_HTTP\_ENDPOINT**: The relational database source type is an Amazon Relational Database Service (Amazon RDS) HTTP endpoint.
Type: String  
Valid Values: `RDS_HTTP_ENDPOINT`   
Required: No

## See Also
<a name="API_RelationalDatabaseDataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/RelationalDatabaseDataSourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/RelationalDatabaseDataSourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/RelationalDatabaseDataSourceConfig) 