---
id: "@specs/aws/transcribe/docs/API_streaming_Entity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Entity"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Entity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_Entity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Entity
<a name="API_streaming_Entity"></a>

Contains entities identified as personally identifiable information (PII) in your transcription output, along with various associated attributes. Examples include category, confidence score, type, stability score, and start and end times.

## Contents
<a name="API_streaming_Entity_Contents"></a>

 ** Category **   <a name="transcribe-Type-streaming_Entity-Category"></a>
The category of information identified. The only category is `PII`.  
Type: String  
Required: No

 ** Confidence **   <a name="transcribe-Type-streaming_Entity-Confidence"></a>
The confidence score associated with the identified PII entity in your audio.  
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.  
Type: Double  
Required: No

 ** Content **   <a name="transcribe-Type-streaming_Entity-Content"></a>
The word or words identified as PII.  
Type: String  
Required: No

 ** EndTime **   <a name="transcribe-Type-streaming_Entity-EndTime"></a>
The end time of the utterance that was identified as PII in seconds, with millisecond precision (e.g., 1.056)  
Type: Double  
Required: No

 ** StartTime **   <a name="transcribe-Type-streaming_Entity-StartTime"></a>
The start time of the utterance that was identified as PII in seconds, with millisecond precision (e.g., 1.056)  
Type: Double  
Required: No

 ** Type **   <a name="transcribe-Type-streaming_Entity-Type"></a>
The type of PII identified. For example, `NAME` or `CREDIT_DEBIT_NUMBER`.  
Type: String  
Required: No

## See Also
<a name="API_streaming_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/Entity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/Entity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/Entity) 