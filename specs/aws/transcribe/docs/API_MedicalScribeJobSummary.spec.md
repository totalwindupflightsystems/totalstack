---
id: "@specs/aws/transcribe/docs/API_MedicalScribeJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeJobSummary"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalScribeJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeJobSummary
<a name="API_MedicalScribeJobSummary"></a>

Provides detailed information about a specific Medical Scribe job.

## Contents
<a name="API_MedicalScribeJobSummary_Contents"></a>

 ** CompletionTime **   <a name="transcribe-Type-MedicalScribeJobSummary-CompletionTime"></a>
The date and time the specified Medical Scribe job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** CreationTime **   <a name="transcribe-Type-MedicalScribeJobSummary-CreationTime"></a>
The date and time the specified Medical Scribe job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** FailureReason **   <a name="transcribe-Type-MedicalScribeJobSummary-FailureReason"></a>
If `MedicalScribeJobStatus` is `FAILED`, `FailureReason` contains information about why the transcription job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-MedicalScribeJobSummary-LanguageCode"></a>
The language code used to create your Medical Scribe job. US English (`en-US`) is the only supported language for Medical Scribe jobs.   
Type: String  
Valid Values: `en-US`   
Required: No

 ** MedicalScribeJobName **   <a name="transcribe-Type-MedicalScribeJobSummary-MedicalScribeJobName"></a>
The name of the Medical Scribe job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** MedicalScribeJobStatus **   <a name="transcribe-Type-MedicalScribeJobSummary-MedicalScribeJobStatus"></a>
Provides the status of the specified Medical Scribe job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `MedicalScribeOutput` If the status is `FAILED`, `FailureReason` provides details on why your Medical Scribe job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** StartTime **   <a name="transcribe-Type-MedicalScribeJobSummary-StartTime"></a>
The date and time your Medical Scribe job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

## See Also
<a name="API_MedicalScribeJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalScribeJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalScribeJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalScribeJobSummary) 