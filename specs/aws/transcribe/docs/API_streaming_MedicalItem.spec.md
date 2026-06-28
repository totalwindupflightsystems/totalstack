---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalItem"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalItem
<a name="API_streaming_MedicalItem"></a>

A word, phrase, or punctuation mark in your transcription output, along with various associated attributes, such as confidence score, type, and start and end times.

## Contents
<a name="API_streaming_MedicalItem_Contents"></a>

 ** Confidence **   <a name="transcribe-Type-streaming_MedicalItem-Confidence"></a>
The confidence score associated with a word or phrase in your transcript.  
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.  
Type: Double  
Required: No

 ** Content **   <a name="transcribe-Type-streaming_MedicalItem-Content"></a>
The word or punctuation that was transcribed.  
Type: String  
Required: No

 ** EndTime **   <a name="transcribe-Type-streaming_MedicalItem-EndTime"></a>
The end time, in seconds, of the transcribed item.  
Type: Double  
Required: No

 ** Speaker **   <a name="transcribe-Type-streaming_MedicalItem-Speaker"></a>
If speaker partitioning is enabled, `Speaker` labels the speaker of the specified item.  
Type: String  
Required: No

 ** StartTime **   <a name="transcribe-Type-streaming_MedicalItem-StartTime"></a>
The start time, in seconds, of the transcribed item.  
Type: Double  
Required: No

 ** Type **   <a name="transcribe-Type-streaming_MedicalItem-Type"></a>
The type of item identified. Options are: `PRONUNCIATION` (spoken words) and `PUNCTUATION`.  
Type: String  
Valid Values: `pronunciation | punctuation`   
Required: No

## See Also
<a name="API_streaming_MedicalItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalItem) 