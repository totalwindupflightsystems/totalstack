---
id: "@specs/aws/fsx/docs/API_WindowsFsrmConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WindowsFsrmConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# WindowsFsrmConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_WindowsFsrmConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WindowsFsrmConfiguration
<a name="API_WindowsFsrmConfiguration"></a>

The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. When FSRM is enabled, you can manage and monitor storage quotas, file screening, storage reports, and file classification.

## Contents
<a name="API_WindowsFsrmConfiguration_Contents"></a>

 ** FsrmServiceEnabled **   <a name="FSx-Type-WindowsFsrmConfiguration-FsrmServiceEnabled"></a>
Specifies whether FSRM is enabled or disabled on the file system. When `TRUE`, the FSRM service is enabled and monitor file operations according to configured policies. When `FALSE` or omitted, FSRM is disabled. The default value is `FALSE`.   
Type: Boolean  
Required: Yes

 ** EventLogDestination **   <a name="FSx-Type-WindowsFsrmConfiguration-EventLogDestination"></a>
The Amazon Resource Name (ARN) for the destination of the FSRM event logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.  
The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.  
The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same AWS partition, AWS Region, and AWS account as your Amazon FSx file system.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`   
Required: No

## See Also
<a name="API_WindowsFsrmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/WindowsFsrmConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/WindowsFsrmConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/WindowsFsrmConfiguration) 