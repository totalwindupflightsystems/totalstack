---
id: "@specs/aws/codepipeline/docs/API_WebhookAuthConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WebhookAuthConfiguration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# WebhookAuthConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_WebhookAuthConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WebhookAuthConfiguration
<a name="API_WebhookAuthConfiguration"></a>

The authentication applied to incoming webhook trigger requests.

## Contents
<a name="API_WebhookAuthConfiguration_Contents"></a>

 ** AllowedIPRange **   <a name="CodePipeline-Type-WebhookAuthConfiguration-AllowedIPRange"></a>
The property used to configure acceptance of webhooks in an IP address range. For IP, only the `AllowedIPRange` property must be set. This property must be set to a valid CIDR range.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** SecretToken **   <a name="CodePipeline-Type-WebhookAuthConfiguration-SecretToken"></a>
The property used to configure GitHub authentication. For GITHUB\_HMAC, only the `SecretToken` property must be set.  
When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.
If a secret token was provided, it will be redacted in the response.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_WebhookAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/WebhookAuthConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/WebhookAuthConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/WebhookAuthConfiguration) 