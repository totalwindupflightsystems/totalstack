---
id: "@specs/aws/sesv2/docs/API_PutEmailIdentityMailFromAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutEmailIdentityMailFromAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutEmailIdentityMailFromAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutEmailIdentityMailFromAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutEmailIdentityMailFromAttributes
<a name="API_PutEmailIdentityMailFromAttributes"></a>

Used to enable or disable the custom Mail-From domain configuration for an email identity.

## Request Syntax
<a name="API_PutEmailIdentityMailFromAttributes_RequestSyntax"></a>

```
PUT /v2/email/identities/{{EmailIdentity}}/mail-from HTTP/1.1
Content-type: application/json

{
   "BehaviorOnMxFailure": "{{string}}",
   "MailFromDomain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutEmailIdentityMailFromAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_PutEmailIdentityMailFromAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityMailFromAttributes-request-uri-EmailIdentity"></a>
The verified email identity.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_PutEmailIdentityMailFromAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BehaviorOnMxFailure](#API_PutEmailIdentityMailFromAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityMailFromAttributes-request-BehaviorOnMxFailure"></a>
The action to take if the required MX record isn't found when you send an email. When you set this value to `UseDefaultValue`, the mail is sent using *amazonses.com* as the MAIL FROM domain. When you set this value to `RejectMessage`, the Amazon SES API v2 returns a `MailFromDomainNotVerified` error, and doesn't attempt to deliver the email.  
These behaviors are taken when the custom MAIL FROM domain configuration is in the `Pending`, `Failed`, and `TemporaryFailure` states.  
Type: String  
Valid Values: `USE_DEFAULT_VALUE | REJECT_MESSAGE`   
Required: No

 ** [MailFromDomain](#API_PutEmailIdentityMailFromAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityMailFromAttributes-request-MailFromDomain"></a>
 The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:  
+ It has to be a subdomain of the verified identity.
+ It can't be used to receive email.
+ It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails.
Type: String  
Required: No

## Response Syntax
<a name="API_PutEmailIdentityMailFromAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutEmailIdentityMailFromAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutEmailIdentityMailFromAttributes_Errors"></a>

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
<a name="API_PutEmailIdentityMailFromAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutEmailIdentityMailFromAttributes) 