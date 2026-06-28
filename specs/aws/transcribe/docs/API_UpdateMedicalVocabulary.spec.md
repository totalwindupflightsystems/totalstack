---
id: "@specs/aws/transcribe/docs/API_UpdateMedicalVocabulary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateMedicalVocabulary"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# UpdateMedicalVocabulary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_UpdateMedicalVocabulary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateMedicalVocabulary
<a name="API_UpdateMedicalVocabulary"></a>

Updates an existing custom medical vocabulary with new values. This operation overwrites all existing information with your new values; you cannot append new terms onto an existing custom vocabulary.

## Request Syntax
<a name="API_UpdateMedicalVocabulary_RequestSyntax"></a>

```
{
   "LanguageCode": "{{string}}",
   "VocabularyFileUri": "{{string}}",
   "VocabularyName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMedicalVocabulary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_UpdateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-request-LanguageCode"></a>
The language code that represents the language of the entries in the custom vocabulary you want to update. US English (`en-US`) is the only language supported with Amazon Transcribe Medical.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: Yes

 ** [VocabularyFileUri](#API_UpdateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-request-VocabularyFileUri"></a>
The Amazon S3 location of the text file that contains your custom medical vocabulary. The URI must be located in the same AWS Region as the resource you're calling.  
Here's an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: Yes

 ** [VocabularyName](#API_UpdateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-request-VocabularyName"></a>
The name of the custom medical vocabulary you want to update. Custom medical vocabulary names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_UpdateMedicalVocabulary_ResponseSyntax"></a>

```
{
   "LanguageCode": "string",
   "LastModifiedTime": number,
   "VocabularyName": "string",
   "VocabularyState": "string"
}
```

## Response Elements
<a name="API_UpdateMedicalVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LanguageCode](#API_UpdateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-response-LanguageCode"></a>
The language code you selected for your custom medical vocabulary. US English (`en-US`) is the only language supported with Amazon Transcribe Medical.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA` 

 ** [LastModifiedTime](#API_UpdateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-response-LastModifiedTime"></a>
The date and time the specified custom medical vocabulary was last updated.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp

 ** [VocabularyName](#API_UpdateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-response-VocabularyName"></a>
The name of the updated custom medical vocabulary.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyState](#API_UpdateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-UpdateMedicalVocabulary-response-VocabularyState"></a>
The processing state of your custom medical vocabulary. If the state is `READY`, you can use the custom vocabulary in a `StartMedicalTranscriptionJob` request.  
Type: String  
Valid Values: `PENDING | READY | FAILED` 

## Errors
<a name="API_UpdateMedicalVocabulary_Errors"></a>

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

 ** NotFoundException **   
We can't find the requested resource. Check that the specified name is correct and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateMedicalVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/UpdateMedicalVocabulary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/UpdateMedicalVocabulary) 