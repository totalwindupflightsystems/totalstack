---
id: "@specs/aws/amplify/docs/API_WafConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WafConfiguration"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# WafConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_WafConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WafConfiguration
<a name="API_WafConfiguration"></a>

Describes the Firewall configuration for a hosted Amplify application. Firewall support enables you to protect your web applications with a direct integration with AWS WAF. For more information about using AWS WAF protections for an Amplify application, see [Firewall support for hosted sites](https://docs.aws.amazon.com/amplify/latest/userguide/WAF-integration.html) in the *Amplify User Guide*. 

## Contents
<a name="API_WafConfiguration_Contents"></a>

 ** statusReason **   <a name="amplify-Type-WafConfiguration-statusReason"></a>
The reason for the current status of the Firewall configuration.  
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** wafStatus **   <a name="amplify-Type-WafConfiguration-wafStatus"></a>
The status of the process to associate or disassociate a web ACL to an Amplify app.  
Type: String  
Valid Values: `ASSOCIATING | ASSOCIATION_FAILED | ASSOCIATION_SUCCESS | DISASSOCIATING | DISASSOCIATION_FAILED`   
Required: No

 ** webAclArn **   <a name="amplify-Type-WafConfiguration-webAclArn"></a>
The Amazon Resource Name (ARN) for the web ACL associated with an Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `^arn:aws:wafv2:.*`   
Required: No

## See Also
<a name="API_WafConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/WafConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/WafConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/WafConfiguration) 