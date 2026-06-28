---
id: "@specs/aws/amp/docs/API_LoggingConfigurationStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LoggingConfigurationStatus"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# LoggingConfigurationStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_LoggingConfigurationStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LoggingConfigurationStatus
<a name="API_LoggingConfigurationStatus"></a>

The status of the logging configuration. 

## Contents
<a name="API_LoggingConfigurationStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-LoggingConfigurationStatus-statusCode"></a>
The current status of the current rules and alerting logging configuration.  
These logging configurations are only for rules and alerting logs.
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATION_FAILED | UPDATE_FAILED`   
Required: Yes

 ** statusReason **   <a name="prometheus-Type-LoggingConfigurationStatus-statusReason"></a>
If failed, the reason for the failure.  
Type: String  
Required: No

## See Also
<a name="API_LoggingConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/LoggingConfigurationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/LoggingConfigurationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/LoggingConfigurationStatus) 