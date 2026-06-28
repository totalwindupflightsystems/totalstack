---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeChannelDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeChannelDefinition"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeChannelDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeChannelDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeChannelDefinition
<a name="API_streaming_MedicalScribeChannelDefinition"></a>

Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set the `ChannelId` of the first `ChannelDefinition` in the list to `0` (to indicate the first channel) and `ParticipantRole` to `CLINICIAN` (to indicate that it's the clinician speaking). Then you would set the `ChannelId` of the second `ChannelDefinition` in the list to `1` (to indicate the second channel) and `ParticipantRole` to `PATIENT` (to indicate that it's the patient speaking). 

If you don't specify a channel definition, HealthScribe will diarize the transcription and identify speaker roles for each speaker.

## Contents
<a name="API_streaming_MedicalScribeChannelDefinition_Contents"></a>

 ** ChannelId **   <a name="transcribe-Type-streaming_MedicalScribeChannelDefinition-ChannelId"></a>
Specify the audio channel you want to define.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: Yes

 ** ParticipantRole **   <a name="transcribe-Type-streaming_MedicalScribeChannelDefinition-ParticipantRole"></a>
Specify the participant that you want to flag. The allowed options are `CLINICIAN` and `PATIENT`.   
Type: String  
Valid Values: `PATIENT | CLINICIAN`   
Required: Yes

## See Also
<a name="API_streaming_MedicalScribeChannelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeChannelDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeChannelDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeChannelDefinition) 