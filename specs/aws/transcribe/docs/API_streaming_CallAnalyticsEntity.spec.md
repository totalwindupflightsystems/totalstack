---
id: "@specs/aws/transcribe/docs/API_streaming_CallAnalyticsEntity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CallAnalyticsEntity"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CallAnalyticsEntity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_CallAnalyticsEntity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CallAnalyticsEntity
<a name="API_streaming_CallAnalyticsEntity"></a>

Contains entities identified as personally identifiable information (PII) in your transcription output, along with various associated attributes. Examples include category, confidence score, content, type, and start and end times.

## Contents
<a name="API_streaming_CallAnalyticsEntity_Contents"></a>

 ** BeginOffsetMillis **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-BeginOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the identified entity.  
Type: Long  
Required: No

 ** Category **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Category"></a>
The category of information identified. For example, `PII`.  
Type: String  
Required: No

 ** Confidence **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Confidence"></a>
The confidence score associated with the identification of an entity in your transcript.  
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.  
Type: Double  
Required: No

 ** Content **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Content"></a>
The word or words that represent the identified entity.  
Type: String  
Required: No

 ** EndOffsetMillis **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-EndOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the end of the identified entity.  
Type: Long  
Required: No

 ** Type **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Type"></a>
The type of PII identified. For example, `NAME` or `CREDIT_DEBIT_NUMBER`.  
Type: String  
Required: No

## See Also
<a name="API_streaming_CallAnalyticsEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CallAnalyticsEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CallAnalyticsEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CallAnalyticsEntity) 