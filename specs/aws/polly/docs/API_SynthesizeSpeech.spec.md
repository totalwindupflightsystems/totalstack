---
id: "@specs/aws/polly/docs/API_SynthesizeSpeech"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SynthesizeSpeech"
status: active
depends_on:
  - "@specs/aws/polly/meta"
---

# SynthesizeSpeech

> **source:** AWS Documentation
> **spec:id:** @specs/aws/polly/docs/API_SynthesizeSpeech
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SynthesizeSpeech
<a name="API_SynthesizeSpeech"></a>

Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see [How it Works](https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html).

## Request Syntax
<a name="API_SynthesizeSpeech_RequestSyntax"></a>

```
POST /v1/speech HTTP/1.1
Content-type: application/json

{
   "Engine": "{{string}}",
   "LanguageCode": "{{string}}",
   "LexiconNames": [ "{{string}}" ],
   "OutputFormat": "{{string}}",
   "SampleRate": "{{string}}",
   "SpeechMarkTypes": [ "{{string}}" ],
   "Text": "{{string}}",
   "TextType": "{{string}}",
   "VoiceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SynthesizeSpeech_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SynthesizeSpeech_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Engine](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-Engine"></a>
Specifies the engine (`standard`, `neural`, `long-form`, or `generative`) for Amazon Polly to use when processing input text for speech synthesis. Provide an engine that is supported by the voice you select. If you don't provide an engine, the standard engine is selected by default. If a chosen voice isn't supported by the standard engine, this will result in an error. For information on Amazon Polly voices and which voices are available for each engine, see [Available Voices](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html).  
Type: String  
Valid Values: `standard | neural | long-form | generative`   
Required: No

 ** [LanguageCode](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-LanguageCode"></a>
Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).   
If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html) operation for the `LanguageCode` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.  
Type: String  
Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH | en-SG`   
Required: No

 ** [LexiconNames](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-LexiconNames"></a>
List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html).  
Type: Array of strings  
Array Members: Maximum number of 5 items.  
Pattern: `[0-9A-Za-z]{1,20}`   
Required: No

 ** [OutputFormat](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-OutputFormat"></a>
 The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg\_vorbis, ogg\_opus, mu-law, a-law or pcm. For speech marks, this will be json.   
When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.   
Type: String  
Valid Values: `json | mp3 | ogg_opus | ogg_vorbis | pcm | mulaw | alaw`   
Required: Yes

 ** [SampleRate](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-SampleRate"></a>
The audio frequency specified in Hz.  
The valid values for mp3 and ogg\_vorbis are "8000", "16000", "22050", "24000", "44100" and "48000". The default value for standard voices is "22050". The default value for neural voices is "24000". The default value for long-form voices is "24000". The default value for generative voices is "24000".  
Valid values for pcm are "8000" and "16000" The default value is "16000".   
Valid value for ogg\_opus is "48000".   
Valid value for mu-law and a-law is "8000".   
Type: String  
Required: No

 ** [SpeechMarkTypes](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-SpeechMarkTypes"></a>
The type of speech marks returned for the input text.  
Type: Array of strings  
Array Members: Maximum number of 4 items.  
Valid Values: `sentence | ssml | viseme | word`   
Required: No

 ** [Text](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-Text"></a>
 Input text to synthesize. If you specify `ssml` as the `TextType`, follow the SSML format for the input text.   
Type: String  
Required: Yes

 ** [TextType](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-TextType"></a>
 Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see [Using SSML](https://docs.aws.amazon.com/polly/latest/dg/ssml.html).  
Type: String  
Valid Values: `ssml | text`   
Required: No

 ** [VoiceId](#API_SynthesizeSpeech_RequestSyntax) **   <a name="polly-SynthesizeSpeech-request-VoiceId"></a>
 Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html) operation.   
Type: String  
Valid Values: `Aditi | Amy | Astrid | Bianca | Brian | Camila | Carla | Carmen | Celine | Chantal | Conchita | Cristiano | Dora | Emma | Enrique | Ewa | Filiz | Gabrielle | Geraint | Giorgio | Gwyneth | Hans | Ines | Ivy | Jacek | Jan | Joanna | Joey | Justin | Karl | Kendra | Kevin | Kimberly | Lea | Liv | Lotte | Lucia | Lupe | Mads | Maja | Marlene | Mathieu | Matthew | Maxim | Mia | Miguel | Mizuki | Naja | Nicole | Olivia | Penelope | Raveena | Ricardo | Ruben | Russell | Salli | Seoyeon | Takumi | Tatyana | Vicki | Vitoria | Zeina | Zhiyu | Aria | Ayanda | Arlet | Hannah | Arthur | Daniel | Liam | Pedro | Kajal | Hiujin | Laura | Elin | Ida | Suvi | Ola | Hala | Andres | Sergio | Remi | Adriano | Thiago | Ruth | Stephen | Kazuha | Tomoko | Niamh | Sofie | Lisa | Isabelle | Zayd | Danielle | Gregory | Burcu | Jitka | Sabrina | Jasmine | Jihye | Ambre | Beatrice | Florian | Lennart | Lorenzo | Tiffany`   
Required: Yes

## Response Syntax
<a name="API_SynthesizeSpeech_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
x-amzn-RequestCharacters: {{RequestCharacters}}

{{AudioStream}}
```

## Response Elements
<a name="API_SynthesizeSpeech_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentType](#API_SynthesizeSpeech_ResponseSyntax) **   <a name="polly-SynthesizeSpeech-response-ContentType"></a>
 Specifies the type audio stream. This should reflect the `OutputFormat` parameter in your request.   
+  If you request `mp3` as the `OutputFormat`, the `ContentType` returned is audio/mpeg. 
+  If you request `ogg_vorbis` as the `OutputFormat`, the `ContentType` returned is audio/ogg. 
+  If you request `ogg_opus` as the `OutputFormat`, the `ContentType` returned is audio/ogg. 
+  If you request `pcm` as the `OutputFormat`, the `ContentType` returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. 
+  If you request `mu-law` as the `OutputFormat`, the `ContentType` returned is audio/mulaw. 
+  If you request `a-law` as the `OutputFormat`, the `ContentType` returned is audio/alaw. 
+ If you request `json` as the `OutputFormat`, the `ContentType` returned is application/x-json-stream.
 

 ** [RequestCharacters](#API_SynthesizeSpeech_ResponseSyntax) **   <a name="polly-SynthesizeSpeech-response-RequestCharacters"></a>
Number of characters synthesized.

The response returns the following as the HTTP body.

 ** [AudioStream](#API_SynthesizeSpeech_ResponseSyntax) **   <a name="polly-SynthesizeSpeech-response-AudioStream"></a>
 Stream containing the synthesized speech. 

## Errors
<a name="API_SynthesizeSpeech_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EngineNotSupportedException **   
This engine is not compatible with the voice that you have designated. Choose a new voice that is compatible with the engine or change the engine and restart the operation.  
HTTP Status Code: 400

 ** InvalidSampleRateException **   
The specified sample rate is not valid.  
HTTP Status Code: 400

 ** InvalidSsmlException **   
The SSML you provided is invalid. Verify the SSML syntax, spelling of tags and values, and then try again.  
HTTP Status Code: 400

 ** LanguageNotSupportedException **   
The language specified is not currently supported by Amazon Polly in this capacity.  
HTTP Status Code: 400

 ** LexiconNotFoundException **   
Amazon Polly can't find the specified lexicon. This could be caused by a lexicon that is missing, its name is misspelled or specifying a lexicon that is in a different region.  
Verify that the lexicon exists, is in the region (see [ListLexicons](API_ListLexicons.md)) and that you spelled its name is spelled correctly. Then try again.  
HTTP Status Code: 404

 ** MarksNotSupportedForFormatException **   
Speech marks are not supported for the `OutputFormat` selected. Speech marks are only available for content in `json` format.  
HTTP Status Code: 400

 ** ServiceFailureException **   
An unknown condition has caused a service failure.  
HTTP Status Code: 500

 ** SsmlMarksNotSupportedForTextTypeException **   
SSML speech marks are not supported for plain text-type input.  
HTTP Status Code: 400

 ** TextLengthExceededException **   
The value of the "Text" parameter is longer than the accepted limits. For the `SynthesizeSpeech` API, the limit for input text is a maximum of 6000 characters total, of which no more than 3000 can be billed characters. For the `StartSpeechSynthesisTask` API, the maximum is 200,000 characters, of which no more than 100,000 can be billed characters. SSML tags are not counted as billed characters.  
HTTP Status Code: 400

## See Also
<a name="API_SynthesizeSpeech_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/polly-2016-06-10/SynthesizeSpeech) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/SynthesizeSpeech) 