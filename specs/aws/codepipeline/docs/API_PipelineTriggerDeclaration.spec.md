---
id: "@specs/aws/codepipeline/docs/API_PipelineTriggerDeclaration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineTriggerDeclaration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineTriggerDeclaration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineTriggerDeclaration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineTriggerDeclaration
<a name="API_PipelineTriggerDeclaration"></a>

Represents information about the specified trigger configuration, such as the filter criteria and the source stage for the action that contains the trigger.

**Note**  
This is only supported for the `CodeStarSourceConnection` action type.

**Note**  
When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

## Contents
<a name="API_PipelineTriggerDeclaration_Contents"></a>

 ** gitConfiguration **   <a name="CodePipeline-Type-PipelineTriggerDeclaration-gitConfiguration"></a>
Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.  
Type: [GitConfiguration](API_GitConfiguration.md) object  
Required: Yes

 ** providerType **   <a name="CodePipeline-Type-PipelineTriggerDeclaration-providerType"></a>
The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.  
Type: String  
Valid Values: `CodeStarSourceConnection`   
Required: Yes

## See Also
<a name="API_PipelineTriggerDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineTriggerDeclaration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineTriggerDeclaration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineTriggerDeclaration) 