---
id: "@specs/aws/polly/docs/API_StartSpeechSynthesisStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartSpeechSynthesisStream"
status: active
depends_on:
  - "@specs/aws/polly/meta"
---

# StartSpeechSynthesisStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/polly/docs/API_StartSpeechSynthesisStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartSpeechSynthesisStream
<a name="API_StartSpeechSynthesisStream"></a>

Synthesizes UTF-8 input, plain text, or SSML over a bidirectional streaming connection. Specify synthesis parameters in HTTP/2 headers, send text incrementally as events on the input stream, and receive synthesized audio as it becomes available.

This operation serves as a bidirectional counterpart to `SynthesizeSpeech`:
+  [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html) 

## Request Syntax
<a name="API_StartSpeechSynthesisStream_RequestSyntax"></a>

```
POST /v1/synthesisStream HTTP/1.1
x-amzn-Engine: {{Engine}}
x-amzn-LanguageCode: {{LanguageCode}}
x-amzn-LexiconNames: {{LexiconNames}}
x-amzn-OutputFormat: {{OutputFormat}}
x-amzn-SampleRate: {{SampleRate}}
x-amzn-VoiceId: {{VoiceId}}
Content-type: application/json

{
   "CloseStreamEvent": { 
   },
   "TextEvent": { 
      "FlushStreamConfiguration": { 
         "Force": {{boolean}}
      },
      "Text": "{{string}}",
      "TextType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartSpeechSynthesisStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Engine](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-Engine"></a>
Specifies the engine for Amazon Polly to use when processing input text for speech synthesis. Currently, only the `generative` engine is supported. If you specify a voice that the selected engine doesn't support, Amazon Polly returns an error.  
Valid Values: `standard | neural | long-form | generative`   
Required: Yes

 ** [LanguageCode](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-LanguageCode"></a>
An optional parameter that sets the language code for the speech synthesis request. Specify this parameter only when using a bilingual voice. If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice.  
Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH | en-SG` 

 ** [LexiconNames](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-LexiconNames"></a>
The names of one or more pronunciation lexicons for the service to apply during synthesis. Amazon Polly applies lexicons only when the lexicon language matches the voice language.  
Array Members: Maximum number of 5 items.  
Pattern: `[0-9A-Za-z]{1,20}` 

 ** [OutputFormat](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-OutputFormat"></a>
The audio format for the synthesized speech. Currently, Amazon Polly does not support JSON speech marks.  
Valid Values: `json | mp3 | ogg_opus | ogg_vorbis | pcm | mulaw | alaw`   
Required: Yes

 ** [SampleRate](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-SampleRate"></a>
The audio frequency, specified in Hz.

 ** [VoiceId](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-VoiceId"></a>
The voice to use in synthesis. To get a list of available voice IDs, use the [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html) operation.  
Valid Values: `Aditi | Amy | Astrid | Bianca | Brian | Camila | Carla | Carmen | Celine | Chantal | Conchita | Cristiano | Dora | Emma | Enrique | Ewa | Filiz | Gabrielle | Geraint | Giorgio | Gwyneth | Hans | Ines | Ivy | Jacek | Jan | Joanna | Joey | Justin | Karl | Kendra | Kevin | Kimberly | Lea | Liv | Lotte | Lucia | Lupe | Mads | Maja | Marlene | Mathieu | Matthew | Maxim | Mia | Miguel | Mizuki | Naja | Nicole | Olivia | Penelope | Raveena | Ricardo | Ruben | Russell | Salli | Seoyeon | Takumi | Tatyana | Vicki | Vitoria | Zeina | Zhiyu | Aria | Ayanda | Arlet | Hannah | Arthur | Daniel | Liam | Pedro | Kajal | Hiujin | Laura | Elin | Ida | Suvi | Ola | Hala | Andres | Sergio | Remi | Adriano | Thiago | Ruth | Stephen | Kazuha | Tomoko | Niamh | Sofie | Lisa | Isabelle | Zayd | Danielle | Gregory | Burcu | Jitka | Sabrina | Jasmine | Jihye | Ambre | Beatrice | Florian | Lennart | Lorenzo | Tiffany`   
Required: Yes

## Request Body
<a name="API_StartSpeechSynthesisStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CloseStreamEvent](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-CloseStreamEvent"></a>
An event indicating the end of the input stream.  
Type: [CloseStreamEvent](API_CloseStreamEvent.md) object  
Required: No

 ** [TextEvent](#API_StartSpeechSynthesisStream_RequestSyntax) **   <a name="polly-StartSpeechSynthesisStream-request-TextEvent"></a>
A text event containing content to be synthesized.  
Type: [TextEvent](API_TextEvent.md) object  
Required: No

## Response Syntax
<a name="API_StartSpeechSynthesisStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AudioEvent": { 
      "AudioChunk": blob
   },
   "ServiceFailureException": { 
   },
   "ServiceQuotaExceededException": { 
   },
   "StreamClosedEvent": { 
      "RequestCharacters": number
   },
   "ThrottlingException": { 
   },
   "ValidationException": { 
   }
}
```

## Response Elements
<a name="API_StartSpeechSynthesisStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AudioEvent](#API_StartSpeechSynthesisStream_ResponseSyntax) **   <a name="polly-StartSpeechSynthesisStream-response-AudioEvent"></a>
An audio event containing synthesized speech.  
Type: [AudioEvent](API_AudioEvent.md) object

 ** [ServiceFailureException](#API_StartSpeechSynthesisStream_ResponseSyntax) **   <a name="polly-StartSpeechSynthesisStream-response-ServiceFailureException"></a>
An unknown condition has caused a service failure.  
Type: Exception  
HTTP Status Code: 500

 ** [ServiceQuotaExceededException](#API_StartSpeechSynthesisStream_ResponseSyntax) **   <a name="polly-StartSpeechSynthesisStream-response-ServiceQuotaExceededException"></a>
An exception indicating a service quota would be exceeded.  
Type: Exception  
HTTP Status Code: 402

 ** [StreamClosedEvent](#API_StartSpeechSynthesisStream_ResponseSyntax) **   <a name="polly-StartSpeechSynthesisStream-response-StreamClosedEvent"></a>
An event, with summary information, indicating the stream has closed.  
Type: [StreamClosedEvent](API_StreamClosedEvent.md) object

 ** [ThrottlingException](#API_StartSpeechSynthesisStream_ResponseSyntax) **   <a name="polly-StartSpeechSynthesisStream-response-ThrottlingException"></a>
An exception indicating the request was throttled.  
Type: Exception  
HTTP Status Code: 400

 ** [ValidationException](#API_StartSpeechSynthesisStream_ResponseSyntax) **   <a name="polly-StartSpeechSynthesisStream-response-ValidationException"></a>
An exception indicating the input failed validation.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_StartSpeechSynthesisStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailureException **   
An unknown condition has caused a service failure.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The request would cause a service quota to be exceeded.    
 ** quotaCode **   
The quota code identifying the specific quota.  
 ** serviceCode **   
The service code identifying the originating service.
HTTP Status Code: 402

 ** ThrottlingException **   
The request was denied because of request throttling.    
 ** throttlingReasons **   
A list of reasons explaining why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.    
 ** fields **   
The fields that caused the validation error.  
 ** reason **   
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_StartSpeechSynthesisStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/polly-2016-06-10/StartSpeechSynthesisStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStream) 