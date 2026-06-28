---
id: "@specs/aws/network-firewall/docs/API_ProxyRuleGroupAttachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRuleGroupAttachment"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRuleGroupAttachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRuleGroupAttachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRuleGroupAttachment
<a name="API_ProxyRuleGroupAttachment"></a>

The proxy rule group(s) to attach to the proxy configuration

## Contents
<a name="API_ProxyRuleGroupAttachment_Contents"></a>

 ** InsertPosition **   <a name="networkfirewall-Type-ProxyRuleGroupAttachment-InsertPosition"></a>
Where to insert a proxy rule group in a proxy configuration.   
Type: Integer  
Required: No

 ** ProxyRuleGroupName **   <a name="networkfirewall-Type-ProxyRuleGroupAttachment-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyRuleGroupAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRuleGroupAttachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRuleGroupAttachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRuleGroupAttachment) 