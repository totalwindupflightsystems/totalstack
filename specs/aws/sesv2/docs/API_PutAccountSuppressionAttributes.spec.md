---
id: "@specs/aws/sesv2/docs/API_PutAccountSuppressionAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAccountSuppressionAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutAccountSuppressionAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutAccountSuppressionAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAccountSuppressionAttributes
<a name="API_PutAccountSuppressionAttributes"></a>

Change the settings for the account-level suppression list.

## Request Syntax
<a name="API_PutAccountSuppressionAttributes_RequestSyntax"></a>

```
PUT /v2/email/account/suppression HTTP/1.1
Content-type: application/json

{
   "SuppressedReasons": [ "{{string}}" ],
   "ValidationAttributes": { 
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
<a name="API_PutAccountSuppressionAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountSuppressionAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SuppressedReasons](#API_PutAccountSuppressionAttributes_RequestSyntax) **   <a name="SES-PutAccountSuppressionAttributes-request-SuppressedReasons"></a>
A list that contains the reasons that email addresses will be automatically added to the suppression list for your account. This list can contain any or all of the following:  
+  `COMPLAINT` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.
+  `BOUNCE` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.
Type: Array of strings  
Valid Values: `BOUNCE | COMPLAINT`   
Required: No

 ** [ValidationAttributes](#API_PutAccountSuppressionAttributes_RequestSyntax) **   <a name="SES-PutAccountSuppressionAttributes-request-ValidationAttributes"></a>
An object that contains additional suppression attributes for your account.  
Type: [SuppressionValidationAttributes](API_SuppressionValidationAttributes.md) object  
Required: No

## Response Syntax
<a name="API_PutAccountSuppressionAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAccountSuppressionAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountSuppressionAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_PutAccountSuppressionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutAccountSuppressionAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutAccountSuppressionAttributes) 