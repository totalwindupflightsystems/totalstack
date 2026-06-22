---
id: "@specs/aws/codepipeline/docs/API_ActionState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionState
<a name="API_ActionState"></a>

Represents information about the state of an action.

## Contents
<a name="API_ActionState_Contents"></a>

 ** actionName **   <a name="CodePipeline-Type-ActionState-actionName"></a>
The name of the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** currentRevision **   <a name="CodePipeline-Type-ActionState-currentRevision"></a>
Represents information about the version (or revision) of an action.  
Type: [ActionRevision](API_ActionRevision.md) object  
Required: No

 ** entityUrl **   <a name="CodePipeline-Type-ActionState-entityUrl"></a>
A URL link for more information about the state of the action, such as a deployment group details page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** latestExecution **   <a name="CodePipeline-Type-ActionState-latestExecution"></a>
Represents information about the run of an action.  
Type: [ActionExecution](API_ActionExecution.md) object  
Required: No

 ** revisionUrl **   <a name="CodePipeline-Type-ActionState-revisionUrl"></a>
A URL link for more information about the revision, such as a commit details page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_ActionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionState) 