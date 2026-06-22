---
id: "@specs/aws/codepipeline/docs/API_GitPullRequestFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GitPullRequestFilter"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GitPullRequestFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GitPullRequestFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GitPullRequestFilter
<a name="API_GitPullRequestFilter"></a>

The event criteria for the pull request trigger configuration, such as the lists of branches or file paths to include and exclude.

The following are valid values for the events for this filter:
+ CLOSED
+ OPEN
+ UPDATED

## Contents
<a name="API_GitPullRequestFilter_Contents"></a>

 ** branches **   <a name="CodePipeline-Type-GitPullRequestFilter-branches"></a>
The field that specifies to filter on branches for the pull request trigger configuration.  
Type: [GitBranchFilterCriteria](API_GitBranchFilterCriteria.md) object  
Required: No

 ** events **   <a name="CodePipeline-Type-GitPullRequestFilter-events"></a>
The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Valid Values: `OPEN | UPDATED | CLOSED`   
Required: No

 ** filePaths **   <a name="CodePipeline-Type-GitPullRequestFilter-filePaths"></a>
The field that specifies to filter on file paths for the pull request trigger configuration.  
Type: [GitFilePathFilterCriteria](API_GitFilePathFilterCriteria.md) object  
Required: No

## See Also
<a name="API_GitPullRequestFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitPullRequestFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitPullRequestFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitPullRequestFilter) 