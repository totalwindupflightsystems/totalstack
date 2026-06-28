---
id: "@specs/aws/network-firewall/docs/API_StatefulEngineOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatefulEngineOptions"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StatefulEngineOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StatefulEngineOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatefulEngineOptions
<a name="API_StatefulEngineOptions"></a>

Configuration settings for the handling of the stateful rule groups in a firewall policy. 

**Important**  
Updating any setting in `StatefulEngineOptions` may require a restart of the stateful engine in order to apply the changes. When this occurs, existing connections will be treated according to your stream exception policy configuration.

## Contents
<a name="API_StatefulEngineOptions_Contents"></a>

 ** FlowTimeouts **   <a name="networkfirewall-Type-StatefulEngineOptions-FlowTimeouts"></a>
Configures the amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle.   
Type: [FlowTimeouts](API_FlowTimeouts.md) object  
Required: No

 ** RuleOrder **   <a name="networkfirewall-Type-StatefulEngineOptions-RuleOrder"></a>
Indicates how to manage the order of stateful rule evaluation for the policy. `STRICT_ORDER` is the recommended option, but `DEFAULT_ACTION_ORDER` is the default option. With `STRICT_ORDER`, provide your rules in the order that you want them to be evaluated. You can then choose one or more default actions for packets that don't match any rules. Choose `STRICT_ORDER` to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is `PASS`, followed by `DROP`, `REJECT`, and `ALERT` actions. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on your settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the * AWS Network Firewall Developer Guide*.   
Type: String  
Valid Values: `DEFAULT_ACTION_ORDER | STRICT_ORDER`   
Required: No

 ** StreamExceptionPolicy **   <a name="networkfirewall-Type-StatefulEngineOptions-StreamExceptionPolicy"></a>
Configures how Network Firewall processes traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself.  
+  `DROP` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior.
+  `CONTINUE` - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to `drop http` traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a `flow:stateless` rule would still match, as would the `aws:drop_strict` default action.
+  `REJECT` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.
Type: String  
Valid Values: `DROP | CONTINUE | REJECT`   
Required: No

## See Also
<a name="API_StatefulEngineOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulEngineOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulEngineOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulEngineOptions) 