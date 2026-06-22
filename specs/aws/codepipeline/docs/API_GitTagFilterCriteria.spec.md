---
id: "@specs/aws/codepipeline/docs/API_GitTagFilterCriteria"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GitTagFilterCriteria"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GitTagFilterCriteria

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GitTagFilterCriteria
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GitTagFilterCriteria
<a name="API_GitTagFilterCriteria"></a>

The Git tags specified as filter criteria for whether a Git tag repository event will start the pipeline.

## Contents
<a name="API_GitTagFilterCriteria_Contents"></a>

 ** excludes **   <a name="CodePipeline-Type-GitTagFilterCriteria-excludes"></a>
The list of patterns of Git tags that, when pushed, are to be excluded from starting the pipeline.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 8 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** includes **   <a name="CodePipeline-Type-GitTagFilterCriteria-includes"></a>
The list of patterns of Git tags that, when pushed, are to be included as criteria that starts the pipeline.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 8 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_GitTagFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitTagFilterCriteria) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitTagFilterCriteria) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitTagFilterCriteria) 