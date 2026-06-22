---
id: "@specs/aws/batch/docs/API_FrontOfQueueDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FrontOfQueueDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FrontOfQueueDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FrontOfQueueDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FrontOfQueueDetail
<a name="API_FrontOfQueueDetail"></a>

Contains a list of the first 100 `RUNNABLE` jobs associated to a single job queue.

## Contents
<a name="API_FrontOfQueueDetail_Contents"></a>

 ** jobs **   <a name="Batch-Type-FrontOfQueueDetail-jobs"></a>
The Amazon Resource Names (ARNs) of the first 100 `RUNNABLE` jobs in a named job queue. For first-in-first-out (FIFO) job queues, jobs are ordered based on their submission time. For fair-share scheduling (FSS) job queues, jobs are ordered based on their job priority and share usage.  
Type: Array of [FrontOfQueueJobSummary](API_FrontOfQueueJobSummary.md) objects  
Required: No

 ** lastUpdatedAt **   <a name="Batch-Type-FrontOfQueueDetail-lastUpdatedAt"></a>
The Unix timestamp (in milliseconds) for when each of the first 100 `RUNNABLE` jobs were last updated.   
Type: Long  
Required: No

## See Also
<a name="API_FrontOfQueueDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FrontOfQueueDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FrontOfQueueDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FrontOfQueueDetail) 