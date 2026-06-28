---
id: "@specs/aws/transcribe/docs/API_MedicalTranscriptionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalTranscriptionJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalTranscriptionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalTranscriptionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalTranscriptionJob
<a name="API_MedicalTranscriptionJob"></a>

Provides detailed information about a medical transcription job.

To view the status of the specified medical transcription job, check the `TranscriptionJobStatus` field. If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.

## Contents
<a name="API_MedicalTranscriptionJob_Contents"></a>

 ** CompletionTime **   <a name="transcribe-Type-MedicalTranscriptionJob-CompletionTime"></a>
The date and time the specified medical transcription job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** ContentIdentificationType **   <a name="transcribe-Type-MedicalTranscriptionJob-ContentIdentificationType"></a>
Indicates whether content identification was enabled for your transcription request.  
Type: String  
Valid Values: `PHI`   
Required: No

 ** CreationTime **   <a name="transcribe-Type-MedicalTranscriptionJob-CreationTime"></a>
The date and time the specified medical transcription job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** FailureReason **   <a name="transcribe-Type-MedicalTranscriptionJob-FailureReason"></a>
If `TranscriptionJobStatus` is `FAILED`, `FailureReason` contains information about why the transcription job request failed.  
The `FailureReason` field contains one of the following values:  
+  `Unsupported media format`.

  The media format specified in `MediaFormat` isn't valid. Refer to refer to the `MediaFormat` parameter for a list of supported formats.
+  `The media format provided does not match the detected media format`.

  The media format specified in `MediaFormat` doesn't match the format of the input file. Check the media format of your media file and correct the specified value.
+  `Invalid sample rate for audio file`.

  The sample rate specified in `MediaSampleRateHertz` isn't valid. The sample rate must be between 16,000 and 48,000 hertz.
+  `The sample rate provided does not match the detected sample rate`.

  The sample rate specified in `MediaSampleRateHertz` doesn't match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.
+  `Invalid file size: file size too large`.

  The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe).
+  `Invalid number of channels: number of channels too large`.

  Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe).
Type: String  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-MedicalTranscriptionJob-LanguageCode"></a>
The language code used to create your medical transcription job. US English (`en-US`) is the only supported language for medical transcriptions.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** Media **   <a name="transcribe-Type-MedicalTranscriptionJob-Media"></a>
Describes the Amazon S3 location of the media file you want to use in your request.  
For information on supported media formats, refer to the `MediaFormat` parameter or the [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) section in the Amazon S3 Developer Guide.  
Type: [Media](API_Media.md) object  
Required: No

 ** MediaFormat **   <a name="transcribe-Type-MedicalTranscriptionJob-MediaFormat"></a>
The format of the input media file.  
Type: String  
Valid Values: `mp3 | mp4 | wav | flac | ogg | amr | webm | m4a`   
Required: No

 ** MediaSampleRateHertz **   <a name="transcribe-Type-MedicalTranscriptionJob-MediaSampleRateHertz"></a>
The sample rate, in hertz, of the audio track in your input media file.  
Type: Integer  
Valid Range: Minimum value of 16000. Maximum value of 48000.  
Required: No

 ** MedicalTranscriptionJobName **   <a name="transcribe-Type-MedicalTranscriptionJob-MedicalTranscriptionJobName"></a>
The name of the medical transcription job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** Settings **   <a name="transcribe-Type-MedicalTranscriptionJob-Settings"></a>
Provides information on any additional settings that were included in your request. Additional settings include channel identification, alternative transcriptions, speaker partitioning, custom vocabularies, and custom vocabulary filters.  
Type: [MedicalTranscriptionSetting](API_MedicalTranscriptionSetting.md) object  
Required: No

 ** Specialty **   <a name="transcribe-Type-MedicalTranscriptionJob-Specialty"></a>
Describes the medical specialty represented in your media.  
Type: String  
Valid Values: `PRIMARYCARE`   
Required: No

 ** StartTime **   <a name="transcribe-Type-MedicalTranscriptionJob-StartTime"></a>
The date and time the specified medical transcription job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** Tags **   <a name="transcribe-Type-MedicalTranscriptionJob-Tags"></a>
The tags, each in the form of a key:value pair, assigned to the specified medical transcription job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** Transcript **   <a name="transcribe-Type-MedicalTranscriptionJob-Transcript"></a>
Provides you with the Amazon S3 URI you can use to access your transcript.  
Type: [MedicalTranscript](API_MedicalTranscript.md) object  
Required: No

 ** TranscriptionJobStatus **   <a name="transcribe-Type-MedicalTranscriptionJob-TranscriptionJobStatus"></a>
Provides the status of the specified medical transcription job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** Type **   <a name="transcribe-Type-MedicalTranscriptionJob-Type"></a>
Indicates whether the input media is a dictation or a conversation, as specified in the `StartMedicalTranscriptionJob` request.  
Type: String  
Valid Values: `CONVERSATION | DICTATION`   
Required: No

## See Also
<a name="API_MedicalTranscriptionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalTranscriptionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalTranscriptionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalTranscriptionJob) 