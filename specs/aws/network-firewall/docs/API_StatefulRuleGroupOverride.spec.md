---
id: "@specs/aws/network-firewall/docs/API_StatefulRuleGroupOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatefulRuleGroupOverride"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StatefulRuleGroupOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StatefulRuleGroupOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatefulRuleGroupOverride
<a name="API_StatefulRuleGroupOverride"></a>

The setting that allows the policy owner to change the behavior of the rule group within a policy. 

## Contents
<a name="API_StatefulRuleGroupOverride_Contents"></a>

 ** Action **   <a name="networkfirewall-Type-StatefulRuleGroupOverride-Action"></a>
The action that changes the rule group from `DROP` to `ALERT`. This only applies to managed rule groups.  
Type: String  
Valid Values: `DROP_TO_ALERT`   
Required: No

## See Also
<a name="API_StatefulRuleGroupOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulRuleGroupOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulRuleGroupOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulRuleGroupOverride) 