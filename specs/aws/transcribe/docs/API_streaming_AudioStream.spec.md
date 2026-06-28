---
id: "@specs/aws/transcribe/docs/API_streaming_AudioStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AudioStream"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# AudioStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_AudioStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AudioStream
<a name="API_streaming_AudioStream"></a>

An encoded stream of audio blobs. Audio streams are encoded as either HTTP/2 or WebSocket data frames.

For more information, see [Transcribing streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html).

## Contents
<a name="API_streaming_AudioStream_Contents"></a>

 ** AudioEvent **   <a name="transcribe-Type-streaming_AudioStream-AudioEvent"></a>
A blob of audio from your application. Your audio stream consists of one or more audio events.  
For more information, see [Event stream encoding](https://docs.aws.amazon.com/transcribe/latest/dg/event-stream.html).  
Type: [AudioEvent](API_streaming_AudioEvent.md) object  
Required: No

 ** ConfigurationEvent **   <a name="transcribe-Type-streaming_AudioStream-ConfigurationEvent"></a>
Contains audio channel definitions and post-call analytics settings.  
Type: [ConfigurationEvent](API_streaming_ConfigurationEvent.md) object  
Required: No

## See Also
<a name="API_streaming_AudioStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/AudioStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/AudioStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/AudioStream) 