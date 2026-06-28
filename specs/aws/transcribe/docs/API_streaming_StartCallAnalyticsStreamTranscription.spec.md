---
id: "@specs/aws/transcribe/docs/API_streaming_StartCallAnalyticsStreamTranscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartCallAnalyticsStreamTranscription"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartCallAnalyticsStreamTranscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_StartCallAnalyticsStreamTranscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartCallAnalyticsStreamTranscription
<a name="API_streaming_StartCallAnalyticsStreamTranscription"></a>

Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe and the transcription results are streamed to your application. Use this operation for [Call Analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html) transcriptions.

The following parameters are required:
+  `language-code` or `identify-language` 
+  `media-encoding` 
+  `sample-rate` 

For more information on streaming with Amazon Transcribe, see [Transcribing streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html).

## Request Syntax
<a name="API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax"></a>

```
POST /call-analytics-stream-transcription HTTP/1.1
x-amzn-transcribe-language-code: {{LanguageCode}}
x-amzn-transcribe-sample-rate: {{MediaSampleRateHertz}}
x-amzn-transcribe-media-encoding: {{MediaEncoding}}
x-amzn-transcribe-vocabulary-name: {{VocabularyName}}
x-amzn-transcribe-session-id: {{SessionId}}
x-amzn-transcribe-vocabulary-filter-name: {{VocabularyFilterName}}
x-amzn-transcribe-vocabulary-filter-method: {{VocabularyFilterMethod}}
x-amzn-transcribe-language-model-name: {{LanguageModelName}}
x-amzn-transcribe-identify-language: {{IdentifyLanguage}}
x-amzn-transcribe-language-options: {{LanguageOptions}}
x-amzn-transcribe-preferred-language: {{PreferredLanguage}}
x-amzn-transcribe-vocabulary-names: {{VocabularyNames}}
x-amzn-transcribe-vocabulary-filter-names: {{VocabularyFilterNames}}
x-amzn-transcribe-enable-partial-results-stabilization: {{EnablePartialResultsStabilization}}
x-amzn-transcribe-partial-results-stability: {{PartialResultsStability}}
x-amzn-transcribe-content-identification-type: {{ContentIdentificationType}}
x-amzn-transcribe-content-redaction-type: {{ContentRedactionType}}
x-amzn-transcribe-pii-entity-types: {{PiiEntityTypes}}
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
<a name="API_streaming_StartCallAnalyticsStreamTranscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContentIdentificationType](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-ContentIdentificationType"></a>
Labels all personally identifiable information (PII) identified in your transcript.  
Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment. If you don't include `PiiEntityTypes` in your request, all PII is identified.  
You can’t set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you set both, your request returns a `BadRequestException`.  
For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html).  
Valid Values: `PII` 

 ** [ContentRedactionType](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-ContentRedactionType"></a>
Redacts all personally identifiable information (PII) identified in your transcript.  
Content redaction is performed at the segment level; PII specified in `PiiEntityTypes` is redacted upon complete transcription of an audio segment. If you don't include `PiiEntityTypes` in your request, all PII is redacted.  
You can’t set `ContentRedactionType` and `ContentIdentificationType` in the same request. If you set both, your request returns a `BadRequestException`.  
For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html).  
Valid Values: `PII` 

 ** [EnablePartialResultsStabilization](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-EnablePartialResultsStabilization"></a>
Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization).

 ** [IdentifyLanguage](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-IdentifyLanguage"></a>
Enables automatic language identification for your Call Analytics transcription.  
If you include `IdentifyLanguage`, you must include a list of language codes, using `LanguageOptions`, that you think may be present in your audio stream. You must provide a minimum of two language selections.  
You can also include a preferred language using `PreferredLanguage`. Adding a preferred language can help Amazon Transcribe identify the language faster than if you omit this parameter.  
Note that you must include either `LanguageCode` or `IdentifyLanguage` in your request. If you include both parameters, your transcription job fails.

 ** [LanguageCode](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-LanguageCode"></a>
Specify the language code that represents the language spoken in your audio.  
For a list of languages supported with real-time Call Analytics, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR` 

 ** [LanguageModelName](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-LanguageModelName"></a>
Specify the name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.  
The language of the specified language model must match the language code you specify in your transcription request. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.  
For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html).  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [LanguageOptions](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-LanguageOptions"></a>
Specify two or more language codes that represent the languages you think may be present in your media.  
Including language options can improve the accuracy of language identification.  
If you include `LanguageOptions` in your request, you must also include `IdentifyLanguage`.  
For a list of languages supported with Call Analytics streaming, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.  
You can only include one language dialect per language per stream. For example, you cannot include `en-US` and `en-AU` in the same request.
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[a-zA-Z-,]+` 

 ** [MediaEncoding](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-MediaEncoding"></a>
Specify the encoding of your input audio. Supported formats are:  
+ FLAC
+ OPUS-encoded audio in an Ogg container
+ PCM (only signed 16-bit little-endian audio formats, which does not include WAV)
For more information, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio).  
Valid Values: `pcm | ogg-opus | flac`   
Required: Yes

 ** [MediaSampleRateHertz](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-MediaSampleRateHertz"></a>
The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.  
Valid Range: Minimum value of 8000. Maximum value of 48000.  
Required: Yes

 ** [PartialResultsStability](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-PartialResultsStability"></a>
Specify the level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization`).  
Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.  
For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization).  
Valid Values: `high | medium | low` 

 ** [PiiEntityTypes](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-PiiEntityTypes"></a>
Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select `ALL`.  
Values must be comma-separated and can include: `ADDRESS`, `BANK_ACCOUNT_NUMBER`, `BANK_ROUTING`, `CREDIT_DEBIT_CVV`, `CREDIT_DEBIT_EXPIRY`, `CREDIT_DEBIT_NUMBER`, `EMAIL`, `NAME`, `PHONE`, `PIN`, `SSN`, or `ALL`.  
Note that if you include `PiiEntityTypes` in your request, you must also include `ContentIdentificationType` or `ContentRedactionType`.  
If you include `ContentRedactionType` or `ContentIdentificationType` in your request, but do not include `PiiEntityTypes`, all PII is redacted or identified.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Pattern: `^[A-Z_, ]+` 

 ** [PreferredLanguage](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-PreferredLanguage"></a>
Specify a preferred language from the subset of languages codes you specified in `LanguageOptions`.  
You can only use this parameter if you've included `IdentifyLanguage` and `LanguageOptions` in your request.  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR` 

 ** [SessionId](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-SessionId"></a>
Specify a name for your Call Analytics transcription session. If you don't include this parameter in your request, Amazon Transcribe generates an ID and returns it in the response.  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

 ** [VocabularyFilterMethod](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-VocabularyFilterMethod"></a>
Specify how you want your vocabulary filter applied to your transcript.  
To replace words with `***`, choose `mask`.  
To delete words, choose `remove`.  
To flag words without changing them, choose `tag`.  
Valid Values: `remove | mask | tag` 

 ** [VocabularyFilterName](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-VocabularyFilterName"></a>
Specify the name of the custom vocabulary filter that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive.  
If the language of the specified custom vocabulary filter doesn't match the language identified in your media, the vocabulary filter is not applied to your transcription.  
For more information, see [Using vocabulary filtering with unwanted words](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html).  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyFilterNames](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-VocabularyFilterNames"></a>
Specify the names of the custom vocabulary filters that you want to use when processing your Call Analytics transcription. Note that vocabulary filter names are case sensitive.  
These filters serve to customize the transcript output.  
This parameter is only intended for use **with** the `IdentifyLanguage` parameter. If you're **not** including `IdentifyLanguage` in your request and want to use a custom vocabulary filter with your transcription, use the `VocabularyFilterName` parameter instead.
For more information, see [Using vocabulary filtering with unwanted words](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html).  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `^[a-zA-Z0-9,-._]+` 

 ** [VocabularyName](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-VocabularyName"></a>
Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.  
If the language of the specified custom vocabulary doesn't match the language identified in your media, the custom vocabulary is not applied to your transcription.  
For more information, see [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html).  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyNames](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-VocabularyNames"></a>
Specify the names of the custom vocabularies that you want to use when processing your Call Analytics transcription. Note that vocabulary names are case sensitive.  
If the custom vocabulary's language doesn't match the identified media language, it won't be applied to the transcription.  
This parameter is only intended for use **with** the `IdentifyLanguage` parameter. If you're **not** including `IdentifyLanguage` in your request and want to use a custom vocabulary with your transcription, use the `VocabularyName` parameter instead.
For more information, see [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html).  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `^[a-zA-Z0-9,-._]+` 

## Request Body
<a name="API_streaming_StartCallAnalyticsStreamTranscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AudioEvent](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-AudioEvent"></a>
A blob of audio from your application. Your audio stream consists of one or more audio events.  
For more information, see [Event stream encoding](https://docs.aws.amazon.com/transcribe/latest/dg/event-stream.html).  
Type: [AudioEvent](API_streaming_AudioEvent.md) object  
Required: No

 ** [ConfigurationEvent](#API_streaming_StartCallAnalyticsStreamTranscription_RequestSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-request-ConfigurationEvent"></a>
Contains audio channel definitions and post-call analytics settings.  
Type: [ConfigurationEvent](API_streaming_ConfigurationEvent.md) object  
Required: No

## Response Syntax
<a name="API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-request-id: {{RequestId}}
x-amzn-transcribe-language-code: {{LanguageCode}}
x-amzn-transcribe-sample-rate: {{MediaSampleRateHertz}}
x-amzn-transcribe-media-encoding: {{MediaEncoding}}
x-amzn-transcribe-vocabulary-name: {{VocabularyName}}
x-amzn-transcribe-session-id: {{SessionId}}
x-amzn-transcribe-vocabulary-filter-name: {{VocabularyFilterName}}
x-amzn-transcribe-vocabulary-filter-method: {{VocabularyFilterMethod}}
x-amzn-transcribe-language-model-name: {{LanguageModelName}}
x-amzn-transcribe-identify-language: {{IdentifyLanguage}}
x-amzn-transcribe-language-options: {{LanguageOptions}}
x-amzn-transcribe-preferred-language: {{PreferredLanguage}}
x-amzn-transcribe-vocabulary-names: {{VocabularyNames}}
x-amzn-transcribe-vocabulary-filter-names: {{VocabularyFilterNames}}
x-amzn-transcribe-enable-partial-results-stabilization: {{EnablePartialResultsStabilization}}
x-amzn-transcribe-partial-results-stability: {{PartialResultsStability}}
x-amzn-transcribe-content-identification-type: {{ContentIdentificationType}}
x-amzn-transcribe-content-redaction-type: {{ContentRedactionType}}
x-amzn-transcribe-pii-entity-types: {{PiiEntityTypes}}
Content-type: application/json

{
   "BadRequestException": { 
   },
   "CategoryEvent": { 
      "MatchedCategories": [ "string" ],
      "MatchedDetails": { 
         "string" : { 
            "TimestampRanges": [ 
               { 
                  "BeginOffsetMillis": number,
                  "EndOffsetMillis": number
               }
            ]
         }
      }
   },
   "ConflictException": { 
   },
   "InternalFailureException": { 
   },
   "LimitExceededException": { 
   },
   "ServiceUnavailableException": { 
   },
   "UtteranceEvent": { 
      "BeginOffsetMillis": number,
      "EndOffsetMillis": number,
      "Entities": [ 
         { 
            "BeginOffsetMillis": number,
            "Category": "string",
            "Confidence": number,
            "Content": "string",
            "EndOffsetMillis": number,
            "Type": "string"
         }
      ],
      "IsPartial": boolean,
      "IssuesDetected": [ 
         { 
            "CharacterOffsets": { 
               "Begin": number,
               "End": number
            }
         }
      ],
      "Items": [ 
         { 
            "BeginOffsetMillis": number,
            "Confidence": number,
            "Content": "string",
            "EndOffsetMillis": number,
            "Stable": boolean,
            "Type": "string",
            "VocabularyFilterMatch": boolean
         }
      ],
      "LanguageCode": "string",
      "LanguageIdentification": [ 
         { 
            "LanguageCode": "string",
            "Score": number
         }
      ],
      "ParticipantRole": "string",
      "Sentiment": "string",
      "Transcript": "string",
      "UtteranceId": "string"
   }
}
```

## Response Elements
<a name="API_streaming_StartCallAnalyticsStreamTranscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentIdentificationType](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-ContentIdentificationType"></a>
Shows whether content identification was enabled for your Call Analytics transcription.  
Valid Values: `PII` 

 ** [ContentRedactionType](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-ContentRedactionType"></a>
Shows whether content redaction was enabled for your Call Analytics transcription.  
Valid Values: `PII` 

 ** [EnablePartialResultsStabilization](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-EnablePartialResultsStabilization"></a>
Shows whether partial results stabilization was enabled for your Call Analytics transcription.

 ** [IdentifyLanguage](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-IdentifyLanguage"></a>
Shows whether automatic language identification was enabled for your Call Analytics transcription.

 ** [LanguageCode](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-LanguageCode"></a>
Provides the language code that you specified in your Call Analytics request.  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR` 

 ** [LanguageModelName](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-LanguageModelName"></a>
Provides the name of the custom language model that you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [LanguageOptions](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-LanguageOptions"></a>
Provides the language codes that you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[a-zA-Z-,]+` 

 ** [MediaEncoding](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-MediaEncoding"></a>
Provides the media encoding you specified in your Call Analytics request.  
Valid Values: `pcm | ogg-opus | flac` 

 ** [MediaSampleRateHertz](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-MediaSampleRateHertz"></a>
Provides the sample rate that you specified in your Call Analytics request.  
Valid Range: Minimum value of 8000. Maximum value of 48000.

 ** [PartialResultsStability](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-PartialResultsStability"></a>
Provides the stabilization level used for your transcription.  
Valid Values: `high | medium | low` 

 ** [PiiEntityTypes](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-PiiEntityTypes"></a>
Lists the PII entity types you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Pattern: `^[A-Z_, ]+` 

 ** [PreferredLanguage](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-PreferredLanguage"></a>
Provides the preferred language that you specified in your Call Analytics request.  
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR` 

 ** [RequestId](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-RequestId"></a>
Provides the identifier for your real-time Call Analytics request.

 ** [SessionId](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-SessionId"></a>
Provides the identifier for your Call Analytics transcription session.  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

 ** [VocabularyFilterMethod](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-VocabularyFilterMethod"></a>
Provides the vocabulary filtering method used in your Call Analytics transcription.  
Valid Values: `remove | mask | tag` 

 ** [VocabularyFilterName](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-VocabularyFilterName"></a>
Provides the name of the custom vocabulary filter that you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyFilterNames](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-VocabularyFilterNames"></a>
Provides the names of the custom vocabulary filters that you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `^[a-zA-Z0-9,-._]+` 

 ** [VocabularyName](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-VocabularyName"></a>
Provides the name of the custom vocabulary that you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [VocabularyNames](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-VocabularyNames"></a>
Provides the names of the custom vocabularies that you specified in your Call Analytics request.  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `^[a-zA-Z0-9,-._]+` 

The following data is returned in JSON format by the service.

 ** [BadRequestException](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-BadRequestException"></a>
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
Type: Exception  
HTTP Status Code: 400

 ** [CategoryEvent](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-CategoryEvent"></a>
Provides information on matched categories that were used to generate real-time supervisor alerts.  
Type: [CategoryEvent](API_streaming_CategoryEvent.md) object

 ** [ConflictException](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-ConflictException"></a>
A new stream started with the same session ID. The current stream has been terminated.  
Type: Exception  
HTTP Status Code: 409

 ** [InternalFailureException](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-InternalFailureException"></a>
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
Type: Exception  
HTTP Status Code: 500

 ** [LimitExceededException](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-LimitExceededException"></a>
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
Type: Exception  
HTTP Status Code: 429

 ** [ServiceUnavailableException](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-ServiceUnavailableException"></a>
The service is currently unavailable. Try your request later.  
Type: Exception  
HTTP Status Code: 503

 ** [UtteranceEvent](#API_streaming_StartCallAnalyticsStreamTranscription_ResponseSyntax) **   <a name="transcribe-streaming_StartCallAnalyticsStreamTranscription-response-UtteranceEvent"></a>
Contains set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to channel definitions, partial result stabilization, sentiment, issue detection, and other transcription-related data.  
Type: [UtteranceEvent](API_streaming_UtteranceEvent.md) object

## Errors
<a name="API_streaming_StartCallAnalyticsStreamTranscription_Errors"></a>

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
<a name="API_streaming_StartCallAnalyticsStreamTranscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/StartCallAnalyticsStreamTranscription) 