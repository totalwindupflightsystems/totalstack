---
id: "@specs/aws/codepipeline/docs/API_ExecutionTrigger"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExecutionTrigger"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ExecutionTrigger

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ExecutionTrigger
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExecutionTrigger
<a name="API_ExecutionTrigger"></a>

The interaction or event that started a pipeline execution.

## Contents
<a name="API_ExecutionTrigger_Contents"></a>

 ** triggerDetail **   <a name="CodePipeline-Type-ExecutionTrigger-triggerDetail"></a>
Detail related to the event that started a pipeline execution, such as the webhook ARN of the webhook that triggered the pipeline execution or the user ARN for a user-initiated `start-pipeline-execution` CLI command.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** triggerType **   <a name="CodePipeline-Type-ExecutionTrigger-triggerType"></a>
The type of change-detection method, command, or user interaction that started a pipeline execution.  
Type: String  
Valid Values: `CreatePipeline | StartPipelineExecution | PollForSourceChanges | Webhook | CloudWatchEvent | PutActionRevision | WebhookV2 | ManualRollback | AutomatedRollback`   
Required: No

## See Also
<a name="API_ExecutionTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ExecutionTrigger) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ExecutionTrigger) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ExecutionTrigger) 