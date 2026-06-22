---
id: "@specs/aws/codepipeline/docs/API_RuleType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleType"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleType
<a name="API_RuleType"></a>

The rule type, which is made up of the combined values for category, owner, provider, and version.

## Contents
<a name="API_RuleType_Contents"></a>

 ** id **   <a name="CodePipeline-Type-RuleType-id"></a>
Represents information about a rule type.  
Type: [RuleTypeId](API_RuleTypeId.md) object  
Required: Yes

 ** inputArtifactDetails **   <a name="CodePipeline-Type-RuleType-inputArtifactDetails"></a>
Returns information about the details of an artifact.  
Type: [ArtifactDetails](API_ArtifactDetails.md) object  
Required: Yes

 ** ruleConfigurationProperties **   <a name="CodePipeline-Type-RuleType-ruleConfigurationProperties"></a>
The configuration properties for the rule type.  
Type: Array of [RuleConfigurationProperty](API_RuleConfigurationProperty.md) objects  
Array Members: Maximum number of 10 items.  
Required: No

 ** settings **   <a name="CodePipeline-Type-RuleType-settings"></a>
Returns information about the settings for a rule type.  
Type: [RuleTypeSettings](API_RuleTypeSettings.md) object  
Required: No

## See Also
<a name="API_RuleType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleType) 