---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeAudioEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeAudioEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeAudioEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeAudioEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeAudioEvent
<a name="API_streaming_MedicalScribeAudioEvent"></a>

A wrapper for your audio chunks

For more information, see [Event stream encoding](https://docs.aws.amazon.com/transcribe/latest/dg/event-stream.html). 

## Contents
<a name="API_streaming_MedicalScribeAudioEvent_Contents"></a>

 ** AudioChunk **   <a name="transcribe-Type-streaming_MedicalScribeAudioEvent-AudioChunk"></a>
 An audio blob containing the next segment of audio from your application, with a maximum duration of 1 second. The maximum size in bytes varies based on audio properties.   
Find recommended size in [Transcribing streaming best practices](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#best-practices).   
 Size calculation: `Duration (s) * Sample Rate (Hz) * Number of Channels * 2 (Bytes per Sample)`   
 For example, a 1-second chunk of 16 kHz, 2-channel, 16-bit audio would be `1 * 16000 * 2 * 2 = 64000 bytes`.   
 For 8 kHz, 1-channel, 16-bit audio, a 1-second chunk would be `1 * 8000 * 1 * 2 = 16000 bytes`.   
Type: Base64-encoded binary data object  
Required: Yes

## See Also
<a name="API_streaming_MedicalScribeAudioEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeAudioEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeAudioEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeAudioEvent) 