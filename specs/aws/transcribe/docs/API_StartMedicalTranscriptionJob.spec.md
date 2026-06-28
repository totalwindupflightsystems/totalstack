---
id: "@specs/aws/transcribe/docs/API_StartMedicalTranscriptionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartMedicalTranscriptionJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartMedicalTranscriptionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_StartMedicalTranscriptionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartMedicalTranscriptionJob
<a name="API_StartMedicalTranscriptionJob"></a>

Transcribes the audio from a medical dictation or conversation and applies any additional Request Parameters you choose to include in your request.

In addition to many standard transcription features, Amazon Transcribe Medical provides you with a robust medical vocabulary and, optionally, content identification, which adds flags to personal health information (PHI). To learn more about these features, refer to [How Amazon Transcribe Medical works](https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works-med.html).

To make a `StartMedicalTranscriptionJob` request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the `Media` parameter.

You must include the following parameters in your `StartMedicalTranscriptionJob` request:
+  `region`: The AWS Region where you are making your request. For a list of AWS Regions supported with Amazon Transcribe, refer to [Amazon Transcribe endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html).
+  `MedicalTranscriptionJobName`: A custom name you create for your transcription job that is unique within your AWS account.
+  `Media` (`MediaFileUri`): The Amazon S3 location of your media file.
+  `LanguageCode`: This must be `en-US`.
+  `OutputBucketName`: The Amazon S3 bucket where you want your transcript stored. If you want your output stored in a sub-folder of this bucket, you must also include `OutputKey`.
+  `Specialty`: This must be `PRIMARYCARE`.
+  `Type`: Choose whether your audio is a conversation or a dictation.

## Request Syntax
<a name="API_StartMedicalTranscriptionJob_RequestSyntax"></a>

