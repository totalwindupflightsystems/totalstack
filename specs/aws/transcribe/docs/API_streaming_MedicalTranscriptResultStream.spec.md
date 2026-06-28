---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalTranscriptResultStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalTranscriptResultStream"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalTranscriptResultStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalTranscriptResultStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalTranscriptResultStream
<a name="API_streaming_MedicalTranscriptResultStream"></a>

Contains detailed information about your streaming session.

## Contents
<a name="API_streaming_MedicalTranscriptResultStream_Contents"></a>

 ** BadRequestException **   <a name="transcribe-Type-streaming_MedicalTranscriptResultStream-BadRequestException"></a>
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** ConflictException **   <a name="transcribe-Type-streaming_MedicalTranscriptResultStream-ConflictException"></a>
A new stream started with the same session ID. The current stream has been terminated.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** InternalFailureException **   <a name="transcribe-Type-streaming_MedicalTranscriptResultStream-InternalFailureException"></a>
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** LimitExceededException **   <a name="transcribe-Type-streaming_MedicalTranscriptResultStream-LimitExceededException"></a>
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** ServiceUnavailableException **   <a name="transcribe-Type-streaming_MedicalTranscriptResultStream-ServiceUnavailableException"></a>
The service is currently unavailable. Try your request later.  
Type: Exception  
HTTP Status Code: 503  
Required: No

 ** TranscriptEvent **   <a name="transcribe-Type-streaming_MedicalTranscriptResultStream-TranscriptEvent"></a>
The `MedicalTranscriptEvent` associated with a `MedicalTranscriptResultStream`.  
Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.  
Type: [MedicalTranscriptEvent](API_streaming_MedicalTranscriptEvent.md) object  
Required: No

## See Also
<a name="API_streaming_MedicalTranscriptResultStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalTranscriptResultStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalTranscriptResultStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalTranscriptResultStream) 