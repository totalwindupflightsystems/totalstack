---
id: "@specs/aws/network-firewall/docs/API_FirewallPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FirewallPolicy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FirewallPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FirewallPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FirewallPolicy
<a name="API_FirewallPolicy"></a>

The firewall policy defines the behavior of a firewall using a collection of stateless and stateful rule groups and other settings. You can use one firewall policy for multiple firewalls. 

This, along with [FirewallPolicyResponse](API_FirewallPolicyResponse.md), define the policy. You can retrieve all objects for a firewall policy by calling [DescribeFirewallPolicy](API_DescribeFirewallPolicy.md).

## Contents
<a name="API_FirewallPolicy_Contents"></a>

 ** StatelessDefaultActions **   <a name="networkfirewall-Type-FirewallPolicy-StatelessDefaultActions"></a>
The actions to take on a packet if it doesn't match any of the stateless rules in the policy. If you want non-matching packets to be forwarded for stateful inspection, specify `aws:forward_to_sfe`.   
You must specify one of the standard actions: `aws:pass`, `aws:drop`, or `aws:forward_to_sfe`. In addition, you can specify custom actions that are compatible with your standard section choice.  
For example, you could specify `["aws:pass"]` or you could specify `["aws:pass", “customActionName”]`. For information about compatibility, see the custom action descriptions under [CustomAction](API_CustomAction.md).  
Type: Array of strings  
Required: Yes

 ** StatelessFragmentDefaultActions **   <a name="networkfirewall-Type-FirewallPolicy-StatelessFragmentDefaultActions"></a>
The actions to take on a fragmented UDP packet if it doesn't match any of the stateless rules in the policy. Network Firewall only manages UDP packet fragments and silently drops packet fragments for other protocols. If you want non-matching fragmented UDP packets to be forwarded for stateful inspection, specify `aws:forward_to_sfe`.   
You must specify one of the standard actions: `aws:pass`, `aws:drop`, or `aws:forward_to_sfe`. In addition, you can specify custom actions that are compatible with your standard section choice.  
For example, you could specify `["aws:pass"]` or you could specify `["aws:pass", “customActionName”]`. For information about compatibility, see the custom action descriptions under [CustomAction](API_CustomAction.md).  
Type: Array of strings  
Required: Yes

 ** EnableTLSSessionHolding **   <a name="networkfirewall-Type-FirewallPolicy-EnableTLSSessionHolding"></a>
When true, prevents TCP and TLS packets from reaching destination servers until TLS Inspection has evaluated Server Name Indication (SNI) rules. Requires an associated TLS Inspection configuration.  
Type: Boolean  
Required: No

 ** PolicyVariables **   <a name="networkfirewall-Type-FirewallPolicy-PolicyVariables"></a>
Contains variables that you can use to override default Suricata settings in your firewall policy.  
Type: [PolicyVariables](API_PolicyVariables.md) object  
Required: No

 ** StatefulDefaultActions **   <a name="networkfirewall-Type-FirewallPolicy-StatefulDefaultActions"></a>
The default actions to take on a packet that doesn't match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.  
Valid values of the stateful default action:  
+ aws:drop\_strict
+ aws:drop\_established
+ aws:alert\_strict
+ aws:alert\_established
+ aws:drop\_established\_app\_layer
+ aws:alert\_established\_app\_layer
+ aws:drop\_established\_app\_layer\_to\_server
+ aws:alert\_established\_app\_layer\_to\_server
For more information, see [Strict evaluation order](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order.html) in the * AWS Network Firewall Developer Guide*.   
Type: Array of strings  
Required: No

 ** StatefulEngineOptions **   <a name="networkfirewall-Type-FirewallPolicy-StatefulEngineOptions"></a>
Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.  
Type: [StatefulEngineOptions](API_StatefulEngineOptions.md) object  
Required: No

 ** StatefulRuleGroupReferences **   <a name="networkfirewall-Type-FirewallPolicy-StatefulRuleGroupReferences"></a>
References to the stateful rule groups that are used in the policy. These define the inspection criteria in stateful rules.   
Type: Array of [StatefulRuleGroupReference](API_StatefulRuleGroupReference.md) objects  
Required: No

 ** StatelessCustomActions **   <a name="networkfirewall-Type-FirewallPolicy-StatelessCustomActions"></a>
The custom action definitions that are available for use in the firewall policy's `StatelessDefaultActions` setting. You name each custom action that you define, and then you can use it by name in your default actions specifications.  
Type: Array of [CustomAction](API_CustomAction.md) objects  
Required: No

 ** StatelessRuleGroupReferences **   <a name="networkfirewall-Type-FirewallPolicy-StatelessRuleGroupReferences"></a>
References to the stateless rule groups that are used in the policy. These define the matching criteria in stateless rules.   
Type: Array of [StatelessRuleGroupReference](API_StatelessRuleGroupReference.md) objects  
Required: No

 ** TLSInspectionConfigurationArn **   <a name="networkfirewall-Type-FirewallPolicy-TLSInspectionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

## See Also
<a name="API_FirewallPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicy) 