---
id: "@specs/aws/transcribe/docs/API_streaming_CallAnalyticsItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CallAnalyticsItem"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CallAnalyticsItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_CallAnalyticsItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CallAnalyticsItem
<a name="API_streaming_CallAnalyticsItem"></a>

A word, phrase, or punctuation mark in your Call Analytics transcription output, along with various associated attributes, such as confidence score, type, and start and end times.

## Contents
<a name="API_streaming_CallAnalyticsItem_Contents"></a>

 ** BeginOffsetMillis **   <a name="transcribe-Type-streaming_CallAnalyticsItem-BeginOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the identified item.  
Type: Long  
Required: No

 ** Confidence **   <a name="transcribe-Type-streaming_CallAnalyticsItem-Confidence"></a>
The confidence score associated with a word or phrase in your transcript.  
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.  
Type: Double  
Required: No

 ** Content **   <a name="transcribe-Type-streaming_CallAnalyticsItem-Content"></a>
The word or punctuation that was transcribed.  
Type: String  
Required: No

 ** EndOffsetMillis **   <a name="transcribe-Type-streaming_CallAnalyticsItem-EndOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the end of the identified item.  
Type: Long  
Required: No

 ** Stable **   <a name="transcribe-Type-streaming_CallAnalyticsItem-Stable"></a>
If partial result stabilization is enabled, `Stable` indicates whether the specified item is stable (`true`) or if it may change when the segment is complete (`false`).  
Type: Boolean  
Required: No

 ** Type **   <a name="transcribe-Type-streaming_CallAnalyticsItem-Type"></a>
The type of item identified. Options are: `PRONUNCIATION` (spoken words) and `PUNCTUATION`.  
Type: String  
Valid Values: `pronunciation | punctuation`   
Required: No

 ** VocabularyFilterMatch **   <a name="transcribe-Type-streaming_CallAnalyticsItem-VocabularyFilterMatch"></a>
Indicates whether the specified item matches a word in the vocabulary filter included in your Call Analytics request. If `true`, there is a vocabulary filter match.  
Type: Boolean  
Required: No

## See Also
<a name="API_streaming_CallAnalyticsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CallAnalyticsItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CallAnalyticsItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CallAnalyticsItem) 