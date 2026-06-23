---
id: "@specs/aws/amplify/docs/API_ListWebhooks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListWebhooks"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListWebhooks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListWebhooks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListWebhooks
<a name="API_ListWebhooks"></a>

Returns a list of webhooks for an Amplify app. 

## Request Syntax
<a name="API_ListWebhooks_RequestSyntax"></a>

```
GET /apps/{{appId}}/webhooks?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWebhooks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListWebhooks_RequestSyntax) **   <a name="amplify-ListWebhooks-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [maxResults](#API_ListWebhooks_RequestSyntax) **   <a name="amplify-ListWebhooks-request-uri-maxResults"></a>
The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 50.

 ** [nextToken](#API_ListWebhooks_RequestSyntax) **   <a name="amplify-ListWebhooks-request-uri-nextToken"></a>
A pagination token. Set to null to start listing webhooks from the start. If non-null,the pagination token is returned in a result. Pass its value in here to list more webhooks.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListWebhooks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWebhooks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "webhooks": [ 
      { 
         "appId": "string",
         "branchName": "string",
         "createTime": number,
         "description": "string",
         "updateTime": number,
         "webhookArn": "string",
         "webhookId": "string",
         "webhookUrl": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWebhooks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWebhooks_ResponseSyntax) **   <a name="amplify-ListWebhooks-response-nextToken"></a>
A pagination token. If non-null, the pagination token is returned in a result. Pass its value in another request to retrieve more entries.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

 ** [webhooks](#API_ListWebhooks_ResponseSyntax) **   <a name="amplify-ListWebhooks-response-webhooks"></a>
A list of webhooks.   
Type: Array of [Webhook](API_Webhook.md) objects

## Errors
<a name="API_ListWebhooks_Errors"></a>

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

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_ListWebhooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListWebhooks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListWebhooks) 