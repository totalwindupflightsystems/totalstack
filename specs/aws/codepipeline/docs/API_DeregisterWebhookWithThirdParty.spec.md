---
id: "@specs/aws/codepipeline/docs/API_DeregisterWebhookWithThirdParty"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeregisterWebhookWithThirdParty"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# DeregisterWebhookWithThirdParty

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_DeregisterWebhookWithThirdParty
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeregisterWebhookWithThirdParty
<a name="API_DeregisterWebhookWithThirdParty"></a>

Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.

## Request Syntax
<a name="API_DeregisterWebhookWithThirdParty_RequestSyntax"></a>

```
{
   "webhookName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterWebhookWithThirdParty_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [webhookName](#API_DeregisterWebhookWithThirdParty_RequestSyntax) **   <a name="CodePipeline-DeregisterWebhookWithThirdParty-request-webhookName"></a>
The name of the webhook you want to deregister.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

## Response Elements
<a name="API_DeregisterWebhookWithThirdParty_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterWebhookWithThirdParty_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

 ** WebhookNotFoundException **   
The specified webhook was entered in an invalid format or cannot be found.  
HTTP Status Code: 400

## See Also
<a name="API_DeregisterWebhookWithThirdParty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty) 