---
id: "@specs/aws/codepipeline/docs/API_PipelineVariable"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineVariable"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineVariable

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineVariable
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineVariable
<a name="API_PipelineVariable"></a>

A pipeline-level variable used for a pipeline execution.

## Contents
<a name="API_PipelineVariable_Contents"></a>

 ** name **   <a name="CodePipeline-Type-PipelineVariable-name"></a>
The name of a pipeline-level variable.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9@\-_]+`   
Required: Yes

 ** value **   <a name="CodePipeline-Type-PipelineVariable-value"></a>
The value of a pipeline-level variable.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `.*`   
Required: Yes

## See Also
<a name="API_PipelineVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineVariable) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineVariable) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineVariable) 