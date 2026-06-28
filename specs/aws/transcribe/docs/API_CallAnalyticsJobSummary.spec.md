---
id: "@specs/aws/transcribe/docs/API_CallAnalyticsJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CallAnalyticsJobSummary"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CallAnalyticsJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CallAnalyticsJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CallAnalyticsJobSummary
<a name="API_CallAnalyticsJobSummary"></a>

Provides detailed information about a specific Call Analytics job.

## Contents
<a name="API_CallAnalyticsJobSummary_Contents"></a>

 ** CallAnalyticsJobDetails **   <a name="transcribe-Type-CallAnalyticsJobSummary-CallAnalyticsJobDetails"></a>
Provides detailed information about a call analytics job, including information about skipped analytics features.  
Type: [CallAnalyticsJobDetails](API_CallAnalyticsJobDetails.md) object  
Required: No

 ** CallAnalyticsJobName **   <a name="transcribe-Type-CallAnalyticsJobSummary-CallAnalyticsJobName"></a>
The name of the Call Analytics job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** CallAnalyticsJobStatus **   <a name="transcribe-Type-CallAnalyticsJobSummary-CallAnalyticsJobStatus"></a>
Provides the status of your Call Analytics job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `TranscriptFileUri` (or `RedactedTranscriptFileUri`, if you requested transcript redaction). If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** CompletionTime **   <a name="transcribe-Type-CallAnalyticsJobSummary-CompletionTime"></a>
The date and time the specified Call Analytics job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** CreationTime **   <a name="transcribe-Type-CallAnalyticsJobSummary-CreationTime"></a>
The date and time the specified Call Analytics job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** FailureReason **   <a name="transcribe-Type-CallAnalyticsJobSummary-FailureReason"></a>
If `CallAnalyticsJobStatus` is `FAILED`, `FailureReason` contains information about why the Call Analytics job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-CallAnalyticsJobSummary-LanguageCode"></a>
The language code used to create your Call Analytics transcription.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** StartTime **   <a name="transcribe-Type-CallAnalyticsJobSummary-StartTime"></a>
The date and time your Call Analytics job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

## See Also
<a name="API_CallAnalyticsJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CallAnalyticsJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CallAnalyticsJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CallAnalyticsJobSummary) 