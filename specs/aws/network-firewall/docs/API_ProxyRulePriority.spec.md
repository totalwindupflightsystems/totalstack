---
id: "@specs/aws/network-firewall/docs/API_ProxyRulePriority"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRulePriority"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRulePriority

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRulePriority
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRulePriority
<a name="API_ProxyRulePriority"></a>

Proxy rule name and new desired position. 

## Contents
<a name="API_ProxyRulePriority_Contents"></a>

 ** NewPosition **   <a name="networkfirewall-Type-ProxyRulePriority-NewPosition"></a>
Where to move a proxy rule in a proxy rule group.   
Type: Integer  
Required: No

 ** ProxyRuleName **   <a name="networkfirewall-Type-ProxyRulePriority-ProxyRuleName"></a>
The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyRulePriority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRulePriority) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRulePriority) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRulePriority) 