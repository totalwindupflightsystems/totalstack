---
id: "@specs/aws/codepipeline/docs/API_GitConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GitConfiguration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GitConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GitConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GitConfiguration
<a name="API_GitConfiguration"></a>

A type of trigger configuration for Git-based source actions.

**Note**  
You can specify the Git configuration trigger type for all third-party Git-based source actions that are supported by the `CodeStarSourceConnection` action type.

## Contents
<a name="API_GitConfiguration_Contents"></a>

 ** sourceActionName **   <a name="CodePipeline-Type-GitConfiguration-sourceActionName"></a>
The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only.  
You can only specify one trigger configuration per source action.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** pullRequest **   <a name="CodePipeline-Type-GitConfiguration-pullRequest"></a>
The field where the repository event that will start the pipeline is specified as pull requests.  
Type: Array of [GitPullRequestFilter](API_GitPullRequestFilter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Required: No

 ** push **   <a name="CodePipeline-Type-GitConfiguration-push"></a>
The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details.  
Type: Array of [GitPushFilter](API_GitPushFilter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Required: No

## See Also
<a name="API_GitConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitConfiguration) 