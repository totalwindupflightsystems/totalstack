---
id: "@specs/aws/transcribe/docs/API_streaming_GetMedicalScribeStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMedicalScribeStream"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetMedicalScribeStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_GetMedicalScribeStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMedicalScribeStream
<a name="API_streaming_GetMedicalScribeStream"></a>

Provides details about the specified AWS HealthScribe streaming session. To view the status of the streaming session, check the `StreamStatus` field in the response. To get the details of post-stream analytics, including its status, check the `PostStreamAnalyticsResult` field in the response. 

## Request Syntax
<a name="API_streaming_GetMedicalScribeStream_RequestSyntax"></a>

```
GET /medical-scribe-stream/{{SessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_streaming_GetMedicalScribeStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SessionId](#API_streaming_GetMedicalScribeStream_RequestSyntax) **   <a name="transcribe-streaming_GetMedicalScribeStream-request-uri-SessionId"></a>
The identifier of the HealthScribe streaming session you want information about.  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`   
Required: Yes

## Request Body
<a name="API_streaming_GetMedicalScribeStream_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_streaming_GetMedicalScribeStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MedicalScribeStreamDetails": { 
      "ChannelDefinitions": [ 
         { 
            "ChannelId": number,
            "ParticipantRole": "string"
         }
      ],
      "EncryptionSettings": { 
         "KmsEncryptionContext": { 
            "string" : "string" 
         },
         "KmsKeyId": "string"
      },
      "LanguageCode": "string",
      "MediaEncoding": "string",
      "MediaSampleRateHertz": number,
      "MedicalScribeContextProvided": boolean,
      "PostStreamAnalyticsResult": { 
         "ClinicalNoteGenerationResult": { 
            "ClinicalNoteOutputLocation": "string",
            "FailureReason": "string",
            "Status": "string",
            "TranscriptOutputLocation": "string"
         }
      },
      "PostStreamAnalyticsSettings": { 
         "ClinicalNoteGenerationSettings": { 
            "NoteTemplate": "string",
            "OutputBucketName": "string"
         }
      },
      "ResourceAccessRoleArn": "string",
      "SessionId": "string",
      "StreamCreatedAt": number,
      "StreamEndedAt": number,
      "StreamStatus": "string",
      "VocabularyFilterMethod": "string",
      "VocabularyFilterName": "string",
      "VocabularyName": "string"
   }
}
```

## Response Elements
<a name="API_streaming_GetMedicalScribeStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MedicalScribeStreamDetails](#API_streaming_GetMedicalScribeStream_ResponseSyntax) **   <a name="transcribe-streaming_GetMedicalScribeStream-response-MedicalScribeStreamDetails"></a>
Provides details about a HealthScribe streaming session.  
Type: [MedicalScribeStreamDetails](API_streaming_MedicalScribeStreamDetails.md) object

## Errors
<a name="API_streaming_GetMedicalScribeStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
One or more arguments to the `StartStreamTranscription`, `StartMedicalStreamTranscription`, or `StartCallAnalyticsStreamTranscription` operation was not valid. For example, `MediaEncoding` or `LanguageCode` used unsupported values. Check the specified parameters and try your request again.  
HTTP Status Code: 400

 ** InternalFailureException **   
A problem occurred while processing the audio. Amazon Transcribe terminated processing.  
HTTP Status Code: 500

 ** LimitExceededException **   
Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.  
HTTP Status Code: 429

 ** ResourceNotFoundException **   
The request references a resource which doesn't exist.  
HTTP Status Code: 404

## See Also
<a name="API_streaming_GetMedicalScribeStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/GetMedicalScribeStream) 