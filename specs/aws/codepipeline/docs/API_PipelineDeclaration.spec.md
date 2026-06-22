---
id: "@specs/aws/codepipeline/docs/API_PipelineDeclaration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineDeclaration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineDeclaration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineDeclaration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineDeclaration
<a name="API_PipelineDeclaration"></a>

Represents the structure of actions and stages to be performed in the pipeline.

## Contents
<a name="API_PipelineDeclaration_Contents"></a>

 ** name **   <a name="CodePipeline-Type-PipelineDeclaration-name"></a>
The name of the pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** roleArn **   <a name="CodePipeline-Type-PipelineDeclaration-roleArn"></a>
The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no `actionRoleArn`, or to use to assume roles for actions with an `actionRoleArn`.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`   
Required: Yes

 ** stages **   <a name="CodePipeline-Type-PipelineDeclaration-stages"></a>
The stage in which to perform the action.  
Type: Array of [StageDeclaration](API_StageDeclaration.md) objects  
Required: Yes

 ** artifactStore **   <a name="CodePipeline-Type-PipelineDeclaration-artifactStore"></a>
Represents information about the S3 bucket where artifacts are stored for the pipeline.  
You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`.
Type: [ArtifactStore](API_ArtifactStore.md) object  
Required: No

 ** artifactStores **   <a name="CodePipeline-Type-PipelineDeclaration-artifactStores"></a>
A mapping of `artifactStore` objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.  
You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`.
Type: String to [ArtifactStore](API_ArtifactStore.md) object map  
Key Length Constraints: Minimum length of 4. Maximum length of 30.  
Required: No

 ** executionMode **   <a name="CodePipeline-Type-PipelineDeclaration-executionMode"></a>
The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.  
Type: String  
Valid Values: `QUEUED | SUPERSEDED | PARALLEL`   
Required: No

 ** pipelineType **   <a name="CodePipeline-Type-PipelineDeclaration-pipelineType"></a>
CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.  
+ V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.
+ V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.
Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.
For information about pricing for CodePipeline, see [Pricing](http://aws.amazon.com/codepipeline/pricing/).  
 For information about which type of pipeline to choose, see [What type of pipeline is right for me?](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html).  
Type: String  
Valid Values: `V1 | V2`   
Required: No

 ** triggers **   <a name="CodePipeline-Type-PipelineDeclaration-triggers"></a>
The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.  
When a trigger configuration is specified, default change detection for repository and branch commits is disabled.
Type: Array of [PipelineTriggerDeclaration](API_PipelineTriggerDeclaration.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

 ** variables **   <a name="CodePipeline-Type-PipelineDeclaration-variables"></a>
A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9@\-_]+`.  
Type: Array of [PipelineVariableDeclaration](API_PipelineVariableDeclaration.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

 ** version **   <a name="CodePipeline-Type-PipelineDeclaration-version"></a>
The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## See Also
<a name="API_PipelineDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineDeclaration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineDeclaration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineDeclaration) 