---
id: "@specs/aws/shield/docs/API_ResponseAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResponseAction"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# ResponseAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_ResponseAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResponseAction
<a name="API_ResponseAction"></a>

Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource. 

## Contents
<a name="API_ResponseAction_Contents"></a>

 ** Block **   <a name="AWSShield-Type-ResponseAction-Block"></a>
Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Block` action.   
You must specify exactly one action, either `Block` or `Count`.  
Type: [BlockAction](API_BlockAction.md) object  
Required: No

 ** Count **   <a name="AWSShield-Type-ResponseAction-Count"></a>
Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Count` action.   
You must specify exactly one action, either `Block` or `Count`.  
Type: [CountAction](API_CountAction.md) object  
Required: No

## See Also
<a name="API_ResponseAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ResponseAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ResponseAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ResponseAction) 