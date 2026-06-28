---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalEntity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalEntity"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalEntity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalEntity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalEntity
<a name="API_streaming_MedicalEntity"></a>

Contains entities identified as personal health information (PHI) in your transcription output, along with various associated attributes. Examples include category, confidence score, type, stability score, and start and end times.

## Contents
<a name="API_streaming_MedicalEntity_Contents"></a>

 ** Category **   <a name="transcribe-Type-streaming_MedicalEntity-Category"></a>
The category of information identified. The only category is `PHI`.  
Type: String  
Required: No

 ** Confidence **   <a name="transcribe-Type-streaming_MedicalEntity-Confidence"></a>
The confidence score associated with the identified PHI entity in your audio.  
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.  
Type: Double  
Required: No

 ** Content **   <a name="transcribe-Type-streaming_MedicalEntity-Content"></a>
The word or words identified as PHI.  
Type: String  
Required: No

 ** EndTime **   <a name="transcribe-Type-streaming_MedicalEntity-EndTime"></a>
The end time, in seconds, of the utterance that was identified as PHI.  
Type: Double  
Required: No

 ** StartTime **   <a name="transcribe-Type-streaming_MedicalEntity-StartTime"></a>
The start time, in seconds, of the utterance that was identified as PHI.  
Type: Double  
Required: No

## See Also
<a name="API_streaming_MedicalEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalEntity) 