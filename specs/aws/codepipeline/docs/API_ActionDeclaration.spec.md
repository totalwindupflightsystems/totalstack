---
id: "@specs/aws/codepipeline/docs/API_ActionDeclaration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionDeclaration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionDeclaration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionDeclaration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionDeclaration
<a name="API_ActionDeclaration"></a>

Represents information about an action declaration.

## Contents
<a name="API_ActionDeclaration_Contents"></a>

 ** actionTypeId **   <a name="CodePipeline-Type-ActionDeclaration-actionTypeId"></a>
Specifies the action type and the provider of the action.  
Type: [ActionTypeId](API_ActionTypeId.md) object  
Required: Yes

 ** name **   <a name="CodePipeline-Type-ActionDeclaration-name"></a>
The action declaration's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** commands **   <a name="CodePipeline-Type-ActionDeclaration-commands"></a>
The shell commands to run with your compute action in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.  
Using compute time for this action will incur separate charges in AWS CodeBuild.
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** configuration **   <a name="CodePipeline-Type-ActionDeclaration-configuration"></a>
The action's configuration. These are key-value pairs that specify input values for an action. For more information, see [Action Structure Requirements in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements). For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see [Configuration Properties Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html) in the * AWS CloudFormation User Guide*. For template snippets with examples, see [Using Parameter Override Functions with CodePipeline Pipelines](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html) in the * AWS CloudFormation User Guide*.  
The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:   
 *JSON:*   
 `"Configuration" : { Key : Value },`   
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 50.  
Value Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** environmentVariables **   <a name="CodePipeline-Type-ActionDeclaration-environmentVariables"></a>
The environment variables for the action.  
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** inputArtifacts **   <a name="CodePipeline-Type-ActionDeclaration-inputArtifacts"></a>
The name or ID of the artifact consumed by the action, such as a test or build artifact.  
Type: Array of [InputArtifact](API_InputArtifact.md) objects  
Required: No

 ** namespace **   <a name="CodePipeline-Type-ActionDeclaration-namespace"></a>
The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9@\-_]+`   
Required: No

 ** outputArtifacts **   <a name="CodePipeline-Type-ActionDeclaration-outputArtifacts"></a>
The name or ID of the result of the action declaration, such as a test or build artifact.  
Type: Array of [OutputArtifact](API_OutputArtifact.md) objects  
Required: No

 ** outputVariables **   <a name="CodePipeline-Type-ActionDeclaration-outputVariables"></a>
The list of variables that are to be exported from the compute action. This is specifically CodeBuild environment variables as used for that action.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 15 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** region **   <a name="CodePipeline-Type-ActionDeclaration-region"></a>
The action declaration's AWS Region, such as us-east-1.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 30.  
Required: No

 ** roleArn **   <a name="CodePipeline-Type-ActionDeclaration-roleArn"></a>
The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`   
Required: No

 ** runOrder **   <a name="CodePipeline-Type-ActionDeclaration-runOrder"></a>
The order in which actions are run.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 999.  
Required: No

 ** timeoutInMinutes **   <a name="CodePipeline-Type-ActionDeclaration-timeoutInMinutes"></a>
A timeout duration in minutes that can be applied against the ActionType’s default timeout value specified in [Quotas for AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html). This attribute is available only to the manual approval ActionType.  
Type: Integer  
Valid Range: Minimum value of 5. Maximum value of 86400.  
Required: No

## See Also
<a name="API_ActionDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionDeclaration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionDeclaration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionDeclaration) 