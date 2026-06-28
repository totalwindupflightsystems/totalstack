---
id: "@specs/aws/transcribe/docs/API_streaming_LanguageWithScore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LanguageWithScore"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# LanguageWithScore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_LanguageWithScore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LanguageWithScore
<a name="API_streaming_LanguageWithScore"></a>

The language code that represents the language identified in your audio, including the associated confidence score. If you enabled channel identification in your request and each channel contained a different language, you will have more than one `LanguageWithScore` result.

## Contents
<a name="API_streaming_LanguageWithScore_Contents"></a>

 ** LanguageCode **   <a name="transcribe-Type-streaming_LanguageWithScore-LanguageCode"></a>
The language code of the identified language.  
Type: String  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR | ja-JP | ko-KR | zh-CN | th-TH | es-ES | ar-SA | pt-PT | ca-ES | ar-AE | hi-IN | zh-HK | nl-NL | no-NO | sv-SE | pl-PL | fi-FI | zh-TW | en-IN | en-IE | en-NZ | en-AB | en-ZA | en-WL | de-CH | af-ZA | eu-ES | hr-HR | cs-CZ | da-DK | fa-IR | gl-ES | el-GR | he-IL | id-ID | lv-LV | ms-MY | ro-RO | ru-RU | sr-RS | sk-SK | so-SO | tl-PH | uk-UA | vi-VN | zu-ZA | am-ET | be-BY | bg-BG | bn-IN | bs-BA | ckb-IQ | ckb-IR | cy-WL | es-MX | et-ET | fa-AF | gu-IN | ht-HT | hu-HU | hy-AM | is-IS | jv-ID | ka-GE | kab-DZ | kk-KZ | km-KH | kn-IN | lg-IN | lt-LT | mk-MK | ml-IN | mr-IN | my-MM | ne-NP | or-IN | pa-IN | ps-AF | si-LK | sl-SI | sq-AL | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | ta-IN | te-IN | tr-TR | uz-UZ`   
Required: No

 ** Score **   <a name="transcribe-Type-streaming_LanguageWithScore-Score"></a>
The confidence score associated with the identified language code. Confidence scores are values between zero and one; larger values indicate a higher confidence in the identified language.  
Type: Double  
Required: No

## See Also
<a name="API_streaming_LanguageWithScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/LanguageWithScore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/LanguageWithScore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/LanguageWithScore) 