---
id: "@specs/aws/transcribe/docs/API_streaming_StartMedicalStreamTranscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartMedicalStreamTranscription"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartMedicalStreamTranscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_StartMedicalStreamTranscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartMedicalStreamTranscription
<a name="API_streaming_StartMedicalStreamTranscription"></a>

Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe Medical and the transcription results are streamed to your application.

The following parameters are required:
+  `language-code` 
+  `media-encoding` 
+  `sample-rate` 

For more information on streaming with Amazon Transcribe Medical, see [Transcribing streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html).

## Request Syntax
<a name="API_streaming_StartMedicalStreamTranscription_RequestSyntax"></a>

```
POST /medical-stream-transcription HTTP/1.1
x-amzn-transcribe-language-code: {{LanguageCode}}
x-amzn-transcribe-sample-rate: {{MediaSampleRateHertz}}
x-amzn-transcribe-media-encoding: {{MediaEncoding}}
x-amzn-transcribe-vocabulary-name: {{VocabularyName}}
x-amzn-transcribe-specialty: {{Specialty}}
x-amzn-transcribe-type: {{Type}}
x-amzn-transcribe-show-speaker-label: {{ShowSpeakerLabel}}
x-amzn-transcribe-session-id: {{SessionId}}
x-amzn-transcribe-enable-channel-identification: {{EnableChannelIdentification}}
x-amzn-transcribe-number-of-channels: {{NumberOfChannels}}
x-amzn-transcribe-content-identification-type: {{ContentIdentificationType}}
Content-type: application/json

{
   "AudioEvent": { 
      "AudioChunk": {{blob}}
   },
   "ConfigurationEvent": { 
      "ChannelDefinitions": [ 
         { 
            "ChannelId": {{number}},
            "ParticipantRole": "{{string}}"
         }
      ],
      "PostCallAnalyticsSettings": { 
         "ContentRedactionOutput": "{{string}}",
         "DataAccessRoleArn": "{{string}}",
         "OutputEncryptionKMSKeyId": "{{string}}",
         "OutputLocation": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_streaming_StartMedicalStreamTranscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContentIdentificationType](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-ContentIdentificationType"></a>
Labels all personal health information (PHI) identified in your transcript.  
Content identification is performed at the segment level; PHI is flagged upon complete transcription of an audio segment.  
For more information, see [Identifying personal health information (PHI) in a transcription](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html).  
Valid Values: `PHI` 

 ** [EnableChannelIdentification](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-EnableChannelIdentification"></a>
Enables channel identification in multi-channel audio.  
Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.  
If you have multi-channel audio and do not enable channel identification, your audio is transcribed in a continuous manner and your transcript is not separated by channel.  
If you include `EnableChannelIdentification` in your request, you must also include `NumberOfChannels`.  
For more information, see [Transcribing multi-channel audio](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html).

 ** [LanguageCode](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-LanguageCode"></a>
Specify the language code that represents the language spoken in your audio.  
Amazon Transcribe Medical only supports US English (`en-US`).
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR | ja-JP | ko-KR | zh-CN | th-TH | es-ES | ar-SA | pt-PT | ca-ES | ar-AE | hi-IN | zh-HK | nl-NL | no-NO | sv-SE | pl-PL | fi-FI | zh-TW | en-IN | en-IE | en-NZ | en-AB | en-ZA | en-WL | de-CH | af-ZA | eu-ES | hr-HR | cs-CZ | da-DK | fa-IR | gl-ES | el-GR | he-IL | id-ID | lv-LV | ms-MY | ro-RO | ru-RU | sr-RS | sk-SK | so-SO | tl-PH | uk-UA | vi-VN | zu-ZA | am-ET | be-BY | bg-BG | bn-IN | bs-BA | ckb-IQ | ckb-IR | cy-WL | es-MX | et-ET | fa-AF | gu-IN | ht-HT | hu-HU | hy-AM | is-IS | jv-ID | ka-GE | kab-DZ | kk-KZ | km-KH | kn-IN | lg-IN | lt-LT | mk-MK | ml-IN | mr-IN | my-MM | ne-NP | or-IN | pa-IN | ps-AF | si-LK | sl-SI | sq-AL | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | ta-IN | te-IN | tr-TR | uz-UZ`   
Required: Yes

 ** [MediaEncoding](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-MediaEncoding"></a>
Specify the encoding used for the input audio. Supported formats are:  
+ FLAC
+ OPUS-encoded audio in an Ogg container
+ PCM (only signed 16-bit little-endian audio formats, which does not include WAV)
For more information, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio).  
Valid Values: `pcm | ogg-opus | flac`   
Required: Yes

 ** [MediaSampleRateHertz](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-MediaSampleRateHertz"></a>
The sample rate of the input audio (in hertz). Amazon Transcribe Medical supports a range from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.  
Valid Range: Minimum value of 8000. Maximum value of 48000.  
Required: Yes

 ** [NumberOfChannels](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-NumberOfChannels"></a>
Specify the number of channels in your audio stream. This value must be `2`, as only two channels are supported. If your audio doesn't contain multiple channels, do not include this parameter in your request.  
If you include `NumberOfChannels` in your request, you must also include `EnableChannelIdentification`.  
Valid Range: Minimum value of 2.

 ** [SessionId](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-SessionId"></a>
Specify a name for your transcription session. If you don't include this parameter in your request, Amazon Transcribe Medical generates an ID and returns it in the response.  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

 ** [ShowSpeakerLabel](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-ShowSpeakerLabel"></a>
Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.  
For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html).

 ** [Specialty](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-Specialty"></a>
Specify the medical specialty contained in your audio.  
Valid Values: `PRIMARYCARE | CARDIOLOGY | NEUROLOGY | ONCOLOGY | RADIOLOGY | UROLOGY`   
Required: Yes

 ** [Type](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-Type"></a>
Specify the type of input audio. For example, choose `DICTATION` for a provider dictating patient notes and `CONVERSATION` for a dialogue between a patient and a medical professional.  
Valid Values: `CONVERSATION | DICTATION`   
Required: Yes

 ** [VocabularyName](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-VocabularyName"></a>
Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

## Request Body
<a name="API_streaming_StartMedicalStreamTranscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AudioEvent](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-AudioEvent"></a>
A blob of audio from your application. Your audio stream consists of one or more audio events.  
For more information, see [Event stream encoding](https://docs.aws.amazon.com/transcribe/latest/dg/event-stream.html).  
Type: [AudioEvent](API_streaming_AudioEvent.md) object  
Required: No

 ** [ConfigurationEvent](#API_streaming_StartMedicalStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-request-ConfigurationEvent"></a>
Contains audio channel definitions and post-call analytics settings.  
Type: [ConfigurationEvent](API_streaming_ConfigurationEvent.md) object  
Required: No

## Response Syntax
<a name="API_streaming_StartMedicalStreamTranscription_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-request-id: {{RequestId}}
x-amzn-transcribe-language-code: {{LanguageCode}}
x-amzn-transcribe-sample-rate: {{MediaSampleRateHertz}}
x-amzn-transcribe-media-encoding: {{MediaEncoding}}
x-amzn-transcribe-vocabulary-name: {{VocabularyName}}
x-amzn-transcribe-specialty: {{Specialty}}
x-amzn-transcribe-type: {{Type}}
x-amzn-transcribe-show-speaker-label: {{ShowSpeakerLabel}}
x-amzn-transcribe-session-id: {{SessionId}}
x-amzn-transcribe-enable-channel-identification: {{EnableChannelIdentification}}
x-amzn-transcribe-number-of-channels: {{NumberOfChannels}}
x-amzn-transcribe-content-identification-type: {{ContentIdentificationType}}
Content-type: application/json

{
   "BadRequestException": { 
   },
   "ConflictException": { 
   },
   "InternalFailureException": { 
   },
   "LimitExceededException": { 
   },
   "ServiceUnavailableException": { 
   },
   "TranscriptEvent": { 
      "Transcript": { 
         "Results": [ 
            { 
               "Alternatives": [ 
                  { 
                     "Entities": [ 
                        { 
                           "Category": "string",
                           "Confidence": number,
                           "Content": "string",
                           "EndTime": number,
                           "StartTime": number
                        }
                     ],
                     "Items": [ 
                        { 
                           "Confidence": number,
                           "Content": "string",
                           "EndTime": number,
                           "Speaker": "string",
                           "StartTime": number,
                           "Type": "string"
                        }
                     ],
                     "Transcript": "string"
                  }
               ],
               "ChannelId": "string",
               "EndTime": number,
               "IsPartial": boolean,
               "ResultId": "string",
               "StartTime": number
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_streaming_StartMedicalStreamTranscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentIdentificationType](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-ContentIdentificationType"></a>
Shows whether content identification was enabled for your transcription.  
Valid Values: `PHI` 

 ** [EnableChannelIdentification](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-EnableChannelIdentification"></a>
Shows whether channel identification was enabled for your transcription.

 ** [LanguageCode](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-LanguageCode"></a>
Provides the language code that you specified in your request. This must be `en-US`.  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR | ja-JP | ko-KR | zh-CN | th-TH | es-ES | ar-SA | pt-PT | ca-ES | ar-AE | hi-IN | zh-HK | nl-NL | no-NO | sv-SE | pl-PL | fi-FI | zh-TW | en-IN | en-IE | en-NZ | en-AB | en-ZA | en-WL | de-CH | af-ZA | eu-ES | hr-HR | cs-CZ | da-DK | fa-IR | gl-ES | el-GR | he-IL | id-ID | lv-LV | ms-MY | ro-RO | ru-RU | sr-RS | sk-SK | so-SO | tl-PH | uk-UA | vi-VN | zu-ZA | am-ET | be-BY | bg-BG | bn-IN | bs-BA | ckb-IQ | ckb-IR | cy-WL | es-MX | et-ET | fa-AF | gu-IN | ht-HT | hu-HU | hy-AM | is-IS | jv-ID | ka-GE | kab-DZ | kk-KZ | km-KH | kn-IN | lg-IN | lt-LT | mk-MK | ml-IN | mr-IN | my-MM | ne-NP | or-IN | pa-IN | ps-AF | si-LK | sl-SI | sq-AL | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | ta-IN | te-IN | tr-TR | uz-UZ` 

 ** [MediaEncoding](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-MediaEncoding"></a>
Provides the media encoding you specified in your request.  
Valid Values: `pcm | ogg-opus | flac` 

 ** [MediaSampleRateHertz](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-MediaSampleRateHertz"></a>
Provides the sample rate that you specified in your request.  
Valid Range: Minimum value of 8000. Maximum value of 48000.

 ** [NumberOfChannels](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-NumberOfChannels"></a>
Provides the number of channels that you specified in your request.  
Valid Range: Minimum value of 2.

 ** [RequestId](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-RequestId"></a>
Provides the identifier for your streaming request.

 ** [SessionId](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-SessionId"></a>
Provides the identifier for your transcription session.  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

 ** [ShowSpeakerLabel](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-ShowSpeakerLabel"></a>
Shows whether speaker partitioning was enabled for your transcription.

 ** [Specialty](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-Specialty"></a>
Provides the medical specialty that you specified in your request.  
Valid Values: `PRIMARYCARE | CARDIOLOGY | NEUROLOGY | ONCOLOGY | RADIOLOGY | UROLOGY` 

 ** [Type](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-Type"></a>
Provides the type of audio you specified in your request.  
Valid Values: `CONVERSATION | DICTATION` 

 ** [VocabularyName](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-VocabularyName"></a>
Provides the name of the custom vocabulary that you specified in your request.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

The following data is returned in JSON format by the service.

 ** [BadRequestException](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-BadRequestException"></a>
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
Type: Exception  
HTTP Status Code: 400

 ** [ConflictException](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-ConflictException"></a>
A new stream started with the same session ID. The current stream has been terminated.  
Type: Exception  
HTTP Status Code: 409

 ** [InternalFailureException](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-InternalFailureException"></a>
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
Type: Exception  
HTTP Status Code: 500

 ** [LimitExceededException](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-LimitExceededException"></a>
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
Type: Exception  
HTTP Status Code: 429

 ** [ServiceUnavailableException](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-ServiceUnavailableException"></a>
The service is currently unavailable. Try your request later.  
Type: Exception  
HTTP Status Code: 503

 ** [TranscriptEvent](#API_streaming_StartMedicalStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalStreamTranscription-response-TranscriptEvent"></a>
The `MedicalTranscriptEvent` associated with a `MedicalTranscriptResultStream`.  
Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.  
Type: [MedicalTranscriptEvent](API_streaming_MedicalTranscriptEvent.md) object

## Errors
<a name="API_streaming_StartMedicalStreamTranscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
HTTP Status Code: 400

 ** ConflictException **   
A new stream started with the same session ID. The current stream has been terminated.  
HTTP Status Code: 409

 ** InternalFailureException **   
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
HTTP Status Code: 500

 ** LimitExceededException **   
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
HTTP Status Code: 429

 ** ServiceUnavailableException **   
The service is currently unavailable. Try your request later.  
HTTP Status Code: 503

## See Also
<a name="API_streaming_StartMedicalStreamTranscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/StartMedicalStreamTranscription) 