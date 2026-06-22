---
id: "@specs/aws/sesv2/docs/API_GetConfigurationSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetConfigurationSet"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetConfigurationSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetConfigurationSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetConfigurationSet
<a name="API_GetConfigurationSet"></a>

Get information about an existing configuration set, including the dedicated IP pool that it's associated with, whether or not it's enabled for sending email, and more.

 *Configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

## Request Syntax
<a name="API_GetConfigurationSet_RequestSyntax"></a>

```
GET /v2/email/configuration-sets/{{ConfigurationSetName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfigurationSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_GetConfigurationSet_RequestSyntax) **   <a name="SES-GetConfigurationSet-request-uri-ConfigurationSetName"></a>
The name of the configuration set.  
Required: Yes

## Request Body
<a name="API_GetConfigurationSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfigurationSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ArchivingOptions": { 
      "ArchiveArn": "string"
   },
   "ConfigurationSetName": "string",
   "DeliveryOptions": { 
      "MaxDeliverySeconds": number,
      "SendingPoolName": "string",
      "TlsPolicy": "string"
   },
   "ReputationOptions": { 
      "LastFreshStart": number,
      "ReputationMetricsEnabled": boolean
   },
   "SendingOptions": { 
      "SendingEnabled": boolean
   },
   "SuppressionOptions": { 
      "SuppressedReasons": [ "string" ],
      "SuppressionScope": "string",
      "ValidationOptions": { 
         "ConditionThreshold": { 
            "ConditionThresholdEnabled": "string",
            "OverallConfidenceThreshold": { 
               "ConfidenceVerdictThreshold": "string"
            }
         }
      }
   },
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "TrackingOptions": { 
      "CustomRedirectDomain": "string",
      "HttpsPolicy": "string"
   },
   "VdmOptions": { 
      "DashboardOptions": { 
         "EngagementMetrics": "string"
      },
      "GuardianOptions": { 
         "OptimizedSharedDelivery": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetConfigurationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchivingOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-ArchivingOptions"></a>
An object that defines the MailManager archive where sent emails are archived that you send using the configuration set.  
Type: [ArchivingOptions](API_ArchivingOptions.md) object

 ** [ConfigurationSetName](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-ConfigurationSetName"></a>
The name of the configuration set.  
Type: String

 ** [DeliveryOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-DeliveryOptions"></a>
An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.  
Type: [DeliveryOptions](API_DeliveryOptions.md) object

 ** [ReputationOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-ReputationOptions"></a>
An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.  
Type: [ReputationOptions](API_ReputationOptions.md) object

 ** [SendingOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-SendingOptions"></a>
An object that defines whether or not Amazon SES can send email that you send using the configuration set.  
Type: [SendingOptions](API_SendingOptions.md) object

 ** [SuppressionOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-SuppressionOptions"></a>
An object that contains information about the suppression list preferences for your account or for a specific tenant.  
Type: [SuppressionOptions](API_SuppressionOptions.md) object

 ** [Tags](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-Tags"></a>
An array of objects that define the tags (keys and values) that are associated with the configuration set.  
Type: Array of [Tag](API_Tag.md) objects

 ** [TrackingOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-TrackingOptions"></a>
An object that defines the open and click tracking options for emails that you send using the configuration set.  
Type: [TrackingOptions](API_TrackingOptions.md) object

 ** [VdmOptions](#API_GetConfigurationSet_ResponseSyntax) **   <a name="SES-GetConfigurationSet-response-VdmOptions"></a>
An object that contains information about the VDM preferences for your configuration set.  
Type: [VdmOptions](API_VdmOptions.md) object

## Errors
<a name="API_GetConfigurationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetConfigurationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetConfigurationSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetConfigurationSet) 