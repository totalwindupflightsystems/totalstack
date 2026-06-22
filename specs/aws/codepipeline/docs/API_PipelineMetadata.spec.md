---
id: "@specs/aws/codepipeline/docs/API_PipelineMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineMetadata"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineMetadata
<a name="API_PipelineMetadata"></a>

Information about a pipeline.

## Contents
<a name="API_PipelineMetadata_Contents"></a>

 ** created **   <a name="CodePipeline-Type-PipelineMetadata-created"></a>
The date and time the pipeline was created, in timestamp format.  
Type: Timestamp  
Required: No

 ** pipelineArn **   <a name="CodePipeline-Type-PipelineMetadata-pipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.  
Type: String  
Pattern: `arn:aws(-[\w]+)*:codepipeline:.+:[0-9]{12}:.+`   
Required: No

 ** pollingDisabledAt **   <a name="CodePipeline-Type-PipelineMetadata-pollingDisabledAt"></a>
The date and time that polling for source changes (periodic checks) was stopped for the pipeline, in timestamp format.   
Pipelines that are inactive for longer than 30 days will have polling disabled for the pipeline. For more information, see [pollingDisabledAt](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#metadata.pollingDisabledAt) in the pipeline structure reference. For the steps to migrate your pipeline from polling to event-based change detection, see [Migrate polling pipelines to use event-based change detection](https://docs.aws.amazon.com/codepipeline/latest/userguide/update-change-detection.html).
You can migrate (update) a polling pipeline to use event-based change detection. For example, for a pipeline with a CodeCommit source, we recommend you migrate (update) your pipeline to use CloudWatch Events. To learn more, see [Migrate polling pipelines to use event-based change detection](https://docs.aws.amazon.com/codepipeline/latest/userguide/update-change-detection.html) in the * AWS CodePipeline User Guide*.  
Type: Timestamp  
Required: No

 ** updated **   <a name="CodePipeline-Type-PipelineMetadata-updated"></a>
The date and time the pipeline was last updated, in timestamp format.  
Type: Timestamp  
Required: No

## See Also
<a name="API_PipelineMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineMetadata) 