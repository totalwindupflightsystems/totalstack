---
id: "@specs/aws/batch/docs/API_JobDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobDetail
<a name="API_JobDetail"></a>

An object that represents an AWS Batch job.

## Contents
<a name="API_JobDetail_Contents"></a>

 ** jobDefinition **   <a name="Batch-Type-JobDetail-jobDefinition"></a>
The Amazon Resource Name (ARN) of the job definition that this job uses.  
Type: String  
Required: Yes

 ** jobId **   <a name="Batch-Type-JobDetail-jobId"></a>
The job ID.  
Type: String  
Required: Yes

 ** jobName **   <a name="Batch-Type-JobDetail-jobName"></a>
The job name.  
Type: String  
Required: Yes

 ** jobQueue **   <a name="Batch-Type-JobDetail-jobQueue"></a>
The Amazon Resource Name (ARN) of the job queue that the job is associated with.  
Type: String  
Required: Yes

 ** startedAt **   <a name="Batch-Type-JobDetail-startedAt"></a>
The Unix timestamp (in milliseconds) for when the job was started. More specifically, it's when the job transitioned from the `STARTING` state to the `RUNNING` state.   
Type: Long  
Required: Yes

 ** status **   <a name="Batch-Type-JobDetail-status"></a>
The current status for the job.  
If your jobs don't progress to `STARTING`, see [Jobs stuck in RUNNABLE status](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#job_stuck_in_runnable) in the troubleshooting section of the * AWS Batch User Guide*.
Type: String  
Valid Values: `SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED`   
Required: Yes

 ** arrayProperties **   <a name="Batch-Type-JobDetail-arrayProperties"></a>
The array properties of the job, if it's an array job.  
Type: [ArrayPropertiesDetail](API_ArrayPropertiesDetail.md) object  
Required: No

 ** attempts **   <a name="Batch-Type-JobDetail-attempts"></a>
A list of job attempts that are associated with this job.  
Type: Array of [AttemptDetail](API_AttemptDetail.md) objects  
Required: No

 ** consumableResourceProperties **   <a name="Batch-Type-JobDetail-consumableResourceProperties"></a>
Contains a list of consumable resources required by the job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: No

 ** container **   <a name="Batch-Type-JobDetail-container"></a>
An object that represents the details for the container that's associated with the job. If the details are for a multiple-container job, this object will be empty.   
Type: [ContainerDetail](API_ContainerDetail.md) object  
Required: No

 ** createdAt **   <a name="Batch-Type-JobDetail-createdAt"></a>
The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the `SUBMITTED` state. This is specifically at the time [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) was called. For array child jobs, this is when the child job was spawned by its parent and entered the `PENDING` state.  
Type: Long  
Required: No

 ** dependsOn **   <a name="Batch-Type-JobDetail-dependsOn"></a>
A list of job IDs that this job depends on.  
Type: Array of [JobDependency](API_JobDependency.md) objects  
Required: No

 ** ecsProperties **   <a name="Batch-Type-JobDetail-ecsProperties"></a>
An object with properties that are specific to Amazon ECS-based jobs.   
Type: [EcsPropertiesDetail](API_EcsPropertiesDetail.md) object  
Required: No

 ** eksAttempts **   <a name="Batch-Type-JobDetail-eksAttempts"></a>
A list of job attempts that are associated with this job.  
Type: Array of [EksAttemptDetail](API_EksAttemptDetail.md) objects  
Required: No

 ** eksProperties **   <a name="Batch-Type-JobDetail-eksProperties"></a>
An object with various properties that are specific to Amazon EKS based jobs.   
Type: [EksPropertiesDetail](API_EksPropertiesDetail.md) object  
Required: No

 ** isCancelled **   <a name="Batch-Type-JobDetail-isCancelled"></a>
Indicates whether the job is canceled.  
Type: Boolean  
Required: No

 ** isTerminated **   <a name="Batch-Type-JobDetail-isTerminated"></a>
Indicates whether the job is terminated.  
Type: Boolean  
Required: No

 ** jobArn **   <a name="Batch-Type-JobDetail-jobArn"></a>
The Amazon Resource Name (ARN) of the job.  
Type: String  
Required: No

 ** nodeDetails **   <a name="Batch-Type-JobDetail-nodeDetails"></a>
An object that represents the details of a node that's associated with a multi-node parallel job.  
Type: [NodeDetails](API_NodeDetails.md) object  
Required: No

 ** nodeProperties **   <a name="Batch-Type-JobDetail-nodeProperties"></a>
An object that represents the node properties of a multi-node parallel job.  
This isn't applicable to jobs that are running on Fargate resources.
Type: [NodeProperties](API_NodeProperties.md) object  
Required: No

 ** parameters **   <a name="Batch-Type-JobDetail-parameters"></a>
Additional parameters that are passed to the job that replace parameter substitution placeholders or override any corresponding parameter defaults from the job definition.  
Type: String to string map  
Required: No

 ** platformCapabilities **   <a name="Batch-Type-JobDetail-platformCapabilities"></a>
The platform capabilities required by the job definition. If no value is specified, it defaults to `EC2`. Jobs run on Fargate resources specify `FARGATE`.  
Type: Array of strings  
Valid Values: `EC2 | FARGATE`   
Required: No

 ** propagateTags **   <a name="Batch-Type-JobDetail-propagateTags"></a>
Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state.  
Type: Boolean  
Required: No

 ** retryStrategy **   <a name="Batch-Type-JobDetail-retryStrategy"></a>
The retry strategy to use for this job if an attempt fails.  
Type: [RetryStrategy](API_RetryStrategy.md) object  
Required: No

 ** schedulingPriority **   <a name="Batch-Type-JobDetail-schedulingPriority"></a>
The scheduling policy of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.  
Type: Integer  
Required: No

 ** shareIdentifier **   <a name="Batch-Type-JobDetail-shareIdentifier"></a>
The share identifier for the job.  
Type: String  
Required: No

 ** statusReason **   <a name="Batch-Type-JobDetail-statusReason"></a>
A short, human-readable string to provide more details for the current status of the job.  
+  `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY` - All compute environments have insufficient capacity to service the job.
+  `MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE` - All compute environments have a `maxVcpu` setting that is smaller than the job requirements.
+  `MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT` - All compute environments have no connected instances that meet the job requirements.
+  `MISCONFIGURATION:SERVICE_ROLE_PERMISSIONS` - All compute environments have problems with the service role permissions.
Type: String  
Required: No

 ** stoppedAt **   <a name="Batch-Type-JobDetail-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the job was stopped. More specifically, it's when the job transitioned from the `RUNNING` state to a terminal state, such as `SUCCEEDED` or `FAILED`.  
Type: Long  
Required: No

 ** tags **   <a name="Batch-Type-JobDetail-tags"></a>
The tags that are applied to the job.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** timeout **   <a name="Batch-Type-JobDetail-timeout"></a>
The timeout configuration for the job.  
Type: [JobTimeout](API_JobTimeout.md) object  
Required: No

## See Also
<a name="API_JobDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobDetail) 