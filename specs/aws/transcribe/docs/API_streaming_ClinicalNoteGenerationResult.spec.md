---
id: "@specs/aws/transcribe/docs/API_streaming_ClinicalNoteGenerationResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClinicalNoteGenerationResult"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ClinicalNoteGenerationResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_ClinicalNoteGenerationResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClinicalNoteGenerationResult
<a name="API_streaming_ClinicalNoteGenerationResult"></a>

The details for clinical note generation, including status, and output locations for clinical note and aggregated transcript if the analytics completed, or failure reason if the analytics failed. 

## Contents
<a name="API_streaming_ClinicalNoteGenerationResult_Contents"></a>

 ** ClinicalNoteOutputLocation **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-ClinicalNoteOutputLocation"></a>
Holds the Amazon S3 URI for the output Clinical Note.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

 ** FailureReason **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-FailureReason"></a>
If `ClinicalNoteGenerationResult` is `FAILED`, information about why it failed.   
Type: String  
Required: No

 ** Status **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-Status"></a>
The status of the clinical note generation.  
Possible Values:  
+  `IN_PROGRESS` 
+  `FAILED` 
+  `COMPLETED` 
 After audio streaming finishes, and you send a `MedicalScribeSessionControlEvent` event (with END\_OF\_SESSION as the Type), the status is set to `IN_PROGRESS`. If the status is `COMPLETED`, the analytics completed successfully, and you can find the results at the locations specified in `ClinicalNoteOutputLocation` and `TranscriptOutputLocation`. If the status is `FAILED`, `FailureReason` provides details about the failure.   
Type: String  
Valid Values: `IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** TranscriptOutputLocation **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-TranscriptOutputLocation"></a>
Holds the Amazon S3 URI for the output Transcript.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

## See Also
<a name="API_streaming_ClinicalNoteGenerationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/ClinicalNoteGenerationResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/ClinicalNoteGenerationResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/ClinicalNoteGenerationResult) 