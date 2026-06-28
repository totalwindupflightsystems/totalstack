---
id: "@specs/aws/transcribe/docs/API_LanguageCodeItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LanguageCodeItem"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# LanguageCodeItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_LanguageCodeItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LanguageCodeItem
<a name="API_LanguageCodeItem"></a>

Provides information on the speech contained in a discreet utterance when multi-language identification is enabled in your request. This utterance represents a block of speech consisting of one language, preceded or followed by a block of speech in a different language.

## Contents
<a name="API_LanguageCodeItem_Contents"></a>

 ** DurationInSeconds **   <a name="transcribe-Type-LanguageCodeItem-DurationInSeconds"></a>
Provides the total time, in seconds, each identified language is spoken in your media.  
Type: Float  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-LanguageCodeItem-LanguageCode"></a>
Provides the language code for each language identified in your media.  
Type: String  
Valid Values: `af-ZA | ar-AE | ar-SA | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fa-IR | fr-CA | fr-FR | he-IL | hi-IN | id-ID | it-IT | ja-JP | ko-KR | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`   
Required: No

## See Also
<a name="API_LanguageCodeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/LanguageCodeItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/LanguageCodeItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/LanguageCodeItem) 