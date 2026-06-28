---
id: "@specs/aws/transcribe/docs/API_streaming_Transcript"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Transcript"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Transcript

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_Transcript
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Transcript
<a name="API_streaming_Transcript"></a>

The `Transcript` associated with a ` TranscriptEvent `.

 `Transcript` contains `Results`, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters.

## Contents
<a name="API_streaming_Transcript_Contents"></a>

 ** Results **   <a name="transcribe-Type-streaming_Transcript-Results"></a>
Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.  
Type: Array of [Result](API_streaming_Result.md) objects  
Required: No

## See Also
<a name="API_streaming_Transcript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/Transcript) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/Transcript) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/Transcript) 