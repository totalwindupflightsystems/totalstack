---
id: "@specs/aws/docdb/docs/API_CloudwatchLogsExportConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudwatchLogsExportConfiguration"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CloudwatchLogsExportConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CloudwatchLogsExportConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudwatchLogsExportConfiguration
<a name="API_CloudwatchLogsExportConfiguration"></a>

The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific instance or cluster.

The `EnableLogTypes` and `DisableLogTypes` arrays determine which logs are exported (or not exported) to CloudWatch Logs. The values within these arrays depend on the engine that is being used.

## Contents
<a name="API_CloudwatchLogsExportConfiguration_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DisableLogTypes.member.N **   
The list of log types to disable.  
Type: Array of strings  
Required: No

 ** EnableLogTypes.member.N **   
The list of log types to enable.  
Type: Array of strings  
Required: No

## See Also
<a name="API_CloudwatchLogsExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CloudwatchLogsExportConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CloudwatchLogsExportConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CloudwatchLogsExportConfiguration) 