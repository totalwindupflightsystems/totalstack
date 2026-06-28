---
id: "@specs/aws/transcribe/docs/API_CreateMedicalVocabulary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateMedicalVocabulary"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CreateMedicalVocabulary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CreateMedicalVocabulary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateMedicalVocabulary
<a name="API_CreateMedicalVocabulary"></a>

Creates a new custom medical vocabulary.

Before creating a new custom medical vocabulary, you must first upload a text file that contains your vocabulary table into an Amazon S3 bucket. Note that this differs from [CreateVocabulary](API_CreateVocabulary.md), where you can include a list of terms within your request using the `Phrases` flag; `CreateMedicalVocabulary` does not support the `Phrases` flag and only accepts vocabularies in table format.

Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary request fails. Refer to [Character Sets for Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html) to get the character set for your language.

For more information, see [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html).

## Request Syntax
<a name="API_CreateMedicalVocabulary_RequestSyntax"></a>

```
{
   "LanguageCode": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VocabularyFileUri": "{{string}}",
   "VocabularyName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMedicalVocabulary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_CreateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-CreateMedicalVocabulary-request-LanguageCode"></a>
The language code that represents the language of the entries in your custom vocabulary. US English (`en-US`) is the only language supported with Amazon Transcribe Medical.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: Yes

 ** [Tags](#API_CreateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-CreateMedicalVocabulary-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to a new custom medical vocabulary at the time you create this new custom vocabulary.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [VocabularyFileUri](#API_CreateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-CreateMedicalVocabulary-request-VocabularyFileUri"></a>
The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary. The URI must be in the same AWS Region as the resource you're calling.  
Here's an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: Yes

 ** [VocabularyName](#API_CreateMedicalVocabulary_RequestSyntax) **   <a name="transcribe-CreateMedicalVocabulary-request-VocabularyName"></a>
A unique name, chosen by you, for your new custom medical vocabulary.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account. If you try to create a new custom medical vocabulary with the same name as an existing custom medical vocabulary, you get a `ConflictException` error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_CreateMedicalVocabulary_ResponseSyntax"></a>

```
{
   "FailureReason": "string",
   "LanguageCode": "string",
   "LastModifiedTime": number,
   "VocabularyName": "string",
   "VocabularyState": "string"
}
```

## Response Elements
<a name="API_CreateMedicalVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailureReason](#API_CreateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-CreateMedicalVocabulary-response-FailureReason"></a>
If `VocabularyState` is `FAILED`, `FailureReason` contains information about why the medical transcription job request failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String

 ** [LanguageCode](#API_CreateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-CreateMedicalVocabulary-response-LanguageCode"></a>
The language code you selected for your custom medical vocabulary. US English (`en-US`) is the only language supported with Amazon Transcribe Medical.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA` 

 ** [LastModifiedTime](#API_CreateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-CreateMedicalVocabulary-response-LastModifiedTime"></a>
The date and time you created your custom medical vocabulary.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp

 ** [VocabularyName](#API_CreateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-CreateMedicalVocabulary-response-VocabularyName"></a>
The name you chose for your custom medical vocabulary.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyState](#API_CreateMedicalVocabulary_ResponseSyntax) **   <a name="transcribe-CreateMedicalVocabulary-response-VocabularyState"></a>
The processing state of your custom medical vocabulary. If the state is `READY`, you can use the custom vocabulary in a `StartMedicalTranscriptionJob` request.  
Type: String  
Valid Values: `PENDING | READY | FAILED` 

## Errors
<a name="API_CreateMedicalVocabulary_Errors"></a>

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
<a name="API_CreateMedicalVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/CreateMedicalVocabulary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CreateMedicalVocabulary) 