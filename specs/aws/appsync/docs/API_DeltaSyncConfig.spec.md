---
id: "@specs/aws/appsync/docs/API_DeltaSyncConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeltaSyncConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DeltaSyncConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DeltaSyncConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeltaSyncConfig
<a name="API_DeltaSyncConfig"></a>

Describes a Delta Sync configuration.

## Contents
<a name="API_DeltaSyncConfig_Contents"></a>

 ** baseTableTTL **   <a name="appsync-Type-DeltaSyncConfig-baseTableTTL"></a>
The number of minutes that an Item is stored in the data source.  
Type: Long  
Required: No

 ** deltaSyncTableName **   <a name="appsync-Type-DeltaSyncConfig-deltaSyncTableName"></a>
The Delta Sync table name.  
Type: String  
Required: No

 ** deltaSyncTableTTL **   <a name="appsync-Type-DeltaSyncConfig-deltaSyncTableTTL"></a>
The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.  
Type: Long  
Required: No

## See Also
<a name="API_DeltaSyncConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DeltaSyncConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DeltaSyncConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DeltaSyncConfig) 