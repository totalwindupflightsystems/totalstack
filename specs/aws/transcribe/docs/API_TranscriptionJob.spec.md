---
id: "@specs/aws/transcribe/docs/API_TranscriptionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TranscriptionJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# TranscriptionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_TranscriptionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TranscriptionJob
<a name="API_TranscriptionJob"></a>

Provides detailed information about a transcription job.

To view the status of the specified transcription job, check the `TranscriptionJobStatus` field. If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.

If you enabled content redaction, the redacted transcript can be found at the location specified in `RedactedTranscriptFileUri`.

## Contents
<a name="API_TranscriptionJob_Contents"></a>

 ** CompletionTime **   <a name="transcribe-Type-TranscriptionJob-CompletionTime"></a>
The date and time the specified transcription job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** ContentRedaction **   <a name="transcribe-Type-TranscriptionJob-ContentRedaction"></a>
Indicates whether redaction was enabled in your transcript.  
Type: [ContentRedaction](API_ContentRedaction.md) object  
Required: No

 ** CreationTime **   <a name="transcribe-Type-TranscriptionJob-CreationTime"></a>
The date and time the specified transcription job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** FailureReason **   <a name="transcribe-Type-TranscriptionJob-FailureReason"></a>
If `TranscriptionJobStatus` is `FAILED`, `FailureReason` contains information about why the transcription job request failed.  
The `FailureReason` field contains one of the following values:  
+  `Unsupported media format`.

  The media format specified in `MediaFormat` isn't valid. Refer to refer to the `MediaFormat` parameter for a list of supported formats.
+  `The media format provided does not match the detected media format`.

  The media format specified in `MediaFormat` doesn't match the format of the input file. Check the media format of your media file and correct the specified value.
+  `Invalid sample rate for audio file`.

  The sample rate specified in `MediaSampleRateHertz` isn't valid. The sample rate must be between 8,000 and 48,000 hertz.
+  `The sample rate provided does not match the detected sample rate`.

  The sample rate specified in `MediaSampleRateHertz` doesn't match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.
+  `Invalid file size: file size too large`.

  The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe).
+  `Invalid number of channels: number of channels too large`.

  Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe).
Type: String  
Required: No

 ** IdentifiedLanguageScore **   <a name="transcribe-Type-TranscriptionJob-IdentifiedLanguageScore"></a>
The confidence score associated with the language identified in your media file.  
Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.  
Type: Float  
Required: No

 ** IdentifyLanguage **   <a name="transcribe-Type-TranscriptionJob-IdentifyLanguage"></a>
Indicates whether automatic language identification was enabled (`TRUE`) for the specified transcription job.  
Type: Boolean  
Required: No

 ** IdentifyMultipleLanguages **   <a name="transcribe-Type-TranscriptionJob-IdentifyMultipleLanguages"></a>
Indicates whether automatic multi-language identification was enabled (`TRUE`) for the specified transcription job.  
Type: Boolean  
Required: No

 ** JobExecutionSettings **   <a name="transcribe-Type-TranscriptionJob-JobExecutionSettings"></a>
Provides information about how your transcription job was processed. This parameter shows if your request was queued and what data access role was used.  
Type: [JobExecutionSettings](API_JobExecutionSettings.md) object  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-TranscriptionJob-LanguageCode"></a>
The language code used to create your transcription job. This parameter is used with single-language identification. For multi-language identification requests, refer to the plural version of this parameter, `LanguageCodes`.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** LanguageCodes **   <a name="transcribe-Type-TranscriptionJob-LanguageCodes"></a>
The language codes used to create your transcription job. This parameter is used with multi-language identification. For single-language identification requests, refer to the singular version of this parameter, `LanguageCode`.  
Type: Array of [LanguageCodeItem](API_LanguageCodeItem.md) objects  
Required: No

 ** LanguageIdSettings **   <a name="transcribe-Type-TranscriptionJob-LanguageIdSettings"></a>
Provides the name and language of all custom language models, custom vocabularies, and custom vocabulary filters that you included in your request.  
Type: String to [LanguageIdSettings](API_LanguageIdSettings.md) object map  
Map Entries: Maximum number of 5 items.  
Valid Keys: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** LanguageOptions **   <a name="transcribe-Type-TranscriptionJob-LanguageOptions"></a>
Provides the language codes you specified in your request.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** Media **   <a name="transcribe-Type-TranscriptionJob-Media"></a>
Provides the Amazon S3 location of the media file you used in your request.  
Type: [Media](API_Media.md) object  
Required: No

 ** MediaFormat **   <a name="transcribe-Type-TranscriptionJob-MediaFormat"></a>
The format of the input media file.  
Type: String  
Valid Values: `mp3 | mp4 | wav | flac | ogg | amr | webm | m4a`   
Required: No

 ** MediaSampleRateHertz **   <a name="transcribe-Type-TranscriptionJob-MediaSampleRateHertz"></a>
The sample rate, in hertz, of the audio track in your input media file.  
Type: Integer  
Valid Range: Minimum value of 8000. Maximum value of 48000.  
Required: No

 ** ModelSettings **   <a name="transcribe-Type-TranscriptionJob-ModelSettings"></a>
Provides information on the custom language model you included in your request.  
Type: [ModelSettings](API_ModelSettings.md) object  
Required: No

 ** Settings **   <a name="transcribe-Type-TranscriptionJob-Settings"></a>
Provides information on any additional settings that were included in your request. Additional settings include channel identification, alternative transcriptions, speaker partitioning, custom vocabularies, and custom vocabulary filters.  
Type: [Settings](API_Settings.md) object  
Required: No

 ** StartTime **   <a name="transcribe-Type-TranscriptionJob-StartTime"></a>
The date and time the specified transcription job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** Subtitles **   <a name="transcribe-Type-TranscriptionJob-Subtitles"></a>
Indicates whether subtitles were generated with your transcription.  
Type: [SubtitlesOutput](API_SubtitlesOutput.md) object  
Required: No

 ** Tags **   <a name="transcribe-Type-TranscriptionJob-Tags"></a>
The tags, each in the form of a key:value pair, assigned to the specified transcription job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** ToxicityDetection **   <a name="transcribe-Type-TranscriptionJob-ToxicityDetection"></a>
Provides information about the toxicity detection settings applied to your transcription.  
Type: Array of [ToxicityDetectionSettings](API_ToxicityDetectionSettings.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** Transcript **   <a name="transcribe-Type-TranscriptionJob-Transcript"></a>
Provides you with the Amazon S3 URI you can use to access your transcript.  
Type: [Transcript](API_Transcript.md) object  
Required: No

 ** TranscriptionJobName **   <a name="transcribe-Type-TranscriptionJob-TranscriptionJobName"></a>
The name of the transcription job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** TranscriptionJobStatus **   <a name="transcribe-Type-TranscriptionJob-TranscriptionJobStatus"></a>
Provides the status of the specified transcription job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri` (or `RedactedTranscriptFileUri`, if you requested transcript redaction). If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

## See Also
<a name="API_TranscriptionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/TranscriptionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/TranscriptionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/TranscriptionJob) 