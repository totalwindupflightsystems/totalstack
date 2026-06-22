---
id: "@specs/aws/emr/docs/API_StepMonitoringConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepMonitoringConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepMonitoringConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepMonitoringConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepMonitoringConfiguration
<a name="API_StepMonitoringConfiguration"></a>

Object that holds configuration properties for logging.

## Contents
<a name="API_StepMonitoringConfiguration_Contents"></a>

 ** S3MonitoringConfiguration **   <a name="EMR-Type-StepMonitoringConfiguration-S3MonitoringConfiguration"></a>
The Amazon S3 configuration for monitoring log publishing. You can configure your step to send log information to Amazon S3. When it's specified, it takes precedence over the cluster's logging configuration. If you don't specify this configuration entirely, or omit individual fields, EMR falls back to cluster-level logging behavior.   
Type: [S3MonitoringConfiguration](API_S3MonitoringConfiguration.md) object  
Required: No

## See Also
<a name="API_StepMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepMonitoringConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepMonitoringConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepMonitoringConfiguration) 