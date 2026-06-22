---
id: "@specs/aws/sesv2/docs/API_ListEmailTemplates"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEmailTemplates"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListEmailTemplates

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListEmailTemplates
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEmailTemplates
<a name="API_ListEmailTemplates"></a>

Lists the email templates present in your Amazon SES account in the current AWS Region.

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_ListEmailTemplates_RequestSyntax"></a>

```
GET /v2/email/templates?NextToken={{NextToken}}&PageSize={{PageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEmailTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_ListEmailTemplates_RequestSyntax) **   <a name="SES-ListEmailTemplates-request-uri-NextToken"></a>
A token returned from a previous call to `ListEmailTemplates` to indicate the position in the list of email templates.

 ** [PageSize](#API_ListEmailTemplates_RequestSyntax) **   <a name="SES-ListEmailTemplates-request-uri-PageSize"></a>
The number of results to show in a single call to `ListEmailTemplates`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.  
The value you specify has to be at least 1, and can be no more than 100.

## Request Body
<a name="API_ListEmailTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEmailTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TemplatesMetadata": [ 
      { 
         "CreatedTimestamp": number,
         "TemplateName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListEmailTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListEmailTemplates_ResponseSyntax) **   <a name="SES-ListEmailTemplates-response-NextToken"></a>
A token indicating that there are additional email templates available to be listed. Pass this token to a subsequent `ListEmailTemplates` call to retrieve the next 10 email templates.  
Type: String

 ** [TemplatesMetadata](#API_ListEmailTemplates_ResponseSyntax) **   <a name="SES-ListEmailTemplates-response-TemplatesMetadata"></a>
An array the contains the name and creation time stamp for each template in your Amazon SES account.  
Type: Array of [EmailTemplateMetadata](API_EmailTemplateMetadata.md) objects

## Errors
<a name="API_ListEmailTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListEmailTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListEmailTemplates) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListEmailTemplates) 