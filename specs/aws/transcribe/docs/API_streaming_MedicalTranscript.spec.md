---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalTranscript"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalTranscript"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalTranscript

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalTranscript
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalTranscript
<a name="API_streaming_MedicalTranscript"></a>

The `MedicalTranscript` associated with a ` MedicalTranscriptEvent `.

 `MedicalTranscript` contains `Results`, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters.

## Contents
<a name="API_streaming_MedicalTranscript_Contents"></a>

 ** Results **   <a name="transcribe-Type-streaming_MedicalTranscript-Results"></a>
Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.  
Type: Array of [MedicalResult](API_streaming_MedicalResult.md) objects  
Required: No

## See Also
<a name="API_streaming_MedicalTranscript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalTranscript) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalTranscript) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalTranscript) 