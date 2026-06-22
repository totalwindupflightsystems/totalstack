---
id: "@specs/aws/appsync/docs/API_EnhancedMetricsConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnhancedMetricsConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# EnhancedMetricsConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_EnhancedMetricsConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnhancedMetricsConfig
<a name="API_EnhancedMetricsConfig"></a>

Enables and controls the enhanced metrics feature. Enhanced metrics emit granular data on API usage and performance such as AppSync request and error counts, latency, and cache hits/misses. All enhanced metric data is sent to your CloudWatch account, and you can configure the types of data that will be sent. 

Enhanced metrics can be configured at the resolver, data source, and operation levels. `EnhancedMetricsConfig` contains three required parameters, each controlling one of these categories:

1.  `resolverLevelMetricsBehavior`: Controls how resolver metrics will be emitted to CloudWatch. Resolver metrics include:
   + GraphQL errors: The number of GraphQL errors that occurred.
   + Requests: The number of invocations that occurred during a request. 
   + Latency: The time to complete a resolver invocation.
   + Cache hits: The number of cache hits during a request.
   + Cache misses: The number of cache misses during a request.

   These metrics can be emitted to CloudWatch per resolver or for all resolvers in the request. Metrics will be recorded by API ID and resolver name. `resolverLevelMetricsBehavior` accepts one of these values at a time:
   +  `FULL_REQUEST_RESOLVER_METRICS`: Records and emits metric data for all resolvers in the request.
   +  `PER_RESOLVER_METRICS`: Records and emits metric data for resolvers that have the `metricsConfig` value set to `ENABLED`.

1.  `dataSourceLevelMetricsBehavior`: Controls how data source metrics will be emitted to CloudWatch. Data source metrics include:
   + Requests: The number of invocations that occured during a request.
   + Latency: The time to complete a data source invocation.
   + Errors: The number of errors that occurred during a data source invocation.

   These metrics can be emitted to CloudWatch per data source or for all data sources in the request. Metrics will be recorded by API ID and data source name. `dataSourceLevelMetricsBehavior` accepts one of these values at a time:
   +  `FULL_REQUEST_DATA_SOURCE_METRICS`: Records and emits metric data for all data sources in the request.
   +  `PER_DATA_SOURCE_METRICS`: Records and emits metric data for data sources that have the `metricsConfig` value set to `ENABLED`.

1.  `operationLevelMetricsConfig`: Controls how operation metrics will be emitted to CloudWatch. Operation metrics include:
   + Requests: The number of times a specified GraphQL operation was called.
   + GraphQL errors: The number of GraphQL errors that occurred during a specified GraphQL operation.

   Metrics will be recorded by API ID and operation name. You can set the value to `ENABLED` or `DISABLED`.

## Contents
<a name="API_EnhancedMetricsConfig_Contents"></a>

 ** dataSourceLevelMetricsBehavior **   <a name="appsync-Type-EnhancedMetricsConfig-dataSourceLevelMetricsBehavior"></a>
Controls how data source metrics will be emitted to CloudWatch. Data source metrics include:  
+ Requests: The number of invocations that occured during a request.
+ Latency: The time to complete a data source invocation.
+ Errors: The number of errors that occurred during a data source invocation.
These metrics can be emitted to CloudWatch per data source or for all data sources in the request. Metrics will be recorded by API ID and data source name. `dataSourceLevelMetricsBehavior` accepts one of these values at a time:  
+  `FULL_REQUEST_DATA_SOURCE_METRICS`: Records and emits metric data for all data sources in the request.
+  `PER_DATA_SOURCE_METRICS`: Records and emits metric data for data sources that have the `metricsConfig` value set to `ENABLED`.
Type: String  
Valid Values: `FULL_REQUEST_DATA_SOURCE_METRICS | PER_DATA_SOURCE_METRICS`   
Required: Yes

 ** operationLevelMetricsConfig **   <a name="appsync-Type-EnhancedMetricsConfig-operationLevelMetricsConfig"></a>
 Controls how operation metrics will be emitted to CloudWatch. Operation metrics include:  
+ Requests: The number of times a specified GraphQL operation was called.
+ GraphQL errors: The number of GraphQL errors that occurred during a specified GraphQL operation.
Metrics will be recorded by API ID and operation name. You can set the value to `ENABLED` or `DISABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** resolverLevelMetricsBehavior **   <a name="appsync-Type-EnhancedMetricsConfig-resolverLevelMetricsBehavior"></a>
Controls how resolver metrics will be emitted to CloudWatch. Resolver metrics include:  
+ GraphQL errors: The number of GraphQL errors that occurred.
+ Requests: The number of invocations that occurred during a request. 
+ Latency: The time to complete a resolver invocation.
+ Cache hits: The number of cache hits during a request.
+ Cache misses: The number of cache misses during a request.
These metrics can be emitted to CloudWatch per resolver or for all resolvers in the request. Metrics will be recorded by API ID and resolver name. `resolverLevelMetricsBehavior` accepts one of these values at a time:  
+  `FULL_REQUEST_RESOLVER_METRICS`: Records and emits metric data for all resolvers in the request.
+  `PER_RESOLVER_METRICS`: Records and emits metric data for resolvers that have the `metricsConfig` value set to `ENABLED`.
Type: String  
Valid Values: `FULL_REQUEST_RESOLVER_METRICS | PER_RESOLVER_METRICS`   
Required: Yes

## See Also
<a name="API_EnhancedMetricsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/EnhancedMetricsConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/EnhancedMetricsConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/EnhancedMetricsConfig) 