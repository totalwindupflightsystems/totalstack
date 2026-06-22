---
id: "@specs/aws/codepipeline/docs/API_PipelineRollbackMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineRollbackMetadata"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineRollbackMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineRollbackMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineRollbackMetadata
<a name="API_PipelineRollbackMetadata"></a>

The metadata for the stage execution to be rolled back.

## Contents
<a name="API_PipelineRollbackMetadata_Contents"></a>

 ** rollbackTargetPipelineExecutionId **   <a name="CodePipeline-Type-PipelineRollbackMetadata-rollbackTargetPipelineExecutionId"></a>
The pipeline execution ID to which the stage will be rolled back.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

## See Also
<a name="API_PipelineRollbackMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineRollbackMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineRollbackMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineRollbackMetadata) 