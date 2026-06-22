---
id: "@specs/aws/appsync/docs/API_RdsHttpEndpointConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RdsHttpEndpointConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# RdsHttpEndpointConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_RdsHttpEndpointConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RdsHttpEndpointConfig
<a name="API_RdsHttpEndpointConfig"></a>

The Amazon Relational Database Service (Amazon RDS) HTTP endpoint configuration.

## Contents
<a name="API_RdsHttpEndpointConfig_Contents"></a>

 ** awsRegion **   <a name="appsync-Type-RdsHttpEndpointConfig-awsRegion"></a>
 AWS Region for Amazon RDS HTTP endpoint.  
Type: String  
Required: No

 ** awsSecretStoreArn **   <a name="appsync-Type-RdsHttpEndpointConfig-awsSecretStoreArn"></a>
 AWS secret store Amazon Resource Name (ARN) for database credentials.  
Type: String  
Required: No

 ** databaseName **   <a name="appsync-Type-RdsHttpEndpointConfig-databaseName"></a>
Logical database name.  
Type: String  
Required: No

 ** dbClusterIdentifier **   <a name="appsync-Type-RdsHttpEndpointConfig-dbClusterIdentifier"></a>
Amazon RDS cluster Amazon Resource Name (ARN).  
Type: String  
Required: No

 ** schema **   <a name="appsync-Type-RdsHttpEndpointConfig-schema"></a>
Logical schema name.  
Type: String  
Required: No

## See Also
<a name="API_RdsHttpEndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/RdsHttpEndpointConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/RdsHttpEndpointConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/RdsHttpEndpointConfig) 