---
id: "@specs/aws/batch/docs/API_ServiceJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobSummary
<a name="API_ServiceJobSummary"></a>

Summary information about a service job.

## Contents
<a name="API_ServiceJobSummary_Contents"></a>

 ** jobId **   <a name="Batch-Type-ServiceJobSummary-jobId"></a>
The job ID for the service job.  
Type: String  
Required: Yes

 ** jobName **   <a name="Batch-Type-ServiceJobSummary-jobName"></a>
The name of the service job.  
Type: String  
Required: Yes

 ** serviceJobType **   <a name="Batch-Type-ServiceJobSummary-serviceJobType"></a>
The type of service job. For SageMaker Training jobs, this value is `SAGEMAKER_TRAINING`.  
Type: String  
Valid Values: `SAGEMAKER_TRAINING`   
Required: Yes

 ** capacityUsage **   <a name="Batch-Type-ServiceJobSummary-capacityUsage"></a>
The capacity usage information for this service job, including the unit of measure and quantity of resources being used.  
Type: Array of [ServiceJobCapacityUsageSummary](API_ServiceJobCapacityUsageSummary.md) objects  
Required: No

 ** createdAt **   <a name="Batch-Type-ServiceJobSummary-createdAt"></a>
The Unix timestamp (in milliseconds) for when the service job was created.  
Type: Long  
Required: No

 ** jobArn **   <a name="Batch-Type-ServiceJobSummary-jobArn"></a>
The Amazon Resource Name (ARN) of the service job.  
Type: String  
Required: No

 ** latestAttempt **   <a name="Batch-Type-ServiceJobSummary-latestAttempt"></a>
Information about the latest attempt for the service job.  
Type: [LatestServiceJobAttempt](API_LatestServiceJobAttempt.md) object  
Required: No

 ** quotaShareName **   <a name="Batch-Type-ServiceJobSummary-quotaShareName"></a>
The quota share for the service job.  
Type: String  
Required: No

 ** scheduledAt **   <a name="Batch-Type-ServiceJobSummary-scheduledAt"></a>
The Unix timestamp (in milliseconds) for when the service job was scheduled for execution.  
Type: Long  
Required: No

 ** shareIdentifier **   <a name="Batch-Type-ServiceJobSummary-shareIdentifier"></a>
The share identifier for the job.  
Type: String  
Required: No

 ** startedAt **   <a name="Batch-Type-ServiceJobSummary-startedAt"></a>
The Unix timestamp (in milliseconds) for when the service job was started.  
Type: Long  
Required: No

 ** status **   <a name="Batch-Type-ServiceJobSummary-status"></a>
The current status of the service job.   
Type: String  
Valid Values: `SUBMITTED | PENDING | RUNNABLE | SCHEDULED | STARTING | RUNNING | SUCCEEDED | FAILED`   
Required: No

 ** statusReason **   <a name="Batch-Type-ServiceJobSummary-statusReason"></a>
A short string to provide more details on the current status of the service job.  
Type: String  
Required: No

 ** stoppedAt **   <a name="Batch-Type-ServiceJobSummary-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the service job stopped running.  
Type: Long  
Required: No

## See Also
<a name="API_ServiceJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobSummary) 