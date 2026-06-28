---
id: "@specs/aws/transcribe/docs/API_StartTranscriptionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartTranscriptionJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartTranscriptionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_StartTranscriptionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartTranscriptionJob
<a name="API_StartTranscriptionJob"></a>

Transcribes the audio from a media file and applies any additional Request Parameters you choose to include in your request.

To make a `StartTranscriptionJob` request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the `Media` parameter.

You must include the following parameters in your `StartTranscriptionJob` request:
+  `region`: The AWS Region where you are making your request. For a list of AWS Regions supported with Amazon Transcribe, refer to [Amazon Transcribe endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html).
+  `TranscriptionJobName`: A custom name you create for your transcription job that is unique within your AWS account.
+  `Media` (`MediaFileUri`): The Amazon S3 location of your media file.
+ One of `LanguageCode`, `IdentifyLanguage`, or `IdentifyMultipleLanguages`: If you know the language of your media file, specify it using the `LanguageCode` parameter; you can find all valid language codes in the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table. If you do not know the languages spoken in your media, use either `IdentifyLanguage` or `IdentifyMultipleLanguages` and let Amazon Transcribe identify the languages for you.

## Request Syntax
<a name="API_StartTranscriptionJob_RequestSyntax"></a>

```
{
   "ContentRedaction": { 
      "PiiEntityTypes": [ "{{string}}" ],
      "RedactionOutput": "{{string}}",
      "RedactionType": "{{string}}"
   },
   "IdentifyLanguage": {{boolean}},
   "IdentifyMultipleLanguages": {{boolean}},
   "JobExecutionSettings": { 
      "AllowDeferredExecution": {{boolean}},
      "DataAccessRoleArn": "{{string}}"
   },
   "KMSEncryptionContext": { 
      "{{string}}" : "{{string}}" 
   },
   "LanguageCode": "{{string}}",
   "LanguageIdSettings": { 
      "{{string}}" : { 
         "LanguageModelName": "{{string}}",
         "VocabularyFilterName": "{{string}}",
         "VocabularyName": "{{string}}"
      }
   },
   "LanguageOptions": [ "{{string}}" ],
   "Media": { 
      "MediaFileUri": "{{string}}",
      "RedactedMediaFileUri": "{{string}}"
   },
   "MediaFormat": "{{string}}",
   "MediaSampleRateHertz": {{number}},
   "ModelSettings": { 
      "LanguageModelName": "{{string}}"
   },
   "OutputBucketName": "{{string}}",
   "OutputEncryptionKMSKeyId": "{{string}}",
   "OutputKey": "{{string}}",
   "Settings": { 
      "ChannelIdentification": {{boolean}},
      "MaxAlternatives": {{number}},
      "MaxSpeakerLabels": {{number}},
      "ShowAlternatives": {{boolean}},
      "ShowSpeakerLabels": {{boolean}},
      "VocabularyFilterMethod": "{{string}}",
      "VocabularyFilterName": "{{string}}",
      "VocabularyName": "{{string}}"
   },
   "Subtitles": { 
      "Formats": [ "{{string}}" ],
      "OutputStartIndex": {{number}}
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ToxicityDetection": [ 
      { 
         "ToxicityCategories": [ "{{string}}" ]
      }
   ],
   "TranscriptionJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartTranscriptionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContentRedaction](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-ContentRedaction"></a>
Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript. If you use `ContentRedaction`, you must also include the sub-parameters: `RedactionOutput` and `RedactionType`. You can optionally include `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.  
Type: [ContentRedaction](API_ContentRedaction.md) object  
Required: No

 ** [IdentifyLanguage](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-IdentifyLanguage"></a>
Enables automatic language identification in your transcription job request. Use this parameter if your media file contains only one language. If your media contains multiple languages, use `IdentifyMultipleLanguages` instead.  
If you include `IdentifyLanguage`, you can optionally include a list of language codes, using `LanguageOptions`, that you think may be present in your media file. Including `LanguageOptions` restricts `IdentifyLanguage` to only the language options that you specify, which can improve transcription accuracy.  
If you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter to your automatic language identification request, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName`, `LanguageModelName`, and `VocabularyFilterName`). If you include `LanguageIdSettings`, also include `LanguageOptions`.  
Note that you must include one of `LanguageCode`, `IdentifyLanguage`, or `IdentifyMultipleLanguages` in your request. If you include more than one of these parameters, your transcription job fails.  
Type: Boolean  
Required: No

 ** [IdentifyMultipleLanguages](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-IdentifyMultipleLanguages"></a>
Enables automatic multi-language identification in your transcription job request. Use this parameter if your media file contains more than one language. If your media contains only one language, use `IdentifyLanguage` instead.  
If you include `IdentifyMultipleLanguages`, you can optionally include a list of language codes, using `LanguageOptions`, that you think may be present in your media file. Including `LanguageOptions` restricts `IdentifyLanguage` to only the language options that you specify, which can improve transcription accuracy.  
If you want to apply a custom vocabulary or a custom vocabulary filter to your automatic language identification request, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName` and `VocabularyFilterName`). If you include `LanguageIdSettings`, also include `LanguageOptions`.  
Note that you must include one of `LanguageCode`, `IdentifyLanguage`, or `IdentifyMultipleLanguages` in your request. If you include more than one of these parameters, your transcription job fails.  
Type: Boolean  
Required: No

 ** [JobExecutionSettings](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-JobExecutionSettings"></a>
Makes it possible to control how your transcription job is processed. Currently, the only `JobExecutionSettings` modification you can choose is enabling job queueing using the `AllowDeferredExecution` sub-parameter.  
If you include `JobExecutionSettings` in your request, you must also include the sub-parameters: `AllowDeferredExecution` and `DataAccessRoleArn`.  
Type: [JobExecutionSettings](API_JobExecutionSettings.md) object  
Required: No

 ** [KMSEncryptionContext](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-KMSEncryptionContext"></a>
A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see [AWS KMS encryption context](https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context) and [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html).  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

 ** [LanguageCode](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-LanguageCode"></a>
The language code that represents the language spoken in the input media file.  
If you're unsure of the language spoken in your media file, consider using `IdentifyLanguage` or `IdentifyMultipleLanguages` to enable automatic language identification.  
Note that you must include one of `LanguageCode`, `IdentifyLanguage`, or `IdentifyMultipleLanguages` in your request. If you include more than one of these parameters, your transcription job fails.  
For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.  
To transcribe speech in Modern Standard Arabic (`ar-SA`) in AWS GovCloud (US) (US-West, us-gov-west-1), AWS GovCloud (US) (US-East, us-gov-east-1), Canada (Calgary, ca-west-1) and Africa (Cape Town, af-south-1), your media file must be encoded at a sample rate of 16,000 Hz or higher.
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** [LanguageIdSettings](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-LanguageIdSettings"></a>
If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName`, `LanguageModelName`, and `VocabularyFilterName`). Note that multi-language identification (`IdentifyMultipleLanguages`) doesn't support custom language models.  
 `LanguageIdSettings` supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.  
It's recommended that you include `LanguageOptions` when using `LanguageIdSettings` to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in `en-US` but Amazon Transcribe determines that the language spoken in your media is `en-AU`, your custom vocabulary *is not* applied to your transcription. If you include `LanguageOptions` and include `en-US` as the only English language dialect, your custom vocabulary *is* applied to your transcription.  
If you want to include a custom language model with your request but **do not** want to use automatic language identification, use instead the ` ModelSettings ` parameter with the `LanguageModelName` sub-parameter. If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but **do not** want to use automatic language identification, use instead the ` Settings ` parameter with the `VocabularyName` or `VocabularyFilterName` (or both) sub-parameter.  
Type: String to [LanguageIdSettings](API_LanguageIdSettings.md) object map  
Map Entries: Maximum number of 5 items.  
Valid Keys: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** [LanguageOptions](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-LanguageOptions"></a>
You can specify two or more language codes that represent the languages you think may be present in your media. Including more than five is not recommended. If you're unsure what languages are present, do not include this parameter.  
If you include `LanguageOptions` in your request, you must also include `IdentifyLanguage`.  
For more information, refer to [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html).  
To transcribe speech in Modern Standard Arabic (`ar-SA`)in AWS GovCloud (US) (US-West, us-gov-west-1), AWS GovCloud (US) (US-East, us-gov-east-1), in Canada (Calgary) ca-west-1 and Africa (Cape Town) af-south-1, your media file must be encoded at a sample rate of 16,000 Hz or higher.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** [Media](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-Media"></a>
Describes the Amazon S3 location of the media file you want to use in your request.  
Type: [Media](API_Media.md) object  
Required: Yes

 ** [MediaFormat](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-MediaFormat"></a>
Specify the format of your input media file.  
Type: String  
Valid Values: `mp3 | mp4 | wav | flac | ogg | amr | webm | m4a`   
Required: No

 ** [MediaSampleRateHertz](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-MediaSampleRateHertz"></a>
The sample rate, in hertz, of the audio track in your input media file.  
If you do not specify the media sample rate, Amazon Transcribe determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe. If there's a mismatch between the value that you specify and the value detected, your job fails. In most cases, you can omit `MediaSampleRateHertz` and let Amazon Transcribe determine the sample rate.  
Type: Integer  
Valid Range: Minimum value of 8000. Maximum value of 48000.  
Required: No

 ** [ModelSettings](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-ModelSettings"></a>
Specify the custom language model you want to include with your transcription job. If you include `ModelSettings` in your request, you must include the `LanguageModelName` sub-parameter.  
For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html).  
Type: [ModelSettings](API_ModelSettings.md) object  
Required: No

 ** [OutputBucketName](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-OutputBucketName"></a>
The name of the Amazon S3 bucket where you want your transcription output stored. Do not include the `S3://` prefix of the specified bucket.  
If you want your output to go to a sub-folder of this bucket, specify it using the `OutputKey` parameter; `OutputBucketName` only accepts the name of a bucket.  
For example, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET`, set `OutputBucketName` to `DOC-EXAMPLE-BUCKET`. However, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET/test-files/`, set `OutputBucketName` to `DOC-EXAMPLE-BUCKET` and `OutputKey` to `test-files/`.  
Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the [AWS Management Console](https://console.aws.amazon.com/s3). See also [Permissions Required for IAM User Roles](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user).  
If you do not specify `OutputBucketName`, your transcript is placed in a service-managed Amazon S3 bucket and you are provided with a URI to access your transcript.  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`   
Required: No

 ** [OutputEncryptionKMSKeyId](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-OutputEncryptionKMSKeyId"></a>
The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your transcription output.  
KMS key ARNs have the format `arn:partition:kms:region:account:key/key-id`. For example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. For more information, see [ KMS key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN).  
If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).  
Note that the role making the [StartTranscriptionJob](#API_StartTranscriptionJob) request and the role specified in the `DataAccessRoleArn` request parameter (if present) must have permission to use the specified KMS key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`   
Required: No

 ** [OutputKey](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-OutputKey"></a>
Use in combination with `OutputBucketName` to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your transcription job (`TranscriptionJobName`).  
Here are some examples of how you can use `OutputKey`:  
+ If you specify 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName` and 'my-transcript.json' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript.json`.
+ If you specify 'my-first-transcription' as the `TranscriptionJobName`, 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName`, and 'my-transcript' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json`.
+ If you specify 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName` and 'test-files/my-transcript.json' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json`.
+ If you specify 'my-first-transcription' as the `TranscriptionJobName`, 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName`, and 'test-files/my-transcript' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json`.
If you specify the name of an Amazon S3 bucket sub-folder that doesn't exist, one is created for you.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9-_.!*'()/]{1,1024}$`   
Required: No

 ** [Settings](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-Settings"></a>
Specify additional optional settings in your [StartTranscriptionJob](#API_StartTranscriptionJob) request, including channel identification, alternative transcriptions, speaker partitioning. You can use that to apply custom vocabularies and vocabulary filters.  
If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but **do not** want to use automatic language identification, use `Settings` with the `VocabularyName` or `VocabularyFilterName` (or both) sub-parameter.  
If you're using automatic language identification with your request and want to include a custom language model, a custom vocabulary, or a custom vocabulary filter, use instead the ` LanguageIdSettings ` parameter with the `LanguageModelName`, `VocabularyName` or `VocabularyFilterName` sub-parameters.  
Type: [Settings](API_Settings.md) object  
Required: No

 ** [Subtitles](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-Subtitles"></a>
Produces subtitle files for your input media. You can specify WebVTT (\*.vtt) and SubRip (\*.srt) formats.  
Type: [Subtitles](API_Subtitles.md) object  
Required: No

 ** [Tags](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to a new transcription job at the time you start this new job.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [ToxicityDetection](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-ToxicityDetection"></a>
Enables toxic speech detection in your transcript. If you include `ToxicityDetection` in your request, you must also include `ToxicityCategories`.  
For information on the types of toxic speech Amazon Transcribe can detect, see [Detecting toxic speech](https://docs.aws.amazon.com/transcribe/latest/dg/toxic-language.html).  
Type: Array of [ToxicityDetectionSettings](API_ToxicityDetectionSettings.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** [TranscriptionJobName](#API_StartTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartTranscriptionJob-request-TranscriptionJobName"></a>
A unique name, chosen by you, for your transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the `OutputKey` parameter.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account. If you try to create a new job with the same name as an existing job, you get a `ConflictException` error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_StartTranscriptionJob_ResponseSyntax"></a>

```
{
   "TranscriptionJob": { 
      "CompletionTime": number,
      "ContentRedaction": { 
         "PiiEntityTypes": [ "string" ],
         "RedactionOutput": "string",
         "RedactionType": "string"
      },
      "CreationTime": number,
      "FailureReason": "string",
      "IdentifiedLanguageScore": number,
      "IdentifyLanguage": boolean,
      "IdentifyMultipleLanguages": boolean,
      "JobExecutionSettings": { 
         "AllowDeferredExecution": boolean,
         "DataAccessRoleArn": "string"
      },
      "LanguageCode": "string",
      "LanguageCodes": [ 
         { 
            "DurationInSeconds": number,
            "LanguageCode": "string"
         }
      ],
      "LanguageIdSettings": { 
         "string" : { 
            "LanguageModelName": "string",
            "VocabularyFilterName": "string",
            "VocabularyName": "string"
         }
      },
      "LanguageOptions": [ "string" ],
      "Media": { 
         "MediaFileUri": "string",
         "RedactedMediaFileUri": "string"
      },
      "MediaFormat": "string",
      "MediaSampleRateHertz": number,
      "ModelSettings": { 
         "LanguageModelName": "string"
      },
      "Settings": { 
         "ChannelIdentification": boolean,
         "MaxAlternatives": number,
         "MaxSpeakerLabels": number,
         "ShowAlternatives": boolean,
         "ShowSpeakerLabels": boolean,
         "VocabularyFilterMethod": "string",
         "VocabularyFilterName": "string",
         "VocabularyName": "string"
      },
      "StartTime": number,
      "Subtitles": { 
         "Formats": [ "string" ],
         "OutputStartIndex": number,
         "SubtitleFileUris": [ "string" ]
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "ToxicityDetection": [ 
         { 
            "ToxicityCategories": [ "string" ]
         }
      ],
      "Transcript": { 
         "RedactedTranscriptFileUri": "string",
         "TranscriptFileUri": "string"
      },
      "TranscriptionJobName": "string",
      "TranscriptionJobStatus": "string"
   }
}
```

## Response Elements
<a name="API_StartTranscriptionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TranscriptionJob](#API_StartTranscriptionJob_ResponseSyntax) **   <a name="transcribe-StartTranscriptionJob-response-TranscriptionJob"></a>
Provides detailed information about the current transcription job, including job status and, if applicable, failure reason.  
Type: [TranscriptionJob](API_TranscriptionJob.md) object

## Errors
<a name="API_StartTranscriptionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** ConflictException **   
A resource already exists with this name. Resource names must be unique within an AWS account.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_StartTranscriptionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/StartTranscriptionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/StartTranscriptionJob) 