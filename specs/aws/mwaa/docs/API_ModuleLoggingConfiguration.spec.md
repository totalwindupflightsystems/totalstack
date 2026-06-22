---
id: "@specs/aws/mwaa/docs/API_ModuleLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModuleLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# ModuleLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_ModuleLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModuleLoggingConfiguration
<a name="API_ModuleLoggingConfiguration"></a>

Describes the Apache Airflow log details for the log type (e.g. `DagProcessingLogs`).

## Contents
<a name="API_ModuleLoggingConfiguration_Contents"></a>

 ** CloudWatchLogGroupArn **   <a name="mwaa-Type-ModuleLoggingConfiguration-CloudWatchLogGroupArn"></a>
The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. `DagProcessingLogs`) is published. For example, `arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:logs:[a-z0-9\-]+:\d{12}:log-group:\w+.*`   
Required: No

 ** Enabled **   <a name="mwaa-Type-ModuleLoggingConfiguration-Enabled"></a>
Indicates whether the Apache Airflow log type (e.g. `DagProcessingLogs`) is enabled.  
Type: Boolean  
Required: No

 ** LogLevel **   <a name="mwaa-Type-ModuleLoggingConfiguration-LogLevel"></a>
The Apache Airflow log level for the log type (e.g. `DagProcessingLogs`).   
Type: String  
Valid Values: `CRITICAL | ERROR | WARNING | INFO | DEBUG`   
Required: No

## See Also
<a name="API_ModuleLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/ModuleLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/ModuleLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/ModuleLoggingConfiguration) 