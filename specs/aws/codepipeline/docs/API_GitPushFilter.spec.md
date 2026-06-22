---
id: "@specs/aws/codepipeline/docs/API_GitPushFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GitPushFilter"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GitPushFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GitPushFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GitPushFilter
<a name="API_GitPushFilter"></a>

The event criteria that specify when a specified repository event will start the pipeline for the specified trigger configuration, such as the lists of Git tags to include and exclude.

## Contents
<a name="API_GitPushFilter_Contents"></a>

 ** branches **   <a name="CodePipeline-Type-GitPushFilter-branches"></a>
The field that specifies to filter on branches for the push trigger configuration.  
Type: [GitBranchFilterCriteria](API_GitBranchFilterCriteria.md) object  
Required: No

 ** filePaths **   <a name="CodePipeline-Type-GitPushFilter-filePaths"></a>
The field that specifies to filter on file paths for the push trigger configuration.  
Type: [GitFilePathFilterCriteria](API_GitFilePathFilterCriteria.md) object  
Required: No

 ** tags **   <a name="CodePipeline-Type-GitPushFilter-tags"></a>
The field that contains the details for the Git tags trigger configuration.  
Type: [GitTagFilterCriteria](API_GitTagFilterCriteria.md) object  
Required: No

## See Also
<a name="API_GitPushFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitPushFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitPushFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitPushFilter) 