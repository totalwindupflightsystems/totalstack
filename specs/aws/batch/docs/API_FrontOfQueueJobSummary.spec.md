---
id: "@specs/aws/batch/docs/API_FrontOfQueueJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FrontOfQueueJobSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FrontOfQueueJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FrontOfQueueJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FrontOfQueueJobSummary
<a name="API_FrontOfQueueJobSummary"></a>

An object that represents summary details for the first 100 `RUNNABLE` jobs in a job queue.

## Contents
<a name="API_FrontOfQueueJobSummary_Contents"></a>

 ** earliestTimeAtPosition **   <a name="Batch-Type-FrontOfQueueJobSummary-earliestTimeAtPosition"></a>
The Unix timestamp (in milliseconds) for when the job transitioned to its current position in the job queue.  
Type: Long  
Required: No

 ** jobArn **   <a name="Batch-Type-FrontOfQueueJobSummary-jobArn"></a>
The ARN for a job in a named job queue.  
Type: String  
Required: No

## See Also
<a name="API_FrontOfQueueJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FrontOfQueueJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FrontOfQueueJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FrontOfQueueJobSummary) 