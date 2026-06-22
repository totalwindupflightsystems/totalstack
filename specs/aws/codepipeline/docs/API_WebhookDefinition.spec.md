---
id: "@specs/aws/codepipeline/docs/API_WebhookDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WebhookDefinition"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# WebhookDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_WebhookDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WebhookDefinition
<a name="API_WebhookDefinition"></a>

Represents information about a webhook and its definition.

## Contents
<a name="API_WebhookDefinition_Contents"></a>

 ** authentication **   <a name="CodePipeline-Type-WebhookDefinition-authentication"></a>
Supported options are GITHUB\_HMAC, IP, and UNAUTHENTICATED.  
When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.
If a secret token was provided, it will be redacted in the response.
+ For information about the authentication scheme implemented by GITHUB\_HMAC, see [Securing your webhooks](https://developer.github.com/webhooks/securing/) on the GitHub Developer website.
+  IP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.
+  UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.
Type: String  
Valid Values: `GITHUB_HMAC | IP | UNAUTHENTICATED`   
Required: Yes

 ** authenticationConfiguration **   <a name="CodePipeline-Type-WebhookDefinition-authenticationConfiguration"></a>
Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB\_HMAC, only the `SecretToken `property must be set. For IP, only the `AllowedIPRange `property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.  
Type: [WebhookAuthConfiguration](API_WebhookAuthConfiguration.md) object  
Required: Yes

 ** filters **   <a name="CodePipeline-Type-WebhookDefinition-filters"></a>
A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.  
Type: Array of [WebhookFilterRule](API_WebhookFilterRule.md) objects  
Array Members: Maximum number of 5 items.  
Required: Yes

 ** name **   <a name="CodePipeline-Type-WebhookDefinition-name"></a>
The name of the webhook.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** targetAction **   <a name="CodePipeline-Type-WebhookDefinition-targetAction"></a>
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** targetPipeline **   <a name="CodePipeline-Type-WebhookDefinition-targetPipeline"></a>
The name of the pipeline you want to connect to the webhook.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## See Also
<a name="API_WebhookDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/WebhookDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/WebhookDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/WebhookDefinition) 