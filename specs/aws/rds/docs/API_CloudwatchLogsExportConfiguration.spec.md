---
id: "@specs/aws/rds/docs/API_CloudwatchLogsExportConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudwatchLogsExportConfiguration"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CloudwatchLogsExportConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CloudwatchLogsExportConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudwatchLogsExportConfiguration
<a name="API_CloudwatchLogsExportConfiguration"></a>

The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.

The `EnableLogTypes` and `DisableLogTypes` arrays determine which logs will be exported (or not exported) to CloudWatch Logs. The values within these arrays depend on the DB engine being used.

For more information about exporting CloudWatch Logs for Amazon RDS DB instances, see [Publishing Database Logs to Amazon CloudWatch Logs ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.

For more information about exporting CloudWatch Logs for Amazon Aurora DB clusters, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_CloudwatchLogsExportConfiguration_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DisableLogTypes.member.N **   
The list of log types to disable.  
The following values are valid for each DB engine:  
+ Aurora MySQL - `audit | error | general | slowquery` 
+ Aurora PostgreSQL - `postgresql` 
+ RDS for MySQL - `error | general | slowquery` 
+ RDS for PostgreSQL - `postgresql | upgrade` 
Type: Array of strings  
Required: No

 ** EnableLogTypes.member.N **   
The list of log types to enable.  
The following values are valid for each DB engine:  
+ Aurora MySQL - `audit | error | general | slowquery` 
+ Aurora PostgreSQL - `postgresql` 
+ RDS for MySQL - `error | general | slowquery` 
+ RDS for PostgreSQL - `postgresql | upgrade` 
Type: Array of strings  
Required: No

## See Also
<a name="API_CloudwatchLogsExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CloudwatchLogsExportConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CloudwatchLogsExportConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CloudwatchLogsExportConfiguration) 