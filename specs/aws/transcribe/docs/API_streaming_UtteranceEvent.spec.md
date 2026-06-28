---
id: "@specs/aws/transcribe/docs/API_streaming_UtteranceEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UtteranceEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# UtteranceEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_UtteranceEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UtteranceEvent
<a name="API_streaming_UtteranceEvent"></a>

Contains set of transcription results from one or more audio segments, along with additional information about the parameters included in your request. For example, channel definitions, partial result stabilization, sentiment, and issue detection.

## Contents
<a name="API_streaming_UtteranceEvent_Contents"></a>

 ** BeginOffsetMillis **   <a name="transcribe-Type-streaming_UtteranceEvent-BeginOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the `UtteranceEvent`.  
Type: Long  
Required: No

 ** EndOffsetMillis **   <a name="transcribe-Type-streaming_UtteranceEvent-EndOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the `UtteranceEvent`.  
Type: Long  
Required: No

 ** Entities **   <a name="transcribe-Type-streaming_UtteranceEvent-Entities"></a>
Contains entities identified as personally identifiable information (PII) in your transcription output.  
Type: Array of [CallAnalyticsEntity](API_streaming_CallAnalyticsEntity.md) objects  
Required: No

 ** IsPartial **   <a name="transcribe-Type-streaming_UtteranceEvent-IsPartial"></a>
Indicates whether the segment in the `UtteranceEvent` is complete (`FALSE`) or partial (`TRUE`).  
Type: Boolean  
Required: No

 ** IssuesDetected **   <a name="transcribe-Type-streaming_UtteranceEvent-IssuesDetected"></a>
Provides the issue that was detected in the specified segment.  
Type: Array of [IssueDetected](API_streaming_IssueDetected.md) objects  
Required: No

 ** Items **   <a name="transcribe-Type-streaming_UtteranceEvent-Items"></a>
Contains words, phrases, or punctuation marks that are associated with the specified `UtteranceEvent`.  
Type: Array of [CallAnalyticsItem](API_streaming_CallAnalyticsItem.md) objects  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-streaming_UtteranceEvent-LanguageCode"></a>
The language code that represents the language spoken in your audio stream.  
Type: String  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR`   
Required: No

 ** LanguageIdentification **   <a name="transcribe-Type-streaming_UtteranceEvent-LanguageIdentification"></a>
The language code of the dominant language identified in your stream.  
Type: Array of [CallAnalyticsLanguageWithScore](API_streaming_CallAnalyticsLanguageWithScore.md) objects  
Required: No

 ** ParticipantRole **   <a name="transcribe-Type-streaming_UtteranceEvent-ParticipantRole"></a>
Provides the role of the speaker for each audio channel, either `CUSTOMER` or `AGENT`.  
Type: String  
Valid Values: `AGENT | CUSTOMER`   
Required: No

 ** Sentiment **   <a name="transcribe-Type-streaming_UtteranceEvent-Sentiment"></a>
Provides the sentiment that was detected in the specified segment.  
Type: String  
Valid Values: `POSITIVE | NEGATIVE | MIXED | NEUTRAL`   
Required: No

 ** Transcript **   <a name="transcribe-Type-streaming_UtteranceEvent-Transcript"></a>
Contains transcribed text.  
Type: String  
Required: No

 ** UtteranceId **   <a name="transcribe-Type-streaming_UtteranceEvent-UtteranceId"></a>
The unique identifier that is associated with the specified `UtteranceEvent`.  
Type: String  
Required: No

## See Also
<a name="API_streaming_UtteranceEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/UtteranceEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/UtteranceEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/UtteranceEvent) 