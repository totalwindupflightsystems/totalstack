---
id: "@specs/aws/codepipeline/docs/API_ActionExecutionInput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionExecutionInput"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionExecutionInput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionExecutionInput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionExecutionInput
<a name="API_ActionExecutionInput"></a>

Input information used for an action execution.

## Contents
<a name="API_ActionExecutionInput_Contents"></a>

 ** actionTypeId **   <a name="CodePipeline-Type-ActionExecutionInput-actionTypeId"></a>
Represents information about an action type.  
Type: [ActionTypeId](API_ActionTypeId.md) object  
Required: No

 ** configuration **   <a name="CodePipeline-Type-ActionExecutionInput-configuration"></a>
Configuration data for an action execution.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 50.  
Value Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** inputArtifacts **   <a name="CodePipeline-Type-ActionExecutionInput-inputArtifacts"></a>
Details of input artifacts of the action that correspond to the action execution.  
Type: Array of [ArtifactDetail](API_ArtifactDetail.md) objects  
Required: No

 ** namespace **   <a name="CodePipeline-Type-ActionExecutionInput-namespace"></a>
The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9@\-_]+`   
Required: No

 ** region **   <a name="CodePipeline-Type-ActionExecutionInput-region"></a>
The AWS Region for the action, such as us-east-1.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 30.  
Required: No

 ** resolvedConfiguration **   <a name="CodePipeline-Type-ActionExecutionInput-resolvedConfiguration"></a>
Configuration data for an action execution with all variable references replaced with their real values for the execution.  
Type: String to string map  
Required: No

 ** roleArn **   <a name="CodePipeline-Type-ActionExecutionInput-roleArn"></a>
The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.   
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`   
Required: No

## See Also
<a name="API_ActionExecutionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecutionInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecutionInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecutionInput) 