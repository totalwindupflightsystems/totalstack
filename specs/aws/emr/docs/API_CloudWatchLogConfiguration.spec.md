---
id: "@specs/aws/emr/docs/API_CloudWatchLogConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudWatchLogConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CloudWatchLogConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CloudWatchLogConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudWatchLogConfiguration
<a name="API_CloudWatchLogConfiguration"></a>

Holds CloudWatch log configuration settings and metadata that specify settings like log files to monitor and where to send them.

## Contents
<a name="API_CloudWatchLogConfiguration_Contents"></a>

 ** Enabled **   <a name="EMR-Type-CloudWatchLogConfiguration-Enabled"></a>
Specifies if CloudWatch logging is enabled.  
Type: Boolean  
Required: Yes

 ** EncryptionKeyArn **   <a name="EMR-Type-CloudWatchLogConfiguration-EncryptionKeyArn"></a>
The ARN of the encryption key used to encrypt the logs.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LogGroupName **   <a name="EMR-Type-CloudWatchLogConfiguration-LogGroupName"></a>
The name of the CloudWatch log group where logs are published.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LogStreamNamePrefix **   <a name="EMR-Type-CloudWatchLogConfiguration-LogStreamNamePrefix"></a>
The prefix of the log stream name.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LogTypes **   <a name="EMR-Type-CloudWatchLogConfiguration-LogTypes"></a>
A map of log types to file names for publishing logs to the standard output or standard error streams for CloudWatch. Valid log types include STEP\_LOGS, SPARK\_DRIVER, and SPARK\_EXECUTOR. Valid file names for each type include STDOUT and STDERR.  
Type: String to array of strings map  
Key Length Constraints: Minimum length of 0. Maximum length of 10280.  
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_CloudWatchLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CloudWatchLogConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CloudWatchLogConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CloudWatchLogConfiguration) 