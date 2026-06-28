---
id: "@specs/aws/network-firewall/docs/API_ProxyConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyConfiguration
<a name="API_ProxyConfiguration"></a>

A Proxy Configuration defines the monitoring and protection behavior for a Proxy. The details of the behavior are defined in the rule groups that you add to your configuration. 

## Contents
<a name="API_ProxyConfiguration_Contents"></a>

 ** CreateTime **   <a name="networkfirewall-Type-ProxyConfiguration-CreateTime"></a>
Time the Proxy Configuration was created.   
Type: Timestamp  
Required: No

 ** DefaultRulePhaseActions **   <a name="networkfirewall-Type-ProxyConfiguration-DefaultRulePhaseActions"></a>
Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied.   
Pre-DNS - before domain resolution.  
Pre-Request - after DNS, before request.  
Post-Response - after receiving response.  
Type: [ProxyConfigDefaultRulePhaseActionsRequest](API_ProxyConfigDefaultRulePhaseActionsRequest.md) object  
Required: No

 ** DeleteTime **   <a name="networkfirewall-Type-ProxyConfiguration-DeleteTime"></a>
Time the Proxy Configuration was deleted.   
Type: Timestamp  
Required: No

 ** Description **   <a name="networkfirewall-Type-ProxyConfiguration-Description"></a>
A description of the proxy configuration.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** ProxyConfigurationArn **   <a name="networkfirewall-Type-ProxyConfiguration-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** ProxyConfigurationName **   <a name="networkfirewall-Type-ProxyConfiguration-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** RuleGroups **   <a name="networkfirewall-Type-ProxyConfiguration-RuleGroups"></a>
Proxy rule groups within the proxy configuration.   
Type: Array of [ProxyConfigRuleGroup](API_ProxyConfigRuleGroup.md) objects  
Required: No

 ** Tags **   <a name="networkfirewall-Type-ProxyConfiguration-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## See Also
<a name="API_ProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyConfiguration) 