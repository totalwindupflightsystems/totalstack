---
id: "@specs/aws/network-firewall/docs/API_RulesSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RulesSource"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# RulesSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_RulesSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RulesSource
<a name="API_RulesSource"></a>

The stateless or stateful rules definitions for use in a single rule group. Each rule group requires a single `RulesSource`. You can use an instance of this for either stateless rules or stateful rules. 

## Contents
<a name="API_RulesSource_Contents"></a>

 ** RulesSourceList **   <a name="networkfirewall-Type-RulesSource-RulesSourceList"></a>
Stateful inspection criteria for a domain list rule group.   
Type: [RulesSourceList](API_RulesSourceList.md) object  
Required: No

 ** RulesString **   <a name="networkfirewall-Type-RulesSource-RulesString"></a>
Stateful inspection criteria, provided in Suricata compatible rules. Suricata is an open-source threat detection framework that includes a standard rule-based language for network traffic inspection.  
These rules contain the inspection criteria and the action to take for traffic that matches the criteria, so this type of rule group doesn't have a separate action setting.  
You can't use the `priority` keyword if the `RuleOrder` option in [StatefulRuleOptions](API_StatefulRuleOptions.md) is set to `STRICT_ORDER`.
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2000000.  
Required: No

 ** StatefulRules **   <a name="networkfirewall-Type-RulesSource-StatefulRules"></a>
An array of individual stateful rules inspection criteria to be used together in a stateful rule group. Use this option to specify simple Suricata rules with protocol, source and destination, ports, direction, and rule options. For information about the Suricata `Rules` format, see [Rules Format](https://suricata.readthedocs.io/en/suricata-7.0.8/rules/intro.html).   
Type: Array of [StatefulRule](API_StatefulRule.md) objects  
Required: No

 ** StatelessRulesAndCustomActions **   <a name="networkfirewall-Type-RulesSource-StatelessRulesAndCustomActions"></a>
Stateless inspection criteria to be used in a stateless rule group.   
Type: [StatelessRulesAndCustomActions](API_StatelessRulesAndCustomActions.md) object  
Required: No

## See Also
<a name="API_RulesSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RulesSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RulesSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RulesSource) 