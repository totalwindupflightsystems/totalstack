---
id: "@specs/aws/codepipeline/docs/API_ExecutorConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExecutorConfiguration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ExecutorConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ExecutorConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExecutorConfiguration
<a name="API_ExecutorConfiguration"></a>

The action engine, or executor, related to the supported integration model used to create and update the action type. The available executor types are `Lambda` and `JobWorker`.

## Contents
<a name="API_ExecutorConfiguration_Contents"></a>

 ** jobWorkerExecutorConfiguration **   <a name="CodePipeline-Type-ExecutorConfiguration-jobWorkerExecutorConfiguration"></a>
Details about the `JobWorker` executor of the action type.  
Type: [JobWorkerExecutorConfiguration](API_JobWorkerExecutorConfiguration.md) object  
Required: No

 ** lambdaExecutorConfiguration **   <a name="CodePipeline-Type-ExecutorConfiguration-lambdaExecutorConfiguration"></a>
Details about the `Lambda` executor of the action type.  
Type: [LambdaExecutorConfiguration](API_LambdaExecutorConfiguration.md) object  
Required: No

## See Also
<a name="API_ExecutorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ExecutorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ExecutorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ExecutorConfiguration) 