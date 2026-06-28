---
id: "@specs/aws/amp/docs/API_RuleGroupsNamespaceDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleGroupsNamespaceDescription"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# RuleGroupsNamespaceDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_RuleGroupsNamespaceDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleGroupsNamespaceDescription
<a name="API_RuleGroupsNamespaceDescription"></a>

The details about one rule groups namespace. 

## Contents
<a name="API_RuleGroupsNamespaceDescription_Contents"></a>

 ** arn **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-arn"></a>
The ARN of the rule groups namespace. For example, `arn:aws:aps:<region>:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1`.  
Type: String  
Required: Yes

 ** createdAt **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-createdAt"></a>
The date and time that the rule groups namespace was created.  
Type: Timestamp  
Required: Yes

 ** data **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-data"></a>
The rule groups file used in the namespace.  
For details about the rule groups namespace structure, see [RuleGroupsNamespaceData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html).  
Type: Base64-encoded binary data object  
Required: Yes

 ** modifiedAt **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-modifiedAt"></a>
The date and time that the rule groups namespace was most recently changed.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-name"></a>
The name of the rule groups namespace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

 ** status **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-status"></a>
The current status of the rule groups namespace.  
Type: [RuleGroupsNamespaceStatus](API_RuleGroupsNamespaceStatus.md) object  
Required: Yes

 ** tags **   <a name="prometheus-Type-RuleGroupsNamespaceDescription-tags"></a>
The list of tag keys and values that are associated with the rule groups namespace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## See Also
<a name="API_RuleGroupsNamespaceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/RuleGroupsNamespaceDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/RuleGroupsNamespaceDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/RuleGroupsNamespaceDescription) 