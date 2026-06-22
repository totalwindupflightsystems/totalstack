---
id: "@specs/aws/codepipeline/docs/API_GitBranchFilterCriteria"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GitBranchFilterCriteria"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GitBranchFilterCriteria

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GitBranchFilterCriteria
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GitBranchFilterCriteria
<a name="API_GitBranchFilterCriteria"></a>

The Git repository branches specified as filter criteria to start the pipeline.

## Contents
<a name="API_GitBranchFilterCriteria_Contents"></a>

 ** excludes **   <a name="CodePipeline-Type-GitBranchFilterCriteria-excludes"></a>
The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 8 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `.*`   
Required: No

 ** includes **   <a name="CodePipeline-Type-GitBranchFilterCriteria-includes"></a>
The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 8 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `.*`   
Required: No

## See Also
<a name="API_GitBranchFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitBranchFilterCriteria) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitBranchFilterCriteria) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitBranchFilterCriteria) 