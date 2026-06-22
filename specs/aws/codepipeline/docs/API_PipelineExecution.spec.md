---
id: "@specs/aws/codepipeline/docs/API_PipelineExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineExecution
<a name="API_PipelineExecution"></a>

Represents information about an execution of a pipeline.

## Contents
<a name="API_PipelineExecution_Contents"></a>

 ** artifactRevisions **   <a name="CodePipeline-Type-PipelineExecution-artifactRevisions"></a>
A list of `ArtifactRevision` objects included in a pipeline execution.  
Type: Array of [ArtifactRevision](API_ArtifactRevision.md) objects  
Required: No

 ** executionMode **   <a name="CodePipeline-Type-PipelineExecution-executionMode"></a>
The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.  
Type: String  
Valid Values: `QUEUED | SUPERSEDED | PARALLEL`   
Required: No

 ** executionType **   <a name="CodePipeline-Type-PipelineExecution-executionType"></a>
The type of the pipeline execution.  
Type: String  
Valid Values: `STANDARD | ROLLBACK`   
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-PipelineExecution-pipelineExecutionId"></a>
The ID of the pipeline execution.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

 ** pipelineName **   <a name="CodePipeline-Type-PipelineExecution-pipelineName"></a>
The name of the pipeline with the specified pipeline execution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** pipelineVersion **   <a name="CodePipeline-Type-PipelineExecution-pipelineVersion"></a>
The version number of the pipeline with the specified pipeline execution.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** rollbackMetadata **   <a name="CodePipeline-Type-PipelineExecution-rollbackMetadata"></a>
The metadata about the execution pertaining to stage rollback.  
Type: [PipelineRollbackMetadata](API_PipelineRollbackMetadata.md) object  
Required: No

 ** status **   <a name="CodePipeline-Type-PipelineExecution-status"></a>
The status of the pipeline execution.  
+ Cancelled: The pipeline’s definition was updated before the pipeline execution could be completed.
+ InProgress: The pipeline execution is currently running.
+ Stopped: The pipeline execution was manually stopped. For more information, see [Stopped Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped).
+ Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see [Stopped Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped).
+ Succeeded: The pipeline execution was completed successfully. 
+ Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see [Superseded Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-superseded).
+ Failed: The pipeline execution was not completed successfully.
Type: String  
Valid Values: `Cancelled | InProgress | Stopped | Stopping | Succeeded | Superseded | Failed`   
Required: No

 ** statusSummary **   <a name="CodePipeline-Type-PipelineExecution-statusSummary"></a>
A summary that contains a description of the pipeline execution status.  
Type: String  
Required: No

 ** trigger **   <a name="CodePipeline-Type-PipelineExecution-trigger"></a>
The interaction or event that started a pipeline execution.  
Type: [ExecutionTrigger](API_ExecutionTrigger.md) object  
Required: No

 ** variables **   <a name="CodePipeline-Type-PipelineExecution-variables"></a>
A list of pipeline variables used for the pipeline execution.  
Type: Array of [ResolvedPipelineVariable](API_ResolvedPipelineVariable.md) objects  
Required: No

## See Also
<a name="API_PipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineExecution) 