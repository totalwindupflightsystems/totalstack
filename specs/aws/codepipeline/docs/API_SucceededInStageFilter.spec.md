---
id: "@specs/aws/codepipeline/docs/API_SucceededInStageFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SucceededInStageFilter"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# SucceededInStageFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_SucceededInStageFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SucceededInStageFilter
<a name="API_SucceededInStageFilter"></a>

Filter for pipeline executions that have successfully completed the stage in the current pipeline version.

## Contents
<a name="API_SucceededInStageFilter_Contents"></a>

 ** stageName **   <a name="CodePipeline-Type-SucceededInStageFilter-stageName"></a>
The name of the stage for filtering for pipeline executions where the stage was successful in the current pipeline version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

## See Also
<a name="API_SucceededInStageFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/SucceededInStageFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/SucceededInStageFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/SucceededInStageFilter) 