```
{
   "ContentIdentificationType": "{{string}}",
   "KMSEncryptionContext": { 
      "{{string}}" : "{{string}}" 
   },
   "LanguageCode": "{{string}}",
   "Media": { 
      "MediaFileUri": "{{string}}",
      "RedactedMediaFileUri": "{{string}}"
   },
   "MediaFormat": "{{string}}",
   "MediaSampleRateHertz": {{number}},
   "MedicalTranscriptionJobName": "{{string}}",
   "OutputBucketName": "{{string}}",
   "OutputEncryptionKMSKeyId": "{{string}}",
   "OutputKey": "{{string}}",
   "Settings": { 
      "ChannelIdentification": {{boolean}},
      "MaxAlternatives": {{number}},
      "MaxSpeakerLabels": {{number}},
      "ShowAlternatives": {{boolean}},
      "ShowSpeakerLabels": {{boolean}},
      "VocabularyName": "{{string}}"
   },
   "Specialty": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMedicalTranscriptionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContentIdentificationType](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-ContentIdentificationType"></a>
Labels all personal health information (PHI) identified in your transcript. For more information, see [Identifying personal health information (PHI) in a transcription](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html).  
Type: String  
Valid Values: `PHI`   
Required: No

 ** [KMSEncryptionContext](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-KMSEncryptionContext"></a>
A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see [AWS KMS encryption context](https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context) and [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html).  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

 ** [LanguageCode](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-LanguageCode"></a>
The language code that represents the language spoken in the input media file. US English (`en-US`) is the only valid value for medical transcription jobs. Any other value you enter for language code results in a `BadRequestException` error.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: Yes

 ** [Media](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-Media"></a>
Describes the Amazon S3 location of the media file you want to use in your request.  
For information on supported media formats, refer to the `MediaFormat` parameter or the [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) section in the Amazon S3 Developer Guide.  
Type: [Media](API_Media.md) object  
Required: Yes

 ** [MediaFormat](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-MediaFormat"></a>
Specify the format of your input media file.  
Type: String  
Valid Values: `mp3 | mp4 | wav | flac | ogg | amr | webm | m4a`   
Required: No

 ** [MediaSampleRateHertz](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-MediaSampleRateHertz"></a>
The sample rate, in hertz, of the audio track in your input media file.  
If you do not specify the media sample rate, Amazon Transcribe Medical determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe Medical; if there's a mismatch between the value that you specify and the value detected, your job fails. Therefore, in most cases, it's advised to omit `MediaSampleRateHertz` and let Amazon Transcribe Medical determine the sample rate.  
Type: Integer  
Valid Range: Minimum value of 16000. Maximum value of 48000.  
Required: No

 ** [MedicalTranscriptionJobName](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-MedicalTranscriptionJobName"></a>
A unique name, chosen by you, for your medical transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the `OutputKey` parameter.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account. If you try to create a new job with the same name as an existing job, you get a `ConflictException` error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [OutputBucketName](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-OutputBucketName"></a>
The name of the Amazon S3 bucket where you want your medical transcription output stored. Do not include the `S3://` prefix of the specified bucket.  
If you want your output to go to a sub-folder of this bucket, specify it using the `OutputKey` parameter; `OutputBucketName` only accepts the name of a bucket.  
For example, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET`, set `OutputBucketName` to `DOC-EXAMPLE-BUCKET`. However, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET/test-files/`, set `OutputBucketName` to `DOC-EXAMPLE-BUCKET` and `OutputKey` to `test-files/`.  
Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the [AWS Management Console](https://console.aws.amazon.com/s3). See also [Permissions Required for IAM User Roles](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user).  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`   
Required: Yes

 ** [OutputEncryptionKMSKeyId](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-OutputEncryptionKMSKeyId"></a>
The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your medical transcription output.  
KMS key ARNs have the format `arn:partition:kms:region:account:key/key-id`. For example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. For more information, see [ KMS key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN).  
If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).  
Note that the role making the [StartMedicalTranscriptionJob](#API_StartMedicalTranscriptionJob) request and the role specified in the `DataAccessRoleArn` request parameter (if present) must have permission to use the specified KMS key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`   
Required: No

 ** [OutputKey](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-OutputKey"></a>
Use in combination with `OutputBucketName` to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your medical transcription job (`MedicalTranscriptionJobName`).  
Here are some examples of how you can use `OutputKey`:  
+ If you specify 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName` and 'my-transcript.json' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript.json`.
+ If you specify 'my-first-transcription' as the `MedicalTranscriptionJobName`, 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName`, and 'my-transcript' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json`.
+ If you specify 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName` and 'test-files/my-transcript.json' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json`.
+ If you specify 'my-first-transcription' as the `MedicalTranscriptionJobName`, 'DOC-EXAMPLE-BUCKET' as the `OutputBucketName`, and 'test-files/my-transcript' as the `OutputKey`, your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json`.
If you specify the name of an Amazon S3 bucket sub-folder that doesn't exist, one is created for you.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9-_.!*'()/]{1,1024}$`   
Required: No

 ** [Settings](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-Settings"></a>
Specify additional optional settings in your [StartMedicalTranscriptionJob](#API_StartMedicalTranscriptionJob) request, including channel identification, alternative transcriptions, and speaker partitioning. You can use that to apply custom vocabularies to your transcription job.  
Type: [MedicalTranscriptionSetting](API_MedicalTranscriptionSetting.md) object  
Required: No

 ** [Specialty](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-Specialty"></a>
Specify the predominant medical specialty represented in your media. For batch transcriptions, `PRIMARYCARE` is the only valid value. If you require additional specialties, refer to [StartMedicalStreamTranscription](API_streaming_StartMedicalStreamTranscription.md).  
Type: String  
Valid Values: `PRIMARYCARE`   
Required: Yes

 ** [Tags](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to a new medical transcription job at the time you start this new job.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [Type](#API_StartMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-request-Type"></a>
Specify whether your input media contains only one person (`DICTATION`) or contains a conversation between two people (`CONVERSATION`).  
For example, `DICTATION` could be used for a medical professional wanting to transcribe voice memos; `CONVERSATION` could be used for transcribing the doctor-patient dialogue during the patient's office visit.  
Type: String  
Valid Values: `CONVERSATION | DICTATION`   
Required: Yes

## Response Syntax
<a name="API_StartMedicalTranscriptionJob_ResponseSyntax"></a>

```
{
   "MedicalTranscriptionJob": { 
      "CompletionTime": number,
      "ContentIdentificationType": "string",
      "CreationTime": number,
      "FailureReason": "string",
      "LanguageCode": "string",
      "Media": { 
         "MediaFileUri": "string",
         "RedactedMediaFileUri": "string"
      },
      "MediaFormat": "string",
      "MediaSampleRateHertz": number,
      "MedicalTranscriptionJobName": "string",
      "Settings": { 
         "ChannelIdentification": boolean,
         "MaxAlternatives": number,
         "MaxSpeakerLabels": number,
         "ShowAlternatives": boolean,
         "ShowSpeakerLabels": boolean,
         "VocabularyName": "string"
      },
      "Specialty": "string",
      "StartTime": number,
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "Transcript": { 
         "TranscriptFileUri": "string"
      },
      "TranscriptionJobStatus": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_StartMedicalTranscriptionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MedicalTranscriptionJob](#API_StartMedicalTranscriptionJob_ResponseSyntax) **   <a name="transcribe-StartMedicalTranscriptionJob-response-MedicalTranscriptionJob"></a>
Provides detailed information about the current medical transcription job, including job status and, if applicable, failure reason.  
Type: [MedicalTranscriptionJob](API_MedicalTranscriptionJob.md) object

## Errors
<a name="API_StartMedicalTranscriptionJob_Errors"></a>

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
<a name="API_StartMedicalTranscriptionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/StartMedicalTranscriptionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/StartMedicalTranscriptionJob) 