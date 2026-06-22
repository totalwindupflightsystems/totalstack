---
id: "@specs/aws/appsync/docs/API_RdsDataApiConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RdsDataApiConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# RdsDataApiConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_RdsDataApiConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RdsDataApiConfig
<a name="API_RdsDataApiConfig"></a>

Contains the metadata required to introspect the RDS cluster.

## Contents
<a name="API_RdsDataApiConfig_Contents"></a>

 ** databaseName **   <a name="appsync-Type-RdsDataApiConfig-databaseName"></a>
The name of the database in the cluster.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** resourceArn **   <a name="appsync-Type-RdsDataApiConfig-resourceArn"></a>
The resource ARN of the RDS cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:[a-z-]*:rds:[a-z0-9-]*:\d{12}:cluster:[0-9A-Za-z_/-]*$`   
Required: Yes

 ** secretArn **   <a name="appsync-Type-RdsDataApiConfig-secretArn"></a>
The secret's ARN that was obtained from Secrets Manager. A secret consists of secret information, the secret value, plus metadata about the secret. A secret value can be a string or binary. It typically includes the ARN, secret name and description, policies, tags, encryption key from the Key Management Service, and key rotation data.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:[a-z-]*:secretsmanager:[a-z0-9-]*:\d{12}:secret:[0-9A-Za-z_/+=.@!-]*$`   
Required: Yes

## See Also
<a name="API_RdsDataApiConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/RdsDataApiConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/RdsDataApiConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/RdsDataApiConfig) 