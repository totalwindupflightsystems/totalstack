---
id: "@specs/aws/transcribe/docs/API_streaming_CallAnalyticsTranscriptResultStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CallAnalyticsTranscriptResultStream"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CallAnalyticsTranscriptResultStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_CallAnalyticsTranscriptResultStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CallAnalyticsTranscriptResultStream
<a name="API_streaming_CallAnalyticsTranscriptResultStream"></a>

Contains detailed information about your real-time Call Analytics session. These details are provided in the `UtteranceEvent` and `CategoryEvent` objects.

## Contents
<a name="API_streaming_CallAnalyticsTranscriptResultStream_Contents"></a>

 ** BadRequestException **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-BadRequestException"></a>
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** CategoryEvent **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-CategoryEvent"></a>
Provides information on matched categories that were used to generate real-time supervisor alerts.  
Type: [CategoryEvent](API_streaming_CategoryEvent.md) object  
Required: No

 ** ConflictException **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-ConflictException"></a>
A new stream started with the same session ID. The current stream has been terminated.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** InternalFailureException **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-InternalFailureException"></a>
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** LimitExceededException **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-LimitExceededException"></a>
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** ServiceUnavailableException **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-ServiceUnavailableException"></a>
The service is currently unavailable. Try your request later.  
Type: Exception  
HTTP Status Code: 503  
Required: No

 ** UtteranceEvent **   <a name="transcribe-Type-streaming_CallAnalyticsTranscriptResultStream-UtteranceEvent"></a>
Contains set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to channel definitions, partial result stabilization, sentiment, issue detection, and other transcription-related data.  
Type: [UtteranceEvent](API_streaming_UtteranceEvent.md) object  
Required: No

## See Also
<a name="API_streaming_CallAnalyticsTranscriptResultStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CallAnalyticsTranscriptResultStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CallAnalyticsTranscriptResultStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CallAnalyticsTranscriptResultStream) 