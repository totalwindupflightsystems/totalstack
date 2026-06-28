---
id: "@specs/aws/transcribe/docs/API_streaming_StartMedicalScribeStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartMedicalScribeStream"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartMedicalScribeStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_StartMedicalScribeStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartMedicalScribeStream
<a name="API_streaming_StartMedicalScribeStream"></a>

Starts a bidirectional HTTP/2 stream, where audio is streamed to AWS HealthScribe and the transcription results are streamed to your application.

When you start a stream, you first specify the stream configuration in a `MedicalScribeConfigurationEvent`. This event includes channel definitions, encryption settings, medical scribe context, and post-stream analytics settings, such as the output configuration for aggregated transcript and clinical note generation. These are additional streaming session configurations beyond those provided in your initial start request headers. Whether you are starting a new session or resuming an existing session, your first event must be a `MedicalScribeConfigurationEvent`. 

 After you send a `MedicalScribeConfigurationEvent`, you start `AudioEvents` and AWS HealthScribe responds with real-time transcription results. When you are finished, to start processing the results with the post-stream analytics, send a `MedicalScribeSessionControlEvent` with a `Type` of `END_OF_SESSION` and AWS HealthScribe starts the analytics. 

You can pause or resume streaming. To pause streaming, complete the input stream without sending the `MedicalScribeSessionControlEvent`. To resume streaming, call the `StartMedicalScribeStream` and specify the same SessionId you used to start the stream. 

The following parameters are required:
+  `language-code` 
+  `media-encoding` 
+  `media-sample-rate-hertz` 



For more information on streaming with AWS HealthScribe, see [AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-streaming.html). 

## Request Syntax
<a name="API_streaming_StartMedicalScribeStream_RequestSyntax"></a>

```
POST /medical-scribe-stream HTTP/1.1
x-amzn-transcribe-session-id: {{SessionId}}
x-amzn-transcribe-language-code: {{LanguageCode}}
x-amzn-transcribe-sample-rate: {{MediaSampleRateHertz}}
x-amzn-transcribe-media-encoding: {{MediaEncoding}}
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
      "EncryptionSettings": { 
         "KmsEncryptionContext": { 
            "{{string}}" : "{{string}}" 
         },
         "KmsKeyId": "{{string}}"
      },
      "MedicalScribeContext": { 
         "PatientContext": { 
            "Pronouns": "{{string}}"
         }
      },
      "PostStreamAnalyticsSettings": { 
         "ClinicalNoteGenerationSettings": { 
            "NoteTemplate": "{{string}}",
            "OutputBucketName": "{{string}}"
         }
      },
      "ResourceAccessRoleArn": "{{string}}",
      "VocabularyFilterMethod": "{{string}}",
      "VocabularyFilterName": "{{string}}",
      "VocabularyName": "{{string}}"
   },
   "SessionControlEvent": { 
      "Type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_streaming_StartMedicalScribeStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LanguageCode](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-LanguageCode"></a>
Specify the language code for your HealthScribe streaming session.  
Valid Values: `en-US`   
Required: Yes

 ** [MediaEncoding](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-MediaEncoding"></a>
Specify the encoding used for the input audio.  
Supported formats are:  
+ FLAC
+ OPUS-encoded audio in an Ogg container
+ PCM (only signed 16-bit little-endian audio formats, which does not include WAV) 
For more information, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio).   
Valid Values: `pcm | ogg-opus | flac`   
Required: Yes

 ** [MediaSampleRateHertz](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-MediaSampleRateHertz"></a>
Specify the sample rate of the input audio (in hertz). AWS HealthScribe supports a range from 16,000 Hz to 48,000 Hz. The sample rate you specify must match that of your audio.   
Valid Range: Minimum value of 16000. Maximum value of 48000.  
Required: Yes

 ** [SessionId](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-SessionId"></a>
Specify an identifier for your streaming session (in UUID format). If you don't include a SessionId in your request, AWS HealthScribe generates an ID and returns it in the response.   
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

## Request Body
<a name="API_streaming_StartMedicalScribeStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AudioEvent](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-AudioEvent"></a>
A wrapper for your audio chunks  
For more information, see [Event stream encoding](https://docs.aws.amazon.com/transcribe/latest/dg/event-stream.html).   
Type: [MedicalScribeAudioEvent](API_streaming_MedicalScribeAudioEvent.md) object  
Required: No

 ** [ConfigurationEvent](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-ConfigurationEvent"></a>
Specify additional streaming session configurations beyond those provided in your initial start request headers. For example, specify channel definitions, encryption settings, and post-stream analytics settings.   
Whether you are starting a new session or resuming an existing session, your first event must be a `MedicalScribeConfigurationEvent`.   
Type: [MedicalScribeConfigurationEvent](API_streaming_MedicalScribeConfigurationEvent.md) object  
Required: No

 ** [SessionControlEvent](#API_streaming_StartMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-request-SessionControlEvent"></a>
Specify the lifecycle of your streaming session, such as ending the session.  
Type: [MedicalScribeSessionControlEvent](API_streaming_MedicalScribeSessionControlEvent.md) object  
Required: No

## Response Syntax
<a name="API_streaming_StartMedicalScribeStream_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-transcribe-session-id: {{SessionId}}
x-amzn-request-id: {{RequestId}}
x-amzn-transcribe-language-code: {{LanguageCode}}
x-amzn-transcribe-sample-rate: {{MediaSampleRateHertz}}
x-amzn-transcribe-media-encoding: {{MediaEncoding}}
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
      "TranscriptSegment": { 
         "BeginAudioTime": number,
         "ChannelId": "string",
         "Content": "string",
         "EndAudioTime": number,
         "IsPartial": boolean,
         "Items": [ 
            { 
               "BeginAudioTime": number,
               "Confidence": number,
               "Content": "string",
               "EndAudioTime": number,
               "Type": "string",
               "VocabularyFilterMatch": boolean
            }
         ],
         "SegmentId": "string"
      }
   }
}
```

