---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeTranscriptItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeTranscriptItem"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeTranscriptItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeTranscriptItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeTranscriptItem
<a name="API_streaming_MedicalScribeTranscriptItem"></a>

A word, phrase, or punctuation mark in your transcription output, along with various associated attributes, such as confidence score, type, and start and end times. 

## Contents
<a name="API_streaming_MedicalScribeTranscriptItem_Contents"></a>

 ** BeginAudioTime **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptItem-BeginAudioTime"></a>
The start time, in milliseconds, of the transcribed item.  
Type: Double  
Required: No

 ** Confidence **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptItem-Confidence"></a>
The confidence score associated with a word or phrase in your transcript.  
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.   
Type: Double  
Required: No

 ** Content **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptItem-Content"></a>
The word, phrase or punctuation mark that was transcribed.  
Type: String  
Required: No

 ** EndAudioTime **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptItem-EndAudioTime"></a>
The end time, in milliseconds, of the transcribed item.  
Type: Double  
Required: No

 ** Type **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptItem-Type"></a>
The type of item identified. Options are: `PRONUNCIATION` (spoken words) and `PUNCTUATION`.   
Type: String  
Valid Values: `pronunciation | punctuation`   
Required: No

 ** VocabularyFilterMatch **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptItem-VocabularyFilterMatch"></a>
Indicates whether the specified item matches a word in the vocabulary filter included in your configuration event. If `true`, there is a vocabulary filter match.   
Type: Boolean  
Required: No

## See Also
<a name="API_streaming_MedicalScribeTranscriptItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeTranscriptItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeTranscriptItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeTranscriptItem) 