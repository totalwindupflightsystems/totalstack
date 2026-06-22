---
id: "@specs/aws/codepipeline/docs/API_PipelineVariableDeclaration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PipelineVariableDeclaration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PipelineVariableDeclaration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PipelineVariableDeclaration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PipelineVariableDeclaration
<a name="API_PipelineVariableDeclaration"></a>

A variable declared at the pipeline level.

## Contents
<a name="API_PipelineVariableDeclaration_Contents"></a>

 ** name **   <a name="CodePipeline-Type-PipelineVariableDeclaration-name"></a>
The name of a pipeline-level variable.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9@\-_]+`   
Required: Yes

 ** defaultValue **   <a name="CodePipeline-Type-PipelineVariableDeclaration-defaultValue"></a>
The value of a pipeline-level variable.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** description **   <a name="CodePipeline-Type-PipelineVariableDeclaration-description"></a>
The description of a pipeline-level variable. It's used to add additional context about the variable, and not being used at time when pipeline executes.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Pattern: `.*`   
Required: No

## See Also
<a name="API_PipelineVariableDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineVariableDeclaration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineVariableDeclaration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineVariableDeclaration) 