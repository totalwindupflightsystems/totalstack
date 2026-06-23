---
id: "@specs/aws/comprehend/docs/API_EventsDetectionJobFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventsDetectionJobFilter"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# EventsDetectionJobFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_EventsDetectionJobFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventsDetectionJobFilter
<a name="API_EventsDetectionJobFilter"></a>

**Important**  
Service availability notice: Amazon Comprehend topic modeling, event detection, and prompt safety classification features will no longer be available to new customers, effective April 30, 2026. For more information, see [Amazon Comprehend feature availability change](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-availability-change.html). 

Provides information for filtering a list of event detection jobs.

## Contents
<a name="API_EventsDetectionJobFilter_Contents"></a>

 ** JobName **   <a name="comprehend-Type-EventsDetectionJobFilter-JobName"></a>
Filters on the name of the events detection job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`   
Required: No

 ** JobStatus **   <a name="comprehend-Type-EventsDetectionJobFilter-JobStatus"></a>
Filters the list of jobs based on job status. Returns only jobs with the specified status.  
Type: String  
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED | STOP_REQUESTED | STOPPED`   
Required: No

 ** SubmitTimeAfter **   <a name="comprehend-Type-EventsDetectionJobFilter-SubmitTimeAfter"></a>
Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.  
Type: Timestamp  
Required: No

 ** SubmitTimeBefore **   <a name="comprehend-Type-EventsDetectionJobFilter-SubmitTimeBefore"></a>
Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.  
Type: Timestamp  
Required: No

## See Also
<a name="API_EventsDetectionJobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/EventsDetectionJobFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/EventsDetectionJobFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/EventsDetectionJobFilter) 