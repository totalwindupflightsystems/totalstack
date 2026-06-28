---
id: "@specs/aws/transcribe/docs/API_UpdateVocabularyFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateVocabularyFilter"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# UpdateVocabularyFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_UpdateVocabularyFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateVocabularyFilter
<a name="API_UpdateVocabularyFilter"></a>

Updates an existing custom vocabulary filter with a new list of words. The new list you provide overwrites all previous entries; you cannot append new terms onto an existing custom vocabulary filter.

## Request Syntax
<a name="API_UpdateVocabularyFilter_RequestSyntax"></a>

```
{
   "DataAccessRoleArn": "{{string}}",
   "VocabularyFilterFileUri": "{{string}}",
   "VocabularyFilterName": "{{string}}",
   "Words": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateVocabularyFilter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataAccessRoleArn](#API_UpdateVocabularyFilter_RequestSyntax) **   <a name="transcribe-UpdateVocabularyFilter-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.  
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.  
For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: No

 ** [VocabularyFilterFileUri](#API_UpdateVocabularyFilter_RequestSyntax) **   <a name="transcribe-UpdateVocabularyFilter-request-VocabularyFilterFileUri"></a>
The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same AWS Region as the resource you're calling.  
Here's an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt`   
Note that if you include `VocabularyFilterFileUri` in your request, you cannot use `Words`; you must choose one or the other.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

 ** [VocabularyFilterName](#API_UpdateVocabularyFilter_RequestSyntax) **   <a name="transcribe-UpdateVocabularyFilter-request-VocabularyFilterName"></a>
The name of the custom vocabulary filter you want to update. Custom vocabulary filter names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [Words](#API_UpdateVocabularyFilter_RequestSyntax) **   <a name="transcribe-UpdateVocabularyFilter-request-Words"></a>
Use this parameter if you want to update your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for updating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the `VocabularyFilterFileUri` parameter.  
Note that if you include `Words` in your request, you cannot use `VocabularyFilterFileUri`; you must choose one or the other.  
Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to [Character Sets for Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html) to get the character set for your language.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_UpdateVocabularyFilter_ResponseSyntax"></a>

```
{
   "LanguageCode": "string",
   "LastModifiedTime": number,
   "VocabularyFilterName": "string"
}
```

## Response Elements
<a name="API_UpdateVocabularyFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LanguageCode](#API_UpdateVocabularyFilter_ResponseSyntax) **   <a name="transcribe-UpdateVocabularyFilter-response-LanguageCode"></a>
The language code you selected for your custom vocabulary filter.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA` 

 ** [LastModifiedTime](#API_UpdateVocabularyFilter_ResponseSyntax) **   <a name="transcribe-UpdateVocabularyFilter-response-LastModifiedTime"></a>
The date and time the specified custom vocabulary filter was last updated.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp

 ** [VocabularyFilterName](#API_UpdateVocabularyFilter_ResponseSyntax) **   <a name="transcribe-UpdateVocabularyFilter-response-VocabularyFilterName"></a>
The name of the updated custom vocabulary filter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

## Errors
<a name="API_UpdateVocabularyFilter_Errors"></a>

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
<a name="API_UpdateVocabularyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/UpdateVocabularyFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/UpdateVocabularyFilter) 