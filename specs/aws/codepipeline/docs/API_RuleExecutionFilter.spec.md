---
id: "@specs/aws/codepipeline/docs/API_RuleExecutionFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleExecutionFilter"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleExecutionFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleExecutionFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleExecutionFilter
<a name="API_RuleExecutionFilter"></a>

Filter values for the rule execution.

## Contents
<a name="API_RuleExecutionFilter_Contents"></a>

 ** latestInPipelineExecution **   <a name="CodePipeline-Type-RuleExecutionFilter-latestInPipelineExecution"></a>
The field that specifies to filter on the latest execution in the pipeline.  
Filtering on the latest execution is available for executions run on or after February 08, 2024.
Type: [LatestInPipelineExecutionFilter](API_LatestInPipelineExecutionFilter.md) object  
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-RuleExecutionFilter-pipelineExecutionId"></a>
The pipeline execution ID used to filter rule execution history.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

## See Also
<a name="API_RuleExecutionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleExecutionFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleExecutionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleExecutionFilter) 