---
id: "@specs/aws/codepipeline/docs/API_StageExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StageExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# StageExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_StageExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StageExecution
<a name="API_StageExecution"></a>

Represents information about the run of a stage.

## Contents
<a name="API_StageExecution_Contents"></a>

 ** pipelineExecutionId **   <a name="CodePipeline-Type-StageExecution-pipelineExecutionId"></a>
The ID of the pipeline execution associated with the stage.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** status **   <a name="CodePipeline-Type-StageExecution-status"></a>
The status of the stage, or for a completed stage, the last status of the stage.  
A status of cancelled means that the pipeline’s definition was updated before the stage execution could be completed.
Type: String  
Valid Values: `Cancelled | InProgress | Failed | Stopped | Stopping | Succeeded | Skipped`   
Required: Yes

 ** type **   <a name="CodePipeline-Type-StageExecution-type"></a>
The type of pipeline execution for the stage, such as a rollback pipeline execution.  
Type: String  
Valid Values: `STANDARD | ROLLBACK`   
Required: No

## See Also
<a name="API_StageExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageExecution) 