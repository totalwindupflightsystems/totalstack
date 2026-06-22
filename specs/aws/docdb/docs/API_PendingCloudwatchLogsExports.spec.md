---
id: "@specs/aws/docdb/docs/API_PendingCloudwatchLogsExports"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PendingCloudwatchLogsExports"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# PendingCloudwatchLogsExports

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_PendingCloudwatchLogsExports
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PendingCloudwatchLogsExports
<a name="API_PendingCloudwatchLogsExports"></a>

A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

## Contents
<a name="API_PendingCloudwatchLogsExports_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** LogTypesToDisable.member.N **   
Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.  
Type: Array of strings  
Required: No

 ** LogTypesToEnable.member.N **   
Log types that are in the process of being deactivated. After they are deactivated, these log types aren't exported to CloudWatch Logs.  
Type: Array of strings  
Required: No

## See Also
<a name="API_PendingCloudwatchLogsExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/PendingCloudwatchLogsExports) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/PendingCloudwatchLogsExports) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/PendingCloudwatchLogsExports) 