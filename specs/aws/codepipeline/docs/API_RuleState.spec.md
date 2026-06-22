---
id: "@specs/aws/codepipeline/docs/API_RuleState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleState
<a name="API_RuleState"></a>

Returns information about the state of a rule.

**Note**  
Values returned in the `revisionId` field indicate the rule revision information, such as the commit ID, for the current state.

## Contents
<a name="API_RuleState_Contents"></a>

 ** currentRevision **   <a name="CodePipeline-Type-RuleState-currentRevision"></a>
The ID of the current revision of the artifact successfully worked on by the job.  
Type: [RuleRevision](API_RuleRevision.md) object  
Required: No

 ** entityUrl **   <a name="CodePipeline-Type-RuleState-entityUrl"></a>
A URL link for more information about the state of the action, such as a details page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** latestExecution **   <a name="CodePipeline-Type-RuleState-latestExecution"></a>
Represents information about the latest run of an rule.  
Type: [RuleExecution](API_RuleExecution.md) object  
Required: No

 ** revisionUrl **   <a name="CodePipeline-Type-RuleState-revisionUrl"></a>
A URL link for more information about the revision, such as a commit details page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** ruleName **   <a name="CodePipeline-Type-RuleState-ruleName"></a>
The name of the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

## See Also
<a name="API_RuleState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleState) 