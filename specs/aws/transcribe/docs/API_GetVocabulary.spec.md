---
id: "@specs/aws/transcribe/docs/API_GetVocabulary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetVocabulary"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetVocabulary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_GetVocabulary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetVocabulary
<a name="API_GetVocabulary"></a>

Provides information about the specified custom vocabulary.

To view the status of the specified custom vocabulary, check the `VocabularyState` field. If the status is `READY`, your custom vocabulary is available to use. If the status is `FAILED`, `FailureReason` provides details on why your custom vocabulary failed.

To get a list of your custom vocabularies, use the [ListVocabularies](API_ListVocabularies.md) operation.

## Request Syntax
<a name="API_GetVocabulary_RequestSyntax"></a>

```
{
   "VocabularyName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetVocabulary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VocabularyName](#API_GetVocabulary_RequestSyntax) **   <a name="transcribe-GetVocabulary-request-VocabularyName"></a>
The name of the custom vocabulary you want information about. Custom vocabulary names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_GetVocabulary_ResponseSyntax"></a>

```
{
   "DownloadUri": "string",
   "FailureReason": "string",
   "LanguageCode": "string",
   "LastModifiedTime": number,
   "VocabularyName": "string",
   "VocabularyState": "string"
}
```

## Response Elements
<a name="API_GetVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DownloadUri](#API_GetVocabulary_ResponseSyntax) **   <a name="transcribe-GetVocabulary-response-DownloadUri"></a>
The Amazon S3 location where the custom vocabulary is stored; use this URI to view or download the custom vocabulary.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+` 

 ** [FailureReason](#API_GetVocabulary_ResponseSyntax) **   <a name="transcribe-GetVocabulary-response-FailureReason"></a>
If `VocabularyState` is `FAILED`, `FailureReason` contains information about why the custom vocabulary request failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String

 ** [LanguageCode](#API_GetVocabulary_ResponseSyntax) **   <a name="transcribe-GetVocabulary-response-LanguageCode"></a>
The language code you selected for your custom vocabulary.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA` 

 ** [LastModifiedTime](#API_GetVocabulary_ResponseSyntax) **   <a name="transcribe-GetVocabulary-response-LastModifiedTime"></a>
The date and time the specified custom vocabulary was last modified.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp

 ** [VocabularyName](#API_GetVocabulary_ResponseSyntax) **   <a name="transcribe-GetVocabulary-response-VocabularyName"></a>
The name of the custom vocabulary you requested information about.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyState](#API_GetVocabulary_ResponseSyntax) **   <a name="transcribe-GetVocabulary-response-VocabularyState"></a>
The processing state of your custom vocabulary. If the state is `READY`, you can use the custom vocabulary in a `StartTranscriptionJob` request.  
Type: String  
Valid Values: `PENDING | READY | FAILED` 

## Errors
<a name="API_GetVocabulary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

 ** NotFoundException **   
We can't find the requested resource. Check that the specified name is correct and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_GetVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetVocabulary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetVocabulary) 