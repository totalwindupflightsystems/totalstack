---
id: "@specs/aws/codepipeline/docs/API_LatestInPipelineExecutionFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LatestInPipelineExecutionFilter"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# LatestInPipelineExecutionFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_LatestInPipelineExecutionFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LatestInPipelineExecutionFilter
<a name="API_LatestInPipelineExecutionFilter"></a>

The field that specifies to filter on the latest execution in the pipeline.

**Note**  
Filtering on the latest execution is available for executions run on or after February 08, 2024.

## Contents
<a name="API_LatestInPipelineExecutionFilter_Contents"></a>

 ** pipelineExecutionId **   <a name="CodePipeline-Type-LatestInPipelineExecutionFilter-pipelineExecutionId"></a>
The execution ID for the latest execution in the pipeline.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** startTimeRange **   <a name="CodePipeline-Type-LatestInPipelineExecutionFilter-startTimeRange"></a>
The start time to filter on for the latest execution in the pipeline. Valid options:  
+ All
+ Latest
Type: String  
Valid Values: `Latest | All`   
Required: Yes

## See Also
<a name="API_LatestInPipelineExecutionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/LatestInPipelineExecutionFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/LatestInPipelineExecutionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/LatestInPipelineExecutionFilter) 