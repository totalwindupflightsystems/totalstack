---
id: "@specs/aws/network-firewall/docs/API_RulesSourceList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RulesSourceList"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# RulesSourceList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_RulesSourceList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RulesSourceList
<a name="API_RulesSourceList"></a>

Stateful inspection criteria for a domain list rule group. 

For HTTPS traffic, domain filtering is SNI-based. It uses the server name indicator extension of the TLS handshake.

By default, Network Firewall domain list inspection only includes traffic coming from the VPC where you deploy the firewall. To inspect traffic from IP addresses outside of the deployment VPC, you set the `HOME_NET` rule variable to include the CIDR range of the deployment VPC plus the other CIDR ranges. For more information, see [RuleVariables](API_RuleVariables.md) in this guide and [Stateful domain list rule groups in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html) in the *Network Firewall Developer Guide*.

## Contents
<a name="API_RulesSourceList_Contents"></a>

 ** GeneratedRulesType **   <a name="networkfirewall-Type-RulesSourceList-GeneratedRulesType"></a>
Whether you want to apply allow, reject, alert, or drop behavior to the domains in your target list.  
When logging is enabled and you choose Alert, traffic that matches the domain specifications generates an alert in the firewall's logs. Then, traffic either passes, is rejected, or drops based on other rules in the firewall policy.
Type: String  
Valid Values: `ALLOWLIST | DENYLIST | REJECTLIST | ALERTLIST`   
Required: Yes

 ** Targets **   <a name="networkfirewall-Type-RulesSourceList-Targets"></a>
The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:  
+ Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com`.
+ Names that use a domain wildcard, which you indicate with an initial '`.`'. For example,`.example.com` matches `example.com` and matches all subdomains of `example.com`, such as `abc.example.com` and `www.example.com`. 
Type: Array of strings  
Required: Yes

 ** TargetTypes **   <a name="networkfirewall-Type-RulesSourceList-TargetTypes"></a>
The protocols you want to inspect. Specify `TLS_SNI` for `HTTPS`. Specify `HTTP_HOST` for `HTTP`. You can specify either or both.   
Type: Array of strings  
Valid Values: `TLS_SNI | HTTP_HOST`   
Required: Yes

## See Also
<a name="API_RulesSourceList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RulesSourceList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RulesSourceList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RulesSourceList) 