---
id: "@specs/aws/fsx/docs/API_WindowsAuditLogCreateConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WindowsAuditLogCreateConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# WindowsAuditLogCreateConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_WindowsAuditLogCreateConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WindowsAuditLogCreateConfiguration
<a name="API_WindowsAuditLogCreateConfiguration"></a>

The Windows file access auditing configuration used when creating or updating an Amazon FSx for Windows File Server file system.

## Contents
<a name="API_WindowsAuditLogCreateConfiguration_Contents"></a>

 ** FileAccessAuditLogLevel **   <a name="FSx-Type-WindowsAuditLogCreateConfiguration-FileAccessAuditLogLevel"></a>
Sets which attempt type is logged by Amazon FSx for file and folder accesses.  
+  `SUCCESS_ONLY` - only successful attempts to access files or folders are logged.
+  `FAILURE_ONLY` - only failed attempts to access files or folders are logged.
+  `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access files or folders are logged.
+  `DISABLED` - access auditing of files and folders is turned off.
Type: String  
Valid Values: `DISABLED | SUCCESS_ONLY | FAILURE_ONLY | SUCCESS_AND_FAILURE`   
Required: Yes

 ** FileShareAccessAuditLogLevel **   <a name="FSx-Type-WindowsAuditLogCreateConfiguration-FileShareAccessAuditLogLevel"></a>
Sets which attempt type is logged by Amazon FSx for file share accesses.  
+  `SUCCESS_ONLY` - only successful attempts to access file shares are logged.
+  `FAILURE_ONLY` - only failed attempts to access file shares are logged.
+  `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access file shares are logged.
+  `DISABLED` - access auditing of file shares is turned off.
Type: String  
Valid Values: `DISABLED | SUCCESS_ONLY | FAILURE_ONLY | SUCCESS_AND_FAILURE`   
Required: Yes

 ** AuditLogDestination **   <a name="FSx-Type-WindowsAuditLogCreateConfiguration-AuditLogDestination"></a>
The Amazon Resource Name (ARN) that specifies the destination of the audit logs.  
The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN, with the following requirements:  
+ The destination ARN that you provide (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same AWS partition, AWS Region, and AWS account as your Amazon FSx file system.
+ The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.
+ If you do not provide a destination in `AuditLogDestination`, Amazon FSx will create and use a log stream in the CloudWatch Logs `/aws/fsx/windows` log group.
+ If `AuditLogDestination` is provided and the resource does not exist, the request will fail with a `BadRequest` error.
+ If `FileAccessAuditLogLevel` and `FileShareAccessAuditLogLevel` are both set to `DISABLED`, you cannot specify a destination in `AuditLogDestination`.
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`   
Required: No

## See Also
<a name="API_WindowsAuditLogCreateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/WindowsAuditLogCreateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/WindowsAuditLogCreateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/WindowsAuditLogCreateConfiguration) 