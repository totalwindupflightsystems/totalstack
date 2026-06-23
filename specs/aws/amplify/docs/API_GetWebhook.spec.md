---
id: "@specs/aws/amplify/docs/API_GetWebhook"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetWebhook"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# GetWebhook

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_GetWebhook
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetWebhook
<a name="API_GetWebhook"></a>

Returns the webhook information that corresponds to a specified webhook ID. 

## Request Syntax
<a name="API_GetWebhook_RequestSyntax"></a>

```
GET /webhooks/{{webhookId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWebhook_RequestParameters"></a>

The request uses the following URI parameters.

 ** [webhookId](#API_GetWebhook_RequestSyntax) **   <a name="amplify-GetWebhook-request-uri-webhookId"></a>
The unique ID for a webhook.   
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

## Request Body
<a name="API_GetWebhook_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWebhook_ResponseSyntax"></a>

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
<a name="API_GetWebhook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [webhook](#API_GetWebhook_ResponseSyntax) **   <a name="amplify-GetWebhook-response-webhook"></a>
Describes the structure of a webhook.   
Type: [Webhook](API_Webhook.md) object

## Errors
<a name="API_GetWebhook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

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
<a name="API_GetWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/GetWebhook) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/GetWebhook) 