---
id: "@specs/aws/network-firewall/docs/API_ProxyRuleCondition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRuleCondition"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRuleCondition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRuleCondition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRuleCondition
<a name="API_ProxyRuleCondition"></a>

Match criteria that specify what traffic attributes to examine.

## Contents
<a name="API_ProxyRuleCondition_Contents"></a>

 ** ConditionKey **   <a name="networkfirewall-Type-ProxyRuleCondition-ConditionKey"></a>
Defines what is to be matched.  
Type: String  
Required: No

 ** ConditionOperator **   <a name="networkfirewall-Type-ProxyRuleCondition-ConditionOperator"></a>
Defines how to perform a match.  
Type: String  
Required: No

 ** ConditionValues **   <a name="networkfirewall-Type-ProxyRuleCondition-ConditionValues"></a>
Specifes the exact value that needs to be matched against.  
Type: Array of strings  
Required: No

## See Also
<a name="API_ProxyRuleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRuleCondition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRuleCondition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRuleCondition) 