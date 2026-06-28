---
id: "@specs/aws/network-firewall/docs/API_DescribeLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeLoggingConfiguration
<a name="API_DescribeLoggingConfiguration"></a>

Returns the logging configuration for the specified firewall. 

## Request Syntax
<a name="API_DescribeLoggingConfiguration_RequestSyntax"></a>

```
{
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLoggingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallArn](#API_DescribeLoggingConfiguration_RequestSyntax) **   <a name="networkfirewall-DescribeLoggingConfiguration-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_DescribeLoggingConfiguration_RequestSyntax) **   <a name="networkfirewall-DescribeLoggingConfiguration-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_DescribeLoggingConfiguration_ResponseSyntax"></a>

```
{
   "EnableMonitoringDashboard": boolean,
   "FirewallArn": "string",
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
<a name="API_DescribeLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EnableMonitoringDashboard](#API_DescribeLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-DescribeLoggingConfiguration-response-EnableMonitoringDashboard"></a>
A boolean that reflects whether or not the firewall monitoring dashboard is enabled on a firewall.  
 Returns `TRUE` when the firewall monitoring dashboard is enabled on the firewall. Returns `FALSE` when the firewall monitoring dashboard is not enabled on the firewall.   
Type: Boolean

 ** [FirewallArn](#API_DescribeLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-DescribeLoggingConfiguration-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [LoggingConfiguration](#API_DescribeLoggingConfiguration_ResponseSyntax) **   <a name="networkfirewall-DescribeLoggingConfiguration-response-LoggingConfiguration"></a>
Defines how AWS Network Firewall performs logging for a [Firewall](API_Firewall.md).   
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object

## Errors
<a name="API_DescribeLoggingConfiguration_Errors"></a>

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

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeLoggingConfiguration) 