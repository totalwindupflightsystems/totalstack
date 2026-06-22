---
id: "@specs/aws/codepipeline/docs/API_ActionContext"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionContext"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionContext

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionContext
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionContext
<a name="API_ActionContext"></a>

Represents the context of an action in the stage of a pipeline to a job worker.

## Contents
<a name="API_ActionContext_Contents"></a>

 ** actionExecutionId **   <a name="CodePipeline-Type-ActionContext-actionExecutionId"></a>
The system-generated unique ID that corresponds to an action's execution.  
Type: String  
Required: No

 ** name **   <a name="CodePipeline-Type-ActionContext-name"></a>
The name of the action in the context of a job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

## See Also
<a name="API_ActionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionContext) 