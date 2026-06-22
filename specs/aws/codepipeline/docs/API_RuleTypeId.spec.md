---
id: "@specs/aws/codepipeline/docs/API_RuleTypeId"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleTypeId"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleTypeId

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleTypeId
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleTypeId
<a name="API_RuleTypeId"></a>

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html). For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Contents
<a name="API_RuleTypeId_Contents"></a>

 ** category **   <a name="CodePipeline-Type-RuleTypeId-category"></a>
A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule`.   
Type: String  
Valid Values: `Rule`   
Required: Yes

 ** provider **   <a name="CodePipeline-Type-RuleTypeId-provider"></a>
The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

 ** owner **   <a name="CodePipeline-Type-RuleTypeId-owner"></a>
The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS`.   
Type: String  
Valid Values: `AWS`   
Required: No

 ** version **   <a name="CodePipeline-Type-RuleTypeId-version"></a>
A string that describes the rule version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `[0-9A-Za-z_-]+`   
Required: No

## See Also
<a name="API_RuleTypeId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleTypeId) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleTypeId) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleTypeId) 