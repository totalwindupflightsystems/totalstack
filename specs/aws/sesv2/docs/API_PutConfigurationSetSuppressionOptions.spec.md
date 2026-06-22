---
id: "@specs/aws/sesv2/docs/API_PutConfigurationSetSuppressionOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutConfigurationSetSuppressionOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutConfigurationSetSuppressionOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutConfigurationSetSuppressionOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutConfigurationSetSuppressionOptions
<a name="API_PutConfigurationSetSuppressionOptions"></a>

Specify the suppression list preferences for a configuration set. You can also use this operation to specify a `SuppressionScope` to override the suppression scope of the tenant or account for emails sent using this configuration set.

## Request Syntax
<a name="API_PutConfigurationSetSuppressionOptions_RequestSyntax"></a>

```
PUT /v2/email/configuration-sets/{{ConfigurationSetName}}/suppression-options HTTP/1.1
Content-type: application/json

{
   "SuppressedReasons": [ "{{string}}" ],
   "SuppressionScope": "{{string}}",
   "ValidationOptions": { 
      "ConditionThreshold": { 
         "ConditionThresholdEnabled": "{{string}}",
         "OverallConfidenceThreshold": { 
            "ConfidenceVerdictThreshold": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetSuppressionOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetSuppressionOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetSuppressionOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set to change the suppression list preferences for.  
Required: Yes

## Request Body
<a name="API_PutConfigurationSetSuppressionOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SuppressedReasons](#API_PutConfigurationSetSuppressionOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetSuppressionOptions-request-SuppressedReasons"></a>
A list that contains the reasons that email addresses are automatically added to the suppression list for your account or for a specific tenant. This list can contain any or all of the following:  
+  `COMPLAINT` – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a complaint.
+  `BOUNCE` – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a hard bounce.
Type: Array of strings  
Valid Values: `BOUNCE | COMPLAINT`   
Required: No

 ** [SuppressionScope](#API_PutConfigurationSetSuppressionOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetSuppressionOptions-request-SuppressionScope"></a>
The suppression scope for the configuration set. This overrides the tenant or account suppression scope for emails sent using this configuration set. Can be one of the following:  
+  `TENANT` – Use the tenant's suppression list.
+  `ACCOUNT` – Use the account-level suppression list.
Type: String  
Valid Values: `ACCOUNT | TENANT`   
Required: No

 ** [ValidationOptions](#API_PutConfigurationSetSuppressionOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetSuppressionOptions-request-ValidationOptions"></a>
An object that contains information about the email address suppression preferences for the configuration set in the current AWS Region.  
Type: [SuppressionValidationOptions](API_SuppressionValidationOptions.md) object  
Required: No

## Response Syntax
<a name="API_PutConfigurationSetSuppressionOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutConfigurationSetSuppressionOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationSetSuppressionOptions_Errors"></a>

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
<a name="API_PutConfigurationSetSuppressionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutConfigurationSetSuppressionOptions) 