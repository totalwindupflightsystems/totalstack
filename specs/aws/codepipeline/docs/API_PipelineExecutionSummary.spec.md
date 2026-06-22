---
id: "@specs/aws/codepipeline/docs/API_PipelineExecutionSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineExecutionSummary"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineExecutionSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineExecutionSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineExecutionSummary
<a name="API_PipelineExecutionSummary"></a>

Summary information about a pipeline execution.

## Contents
<a name="API_PipelineExecutionSummary_Contents"></a>

 ** executionMode **   <a name="CodePipeline-Type-PipelineExecutionSummary-executionMode"></a>
The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.  
Type: String  
Valid Values: `QUEUED | SUPERSEDED | PARALLEL`   
Required: No

 ** executionType **   <a name="CodePipeline-Type-PipelineExecutionSummary-executionType"></a>
Type of the pipeline execution.  
Type: String  
Valid Values: `STANDARD | ROLLBACK`   
Required: No

 ** lastUpdateTime **   <a name="CodePipeline-Type-PipelineExecutionSummary-lastUpdateTime"></a>
The date and time of the last change to the pipeline execution, in timestamp format.  
Type: Timestamp  
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-PipelineExecutionSummary-pipelineExecutionId"></a>
The ID of the pipeline execution.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

 ** rollbackMetadata **   <a name="CodePipeline-Type-PipelineExecutionSummary-rollbackMetadata"></a>
The metadata for the stage execution to be rolled back.  
Type: [PipelineRollbackMetadata](API_PipelineRollbackMetadata.md) object  
Required: No

 ** sourceRevisions **   <a name="CodePipeline-Type-PipelineExecutionSummary-sourceRevisions"></a>
A list of the source artifact revisions that initiated a pipeline execution.  
Type: Array of [SourceRevision](API_SourceRevision.md) objects  
Required: No

 ** startTime **   <a name="CodePipeline-Type-PipelineExecutionSummary-startTime"></a>
The date and time when the pipeline execution began, in timestamp format.  
Type: Timestamp  
Required: No

 ** status **   <a name="CodePipeline-Type-PipelineExecutionSummary-status"></a>
The status of the pipeline execution.  
+ InProgress: The pipeline execution is currently running.
+ Stopped: The pipeline execution was manually stopped. For more information, see [Stopped Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped).
+ Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see [Stopped Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped).
+ Succeeded: The pipeline execution was completed successfully. 
+ Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see [Superseded Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-superseded).
+ Failed: The pipeline execution was not completed successfully.
Type: String  
Valid Values: `Cancelled | InProgress | Stopped | Stopping | Succeeded | Superseded | Failed`   
Required: No

 ** statusSummary **   <a name="CodePipeline-Type-PipelineExecutionSummary-statusSummary"></a>
Status summary for the pipeline.  
Type: String  
Required: No

 ** stopTrigger **   <a name="CodePipeline-Type-PipelineExecutionSummary-stopTrigger"></a>
The interaction that stopped a pipeline execution.  
Type: [StopExecutionTrigger](API_StopExecutionTrigger.md) object  
Required: No

 ** trigger **   <a name="CodePipeline-Type-PipelineExecutionSummary-trigger"></a>
The interaction or event that started a pipeline execution, such as automated change detection or a `StartPipelineExecution` API call.  
Type: [ExecutionTrigger](API_ExecutionTrigger.md) object  
Required: No

## See Also
<a name="API_PipelineExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineExecutionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineExecutionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineExecutionSummary) 