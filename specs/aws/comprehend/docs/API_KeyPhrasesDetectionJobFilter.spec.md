---
id: "@specs/aws/comprehend/docs/API_KeyPhrasesDetectionJobFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KeyPhrasesDetectionJobFilter"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# KeyPhrasesDetectionJobFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_KeyPhrasesDetectionJobFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KeyPhrasesDetectionJobFilter
<a name="API_KeyPhrasesDetectionJobFilter"></a>

Provides information for filtering a list of dominant language detection jobs. For more information, see the [ListKeyPhrasesDetectionJobs](API_ListKeyPhrasesDetectionJobs.md) operation.

## Contents
<a name="API_KeyPhrasesDetectionJobFilter_Contents"></a>

 ** JobName **   <a name="comprehend-Type-KeyPhrasesDetectionJobFilter-JobName"></a>
Filters on the name of the job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`   
Required: No

 ** JobStatus **   <a name="comprehend-Type-KeyPhrasesDetectionJobFilter-JobStatus"></a>
Filters the list of jobs based on job status. Returns only jobs with the specified status.  
Type: String  
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED | STOP_REQUESTED | STOPPED`   
Required: No

 ** SubmitTimeAfter **   <a name="comprehend-Type-KeyPhrasesDetectionJobFilter-SubmitTimeAfter"></a>
Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.  
Type: Timestamp  
Required: No

 ** SubmitTimeBefore **   <a name="comprehend-Type-KeyPhrasesDetectionJobFilter-SubmitTimeBefore"></a>
Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.  
Type: Timestamp  
Required: No

## See Also
<a name="API_KeyPhrasesDetectionJobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/KeyPhrasesDetectionJobFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/KeyPhrasesDetectionJobFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/KeyPhrasesDetectionJobFilter) 