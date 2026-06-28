---
id: "@specs/aws/fsx/docs/API_LustreLogCreateConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LustreLogCreateConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# LustreLogCreateConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_LustreLogCreateConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LustreLogCreateConfiguration
<a name="API_LustreLogCreateConfiguration"></a>

The Lustre logging configuration used when creating or updating an Amazon FSx for Lustre file system. An Amazon File Cache is created with Lustre logging enabled by default, with a setting of `WARN_ERROR` for the logging events. which can't be changed.

Lustre logging writes the enabled logging events for your file system or cache to Amazon CloudWatch Logs.

## Contents
<a name="API_LustreLogCreateConfiguration_Contents"></a>

 ** Level **   <a name="FSx-Type-LustreLogCreateConfiguration-Level"></a>
Sets which data repository events are logged by Amazon FSx.  
+  `WARN_ONLY` - only warning events are logged.
+  `ERROR_ONLY` - only error events are logged.
+  `WARN_ERROR` - both warning events and error events are logged.
+  `DISABLED` - logging of data repository events is turned off.
Type: String  
Valid Values: `DISABLED | WARN_ONLY | ERROR_ONLY | WARN_ERROR`   
Required: Yes

 ** Destination **   <a name="FSx-Type-LustreLogCreateConfiguration-Destination"></a>
The Amazon Resource Name (ARN) that specifies the destination of the logs.  
The destination can be any Amazon CloudWatch Logs log group ARN, with the following requirements:  
+ The destination ARN that you provide must be in the same AWS partition, AWS Region, and AWS account as your Amazon FSx file system.
+ The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix.
+ If you do not provide a destination, Amazon FSx will create and use a log stream in the CloudWatch Logs `/aws/fsx/lustre` log group (for Amazon FSx for Lustre) or `/aws/fsx/filecache` (for Amazon File Cache).
+ If `Destination` is provided and the resource does not exist, the request will fail with a `BadRequest` error.
+ If `Level` is set to `DISABLED`, you cannot specify a destination in `Destination`.
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`   
Required: No

## See Also
<a name="API_LustreLogCreateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/LustreLogCreateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/LustreLogCreateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/LustreLogCreateConfiguration) 