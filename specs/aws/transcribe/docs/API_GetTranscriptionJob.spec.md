---
id: "@specs/aws/transcribe/docs/API_GetTranscriptionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetTranscriptionJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetTranscriptionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_GetTranscriptionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetTranscriptionJob
<a name="API_GetTranscriptionJob"></a>

Provides information about the specified transcription job.

To view the status of the specified transcription job, check the `TranscriptionJobStatus` field. If the status is `COMPLETED`, the job is finished. You can find the results at the location specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.

If you enabled content redaction, the redacted transcript can be found at the location specified in `RedactedTranscriptFileUri`.

To get a list of your transcription jobs, use the [ListTranscriptionJobs](API_ListTranscriptionJobs.md) operation.

## Request Syntax
<a name="API_GetTranscriptionJob_RequestSyntax"></a>

```
{
   "TranscriptionJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTranscriptionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TranscriptionJobName](#API_GetTranscriptionJob_RequestSyntax) **   <a name="transcribe-GetTranscriptionJob-request-TranscriptionJobName"></a>
The name of the transcription job you want information about. Job names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_GetTranscriptionJob_ResponseSyntax"></a>

```
{
   "TranscriptionJob": { 
      "CompletionTime": number,
      "ContentRedaction": { 
         "PiiEntityTypes": [ "string" ],
         "RedactionOutput": "string",
         "RedactionType": "string"
      },
      "CreationTime": number,
      "FailureReason": "string",
      "IdentifiedLanguageScore": number,
      "IdentifyLanguage": boolean,
      "IdentifyMultipleLanguages": boolean,
      "JobExecutionSettings": { 
         "AllowDeferredExecution": boolean,
         "DataAccessRoleArn": "string"
      },
      "LanguageCode": "string",
      "LanguageCodes": [ 
         { 
            "DurationInSeconds": number,
            "LanguageCode": "string"
         }
      ],
      "LanguageIdSettings": { 
         "string" : { 
            "LanguageModelName": "string",
            "VocabularyFilterName": "string",
            "VocabularyName": "string"
         }
      },
      "LanguageOptions": [ "string" ],
      "Media": { 
         "MediaFileUri": "string",
         "RedactedMediaFileUri": "string"
      },
      "MediaFormat": "string",
      "MediaSampleRateHertz": number,
      "ModelSettings": { 
         "LanguageModelName": "string"
      },
      "Settings": { 
         "ChannelIdentification": boolean,
         "MaxAlternatives": number,
         "MaxSpeakerLabels": number,
         "ShowAlternatives": boolean,
         "ShowSpeakerLabels": boolean,
         "VocabularyFilterMethod": "string",
         "VocabularyFilterName": "string",
         "VocabularyName": "string"
      },
      "StartTime": number,
      "Subtitles": { 
         "Formats": [ "string" ],
         "OutputStartIndex": number,
         "SubtitleFileUris": [ "string" ]
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "ToxicityDetection": [ 
         { 
            "ToxicityCategories": [ "string" ]
         }
      ],
      "Transcript": { 
         "RedactedTranscriptFileUri": "string",
         "TranscriptFileUri": "string"
      },
      "TranscriptionJobName": "string",
      "TranscriptionJobStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetTranscriptionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TranscriptionJob](#API_GetTranscriptionJob_ResponseSyntax) **   <a name="transcribe-GetTranscriptionJob-response-TranscriptionJob"></a>
Provides detailed information about the specified transcription job, including job status and, if applicable, failure reason.  
Type: [TranscriptionJob](API_TranscriptionJob.md) object

## Errors
<a name="API_GetTranscriptionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

 ** NotFoundException **   
We can't find the requested resource. Check that the specified name is correct and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_GetTranscriptionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetTranscriptionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetTranscriptionJob) 