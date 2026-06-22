---
id: "@specs/aws/emr/docs/API_MonitoringConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MonitoringConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# MonitoringConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_MonitoringConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MonitoringConfiguration
<a name="API_MonitoringConfiguration"></a>

Contains CloudWatch log configuration and S3 logging configuration metadata and settings.

## Contents
<a name="API_MonitoringConfiguration_Contents"></a>

 ** CloudWatchLogConfiguration **   <a name="EMR-Type-MonitoringConfiguration-CloudWatchLogConfiguration"></a>
CloudWatch log configuration settings and metadata that specify settings like log files to monitor and where to send them.  
Type: [CloudWatchLogConfiguration](API_CloudWatchLogConfiguration.md) object  
Required: No

 ** S3LoggingConfiguration **   <a name="EMR-Type-MonitoringConfiguration-S3LoggingConfiguration"></a>
S3 logging configuration that controls how different types of logs (system logs, application logs, and persistent UI logs) are uploaded to S3. Each log type can be configured with a specific upload policy.  
Type: [S3LoggingConfiguration](API_S3LoggingConfiguration.md) object  
Required: No

## See Also
<a name="API_MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/MonitoringConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/MonitoringConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/MonitoringConfiguration) 