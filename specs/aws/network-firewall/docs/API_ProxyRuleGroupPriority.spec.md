---
id: "@specs/aws/network-firewall/docs/API_ProxyRuleGroupPriority"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRuleGroupPriority"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRuleGroupPriority

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRuleGroupPriority
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRuleGroupPriority
<a name="API_ProxyRuleGroupPriority"></a>

Proxy rule group name and new desired position. 

## Contents
<a name="API_ProxyRuleGroupPriority_Contents"></a>

 ** NewPosition **   <a name="networkfirewall-Type-ProxyRuleGroupPriority-NewPosition"></a>
Where to move a proxy rule group in a proxy configuration.   
Type: Integer  
Required: No

 ** ProxyRuleGroupName **   <a name="networkfirewall-Type-ProxyRuleGroupPriority-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyRuleGroupPriority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRuleGroupPriority) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRuleGroupPriority) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRuleGroupPriority) 