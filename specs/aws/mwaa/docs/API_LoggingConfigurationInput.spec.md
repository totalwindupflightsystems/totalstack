---
id: "@specs/aws/mwaa/docs/API_LoggingConfigurationInput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LoggingConfigurationInput"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# LoggingConfigurationInput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_LoggingConfigurationInput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LoggingConfigurationInput
<a name="API_LoggingConfigurationInput"></a>

Defines the Apache Airflow log types to send to CloudWatch Logs.

## Contents
<a name="API_LoggingConfigurationInput_Contents"></a>

 ** DagProcessingLogs **   <a name="mwaa-Type-LoggingConfigurationInput-DagProcessingLogs"></a>
Publishes Airflow DAG processing logs to CloudWatch Logs.  
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object  
Required: No

 ** SchedulerLogs **   <a name="mwaa-Type-LoggingConfigurationInput-SchedulerLogs"></a>
Publishes Airflow scheduler logs to CloudWatch Logs.  
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object  
Required: No

 ** TaskLogs **   <a name="mwaa-Type-LoggingConfigurationInput-TaskLogs"></a>
Publishes Airflow task logs to CloudWatch Logs.  
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object  
Required: No

 ** WebserverLogs **   <a name="mwaa-Type-LoggingConfigurationInput-WebserverLogs"></a>
Publishes Airflow web server logs to CloudWatch Logs.  
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object  
Required: No

 ** WorkerLogs **   <a name="mwaa-Type-LoggingConfigurationInput-WorkerLogs"></a>
Publishes Airflow worker logs to CloudWatch Logs.  
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object  
Required: No

## See Also
<a name="API_LoggingConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/LoggingConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/LoggingConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/LoggingConfigurationInput) 