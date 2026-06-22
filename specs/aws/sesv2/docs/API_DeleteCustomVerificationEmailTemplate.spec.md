---
id: "@specs/aws/sesv2/docs/API_DeleteCustomVerificationEmailTemplate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCustomVerificationEmailTemplate"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeleteCustomVerificationEmailTemplate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeleteCustomVerificationEmailTemplate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCustomVerificationEmailTemplate
<a name="API_DeleteCustomVerificationEmailTemplate"></a>

Deletes an existing custom verification email template.

For more information about custom verification email templates, see [Using custom verification email templates](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_DeleteCustomVerificationEmailTemplate_RequestSyntax"></a>

```
DELETE /v2/email/custom-verification-email-templates/{{TemplateName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCustomVerificationEmailTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TemplateName](#API_DeleteCustomVerificationEmailTemplate_RequestSyntax) **   <a name="SES-DeleteCustomVerificationEmailTemplate-request-uri-TemplateName"></a>
The name of the custom verification email template that you want to delete.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_DeleteCustomVerificationEmailTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCustomVerificationEmailTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCustomVerificationEmailTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomVerificationEmailTemplate_Errors"></a>

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
<a name="API_DeleteCustomVerificationEmailTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeleteCustomVerificationEmailTemplate) 