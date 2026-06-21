---
id: "@specs/aws/wafv2/docs/API_waf_PutLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# PutLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_PutLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutLoggingConfiguration
<a name="API_waf_PutLoggingConfiguration"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Associates a [LoggingConfiguration](API_waf_LoggingConfiguration.md) with a specified web ACL.

You can access information about all traffic that AWS WAF inspects using the following steps:

1. Create an Amazon Data Firehose. 

   Create the data firehose with a PUT source and in the region that you are operating. However, if you are capturing logs for Amazon CloudFront, always create the firehose in US East (N. Virginia). 

   Give the data firehose a name that starts with the prefix `aws-waf-logs-`. For example, `aws-waf-logs-us-east-2-analytics`.
**Note**  
Do not create the data firehose using a `Kinesis stream` as your source.

1. Associate that firehose to your web ACL using a `PutLoggingConfiguration` request.

When you successfully enable logging using a `PutLoggingConfiguration` request, AWS WAF will create a service linked role with the necessary permissions to write logs to the Amazon Data Firehose. For more information, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) in the * AWS WAF Developer Guide*.

## Request Syntax
<a name="API_waf_PutLoggingConfiguration_RequestSyntax"></a>

```
{
   "LoggingConfiguration": { 
      "LogDestinationConfigs": [ "{{string}}" ],
      "RedactedFields": [ 
         { 
            "Data": "{{string}}",
            "Type": "{{string}}"
         }
      ],
      "ResourceArn": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_waf_PutLoggingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LoggingConfiguration](#API_waf_PutLoggingConfiguration_RequestSyntax) **   <a name="WAF-waf_PutLoggingConfiguration-request-LoggingConfiguration"></a>
The Amazon Data Firehose that contains the inspected traffic information, the redacted fields details, and the Amazon Resource Name (ARN) of the web ACL to monitor.  
When specifying `Type` in `RedactedFields`, you must use one of the following values: `URI`, `QUERY_STRING`, `HEADER`, or `METHOD`.
Type: [LoggingConfiguration](API_waf_LoggingConfiguration.md) object  
Required: Yes

## Response Syntax
<a name="API_waf_PutLoggingConfiguration_ResponseSyntax"></a>

```
{
   "LoggingConfiguration": { 
      "LogDestinationConfigs": [ "string" ],
      "RedactedFields": [ 
         { 
            "Data": "string",
            "Type": "string"
         }
      ],
      "ResourceArn": "string"
   }
}
```

## Response Elements
<a name="API_waf_PutLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LoggingConfiguration](#API_waf_PutLoggingConfiguration_ResponseSyntax) **   <a name="WAF-waf_PutLoggingConfiguration-response-LoggingConfiguration"></a>
The [LoggingConfiguration](API_waf_LoggingConfiguration.md) that you submitted in the request.  
Type: [LoggingConfiguration](API_waf_LoggingConfiguration.md) object

## Errors
<a name="API_waf_PutLoggingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

 ** WAFServiceLinkedRoleErrorException **   
 AWS WAF is not able to access the service linked role. This can be caused by a previous `PutLoggingConfiguration` request, which can lock the service linked role for about 20 seconds. Please try your request again. The service linked role can also be locked by a previous `DeleteServiceLinkedRole` request, which can lock the role for 15 minutes or more. If you recently made a `DeleteServiceLinkedRole`, wait at least 15 minutes and try the request again. If you receive this same exception again, you will have to wait additional time until the role is unlocked.  
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

## See Also
<a name="API_waf_PutLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/PutLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/PutLoggingConfiguration) 