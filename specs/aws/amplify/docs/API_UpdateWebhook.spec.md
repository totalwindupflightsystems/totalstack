---
id: "@specs/aws/amplify/docs/API_UpdateWebhook"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateWebhook"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# UpdateWebhook

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_UpdateWebhook
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateWebhook
<a name="API_UpdateWebhook"></a>

Updates a webhook. 

## Request Syntax
<a name="API_UpdateWebhook_RequestSyntax"></a>

```
POST /webhooks/{{webhookId}} HTTP/1.1
Content-type: application/json

{
   "branchName": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWebhook_RequestParameters"></a>

The request uses the following URI parameters.

 ** [webhookId](#API_UpdateWebhook_RequestSyntax) **   <a name="amplify-UpdateWebhook-request-uri-webhookId"></a>
The unique ID for a webhook.   
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

## Request Body
<a name="API_UpdateWebhook_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [branchName](#API_UpdateWebhook_RequestSyntax) **   <a name="amplify-UpdateWebhook-request-branchName"></a>
The name for a branch that is part of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** [description](#API_UpdateWebhook_RequestSyntax) **   <a name="amplify-UpdateWebhook-request-description"></a>
The description for a webhook.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

## Response Syntax
<a name="API_UpdateWebhook_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "webhook": { 
      "appId": "string",
      "branchName": "string",
      "createTime": number,
      "description": "string",
      "updateTime": number,
      "webhookArn": "string",
      "webhookId": "string",
      "webhookUrl": "string"
   }
}
```

## Response Elements
<a name="API_UpdateWebhook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [webhook](#API_UpdateWebhook_ResponseSyntax) **   <a name="amplify-UpdateWebhook-response-webhook"></a>
Describes a webhook that connects repository events to an Amplify app.   
Type: [Webhook](API_Webhook.md) object

## Errors
<a name="API_UpdateWebhook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** DependentServiceFailureException **   
An operation failed because a dependent service threw an exception.   
HTTP Status Code: 503

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_UpdateWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/UpdateWebhook) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/UpdateWebhook) 