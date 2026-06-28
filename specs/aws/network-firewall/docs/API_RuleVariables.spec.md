---
id: "@specs/aws/network-firewall/docs/API_RuleVariables"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleVariables"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# RuleVariables

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_RuleVariables
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleVariables
<a name="API_RuleVariables"></a>

Settings that are available for use in the rules in the [RuleGroup](API_RuleGroup.md) where this is defined. See [CreateRuleGroup](API_CreateRuleGroup.md) or [UpdateRuleGroup](API_UpdateRuleGroup.md) for usage.

## Contents
<a name="API_RuleVariables_Contents"></a>

 ** IPSets **   <a name="networkfirewall-Type-RuleVariables-IPSets"></a>
A list of IP addresses and address ranges, in CIDR notation.   
Type: String to [IPSet](API_IPSet.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 32.  
Key Pattern: `^[A-Za-z][A-Za-z0-9_]*$`   
Required: No

 ** PortSets **   <a name="networkfirewall-Type-RuleVariables-PortSets"></a>
A list of port ranges.   
Type: String to [PortSet](API_PortSet.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 32.  
Key Pattern: `^[A-Za-z][A-Za-z0-9_]*$`   
Required: No

## See Also
<a name="API_RuleVariables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleVariables) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleVariables) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleVariables) 