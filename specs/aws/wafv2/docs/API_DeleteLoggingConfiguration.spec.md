---
id: "@specs/aws/wafv2/docs/API_DeleteLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# DeleteLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_DeleteLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteLoggingConfiguration
<a name="API_DeleteLoggingConfiguration"></a>

Deletes the [LoggingConfiguration](API_LoggingConfiguration.md) from the specified web ACL.

## Request Syntax
<a name="API_DeleteLoggingConfiguration_RequestSyntax"></a>

```
{
   "LogScope": "{{string}}",
   "LogType": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteLoggingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LogScope](#API_DeleteLoggingConfiguration_RequestSyntax) **   <a name="WAF-DeleteLoggingConfiguration-request-LogScope"></a>
The owner of the logging configuration, which must be set to `CUSTOMER` for the configurations that you manage.   
The log scope `SECURITY_LAKE` indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see [Collecting data from AWS services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) in the *Amazon Security Lake user guide*.   
The log scope `CLOUDWATCH_TELEMETRY_RULE_MANAGED` indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see [What is Amazon CloudWatch Logs ?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) in the *Amazon CloudWatch Logs user guide*.   
Default: `CUSTOMER`   
Type: String  
Valid Values: `CUSTOMER | SECURITY_LAKE | CLOUDWATCH_TELEMETRY_RULE_MANAGED`   
Required: No

 ** [LogType](#API_DeleteLoggingConfiguration_RequestSyntax) **   <a name="WAF-DeleteLoggingConfiguration-request-LogType"></a>
Used to distinguish between various logging options. Currently, there is one option.  
Default: `WAF_LOGS`   
Type: String  
Valid Values: `WAF_LOGS`   
Required: No

 ** [ResourceArn](#API_DeleteLoggingConfiguration_RequestSyntax) **   <a name="WAF-DeleteLoggingConfiguration-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the web ACL from which you want to delete the [LoggingConfiguration](API_LoggingConfiguration.md).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: Yes

## Response Elements
<a name="API_DeleteLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLoggingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation isn't valid.   
HTTP Status Code: 400

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:   
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. 
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.  
 ** Field **   
The settings where the invalid parameter was found.   
 ** Parameter **   
The invalid parameter that resulted in the exception.   
 ** Reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

 ** WAFOptimisticLockException **   
 AWS WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/DeleteLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DeleteLoggingConfiguration) 