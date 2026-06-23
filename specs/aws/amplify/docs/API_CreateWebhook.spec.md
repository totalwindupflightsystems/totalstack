---
id: "@specs/aws/amplify/docs/API_CreateWebhook"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateWebhook"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CreateWebhook

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CreateWebhook
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateWebhook
<a name="API_CreateWebhook"></a>

Creates a new webhook on an Amplify app. 

## Request Syntax
<a name="API_CreateWebhook_RequestSyntax"></a>

```
POST /apps/{{appId}}/webhooks HTTP/1.1
Content-type: application/json

{
   "branchName": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWebhook_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_CreateWebhook_RequestSyntax) **   <a name="amplify-CreateWebhook-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_CreateWebhook_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [branchName](#API_CreateWebhook_RequestSyntax) **   <a name="amplify-CreateWebhook-request-branchName"></a>
The name for a branch that is part of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** [description](#API_CreateWebhook_RequestSyntax) **   <a name="amplify-CreateWebhook-request-description"></a>
The description for a webhook.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

## Response Syntax
<a name="API_CreateWebhook_ResponseSyntax"></a>

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
<a name="API_CreateWebhook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [webhook](#API_CreateWebhook_ResponseSyntax) **   <a name="amplify-CreateWebhook-response-webhook"></a>
Describes a webhook that connects repository events to an Amplify app.   
Type: [Webhook](API_Webhook.md) object

## Errors
<a name="API_CreateWebhook_Errors"></a>

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

 ** LimitExceededException **   
A resource could not be created because service quotas were exceeded.   
HTTP Status Code: 429

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_CreateWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/CreateWebhook) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CreateWebhook) 