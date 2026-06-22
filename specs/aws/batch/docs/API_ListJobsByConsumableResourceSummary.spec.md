---
id: "@specs/aws/batch/docs/API_ListJobsByConsumableResourceSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListJobsByConsumableResourceSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListJobsByConsumableResourceSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListJobsByConsumableResourceSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListJobsByConsumableResourceSummary
<a name="API_ListJobsByConsumableResourceSummary"></a>

Current information about a consumable resource required by a job.

## Contents
<a name="API_ListJobsByConsumableResourceSummary_Contents"></a>

 ** consumableResourceProperties **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-consumableResourceProperties"></a>
Contains a list of consumable resources required by the job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: Yes

 ** createdAt **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-createdAt"></a>
The Unix timestamp (in milliseconds) for when the consumable resource was created.  
Type: Long  
Required: Yes

 ** jobArn **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-jobArn"></a>
The Amazon Resource Name (ARN) of the job.  
Type: String  
Required: Yes

 ** jobName **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-jobName"></a>
The name of the job.  
Type: String  
Required: Yes

 ** jobQueueArn **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-jobQueueArn"></a>
The Amazon Resource Name (ARN) of the job queue.  
Type: String  
Required: Yes

 ** jobStatus **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-jobStatus"></a>
The status of the job. Can be one of:  
+  `SUBMITTED` 
+  `PENDING` 
+  `RUNNABLE` 
+  `STARTING` 
+  `RUNNING` 
+  `SUCCEEDED` 
+  `FAILED` 
Type: String  
Required: Yes

 ** quantity **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-quantity"></a>
The total amount of the consumable resource that is available.  
Type: Long  
Required: Yes

 ** jobDefinitionArn **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-jobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the job definition.  
Type: String  
Required: No

 ** shareIdentifier **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-shareIdentifier"></a>
The fair-share scheduling identifier for the job.  
Type: String  
Required: No

 ** startedAt **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-startedAt"></a>
The Unix timestamp for when the job was started. More specifically, it's when the job transitioned from the `STARTING` state to the `RUNNING` state.  
Type: Long  
Required: No

 ** statusReason **   <a name="Batch-Type-ListJobsByConsumableResourceSummary-statusReason"></a>
A short, human-readable string to provide more details for the current status of the job.  
Type: String  
Required: No

## See Also
<a name="API_ListJobsByConsumableResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListJobsByConsumableResourceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListJobsByConsumableResourceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListJobsByConsumableResourceSummary) 