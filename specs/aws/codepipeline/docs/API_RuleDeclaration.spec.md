---
id: "@specs/aws/codepipeline/docs/API_RuleDeclaration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleDeclaration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleDeclaration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleDeclaration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleDeclaration
<a name="API_RuleDeclaration"></a>

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html). For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Contents
<a name="API_RuleDeclaration_Contents"></a>

 ** name **   <a name="CodePipeline-Type-RuleDeclaration-name"></a>
The name of the rule that is created for the condition, such as `VariableCheck`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** ruleTypeId **   <a name="CodePipeline-Type-RuleDeclaration-ruleTypeId"></a>
The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.  
Type: [RuleTypeId](API_RuleTypeId.md) object  
Required: Yes

 ** commands **   <a name="CodePipeline-Type-RuleDeclaration-commands"></a>
The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.  
Using compute time for this action will incur separate charges in AWS CodeBuild.
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** configuration **   <a name="CodePipeline-Type-RuleDeclaration-configuration"></a>
The action configuration fields for the rule.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 50.  
Value Length Constraints: Minimum length of 1. Maximum length of 10000.  
Required: No

 ** inputArtifacts **   <a name="CodePipeline-Type-RuleDeclaration-inputArtifacts"></a>
The input artifacts fields for the rule, such as specifying an input file for the rule.  
Type: Array of [InputArtifact](API_InputArtifact.md) objects  
Required: No

 ** region **   <a name="CodePipeline-Type-RuleDeclaration-region"></a>
The Region for the condition associated with the rule.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 30.  
Required: No

 ** roleArn **   <a name="CodePipeline-Type-RuleDeclaration-roleArn"></a>
The pipeline role ARN associated with the rule.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`   
Required: No

 ** timeoutInMinutes **   <a name="CodePipeline-Type-RuleDeclaration-timeoutInMinutes"></a>
The action timeout for the rule.  
Type: Integer  
Valid Range: Minimum value of 5. Maximum value of 86400.  
Required: No

## See Also
<a name="API_RuleDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleDeclaration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleDeclaration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleDeclaration) 