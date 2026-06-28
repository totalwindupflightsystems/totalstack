---
id: "@specs/aws/network-firewall/docs/API_UpdateLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateLoggingConfiguration
<a name="API_UpdateLoggingConfiguration"></a>

Sets the logging configuration for the specified firewall. 

To change the logging configuration, retrieve the [LoggingConfiguration](API_LoggingConfiguration.md) by calling [DescribeLoggingConfiguration](API_DescribeLoggingConfiguration.md), then change it and provide the modified object to this update call. You must change the logging configuration one [LogDestinationConfig](API_LogDestinationConfig.md) at a time inside the retrieved [LoggingConfiguration](API_LoggingConfiguration.md) object. 

You can perform only one of the following actions in any call to `UpdateLoggingConfiguration`: 
+ Create a new log destination object by adding a single `LogDestinationConfig` array element to `LogDestinationConfigs`.
+ Delete a log destination object by removing a single `LogDestinationConfig` array element from `LogDestinationConfigs`.
+ Change the `LogDestination` setting in a single `LogDestinationConfig` array element.

You can't change the `LogDestinationType` or `LogType` in a `LogDestinationConfig`. To change these settings, delete the existing `LogDestinationConfig` object and create a new one, using two separate calls to this update operation.

## Request Syntax
<a name="API_UpdateLoggingConfiguration_RequestSyntax"></a>

```
{
   "EnableMonitoringDashboard": {{boolean}},
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}",
   "LoggingConfiguration": { 
      "LogDestinationConfigs": [ 
         { 
            "LogDestination": { 
               "{{string}}" : "{{string}}" 
            },
            "LogDestinationType": "{{string}}",
            "LogType": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_UpdateLoggingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EnableMonitoringDashboard](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-request-EnableMonitoringDashboard"></a>
A boolean that lets you enable or disable the detailed firewall monitoring dashboard on the firewall.   
The monitoring dashboard provides comprehensive visibility into your firewall's flow logs and alert logs. After you enable detailed monitoring, you can access these dashboards directly from the **Monitoring** page of the Network Firewall console.  
 Specify `TRUE` to enable the the detailed monitoring dashboard on the firewall. Specify `FALSE` to disable the the detailed monitoring dashboard on the firewall.   
Type: Boolean  
Required: No

 ** [FirewallArn](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [LoggingConfiguration](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-request-LoggingConfiguration"></a>
Defines how Network Firewall performs logging for a firewall. If you omit this setting, Network Firewall disables logging for the firewall.  
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_UpdateLoggingConfiguration_ResponseSyntax"></a>

```
{
   "EnableMonitoringDashboard": boolean,
   "FirewallArn": "string",
   "FirewallName": "string",
   "LoggingConfiguration": { 
      "LogDestinationConfigs": [ 
         { 
            "LogDestination": { 
               "string" : "string" 
            },
            "LogDestinationType": "string",
            "LogType": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EnableMonitoringDashboard](#API_UpdateLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-response-EnableMonitoringDashboard"></a>
A boolean that reflects whether or not the firewall monitoring dashboard is enabled on a firewall.  
 Returns `TRUE` when the firewall monitoring dashboard is enabled on the firewall. Returns `FALSE` when the firewall monitoring dashboard is not enabled on the firewall.   
Type: Boolean

 ** [FirewallArn](#API_UpdateLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FirewallName](#API_UpdateLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-response-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [LoggingConfiguration](#API_UpdateLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateLoggingConfiguration-response-LoggingConfiguration"></a>
Defines how AWS Network Firewall performs logging for a [Firewall](API_Firewall.md).   
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object

## Errors
<a name="API_UpdateLoggingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** InvalidTokenException **   
The token you provided is stale or isn't valid for the operation.   
HTTP Status Code: 400

 ** LogDestinationPermissionException **   
Unable to send logs to a configured logging destination.   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateLoggingConfiguration) 