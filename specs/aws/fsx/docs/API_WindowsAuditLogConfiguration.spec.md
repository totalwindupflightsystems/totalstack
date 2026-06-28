---
id: "@specs/aws/fsx/docs/API_WindowsAuditLogConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WindowsAuditLogConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# WindowsAuditLogConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_WindowsAuditLogConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WindowsAuditLogConfiguration
<a name="API_WindowsAuditLogConfiguration"></a>

The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system. For more information, see [ File access auditing](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/file-access-auditing.html).

## Contents
<a name="API_WindowsAuditLogConfiguration_Contents"></a>

 ** FileAccessAuditLogLevel **   <a name="FSx-Type-WindowsAuditLogConfiguration-FileAccessAuditLogLevel"></a>
Sets which attempt type is logged by Amazon FSx for file and folder accesses.  
+  `SUCCESS_ONLY` - only successful attempts to access files or folders are logged.
+  `FAILURE_ONLY` - only failed attempts to access files or folders are logged.
+  `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access files or folders are logged.
+  `DISABLED` - access auditing of files and folders is turned off.
Type: String  
Valid Values: `DISABLED | SUCCESS_ONLY | FAILURE_ONLY | SUCCESS_AND_FAILURE`   
Required: Yes

 ** FileShareAccessAuditLogLevel **   <a name="FSx-Type-WindowsAuditLogConfiguration-FileShareAccessAuditLogLevel"></a>
Sets which attempt type is logged by Amazon FSx for file share accesses.  
+  `SUCCESS_ONLY` - only successful attempts to access file shares are logged.
+  `FAILURE_ONLY` - only failed attempts to access file shares are logged.
+  `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access file shares are logged.
+  `DISABLED` - access auditing of file shares is turned off.
Type: String  
Valid Values: `DISABLED | SUCCESS_ONLY | FAILURE_ONLY | SUCCESS_AND_FAILURE`   
Required: Yes

 ** AuditLogDestination **   <a name="FSx-Type-WindowsAuditLogConfiguration-AuditLogDestination"></a>
The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.  
The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.  
The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same AWS partition, AWS Region, and AWS account as your Amazon FSx file system.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`   
Required: No

## See Also
<a name="API_WindowsAuditLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/WindowsAuditLogConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/WindowsAuditLogConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/WindowsAuditLogConfiguration) 