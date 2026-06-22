---
id: "@specs/aws/sesv2/docs/API_GetEmailAddressInsights"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetEmailAddressInsights"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetEmailAddressInsights

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetEmailAddressInsights
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetEmailAddressInsights
<a name="API_GetEmailAddressInsights"></a>

Provides validation insights about a specific email address, including syntax validation, DNS record checks, mailbox existence, and other deliverability factors.

## Request Syntax
<a name="API_GetEmailAddressInsights_RequestSyntax"></a>

```
POST /v2/email/email-address-insights/ HTTP/1.1
Content-type: application/json

{
   "EmailAddress": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetEmailAddressInsights_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEmailAddressInsights_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailAddress](#API_GetEmailAddressInsights_RequestSyntax) **   <a name="SES-GetEmailAddressInsights-request-EmailAddress"></a>
The email address to analyze for validation insights.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_GetEmailAddressInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MailboxValidation": { 
      "Evaluations": { 
         "HasValidDnsRecords": { 
            "ConfidenceVerdict": "string"
         },
         "HasValidSyntax": { 
            "ConfidenceVerdict": "string"
         },
         "IsDisposable": { 
            "ConfidenceVerdict": "string"
         },
         "IsRandomInput": { 
            "ConfidenceVerdict": "string"
         },
         "IsRoleAddress": { 
            "ConfidenceVerdict": "string"
         },
         "MailboxExists": { 
            "ConfidenceVerdict": "string"
         }
      },
      "IsValid": { 
         "ConfidenceVerdict": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetEmailAddressInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MailboxValidation](#API_GetEmailAddressInsights_ResponseSyntax) **   <a name="SES-GetEmailAddressInsights-response-MailboxValidation"></a>
Detailed validation results for the email address.  
Type: [MailboxValidation](API_MailboxValidation.md) object

## Errors
<a name="API_GetEmailAddressInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetEmailAddressInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetEmailAddressInsights) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetEmailAddressInsights) 