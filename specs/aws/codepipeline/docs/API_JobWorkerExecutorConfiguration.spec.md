---
id: "@specs/aws/codepipeline/docs/API_JobWorkerExecutorConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobWorkerExecutorConfiguration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# JobWorkerExecutorConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_JobWorkerExecutorConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobWorkerExecutorConfiguration
<a name="API_JobWorkerExecutorConfiguration"></a>

Details about the polling configuration for the `JobWorker` action engine, or executor.

## Contents
<a name="API_JobWorkerExecutorConfiguration_Contents"></a>

 ** pollingAccounts **   <a name="CodePipeline-Type-JobWorkerExecutorConfiguration-pollingAccounts"></a>
The accounts in which the job worker is configured and might poll for jobs as part of the action execution.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Pattern: `[0-9]{12}`   
Required: No

 ** pollingServicePrincipals **   <a name="CodePipeline-Type-JobWorkerExecutorConfiguration-pollingServicePrincipals"></a>
The service Principals in which the job worker is configured and might poll for jobs as part of the action execution.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

## See Also
<a name="API_JobWorkerExecutorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/JobWorkerExecutorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/JobWorkerExecutorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/JobWorkerExecutorConfiguration) 