## Response Elements
<a name="API_streaming_StartMedicalScribeStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [LanguageCode](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-LanguageCode"></a>
The Language Code that you specified in your request. Same as provided in the `StartMedicalScribeStreamRequest`.   
Valid Values: `en-US` 

 ** [MediaEncoding](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-MediaEncoding"></a>
The Media Encoding you specified in your request. Same as provided in the `StartMedicalScribeStreamRequest`   
Valid Values: `pcm | ogg-opus | flac` 

 ** [MediaSampleRateHertz](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-MediaSampleRateHertz"></a>
The sample rate (in hertz) that you specified in your request. Same as provided in the `StartMedicalScribeStreamRequest`   
Valid Range: Minimum value of 16000. Maximum value of 48000.

 ** [RequestId](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-RequestId"></a>
The unique identifier for your streaming request. 

 ** [SessionId](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-SessionId"></a>
The identifier (in UUID format) for your streaming session.  
If you already started streaming, this is same ID as the one you specified in your initial `StartMedicalScribeStreamRequest`.   
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

The following data is returned in JSON format by the service.

 ** [BadRequestException](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-BadRequestException"></a>
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
Type: Exception  
HTTP Status Code: 400

 ** [ConflictException](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-ConflictException"></a>
A new stream started with the same session ID. The current stream has been terminated.  
Type: Exception  
HTTP Status Code: 409

 ** [InternalFailureException](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-InternalFailureException"></a>
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
Type: Exception  
HTTP Status Code: 500

 ** [LimitExceededException](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-LimitExceededException"></a>
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
Type: Exception  
HTTP Status Code: 429

 ** [ServiceUnavailableException](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-ServiceUnavailableException"></a>
The service is currently unavailable. Try your request later.  
Type: Exception  
HTTP Status Code: 503

 ** [TranscriptEvent](#API_streaming_StartMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_StartMedicalScribeStream-response-TranscriptEvent"></a>
The transcript event that contains real-time transcription results.   
Type: [MedicalScribeTranscriptEvent](API_streaming_MedicalScribeTranscriptEvent.md) object

## Errors
<a name="API_streaming_StartMedicalScribeStream_Errors"></a>

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
<a name="API_streaming_StartMedicalScribeStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/StartMedicalScribeStream) 