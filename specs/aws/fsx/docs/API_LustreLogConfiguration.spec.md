---
id: "@specs/aws/fsx/docs/API_LustreLogConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LustreLogConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# LustreLogConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_LustreLogConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LustreLogConfiguration
<a name="API_LustreLogConfiguration"></a>

The configuration for Lustre logging used to write the enabled logging events for your Amazon FSx for Lustre file system or Amazon File Cache resource to Amazon CloudWatch Logs.

## Contents
<a name="API_LustreLogConfiguration_Contents"></a>

 ** Level **   <a name="FSx-Type-LustreLogConfiguration-Level"></a>
The data repository events that are logged by Amazon FSx.  
+  `WARN_ONLY` - only warning events are logged.
+  `ERROR_ONLY` - only error events are logged.
+  `WARN_ERROR` - both warning events and error events are logged.
+  `DISABLED` - logging of data repository events is turned off.
Note that Amazon File Cache uses a default setting of `WARN_ERROR`, which can't be changed.  
Type: String  
Valid Values: `DISABLED | WARN_ONLY | ERROR_ONLY | WARN_ERROR`   
Required: Yes

 ** Destination **   <a name="FSx-Type-LustreLogConfiguration-Destination"></a>
The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same AWS partition, AWS Region, and AWS account as your Amazon FSx file system.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`   
Required: No

## See Also
<a name="API_LustreLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/LustreLogConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/LustreLogConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/LustreLogConfiguration) 