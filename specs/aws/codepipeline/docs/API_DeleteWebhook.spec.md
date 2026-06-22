---
id: "@specs/aws/codepipeline/docs/API_DeleteWebhook"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteWebhook"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# DeleteWebhook

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_DeleteWebhook
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteWebhook
<a name="API_DeleteWebhook"></a>

Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.

## Request Syntax
<a name="API_DeleteWebhook_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWebhook_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_DeleteWebhook_RequestSyntax) **   <a name="CodePipeline-DeleteWebhook-request-name"></a>
The name of the webhook you want to delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Elements
<a name="API_DeleteWebhook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWebhook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **   
Unable to modify the tag due to a simultaneous update request.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/DeleteWebhook) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/DeleteWebhook) 