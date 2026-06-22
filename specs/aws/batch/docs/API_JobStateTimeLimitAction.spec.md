---
id: "@specs/aws/batch/docs/API_JobStateTimeLimitAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobStateTimeLimitAction"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobStateTimeLimitAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobStateTimeLimitAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobStateTimeLimitAction
<a name="API_JobStateTimeLimitAction"></a>

Specifies an action that AWS Batch will take after the job has remained at the head of the queue in the specified state for longer than the specified time.

## Contents
<a name="API_JobStateTimeLimitAction_Contents"></a>

 ** action **   <a name="Batch-Type-JobStateTimeLimitAction-action"></a>
The action to take when a job is at the head of the job queue in the specified state for the specified period of time. For job queues connected to a `ECS`, `FARGATE` or `EKS` compute environment, the only supported value is `CANCEL`, which will cancel the job. For job queues connected to a `SAGEMAKER_TRAINING` service environment, the only supported value is `TERMINATE`, which will terminate the job.  
Type: String  
Valid Values: `CANCEL | TERMINATE`   
Required: Yes

 ** maxTimeSeconds **   <a name="Batch-Type-JobStateTimeLimitAction-maxTimeSeconds"></a>
The approximate amount of time, in seconds, that must pass with the job in the specified state before the action is taken. The minimum value is 600 (10 minutes) and the maximum value is 86,400 (24 hours).  
Type: Integer  
Required: Yes

 ** reason **   <a name="Batch-Type-JobStateTimeLimitAction-reason"></a>
The reason to log for the action being taken.  
Type: String  
Required: Yes

 ** state **   <a name="Batch-Type-JobStateTimeLimitAction-state"></a>
The state of the job needed to trigger the action. The only supported value is `RUNNABLE`.  
Type: String  
Valid Values: `RUNNABLE`   
Required: Yes

## See Also
<a name="API_JobStateTimeLimitAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobStateTimeLimitAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobStateTimeLimitAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobStateTimeLimitAction) 