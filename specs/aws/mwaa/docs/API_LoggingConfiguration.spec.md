---
id: "@specs/aws/mwaa/docs/API_LoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# LoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_LoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LoggingConfiguration
<a name="API_LoggingConfiguration"></a>

Describes the Apache Airflow log types that are published to CloudWatch Logs.

## Contents
<a name="API_LoggingConfiguration_Contents"></a>

 ** DagProcessingLogs **   <a name="mwaa-Type-LoggingConfiguration-DagProcessingLogs"></a>
The Airflow DAG processing logs published to CloudWatch Logs and the log level.  
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object  
Required: No

 ** SchedulerLogs **   <a name="mwaa-Type-LoggingConfiguration-SchedulerLogs"></a>
The Airflow scheduler logs published to CloudWatch Logs and the log level.  
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object  
Required: No

 ** TaskLogs **   <a name="mwaa-Type-LoggingConfiguration-TaskLogs"></a>
The Airflow task logs published to CloudWatch Logs and the log level.  
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object  
Required: No

 ** WebserverLogs **   <a name="mwaa-Type-LoggingConfiguration-WebserverLogs"></a>
The Airflow web server logs published to CloudWatch Logs and the log level.  
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object  
Required: No

 ** WorkerLogs **   <a name="mwaa-Type-LoggingConfiguration-WorkerLogs"></a>
The Airflow worker logs published to CloudWatch Logs and the log level.  
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object  
Required: No

## See Also
<a name="API_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/LoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/LoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/LoggingConfiguration) 