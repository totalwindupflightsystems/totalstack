---
id: "@specs/aws/appsync/docs/API_Resolver"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Resolver"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# Resolver

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_Resolver
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Resolver
<a name="API_Resolver"></a>

Describes a resolver.

## Contents
<a name="API_Resolver_Contents"></a>

 ** cachingConfig **   <a name="appsync-Type-Resolver-cachingConfig"></a>
The caching configuration for the resolver.  
Type: [CachingConfig](API_CachingConfig.md) object  
Required: No

 ** code **   <a name="appsync-Type-Resolver-code"></a>
The `resolver` code that contains the request and response functions. When code is used, the `runtime` is required. The `runtime` value must be `APPSYNC_JS`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: No

 ** dataSourceName **   <a name="appsync-Type-Resolver-dataSourceName"></a>
The resolver data source name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

 ** fieldName **   <a name="appsync-Type-Resolver-fieldName"></a>
The resolver field name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

 ** kind **   <a name="appsync-Type-Resolver-kind"></a>
The resolver type.  
+  **UNIT**: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.
+  **PIPELINE**: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of `Function` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.
Type: String  
Valid Values: `UNIT | PIPELINE`   
Required: No

 ** maxBatchSize **   <a name="appsync-Type-Resolver-maxBatchSize"></a>
The maximum batching size for a resolver.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2000.  
Required: No

 ** metricsConfig **   <a name="appsync-Type-Resolver-metricsConfig"></a>
Enables or disables enhanced resolver metrics for specified resolvers. Note that `metricsConfig` won't be used unless the `resolverLevelMetricsBehavior` value is set to `PER_RESOLVER_METRICS`. If the `resolverLevelMetricsBehavior` is set to `FULL_REQUEST_RESOLVER_METRICS` instead, `metricsConfig` will be ignored. However, you can still set its value.  
 `metricsConfig` can be `ENABLED` or `DISABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** pipelineConfig **   <a name="appsync-Type-Resolver-pipelineConfig"></a>
The `PipelineConfig`.  
Type: [PipelineConfig](API_PipelineConfig.md) object  
Required: No

 ** requestMappingTemplate **   <a name="appsync-Type-Resolver-requestMappingTemplate"></a>
The request mapping template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `^.*$`   
Required: No

 ** resolverArn **   <a name="appsync-Type-Resolver-resolverArn"></a>
The resolver Amazon Resource Name (ARN).  
Type: String  
Required: No

 ** responseMappingTemplate **   <a name="appsync-Type-Resolver-responseMappingTemplate"></a>
The response mapping template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `^.*$`   
Required: No

 ** runtime **   <a name="appsync-Type-Resolver-runtime"></a>
Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.  
Type: [AppSyncRuntime](API_AppSyncRuntime.md) object  
Required: No

 ** syncConfig **   <a name="appsync-Type-Resolver-syncConfig"></a>
The `SyncConfig` for a resolver attached to a versioned data source.  
Type: [SyncConfig](API_SyncConfig.md) object  
Required: No

 ** typeName **   <a name="appsync-Type-Resolver-typeName"></a>
The resolver type name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

## See Also
<a name="API_Resolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/Resolver) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/Resolver) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/Resolver) 