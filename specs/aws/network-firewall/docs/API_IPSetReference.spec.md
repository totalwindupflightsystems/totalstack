---
id: "@specs/aws/network-firewall/docs/API_IPSetReference"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IPSetReference"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# IPSetReference

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_IPSetReference
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IPSetReference
<a name="API_IPSetReference"></a>

Configures one or more IP set references for a Suricata-compatible rule group. This is used in [CreateRuleGroup](API_CreateRuleGroup.md) or [UpdateRuleGroup](API_UpdateRuleGroup.md). An IP set reference is a rule variable that references resources that you create and manage in another AWS service, such as an Amazon VPC prefix list. Network Firewall IP set references enable you to dynamically update the contents of your rules. When you create, update, or delete the resource you are referencing in your rule, Network Firewall automatically updates the rule's content with the changes. For more information about IP set references in Network Firewall, see [Using IP set references](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references) in the *Network Firewall Developer Guide*.

 Network Firewall currently supports [Amazon VPC prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) and [resource groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html#rule-groups-referencing-resource-groups) in IP set references. 

## Contents
<a name="API_IPSetReference_Contents"></a>

 ** ReferenceArn **   <a name="networkfirewall-Type-IPSetReference-ReferenceArn"></a>
The Amazon Resource Name (ARN) of the resource that you are referencing in your rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

## See Also
<a name="API_IPSetReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/IPSetReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/IPSetReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/IPSetReference) 