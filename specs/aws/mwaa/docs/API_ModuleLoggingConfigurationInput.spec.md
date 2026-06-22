---
id: "@specs/aws/mwaa/docs/API_ModuleLoggingConfigurationInput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModuleLoggingConfigurationInput"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# ModuleLoggingConfigurationInput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_ModuleLoggingConfigurationInput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModuleLoggingConfigurationInput
<a name="API_ModuleLoggingConfigurationInput"></a>

Enables the Apache Airflow log type (e.g. `DagProcessingLogs`) and defines the log level to send to CloudWatch Logs (e.g. `INFO`).

## Contents
<a name="API_ModuleLoggingConfigurationInput_Contents"></a>

 ** Enabled **   <a name="mwaa-Type-ModuleLoggingConfigurationInput-Enabled"></a>
Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs`).  
Type: Boolean  
Required: Yes

 ** LogLevel **   <a name="mwaa-Type-ModuleLoggingConfigurationInput-LogLevel"></a>
Defines the Apache Airflow log level (e.g. `INFO`) to send to CloudWatch Logs.  
Type: String  
Valid Values: `CRITICAL | ERROR | WARNING | INFO | DEBUG`   
Required: Yes

## See Also
<a name="API_ModuleLoggingConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/ModuleLoggingConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/ModuleLoggingConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/ModuleLoggingConfigurationInput) 