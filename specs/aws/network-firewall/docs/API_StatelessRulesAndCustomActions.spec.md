---
id: "@specs/aws/network-firewall/docs/API_StatelessRulesAndCustomActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatelessRulesAndCustomActions"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StatelessRulesAndCustomActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StatelessRulesAndCustomActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatelessRulesAndCustomActions
<a name="API_StatelessRulesAndCustomActions"></a>

Stateless inspection criteria. Each stateless rule group uses exactly one of these data types to define its stateless rules. 

## Contents
<a name="API_StatelessRulesAndCustomActions_Contents"></a>

 ** StatelessRules **   <a name="networkfirewall-Type-StatelessRulesAndCustomActions-StatelessRules"></a>
Defines the set of stateless rules for use in a stateless rule group.   
Type: Array of [StatelessRule](API_StatelessRule.md) objects  
Required: Yes

 ** CustomActions **   <a name="networkfirewall-Type-StatelessRulesAndCustomActions-CustomActions"></a>
Defines an array of individual custom action definitions that are available for use by the stateless rules in this `StatelessRulesAndCustomActions` specification. You name each custom action that you define, and then you can use it by name in your [StatelessRule](API_StatelessRule.md) [RuleDefinition](API_RuleDefinition.md) `Actions` specification.  
Type: Array of [CustomAction](API_CustomAction.md) objects  
Required: No

## See Also
<a name="API_StatelessRulesAndCustomActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatelessRulesAndCustomActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatelessRulesAndCustomActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatelessRulesAndCustomActions) 