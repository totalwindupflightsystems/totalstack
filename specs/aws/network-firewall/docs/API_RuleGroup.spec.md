---
id: "@specs/aws/network-firewall/docs/API_RuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleGroup"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# RuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_RuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleGroup
<a name="API_RuleGroup"></a>

The object that defines the rules in a rule group. This, along with [RuleGroupResponse](API_RuleGroupResponse.md), define the rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](API_DescribeRuleGroup.md). 

 AWS Network Firewall uses a rule group to inspect and control network traffic. You define stateless rule groups to inspect individual packets and you define stateful rule groups to inspect packets in the context of their traffic flow. 

To use a rule group, you include it by reference in an Network Firewall firewall policy, then you use the policy in a firewall. You can reference a rule group from more than one firewall policy, and you can use a firewall policy in more than one firewall. 

## Contents
<a name="API_RuleGroup_Contents"></a>

 ** RulesSource **   <a name="networkfirewall-Type-RuleGroup-RulesSource"></a>
The stateful rules or stateless rules for the rule group.   
Type: [RulesSource](API_RulesSource.md) object  
Required: Yes

 ** ReferenceSets **   <a name="networkfirewall-Type-RuleGroup-ReferenceSets"></a>
The list of a rule group's reference sets.  
Type: [ReferenceSets](API_ReferenceSets.md) object  
Required: No

 ** RuleVariables **   <a name="networkfirewall-Type-RuleGroup-RuleVariables"></a>
Settings that are available for use in the rules in the rule group. You can only use these for stateful rule groups.   
Type: [RuleVariables](API_RuleVariables.md) object  
Required: No

 ** StatefulRuleOptions **   <a name="networkfirewall-Type-RuleGroup-StatefulRuleOptions"></a>
Additional options governing how Network Firewall handles stateful rules. The policies where you use your stateful rule group must have stateful rule options settings that are compatible with these settings. Some limitations apply; for more information, see [Strict evaluation order](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html) in the * AWS Network Firewall Developer Guide*.  
Type: [StatefulRuleOptions](API_StatefulRuleOptions.md) object  
Required: No

## See Also
<a name="API_RuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleGroup) 