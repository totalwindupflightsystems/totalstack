---
id: "@specs/aws/network-firewall/docs/API_ProxyRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRuleGroup"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRuleGroup
<a name="API_ProxyRuleGroup"></a>

Collections of related proxy filtering rules. Rule groups help you manage and reuse sets of rules across multiple proxy configurations. 

## Contents
<a name="API_ProxyRuleGroup_Contents"></a>

 ** CreateTime **   <a name="networkfirewall-Type-ProxyRuleGroup-CreateTime"></a>
Time the Proxy Rule Group was created.   
Type: Timestamp  
Required: No

 ** DeleteTime **   <a name="networkfirewall-Type-ProxyRuleGroup-DeleteTime"></a>
Time the Proxy Rule Group was deleted.   
Type: Timestamp  
Required: No

 ** Description **   <a name="networkfirewall-Type-ProxyRuleGroup-Description"></a>
A description of the proxy rule group.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** ProxyRuleGroupArn **   <a name="networkfirewall-Type-ProxyRuleGroup-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** ProxyRuleGroupName **   <a name="networkfirewall-Type-ProxyRuleGroup-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** Rules **   <a name="networkfirewall-Type-ProxyRuleGroup-Rules"></a>
Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert).   
Type: [ProxyRulesByRequestPhase](API_ProxyRulesByRequestPhase.md) object  
Required: No

 ** Tags **   <a name="networkfirewall-Type-ProxyRuleGroup-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## See Also
<a name="API_ProxyRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRuleGroup) 