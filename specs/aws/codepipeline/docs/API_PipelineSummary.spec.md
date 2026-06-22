---
id: "@specs/aws/codepipeline/docs/API_PipelineSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineSummary"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineSummary
<a name="API_PipelineSummary"></a>

Returns a summary of a pipeline.

## Contents
<a name="API_PipelineSummary_Contents"></a>

 ** created **   <a name="CodePipeline-Type-PipelineSummary-created"></a>
The date and time the pipeline was created, in timestamp format.  
Type: Timestamp  
Required: No

 ** executionMode **   <a name="CodePipeline-Type-PipelineSummary-executionMode"></a>
The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.  
Type: String  
Valid Values: `QUEUED | SUPERSEDED | PARALLEL`   
Required: No

 ** name **   <a name="CodePipeline-Type-PipelineSummary-name"></a>
The name of the pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** pipelineType **   <a name="CodePipeline-Type-PipelineSummary-pipelineType"></a>
CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.  
+ V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.
+ V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.
Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.
For information about pricing for CodePipeline, see [Pricing](http://aws.amazon.com/codepipeline/pricing/).  
 For information about which type of pipeline to choose, see [What type of pipeline is right for me?](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html).  
Type: String  
Valid Values: `V1 | V2`   
Required: No

 ** updated **   <a name="CodePipeline-Type-PipelineSummary-updated"></a>
The date and time of the last update to the pipeline, in timestamp format.  
Type: Timestamp  
Required: No

 ** version **   <a name="CodePipeline-Type-PipelineSummary-version"></a>
The version number of the pipeline.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## See Also
<a name="API_PipelineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineSummary) 