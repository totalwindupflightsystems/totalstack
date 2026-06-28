---
id: "@specs/aws/network-firewall/docs/API_CustomAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomAction"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CustomAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CustomAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomAction
<a name="API_CustomAction"></a>

An optional, non-standard action to use for stateless packet handling. You can define this in addition to the standard action that you must specify. 

You define and name the custom actions that you want to be able to use, and then you reference them by name in your actions settings. 

You can use custom actions in the following places: 
+ In a rule group's [StatelessRulesAndCustomActions](API_StatelessRulesAndCustomActions.md) specification. The custom actions are available for use by name inside the `StatelessRulesAndCustomActions` where you define them. You can use them for your stateless rule actions to specify what to do with a packet that matches the rule's match attributes. 
+ In a [FirewallPolicy](API_FirewallPolicy.md) specification, in `StatelessCustomActions`. The custom actions are available for use inside the policy where you define them. You can use them for the policy's default stateless actions settings to specify what to do with packets that don't match any of the policy's stateless rules. 

## Contents
<a name="API_CustomAction_Contents"></a>

 ** ActionDefinition **   <a name="networkfirewall-Type-CustomAction-ActionDefinition"></a>
The custom action associated with the action name.  
Type: [ActionDefinition](API_ActionDefinition.md) object  
Required: Yes

 ** ActionName **   <a name="networkfirewall-Type-CustomAction-ActionName"></a>
The descriptive name of the custom action. You can't change the name of a custom action after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9]+$`   
Required: Yes

## See Also
<a name="API_CustomAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CustomAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CustomAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CustomAction) 