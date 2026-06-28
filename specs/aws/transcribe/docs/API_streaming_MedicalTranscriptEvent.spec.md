---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalTranscriptEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalTranscriptEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalTranscriptEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalTranscriptEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalTranscriptEvent
<a name="API_streaming_MedicalTranscriptEvent"></a>

The `MedicalTranscriptEvent` associated with a `MedicalTranscriptResultStream`.

Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters.

## Contents
<a name="API_streaming_MedicalTranscriptEvent_Contents"></a>

 ** Transcript **   <a name="transcribe-Type-streaming_MedicalTranscriptEvent-Transcript"></a>
Contains `Results`, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.  
Type: [MedicalTranscript](API_streaming_MedicalTranscript.md) object  
Required: No

## See Also
<a name="API_streaming_MedicalTranscriptEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalTranscriptEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalTranscriptEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalTranscriptEvent) 