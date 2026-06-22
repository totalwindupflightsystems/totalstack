---
id: "@specs/aws/codepipeline/docs/API_Condition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Condition"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# Condition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_Condition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Condition
<a name="API_Condition"></a>

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).. For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Contents
<a name="API_Condition_Contents"></a>

 ** result **   <a name="CodePipeline-Type-Condition-result"></a>
The action to be done when the condition is met. For example, rolling back an execution for a failure condition.  
Type: String  
Valid Values: `ROLLBACK | FAIL | RETRY | SKIP`   
Required: No

 ** rules **   <a name="CodePipeline-Type-Condition-rules"></a>
The rules that make up the condition.  
Type: Array of [RuleDeclaration](API_RuleDeclaration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/Condition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/Condition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/Condition) 