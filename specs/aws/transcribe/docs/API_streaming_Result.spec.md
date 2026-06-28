---
id: "@specs/aws/transcribe/docs/API_streaming_Result"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Result"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Result

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_Result
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Result
<a name="API_streaming_Result"></a>

The `Result` associated with a ` Transcript `.

Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.

## Contents
<a name="API_streaming_Result_Contents"></a>

 ** Alternatives **   <a name="transcribe-Type-streaming_Result-Alternatives"></a>
A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of `Items`, `Entities`, or `Transcript`.  
Type: Array of [Alternative](API_streaming_Alternative.md) objects  
Required: No

 ** ChannelId **   <a name="transcribe-Type-streaming_Result-ChannelId"></a>
Indicates which audio channel is associated with the `Result`.  
Type: String  
Required: No

 ** EndTime **   <a name="transcribe-Type-streaming_Result-EndTime"></a>
The end time of the `Result` in seconds, with millisecond precision (e.g., 1.056).  
Type: Double  
Required: No

 ** IsPartial **   <a name="transcribe-Type-streaming_Result-IsPartial"></a>
Indicates if the segment is complete.  
If `IsPartial` is `true`, the segment is not complete. If `IsPartial` is `false`, the segment is complete.  
Type: Boolean  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-streaming_Result-LanguageCode"></a>
The language code that represents the language spoken in your audio stream.  
Type: String  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR | ja-JP | ko-KR | zh-CN | th-TH | es-ES | ar-SA | pt-PT | ca-ES | ar-AE | hi-IN | zh-HK | nl-NL | no-NO | sv-SE | pl-PL | fi-FI | zh-TW | en-IN | en-IE | en-NZ | en-AB | en-ZA | en-WL | de-CH | af-ZA | eu-ES | hr-HR | cs-CZ | da-DK | fa-IR | gl-ES | el-GR | he-IL | id-ID | lv-LV | ms-MY | ro-RO | ru-RU | sr-RS | sk-SK | so-SO | tl-PH | uk-UA | vi-VN | zu-ZA | am-ET | be-BY | bg-BG | bn-IN | bs-BA | ckb-IQ | ckb-IR | cy-WL | es-MX | et-ET | fa-AF | gu-IN | ht-HT | hu-HU | hy-AM | is-IS | jv-ID | ka-GE | kab-DZ | kk-KZ | km-KH | kn-IN | lg-IN | lt-LT | mk-MK | ml-IN | mr-IN | my-MM | ne-NP | or-IN | pa-IN | ps-AF | si-LK | sl-SI | sq-AL | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | ta-IN | te-IN | tr-TR | uz-UZ`   
Required: No

 ** LanguageIdentification **   <a name="transcribe-Type-streaming_Result-LanguageIdentification"></a>
The language code of the dominant language identified in your stream.  
If you enabled channel identification and each channel of your audio contains a different language, you may have more than one result.  
Type: Array of [LanguageWithScore](API_streaming_LanguageWithScore.md) objects  
Required: No

 ** ResultId **   <a name="transcribe-Type-streaming_Result-ResultId"></a>
Provides a unique identifier for the `Result`.  
Type: String  
Required: No

 ** StartTime **   <a name="transcribe-Type-streaming_Result-StartTime"></a>
The start time of the `Result` in seconds, with millisecond precision (e.g., 1.056).  
Type: Double  
Required: No

## See Also
<a name="API_streaming_Result_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/Result) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/Result) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/Result) 