---
id: "@specs/aws/amplify/docs/API_Webhook"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Webhook"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# Webhook

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_Webhook
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Webhook
<a name="API_Webhook"></a>

Describes a webhook that connects repository events to an Amplify app. 

## Contents
<a name="API_Webhook_Contents"></a>

 ** branchName **   <a name="amplify-Type-Webhook-branchName"></a>
The name for a branch that is part of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** createTime **   <a name="amplify-Type-Webhook-createTime"></a>
A timestamp of when Amplify created the webhook in your Git repository.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="amplify-Type-Webhook-description"></a>
The description for a webhook.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: Yes

 ** updateTime **   <a name="amplify-Type-Webhook-updateTime"></a>
A timestamp of when Amplify updated the webhook in your Git repository.  
Type: Timestamp  
Required: Yes

 ** webhookArn **   <a name="amplify-Type-Webhook-webhookArn"></a>
The Amazon Resource Name (ARN) for the webhook.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** webhookId **   <a name="amplify-Type-Webhook-webhookId"></a>
The ID of the webhook.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

 ** webhookUrl **   <a name="amplify-Type-Webhook-webhookUrl"></a>
The URL of the webhook.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** appId **   <a name="amplify-Type-Webhook-appId"></a>
The unique ID of an Amplify app.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: No

## See Also
<a name="API_Webhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/Webhook) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/Webhook) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/Webhook) 