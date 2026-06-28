---
id: "@specs/aws/network-firewall/docs/API_StatefulRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatefulRule"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StatefulRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StatefulRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatefulRule
<a name="API_StatefulRule"></a>

A single Suricata rules specification, for use in a stateful rule group. Use this option to specify a simple Suricata rule with protocol, source and destination, ports, direction, and rule options. For information about the Suricata `Rules` format, see [Rules Format](https://suricata.readthedocs.io/en/suricata-7.0.8/rules/intro.html). 

## Contents
<a name="API_StatefulRule_Contents"></a>

 ** Action **   <a name="networkfirewall-Type-StatefulRule-Action"></a>
Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria. For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow.   
The actions for a stateful rule are defined as follows:   
+  **PASS** - Permits the packets to go to the intended destination.
+  **DROP** - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the [Firewall](API_Firewall.md) [LoggingConfiguration](API_LoggingConfiguration.md). 
+  **ALERT** - Sends an alert log message, if alert logging is configured in the [Firewall](API_Firewall.md) [LoggingConfiguration](API_LoggingConfiguration.md). 

  You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with `ALERT` action, verify in the logs that the rule is filtering as you want, then change the action to `DROP`.
+  **REJECT** - Drops traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and an RST bit contained in the TCP header flags. REJECT is available only for TCP traffic. This option doesn't support FTP or IMAP protocols.
Type: String  
Valid Values: `PASS | DROP | ALERT | REJECT`   
Required: Yes

 ** Header **   <a name="networkfirewall-Type-StatefulRule-Header"></a>
The stateful inspection criteria for this rule, used to inspect traffic flows.   
Type: [Header](API_Header.md) object  
Required: Yes

 ** RuleOptions **   <a name="networkfirewall-Type-StatefulRule-RuleOptions"></a>
Additional options for the rule. These are the Suricata `RuleOptions` settings.  
Type: Array of [RuleOption](API_RuleOption.md) objects  
Required: Yes

## See Also
<a name="API_StatefulRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulRule) 