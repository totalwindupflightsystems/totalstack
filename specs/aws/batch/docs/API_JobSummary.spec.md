---
id: "@specs/aws/batch/docs/API_JobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobSummary
<a name="API_JobSummary"></a>

An object that represents summary details of a job.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** jobId **   <a name="Batch-Type-JobSummary-jobId"></a>
The job ID.  
Type: String  
Required: Yes

 ** jobName **   <a name="Batch-Type-JobSummary-jobName"></a>
The job name.  
Type: String  
Required: Yes

 ** arrayProperties **   <a name="Batch-Type-JobSummary-arrayProperties"></a>
The array properties of the job, if it's an array job.  
Type: [ArrayPropertiesSummary](API_ArrayPropertiesSummary.md) object  
Required: No

 ** capacityUsage **   <a name="Batch-Type-JobSummary-capacityUsage"></a>
The configured capacity usage information for this job, including the unit of measure and quantity of resources.  
Type: Array of [JobCapacityUsageSummary](API_JobCapacityUsageSummary.md) objects  
Required: No

 ** container **   <a name="Batch-Type-JobSummary-container"></a>
An object that represents the details of the container that's associated with the job.  
Type: [ContainerSummary](API_ContainerSummary.md) object  
Required: No

 ** createdAt **   <a name="Batch-Type-JobSummary-createdAt"></a>
The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the `SUBMITTED` state (at the time [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) was called). For array child jobs, this is when the child job was spawned by its parent and entered the `PENDING` state.  
Type: Long  
Required: No

 ** jobArn **   <a name="Batch-Type-JobSummary-jobArn"></a>
The Amazon Resource Name (ARN) of the job.  
Type: String  
Required: No

 ** jobDefinition **   <a name="Batch-Type-JobSummary-jobDefinition"></a>
The Amazon Resource Name (ARN) of the job definition.  
Type: String  
Required: No

 ** nodeProperties **   <a name="Batch-Type-JobSummary-nodeProperties"></a>
The node properties for a single node in a job summary list.  
This isn't applicable to jobs that are running on Fargate resources.
Type: [NodePropertiesSummary](API_NodePropertiesSummary.md) object  
Required: No

 ** scheduledAt **   <a name="Batch-Type-JobSummary-scheduledAt"></a>
The Unix timestamp (in milliseconds) for when the job was scheduled for execution. For more information on job statues, see [Service job status](https://docs.aws.amazon.com/batch/latest/userguide/service-job-status.html) in the * AWS Batch User Guide*.  
Type: Long  
Required: No

 ** shareIdentifier **   <a name="Batch-Type-JobSummary-shareIdentifier"></a>
The share identifier for the fairshare scheduling queue that this job is associated with.  
Type: String  
Required: No

 ** startedAt **   <a name="Batch-Type-JobSummary-startedAt"></a>
The Unix timestamp for when the job was started. More specifically, it's when the job transitioned from the `STARTING` state to the `RUNNING` state.  
Type: Long  
Required: No

 ** status **   <a name="Batch-Type-JobSummary-status"></a>
The current status for the job.  
Type: String  
Valid Values: `SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED`   
Required: No

 ** statusReason **   <a name="Batch-Type-JobSummary-statusReason"></a>
A short, human-readable string to provide more details for the current status of the job.  
Type: String  
Required: No

 ** stoppedAt **   <a name="Batch-Type-JobSummary-stoppedAt"></a>
The Unix timestamp for when the job was stopped. More specifically, it's when the job transitioned from the `RUNNING` state to a terminal state, such as `SUCCEEDED` or `FAILED`.  
Type: Long  
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobSummary) 