---
id: "@specs/aws/appsync/docs/API_LogConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LogConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# LogConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_LogConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LogConfig
<a name="API_LogConfig"></a>

The Amazon CloudWatch Logs configuration.

## Contents
<a name="API_LogConfig_Contents"></a>

 ** cloudWatchLogsRoleArn **   <a name="appsync-Type-LogConfig-cloudWatchLogsRoleArn"></a>
The service role that AWS AppSync assumes to publish to CloudWatch logs in your account.  
Type: String  
Required: Yes

 ** fieldLogLevel **   <a name="appsync-Type-LogConfig-fieldLogLevel"></a>
The field logging level. Values can be NONE, ERROR, or ALL.  
+  **NONE**: No field-level logs are captured.
+  **ERROR**: Logs the following information only for the fields that are in error:
  + The error section in the server response.
  + Field-level errors.
  + The generated request/response functions that got resolved for error fields.
+  **ALL**: The following information is logged for all fields in the query:
  + Field-level tracing information.
  + The generated request/response functions that got resolved for each field.
Type: String  
Valid Values: `NONE | ERROR | ALL | INFO | DEBUG`   
Required: Yes

 ** excludeVerboseContent **   <a name="appsync-Type-LogConfig-excludeVerboseContent"></a>
Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.  
Type: Boolean  
Required: No

## See Also
<a name="API_LogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/LogConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/LogConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/LogConfig) 