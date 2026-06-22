---
id: "@specs/aws/batch/docs/API_UpdatePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdatePolicy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdatePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdatePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdatePolicy
<a name="API_UpdatePolicy"></a>

Specifies the infrastructure update policy for the Amazon EC2 compute environment. For more information about infrastructure updates, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_UpdatePolicy_Contents"></a>

 ** jobExecutionTimeoutMinutes **   <a name="Batch-Type-UpdatePolicy-jobExecutionTimeoutMinutes"></a>
Specifies the job timeout (in minutes) when the compute environment infrastructure is updated. The default value is 30. The maximum value is 7200.  
Increasing `jobExecutionTimeoutMinutes` during infrastructure updates delays the replacement of instances with new instances that include updates such as security patches, but provides more time for jobs to execute. Consider the security implications of this tradeoff when setting timeout values.
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 7200.  
Required: No

 ** terminateJobsOnUpdate **   <a name="Batch-Type-UpdatePolicy-terminateJobsOnUpdate"></a>
Specifies whether jobs are automatically terminated when the compute environment infrastructure is updated. The default value is `false`.  
Type: Boolean  
Required: No

## See Also
<a name="API_UpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdatePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdatePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdatePolicy) 