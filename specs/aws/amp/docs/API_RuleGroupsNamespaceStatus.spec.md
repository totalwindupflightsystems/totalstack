---
id: "@specs/aws/amp/docs/API_RuleGroupsNamespaceStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleGroupsNamespaceStatus"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# RuleGroupsNamespaceStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_RuleGroupsNamespaceStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleGroupsNamespaceStatus
<a name="API_RuleGroupsNamespaceStatus"></a>

The status information about a rule groups namespace. 

## Contents
<a name="API_RuleGroupsNamespaceStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-RuleGroupsNamespaceStatus-statusCode"></a>
The current status of the namespace.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATION_FAILED | UPDATE_FAILED`   
Required: Yes

 ** statusReason **   <a name="prometheus-Type-RuleGroupsNamespaceStatus-statusReason"></a>
The reason for the failure, if any.  
Type: String  
Required: No

## See Also
<a name="API_RuleGroupsNamespaceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/RuleGroupsNamespaceStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/RuleGroupsNamespaceStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/RuleGroupsNamespaceStatus) 