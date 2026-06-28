---
id: "@specs/aws/amp/docs/API_QueryLoggingConfigurationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QueryLoggingConfigurationMetadata"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# QueryLoggingConfigurationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_QueryLoggingConfigurationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QueryLoggingConfigurationMetadata
<a name="API_QueryLoggingConfigurationMetadata"></a>

The metadata for a query logging configuration.

## Contents
<a name="API_QueryLoggingConfigurationMetadata_Contents"></a>

 ** createdAt **   <a name="prometheus-Type-QueryLoggingConfigurationMetadata-createdAt"></a>
The date and time when the query logging configuration was created.  
Type: Timestamp  
Required: Yes

 ** destinations **   <a name="prometheus-Type-QueryLoggingConfigurationMetadata-destinations"></a>
The configured destinations for the query logging configuration.  
Type: Array of [LoggingDestination](API_LoggingDestination.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** modifiedAt **   <a name="prometheus-Type-QueryLoggingConfigurationMetadata-modifiedAt"></a>
The date and time when the query logging configuration was last modified.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="prometheus-Type-QueryLoggingConfigurationMetadata-status"></a>
The current status of the query logging configuration.  
Type: [QueryLoggingConfigurationStatus](API_QueryLoggingConfigurationStatus.md) object  
Required: Yes

 ** workspace **   <a name="prometheus-Type-QueryLoggingConfigurationMetadata-workspace"></a>
The ID of the workspace associated with this query logging configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## See Also
<a name="API_QueryLoggingConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/QueryLoggingConfigurationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/QueryLoggingConfigurationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/QueryLoggingConfigurationMetadata) 