---
id: "@specs/aws/network-firewall/docs/API_ProxyConfigRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyConfigRuleGroup"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyConfigRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyConfigRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyConfigRuleGroup
<a name="API_ProxyConfigRuleGroup"></a>

Proxy rule group contained within a proxy configuration. 

## Contents
<a name="API_ProxyConfigRuleGroup_Contents"></a>

 ** Priority **   <a name="networkfirewall-Type-ProxyConfigRuleGroup-Priority"></a>
Priority of the proxy rule group in the proxy configuration.   
Type: Integer  
Required: No

 ** ProxyRuleGroupArn **   <a name="networkfirewall-Type-ProxyConfigRuleGroup-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** ProxyRuleGroupName **   <a name="networkfirewall-Type-ProxyConfigRuleGroup-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** Type **   <a name="networkfirewall-Type-ProxyConfigRuleGroup-Type"></a>
Proxy rule group type.   
Type: String  
Required: No

## See Also
<a name="API_ProxyConfigRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyConfigRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyConfigRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyConfigRuleGroup) 