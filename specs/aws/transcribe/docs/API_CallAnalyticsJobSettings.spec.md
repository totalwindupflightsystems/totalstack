---
id: "@specs/aws/transcribe/docs/API_CallAnalyticsJobSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CallAnalyticsJobSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CallAnalyticsJobSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CallAnalyticsJobSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CallAnalyticsJobSettings
<a name="API_CallAnalyticsJobSettings"></a>

Provides additional optional settings for your [StartCallAnalyticsJob](API_StartCallAnalyticsJob.md) request, including content redaction, automatic language identification; allows you to apply custom language models, custom vocabulary filters, and custom vocabularies.

## Contents
<a name="API_CallAnalyticsJobSettings_Contents"></a>

 ** ContentRedaction **   <a name="transcribe-Type-CallAnalyticsJobSettings-ContentRedaction"></a>
Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript. If you use `ContentRedaction`, you must also include the sub-parameters: `RedactionOutput` and `RedactionType`. You can optionally include `PiiEntityTypes` to choose which types of PII you want to redact.  
Type: [ContentRedaction](API_ContentRedaction.md) object  
Required: No

 ** LanguageIdSettings **   <a name="transcribe-Type-CallAnalyticsJobSettings-LanguageIdSettings"></a>
If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName`, `LanguageModelName`, and `VocabularyFilterName`).  
 `LanguageIdSettings` supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.  
It's recommended that you include `LanguageOptions` when using `LanguageIdSettings` to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in `en-US` but Amazon Transcribe determines that the language spoken in your media is `en-AU`, your custom vocabulary *is not* applied to your transcription. If you include `LanguageOptions` and include `en-US` as the only English language dialect, your custom vocabulary *is* applied to your transcription.  
If you want to include a custom language model, custom vocabulary, or custom vocabulary filter with your request but **do not** want to use automatic language identification, use instead the ` CallAnalyticsJobSettings ` parameter with the `LanguageModelName`, `VocabularyName`, or `VocabularyFilterName` sub-parameters.  
For a list of languages supported with Call Analytics, refer to [Supported languages and language-specific features](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html).  
Type: String to [LanguageIdSettings](API_LanguageIdSettings.md) object map  
Map Entries: Maximum number of 5 items.  
Valid Keys: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** LanguageModelName **   <a name="transcribe-Type-CallAnalyticsJobSettings-LanguageModelName"></a>
The name of the custom language model you want to use when processing your Call Analytics job. Note that custom language model names are case sensitive.  
The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** LanguageOptions **   <a name="transcribe-Type-CallAnalyticsJobSettings-LanguageOptions"></a>
You can specify two or more language codes that represent the languages you think may be present in your media. Including more than five is not recommended. If you're unsure what languages are present, do not include this parameter.  
Including language options can improve the accuracy of language identification.  
For a list of languages supported with Call Analytics, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.  
To transcribe speech in Modern Standard Arabic (`ar-SA`) in AWS GovCloud (US) (US-West, us-gov-west-1), AWS GovCloud (US) (US-East, us-gov-east-1), Canada (Calgary) ca-west-1 and Africa (Cape Town) af-south-1, your media file must be encoded at a sample rate of 16,000 Hz or higher.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** Summarization **   <a name="transcribe-Type-CallAnalyticsJobSettings-Summarization"></a>
Contains `GenerateAbstractiveSummary`, which is a required parameter if you want to enable Generative call summarization in your Call Analytics request.  
Type: [Summarization](API_Summarization.md) object  
Required: No

 ** VocabularyFilterMethod **   <a name="transcribe-Type-CallAnalyticsJobSettings-VocabularyFilterMethod"></a>
Specify how you want your custom vocabulary filter applied to your transcript.  
To replace words with `***`, choose `mask`.  
To delete words, choose `remove`.  
To flag words without changing them, choose `tag`.  
Type: String  
Valid Values: `remove | mask | tag`   
Required: No

 ** VocabularyFilterName **   <a name="transcribe-Type-CallAnalyticsJobSettings-VocabularyFilterName"></a>
The name of the custom vocabulary filter you want to include in your Call Analytics transcription request. Custom vocabulary filter names are case sensitive.  
Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyName **   <a name="transcribe-Type-CallAnalyticsJobSettings-VocabularyName"></a>
The name of the custom vocabulary you want to include in your Call Analytics transcription request. Custom vocabulary names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

## See Also
<a name="API_CallAnalyticsJobSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CallAnalyticsJobSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CallAnalyticsJobSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CallAnalyticsJobSettings) 