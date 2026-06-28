---
id: "@specs/aws/transcribe/docs/API_CallAnalyticsJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CallAnalyticsJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CallAnalyticsJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CallAnalyticsJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CallAnalyticsJob
<a name="API_CallAnalyticsJob"></a>

Provides detailed information about a Call Analytics job.

To view the job's status, refer to `CallAnalyticsJobStatus`. If the status is `COMPLETED`, the job is finished. You can find your completed transcript at the URI specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.

If you enabled personally identifiable information (PII) redaction, the redacted transcript appears at the location specified in `RedactedTranscriptFileUri`.

If you chose to redact the audio in your media file, you can find your redacted media file at the location specified in the `RedactedMediaFileUri` field of your response.

## Contents
<a name="API_CallAnalyticsJob_Contents"></a>

 ** CallAnalyticsJobDetails **   <a name="transcribe-Type-CallAnalyticsJob-CallAnalyticsJobDetails"></a>
Provides detailed information about a call analytics job, including information about skipped analytics features.  
Type: [CallAnalyticsJobDetails](API_CallAnalyticsJobDetails.md) object  
Required: No

 ** CallAnalyticsJobName **   <a name="transcribe-Type-CallAnalyticsJob-CallAnalyticsJobName"></a>
The name of the Call Analytics job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** CallAnalyticsJobStatus **   <a name="transcribe-Type-CallAnalyticsJob-CallAnalyticsJobStatus"></a>
Provides the status of the specified Call Analytics job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri` (or `RedactedTranscriptFileUri`, if you requested transcript redaction). If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** ChannelDefinitions **   <a name="transcribe-Type-CallAnalyticsJob-ChannelDefinitions"></a>
Indicates which speaker is on which channel.  
Type: Array of [ChannelDefinition](API_ChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** CompletionTime **   <a name="transcribe-Type-CallAnalyticsJob-CompletionTime"></a>
The date and time the specified Call Analytics job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** CreationTime **   <a name="transcribe-Type-CallAnalyticsJob-CreationTime"></a>
The date and time the specified Call Analytics job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** DataAccessRoleArn **   <a name="transcribe-Type-CallAnalyticsJob-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) you included in your request.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: No

 ** FailureReason **   <a name="transcribe-Type-CallAnalyticsJob-FailureReason"></a>
If `CallAnalyticsJobStatus` is `FAILED`, `FailureReason` contains information about why the Call Analytics job request failed.  
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

 ** IdentifiedLanguageScore **   <a name="transcribe-Type-CallAnalyticsJob-IdentifiedLanguageScore"></a>
The confidence score associated with the language identified in your media file.  
Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.  
Type: Float  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-CallAnalyticsJob-LanguageCode"></a>
The language code used to create your Call Analytics job. For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.  
If you do not know the language spoken in your media file, you can omit this field and let Amazon Transcribe automatically identify the language of your media. To improve the accuracy of language identification, you can include several language codes and Amazon Transcribe chooses the closest match for your transcription.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** Media **   <a name="transcribe-Type-CallAnalyticsJob-Media"></a>
Provides the Amazon S3 location of the media file you used in your Call Analytics request.  
Type: [Media](API_Media.md) object  
Required: No

 ** MediaFormat **   <a name="transcribe-Type-CallAnalyticsJob-MediaFormat"></a>
The format of the input media file.  
Type: String  
Valid Values: `mp3 | mp4 | wav | flac | ogg | amr | webm | m4a`   
Required: No

 ** MediaSampleRateHertz **   <a name="transcribe-Type-CallAnalyticsJob-MediaSampleRateHertz"></a>
The sample rate, in hertz, of the audio track in your input media file.  
Type: Integer  
Valid Range: Minimum value of 8000. Maximum value of 48000.  
Required: No

 ** Settings **   <a name="transcribe-Type-CallAnalyticsJob-Settings"></a>
Provides information on any additional settings that were included in your request. Additional settings include content redaction and language identification settings.  
Type: [CallAnalyticsJobSettings](API_CallAnalyticsJobSettings.md) object  
Required: No

 ** StartTime **   <a name="transcribe-Type-CallAnalyticsJob-StartTime"></a>
The date and time the specified Call Analytics job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** Tags **   <a name="transcribe-Type-CallAnalyticsJob-Tags"></a>
The tags, each in the form of a key:value pair, assigned to the specified call analytics job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** Transcript **   <a name="transcribe-Type-CallAnalyticsJob-Transcript"></a>
Provides you with the Amazon S3 URI you can use to access your transcript.  
Type: [Transcript](API_Transcript.md) object  
Required: No

## See Also
<a name="API_CallAnalyticsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CallAnalyticsJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CallAnalyticsJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CallAnalyticsJob) 