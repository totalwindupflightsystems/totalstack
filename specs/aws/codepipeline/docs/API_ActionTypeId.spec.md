---
id: "@specs/aws/codepipeline/docs/API_ActionTypeId"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeId"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeId

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeId
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeId
<a name="API_ActionTypeId"></a>

Represents information about an action type.

## Contents
<a name="API_ActionTypeId_Contents"></a>

 ** category **   <a name="CodePipeline-Type-ActionTypeId-category"></a>
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.   
+ Source
+ Build
+ Test
+ Deploy
+ Invoke
+ Approval
+ Compute
Type: String  
Valid Values: `Source | Build | Deploy | Test | Invoke | Approval | Compute`   
Required: Yes

 ** owner **   <a name="CodePipeline-Type-ActionTypeId-owner"></a>
The creator of the action being called. There are three valid values for the `Owner` field in the action category section within your pipeline structure: `AWS`, `ThirdParty`, and `Custom`. For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers).  
Type: String  
Valid Values: `AWS | ThirdParty | Custom`   
Required: Yes

 ** provider **   <a name="CodePipeline-Type-ActionTypeId-provider"></a>
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as `CodeDeploy`. For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

 ** version **   <a name="CodePipeline-Type-ActionTypeId-version"></a>
A string that describes the action version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

## See Also
<a name="API_ActionTypeId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeId) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeId) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeId) 