---
id: "@specs/aws/transcribe/docs/API_MedicalScribeSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalScribeSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeSettings
<a name="API_MedicalScribeSettings"></a>

Makes it possible to control how your Medical Scribe job is processed using a `MedicalScribeSettings` object. Specify `ChannelIdentification` if `ChannelDefinitions` are set. Enabled `ShowSpeakerLabels` if `ChannelIdentification` and `ChannelDefinitions` are not set. One and only one of `ChannelIdentification` and `ShowSpeakerLabels` must be set. If `ShowSpeakerLabels` is set, `MaxSpeakerLabels` must also be set. Use `Settings` to specify a vocabulary or vocabulary filter or both using `VocabularyName`, `VocabularyFilterName`. `VocabularyFilterMethod` must be specified if `VocabularyFilterName` is set. 

## Contents
<a name="API_MedicalScribeSettings_Contents"></a>

 ** ChannelIdentification **   <a name="transcribe-Type-MedicalScribeSettings-ChannelIdentification"></a>
Enables channel identification in multi-channel audio.  
Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.  
For more information, see [Transcribing multi-channel audio](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html).  
Type: Boolean  
Required: No

 ** ClinicalNoteGenerationSettings **   <a name="transcribe-Type-MedicalScribeSettings-ClinicalNoteGenerationSettings"></a>
Specify settings for the clinical note generation.  
Type: [ClinicalNoteGenerationSettings](API_ClinicalNoteGenerationSettings.md) object  
Required: No

 ** MaxSpeakerLabels **   <a name="transcribe-Type-MedicalScribeSettings-MaxSpeakerLabels"></a>
Specify the maximum number of speakers you want to partition in your media.  
Note that if your media contains more speakers than the specified number, multiple speakers are treated as a single speaker.  
If you specify the `MaxSpeakerLabels` field, you must set the `ShowSpeakerLabels` field to true.  
Type: Integer  
Valid Range: Minimum value of 2. Maximum value of 30.  
Required: No

 ** ShowSpeakerLabels **   <a name="transcribe-Type-MedicalScribeSettings-ShowSpeakerLabels"></a>
Enables speaker partitioning (diarization) in your Medical Scribe output. Speaker partitioning labels the speech from individual speakers in your media file.  
If you enable `ShowSpeakerLabels` in your request, you must also include `MaxSpeakerLabels`.  
For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html).  
Type: Boolean  
Required: No

 ** VocabularyFilterMethod **   <a name="transcribe-Type-MedicalScribeSettings-VocabularyFilterMethod"></a>
Specify how you want your custom vocabulary filter applied to your transcript.  
To replace words with `***`, choose `mask`.  
To delete words, choose `remove`.  
To flag words without changing them, choose `tag`.  
Type: String  
Valid Values: `remove | mask | tag`   
Required: No

 ** VocabularyFilterName **   <a name="transcribe-Type-MedicalScribeSettings-VocabularyFilterName"></a>
The name of the custom vocabulary filter you want to include in your Medical Scribe request. Custom vocabulary filter names are case sensitive.  
Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyName **   <a name="transcribe-Type-MedicalScribeSettings-VocabularyName"></a>
The name of the custom vocabulary you want to include in your Medical Scribe request. Custom vocabulary names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

## See Also
<a name="API_MedicalScribeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalScribeSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalScribeSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalScribeSettings) 