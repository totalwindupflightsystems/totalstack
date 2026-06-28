---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalResult"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalResult
<a name="API_streaming_MedicalResult"></a>

The `Result` associated with a ` MedicalTranscript `.

Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.

## Contents
<a name="API_streaming_MedicalResult_Contents"></a>

 ** Alternatives **   <a name="transcribe-Type-streaming_MedicalResult-Alternatives"></a>
A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of `Items`, `Entities`, or `Transcript`.  
Type: Array of [MedicalAlternative](API_streaming_MedicalAlternative.md) objects  
Required: No

 ** ChannelId **   <a name="transcribe-Type-streaming_MedicalResult-ChannelId"></a>
Indicates the channel identified for the `Result`.  
Type: String  
Required: No

 ** EndTime **   <a name="transcribe-Type-streaming_MedicalResult-EndTime"></a>
The end time, in seconds, of the `Result`.  
Type: Double  
Required: No

 ** IsPartial **   <a name="transcribe-Type-streaming_MedicalResult-IsPartial"></a>
Indicates if the segment is complete.  
If `IsPartial` is `true`, the segment is not complete. If `IsPartial` is `false`, the segment is complete.  
Type: Boolean  
Required: No

 ** ResultId **   <a name="transcribe-Type-streaming_MedicalResult-ResultId"></a>
Provides a unique identifier for the `Result`.  
Type: String  
Required: No

 ** StartTime **   <a name="transcribe-Type-streaming_MedicalResult-StartTime"></a>
The start time, in seconds, of the `Result`.  
Type: Double  
Required: No

## See Also
<a name="API_streaming_MedicalResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalResult) 