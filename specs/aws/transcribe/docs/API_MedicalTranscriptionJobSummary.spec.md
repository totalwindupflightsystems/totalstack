---
id: "@specs/aws/transcribe/docs/API_MedicalTranscriptionJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalTranscriptionJobSummary"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalTranscriptionJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalTranscriptionJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalTranscriptionJobSummary
<a name="API_MedicalTranscriptionJobSummary"></a>

Provides detailed information about a specific medical transcription job.

## Contents
<a name="API_MedicalTranscriptionJobSummary_Contents"></a>

 ** CompletionTime **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-CompletionTime"></a>
The date and time the specified medical transcription job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** ContentIdentificationType **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-ContentIdentificationType"></a>
Labels all personal health information (PHI) identified in your transcript. For more information, see [Identifying personal health information (PHI) in a transcription](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html).  
Type: String  
Valid Values: `PHI`   
Required: No

 ** CreationTime **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-CreationTime"></a>
The date and time the specified medical transcription job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** FailureReason **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-FailureReason"></a>
If `TranscriptionJobStatus` is `FAILED`, `FailureReason` contains information about why the transcription job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-LanguageCode"></a>
The language code used to create your medical transcription. US English (`en-US`) is the only supported language for medical transcriptions.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** MedicalTranscriptionJobName **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-MedicalTranscriptionJobName"></a>
The name of the medical transcription job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** OutputLocationType **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-OutputLocationType"></a>
Indicates where the specified medical transcription output is stored.  
If the value is `CUSTOMER_BUCKET`, the location is the Amazon S3 bucket you specified using the `OutputBucketName` parameter in your [StartMedicalTranscriptionJob](API_StartMedicalTranscriptionJob.md) request. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.  
If the value is `SERVICE_BUCKET`, the location is a service-managed Amazon S3 bucket. To access a transcript stored in a service-managed bucket, use the URI shown in the `TranscriptFileUri` field.  
Type: String  
Valid Values: `CUSTOMER_BUCKET | SERVICE_BUCKET`   
Required: No

 ** Specialty **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-Specialty"></a>
Provides the medical specialty represented in your media.  
Type: String  
Valid Values: `PRIMARYCARE`   
Required: No

 ** StartTime **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-StartTime"></a>
The date and time your medical transcription job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** TranscriptionJobStatus **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-TranscriptionJobStatus"></a>
Provides the status of your medical transcription job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** Type **   <a name="transcribe-Type-MedicalTranscriptionJobSummary-Type"></a>
Indicates whether the input media is a dictation or a conversation, as specified in the `StartMedicalTranscriptionJob` request.  
Type: String  
Valid Values: `CONVERSATION | DICTATION`   
Required: No

## See Also
<a name="API_MedicalTranscriptionJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalTranscriptionJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalTranscriptionJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalTranscriptionJobSummary) 