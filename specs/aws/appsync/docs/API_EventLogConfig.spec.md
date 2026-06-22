---
id: "@specs/aws/appsync/docs/API_EventLogConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventLogConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# EventLogConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_EventLogConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventLogConfig
<a name="API_EventLogConfig"></a>

Describes the CloudWatch Logs configuration for the Event API.

## Contents
<a name="API_EventLogConfig_Contents"></a>

 ** cloudWatchLogsRoleArn **   <a name="appsync-Type-EventLogConfig-cloudWatchLogsRoleArn"></a>
The IAM service role that AWS AppSync assumes to publish CloudWatch Logs in your account.  
Type: String  
Required: Yes

 ** logLevel **   <a name="appsync-Type-EventLogConfig-logLevel"></a>
The type of information to log for the Event API.   
Type: String  
Valid Values: `NONE | ERROR | ALL | INFO | DEBUG`   
Required: Yes

## See Also
<a name="API_EventLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/EventLogConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/EventLogConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/EventLogConfig) 