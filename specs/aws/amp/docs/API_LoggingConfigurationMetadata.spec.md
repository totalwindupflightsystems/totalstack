---
id: "@specs/aws/amp/docs/API_LoggingConfigurationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LoggingConfigurationMetadata"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# LoggingConfigurationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_LoggingConfigurationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LoggingConfigurationMetadata
<a name="API_LoggingConfigurationMetadata"></a>

Contains information about the current rules and alerting logging configuration for the workspace.

**Note**  
These logging configurations are only for rules and alerting logs.

## Contents
<a name="API_LoggingConfigurationMetadata_Contents"></a>

 ** createdAt **   <a name="prometheus-Type-LoggingConfigurationMetadata-createdAt"></a>
The date and time that the logging configuration was created.  
Type: Timestamp  
Required: Yes

 ** logGroupArn **   <a name="prometheus-Type-LoggingConfigurationMetadata-logGroupArn"></a>
The ARN of the CloudWatch log group to which the vended log data will be published.  
Type: String  
Pattern: `arn:aws[a-z0-9-]*:logs:[a-z0-9-]+:[0-9]{12}:log-group:[A-Za-z0-9\.\-\_\#/]{1,512}\:\*`   
Required: Yes

 ** modifiedAt **   <a name="prometheus-Type-LoggingConfigurationMetadata-modifiedAt"></a>
The date and time that the logging configuration was most recently changed.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="prometheus-Type-LoggingConfigurationMetadata-status"></a>
The current status of the logging configuration.  
Type: [LoggingConfigurationStatus](API_LoggingConfigurationStatus.md) object  
Required: Yes

 ** workspace **   <a name="prometheus-Type-LoggingConfigurationMetadata-workspace"></a>
The ID of the workspace the logging configuration is for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## See Also
<a name="API_LoggingConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/LoggingConfigurationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/LoggingConfigurationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/LoggingConfigurationMetadata) 