---
id: "@specs/aws/sesv2/docs/API_GetEmailIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetEmailIdentity"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetEmailIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetEmailIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetEmailIdentity
<a name="API_GetEmailIdentity"></a>

Provides information about a specific identity, including the identity's verification status, sending authorization policies, its DKIM authentication status, and its custom Mail-From settings.

## Request Syntax
<a name="API_GetEmailIdentity_RequestSyntax"></a>

```
GET /v2/email/identities/{{EmailIdentity}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEmailIdentity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_GetEmailIdentity_RequestSyntax) **   <a name="SES-GetEmailIdentity-request-uri-EmailIdentity"></a>
The email identity.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_GetEmailIdentity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEmailIdentity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationSetName": "string",
   "DkimAttributes": { 
      "CurrentSigningKeyLength": "string",
      "LastKeyGenerationTimestamp": number,
      "NextSigningKeyLength": "string",
      "SigningAttributesOrigin": "string",
      "SigningEnabled": boolean,
      "SigningHostedZone": "string",
      "Status": "string",
      "Tokens": [ "string" ]
   },
   "FeedbackForwardingStatus": boolean,
   "IdentityType": "string",
   "MailFromAttributes": { 
      "BehaviorOnMxFailure": "string",
      "MailFromDomain": "string",
      "MailFromDomainStatus": "string"
   },
   "Policies": { 
      "string" : "string" 
   },
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "VerificationInfo": { 
      "ErrorType": "string",
      "LastCheckedTimestamp": number,
      "LastSuccessTimestamp": number,
      "SOARecord": { 
         "AdminEmail": "string",
         "PrimaryNameServer": "string",
         "SerialNumber": number
      }
   },
   "VerificationStatus": "string",
   "VerifiedForSendingStatus": boolean
}
```

## Response Elements
<a name="API_GetEmailIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetName](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-ConfigurationSetName"></a>
The configuration set used by default when sending from this identity.  
Type: String

 ** [DkimAttributes](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-DkimAttributes"></a>
An object that contains information about the DKIM attributes for the identity.  
Type: [DkimAttributes](API_DkimAttributes.md) object

 ** [FeedbackForwardingStatus](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-FeedbackForwardingStatus"></a>
The feedback forwarding configuration for the identity.  
If the value is `true`, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the `Return-Path` header of the original email.  
You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).  
Type: Boolean

 ** [IdentityType](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-IdentityType"></a>
The email identity type. Note: the `MANAGED_DOMAIN` identity type is not supported.  
Type: String  
Valid Values: `EMAIL_ADDRESS | DOMAIN | MANAGED_DOMAIN` 

 ** [MailFromAttributes](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-MailFromAttributes"></a>
An object that contains information about the Mail-From attributes for the email identity.  
Type: [MailFromAttributes](API_MailFromAttributes.md) object

 ** [Policies](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-Policies"></a>
A map of policy names to policies.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 64.  
Value Length Constraints: Minimum length of 1.

 ** [Tags](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-Tags"></a>
An array of objects that define the tags (keys and values) that are associated with the email identity.  
Type: Array of [Tag](API_Tag.md) objects

 ** [VerificationInfo](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-VerificationInfo"></a>
An object that contains additional information about the verification status for the identity.  
Type: [VerificationInfo](API_VerificationInfo.md) object

 ** [VerificationStatus](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-VerificationStatus"></a>
The verification status of the identity. The status can be one of the following:  
+  `PENDING` – The verification process was initiated, but Amazon SES hasn't yet been able to verify the identity.
+  `SUCCESS` – The verification process completed successfully.
+  `FAILED` – The verification process failed.
+  `TEMPORARY_FAILURE` – A temporary issue is preventing Amazon SES from determining the verification status of the identity.
+  `NOT_STARTED` – The verification process hasn't been initiated for the identity.
Type: String  
Valid Values: `PENDING | SUCCESS | FAILED | TEMPORARY_FAILURE | NOT_STARTED` 

 ** [VerifiedForSendingStatus](#API_GetEmailIdentity_ResponseSyntax) **   <a name="SES-GetEmailIdentity-response-VerifiedForSendingStatus"></a>
Specifies whether or not the identity is verified. You can only send email from verified email addresses or domains. For more information about verifying identities, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html).  
Type: Boolean

## Errors
<a name="API_GetEmailIdentity_Errors"></a>

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
<a name="API_GetEmailIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetEmailIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetEmailIdentity) 