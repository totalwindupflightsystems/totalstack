---
id: "@specs/aws/sesv2/docs/API_ImportJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImportJobSummary"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ImportJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ImportJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImportJobSummary
<a name="API_ImportJobSummary"></a>

A summary of the import job.

## Contents
<a name="API_ImportJobSummary_Contents"></a>

 ** CreatedTimestamp **   <a name="SES-Type-ImportJobSummary-CreatedTimestamp"></a>
The date and time when the import job was created.  
Type: Timestamp  
Required: No

 ** FailedRecordsCount **   <a name="SES-Type-ImportJobSummary-FailedRecordsCount"></a>
The number of records that failed processing because of invalid input or other reasons.  
Type: Integer  
Required: No

 ** ImportDestination **   <a name="SES-Type-ImportJobSummary-ImportDestination"></a>
An object that contains details about the resource destination the import job is going to target.  
Type: [ImportDestination](API_ImportDestination.md) object  
Required: No

 ** JobId **   <a name="SES-Type-ImportJobSummary-JobId"></a>
A string that represents a job ID.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** JobStatus **   <a name="SES-Type-ImportJobSummary-JobStatus"></a>
The status of a job.  
+  `CREATED` – Job has just been created.
+  `PROCESSING` – Job is processing.
+  `ERROR` – An error occurred during processing.
+  `COMPLETED` – Job has completed processing successfully.
Type: String  
Valid Values: `CREATED | PROCESSING | COMPLETED | FAILED | CANCELLED`   
Required: No

 ** ProcessedRecordsCount **   <a name="SES-Type-ImportJobSummary-ProcessedRecordsCount"></a>
The current number of records processed.  
Type: Integer  
Required: No

## See Also
<a name="API_ImportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ImportJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ImportJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ImportJobSummary) 