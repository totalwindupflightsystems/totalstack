---
id: "@specs/aws/transcribe/docs/API_VocabularyInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VocabularyInfo"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# VocabularyInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_VocabularyInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VocabularyInfo
<a name="API_VocabularyInfo"></a>

Provides information about a custom vocabulary, including the language of the custom vocabulary, when it was last modified, its name, and the processing state.

## Contents
<a name="API_VocabularyInfo_Contents"></a>

 ** LanguageCode **   <a name="transcribe-Type-VocabularyInfo-LanguageCode"></a>
The language code used to create your custom vocabulary. Each custom vocabulary must contain terms in only one language.  
A custom vocabulary can only be used to transcribe files in the same language as the custom vocabulary. For example, if you create a custom vocabulary using US English (`en-US`), you can only apply this custom vocabulary to files that contain English audio.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

 ** LastModifiedTime **   <a name="transcribe-Type-VocabularyInfo-LastModifiedTime"></a>
The date and time the specified custom vocabulary was last modified.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** VocabularyName **   <a name="transcribe-Type-VocabularyInfo-VocabularyName"></a>
A unique name, chosen by you, for your custom vocabulary. This name is case sensitive, cannot contain spaces, and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyState **   <a name="transcribe-Type-VocabularyInfo-VocabularyState"></a>
The processing state of your custom vocabulary. If the state is `READY`, you can use the custom vocabulary in a `StartTranscriptionJob` request.  
Type: String  
Valid Values: `PENDING | READY | FAILED`   
Required: No

## See Also
<a name="API_VocabularyInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/VocabularyInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/VocabularyInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/VocabularyInfo) 