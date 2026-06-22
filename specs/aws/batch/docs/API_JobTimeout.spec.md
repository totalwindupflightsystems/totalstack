---
id: "@specs/aws/batch/docs/API_JobTimeout"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobTimeout"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobTimeout

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobTimeout
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobTimeout
<a name="API_JobTimeout"></a>

An object that represents a job timeout configuration.

## Contents
<a name="API_JobTimeout_Contents"></a>

 ** attemptDurationSeconds **   <a name="Batch-Type-JobTimeout-attemptDurationSeconds"></a>
The job timeout time (in seconds) that's measured from the job attempt's `startedAt` timestamp. After this time passes, AWS Batch terminates your jobs if they aren't finished. The minimum value for the timeout is 60 seconds.  
For array jobs, the timeout applies to the child jobs, not to the parent array job.  
For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.  
Type: Integer  
Required: No

## See Also
<a name="API_JobTimeout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobTimeout) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobTimeout) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobTimeout) 