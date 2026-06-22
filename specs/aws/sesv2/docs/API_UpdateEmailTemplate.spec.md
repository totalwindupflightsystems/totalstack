---
id: "@specs/aws/sesv2/docs/API_UpdateEmailTemplate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateEmailTemplate"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# UpdateEmailTemplate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_UpdateEmailTemplate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateEmailTemplate
<a name="API_UpdateEmailTemplate"></a>

Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html).

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_UpdateEmailTemplate_RequestSyntax"></a>

```
PUT /v2/email/templates/{{TemplateName}} HTTP/1.1
Content-type: application/json

{
   "TemplateContent": { 
      "Html": "{{string}}",
      "Subject": "{{string}}",
      "Text": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateEmailTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TemplateName](#API_UpdateEmailTemplate_RequestSyntax) **   <a name="SES-UpdateEmailTemplate-request-uri-TemplateName"></a>
The name of the template.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_UpdateEmailTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TemplateContent](#API_UpdateEmailTemplate_RequestSyntax) **   <a name="SES-UpdateEmailTemplate-request-TemplateContent"></a>
The content of the email template, composed of a subject line, an HTML part, and a text-only part.  
Type: [EmailTemplateContent](API_EmailTemplateContent.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateEmailTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateEmailTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateEmailTemplate_Errors"></a>

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
<a name="API_UpdateEmailTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/UpdateEmailTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/UpdateEmailTemplate) 