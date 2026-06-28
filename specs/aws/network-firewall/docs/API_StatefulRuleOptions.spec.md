---
id: "@specs/aws/network-firewall/docs/API_StatefulRuleOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatefulRuleOptions"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StatefulRuleOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StatefulRuleOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatefulRuleOptions
<a name="API_StatefulRuleOptions"></a>

Additional options governing how Network Firewall handles the rule group. You can only use these for stateful rule groups.

## Contents
<a name="API_StatefulRuleOptions_Contents"></a>

 ** RuleOrder **   <a name="networkfirewall-Type-StatefulRuleOptions-RuleOrder"></a>
Indicates how to manage the order of the rule evaluation for the rule group. `DEFAULT_ACTION_ORDER` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the * AWS Network Firewall Developer Guide*.   
Type: String  
Valid Values: `DEFAULT_ACTION_ORDER | STRICT_ORDER`   
Required: No

## See Also
<a name="API_StatefulRuleOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulRuleOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulRuleOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulRuleOptions) 