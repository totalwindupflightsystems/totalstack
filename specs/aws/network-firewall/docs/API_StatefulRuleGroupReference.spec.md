---
id: "@specs/aws/network-firewall/docs/API_StatefulRuleGroupReference"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatefulRuleGroupReference"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StatefulRuleGroupReference

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StatefulRuleGroupReference
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatefulRuleGroupReference
<a name="API_StatefulRuleGroupReference"></a>

Identifier for a single stateful rule group, used in a firewall policy to refer to a rule group. 

## Contents
<a name="API_StatefulRuleGroupReference_Contents"></a>

 ** ResourceArn **   <a name="networkfirewall-Type-StatefulRuleGroupReference-ResourceArn"></a>
The Amazon Resource Name (ARN) of the stateful rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** DeepThreatInspection **   <a name="networkfirewall-Type-StatefulRuleGroupReference-DeepThreatInspection"></a>
 AWS Network Firewall plans to augment the active threat defense managed rule group with an additional deep threat inspection capability. When this capability is released, AWS will analyze service logs of network traffic processed by these rule groups to identify threat indicators across customers. AWS will use these threat indicators to improve the active threat defense managed rule groups and protect the security of AWS customers and services.  
Customers can opt-out of deep threat inspection at any time through the AWS Network Firewall console or API. When customers opt out, AWS Network Firewall will not use the network traffic processed by those customers' active threat defense rule groups for rule group improvement.
Type: Boolean  
Required: No

 ** Override **   <a name="networkfirewall-Type-StatefulRuleGroupReference-Override"></a>
The action that allows the policy owner to override the behavior of the rule group within a policy.  
Type: [StatefulRuleGroupOverride](API_StatefulRuleGroupOverride.md) object  
Required: No

 ** Priority **   <a name="networkfirewall-Type-StatefulRuleGroupReference-Priority"></a>
An integer setting that indicates the order in which to run the stateful rule groups in a single [FirewallPolicy](API_FirewallPolicy.md). This setting only applies to firewall policies that specify the `STRICT_ORDER` rule order in the stateful engine options settings.  
Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.  
You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_StatefulRuleGroupReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulRuleGroupReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulRuleGroupReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulRuleGroupReference) 