---
id: "@specs/aws/network-firewall/docs/API_ProxyRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRule"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRule
<a name="API_ProxyRule"></a>

Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). 

## Contents
<a name="API_ProxyRule_Contents"></a>

 ** Action **   <a name="networkfirewall-Type-ProxyRule-Action"></a>
Action to take.   
Type: String  
Valid Values: `ALLOW | DENY | ALERT`   
Required: No

 ** Conditions **   <a name="networkfirewall-Type-ProxyRule-Conditions"></a>
Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against.   
Type: Array of [ProxyRuleCondition](API_ProxyRuleCondition.md) objects  
Required: No

 ** Description **   <a name="networkfirewall-Type-ProxyRule-Description"></a>
A description of the proxy rule.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** ProxyRuleName **   <a name="networkfirewall-Type-ProxyRule-ProxyRuleName"></a>
The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRule) 