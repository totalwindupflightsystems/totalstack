---
id: "@specs/aws/codepipeline/docs/API_ActionTypeExecutor"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeExecutor"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeExecutor

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeExecutor
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeExecutor
<a name="API_ActionTypeExecutor"></a>

The action engine, or executor, for an action type created for a provider, where the action is to be used by customers of the provider. The action engine is associated with the model used to create and update the action, such as the Lambda integration model.

## Contents
<a name="API_ActionTypeExecutor_Contents"></a>

 ** configuration **   <a name="CodePipeline-Type-ActionTypeExecutor-configuration"></a>
The action configuration properties for the action type. These properties are specified in the action definition when the action type is created.  
Type: [ExecutorConfiguration](API_ExecutorConfiguration.md) object  
Required: Yes

 ** type **   <a name="CodePipeline-Type-ActionTypeExecutor-type"></a>
The integration model used to create and update the action type, `Lambda` or `JobWorker`.   
Type: String  
Valid Values: `JobWorker | Lambda`   
Required: Yes

 ** jobTimeout **   <a name="CodePipeline-Type-ActionTypeExecutor-jobTimeout"></a>
The timeout in seconds for the job. An action execution can have multiple jobs. This is the timeout for a single job, not the entire action execution.  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 43200.  
Required: No

 ** policyStatementsTemplate **   <a name="CodePipeline-Type-ActionTypeExecutor-policyStatementsTemplate"></a>
The policy statement that specifies the permissions in the CodePipeline customer account that are needed to successfully run an action.  
To grant permission to another account, specify the account ID as the Principal, a domain-style identifier defined by the service, for example `codepipeline.amazonaws.com`.  
The size of the passed JSON policy document cannot exceed 2048 characters.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_ActionTypeExecutor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeExecutor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeExecutor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeExecutor) 