---
id: "@specs/aws/transcribe/docs/API_streaming_TranscriptResultStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TranscriptResultStream"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# TranscriptResultStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_TranscriptResultStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TranscriptResultStream
<a name="API_streaming_TranscriptResultStream"></a>

Contains detailed information about your streaming session.

## Contents
<a name="API_streaming_TranscriptResultStream_Contents"></a>

 ** BadRequestException **   <a name="transcribe-Type-streaming_TranscriptResultStream-BadRequestException"></a>
A client error occurred when the stream was created. Check the parameters of the request and try your request again.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** ConflictException **   <a name="transcribe-Type-streaming_TranscriptResultStream-ConflictException"></a>
A new stream started with the same session ID. The current stream has been terminated.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** InternalFailureException **   <a name="transcribe-Type-streaming_TranscriptResultStream-InternalFailureException"></a>
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** LimitExceededException **   <a name="transcribe-Type-streaming_TranscriptResultStream-LimitExceededException"></a>
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** ServiceUnavailableException **   <a name="transcribe-Type-streaming_TranscriptResultStream-ServiceUnavailableException"></a>
The service is currently unavailable. Try your request later.  
Type: Exception  
HTTP Status Code: 503  
Required: No

 ** TranscriptEvent **   <a name="transcribe-Type-streaming_TranscriptResultStream-TranscriptEvent"></a>
Contains `Transcript`, which contains `Results`. The ` Result ` object contains a set of transcription results from one or more audio segments, along with additional information per your request parameters.  
Type: [TranscriptEvent](API_streaming_TranscriptEvent.md) object  
Required: No

## See Also
<a name="API_streaming_TranscriptResultStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/TranscriptResultStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/TranscriptResultStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/TranscriptResultStream) 