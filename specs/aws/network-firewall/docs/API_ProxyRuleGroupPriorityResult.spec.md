---
id: "@specs/aws/network-firewall/docs/API_ProxyRuleGroupPriorityResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRuleGroupPriorityResult"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRuleGroupPriorityResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRuleGroupPriorityResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRuleGroupPriorityResult
<a name="API_ProxyRuleGroupPriorityResult"></a>

Proxy rule group along with its priority. 

## Contents
<a name="API_ProxyRuleGroupPriorityResult_Contents"></a>

 ** Priority **   <a name="networkfirewall-Type-ProxyRuleGroupPriorityResult-Priority"></a>
Priority of the proxy rule group in the proxy configuration.   
Type: Integer  
Required: No

 ** ProxyRuleGroupName **   <a name="networkfirewall-Type-ProxyRuleGroupPriorityResult-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyRuleGroupPriorityResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRuleGroupPriorityResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRuleGroupPriorityResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRuleGroupPriorityResult) 