---
id: "@specs/aws/transcribe/docs/API_GetCallAnalyticsJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCallAnalyticsJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetCallAnalyticsJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_GetCallAnalyticsJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCallAnalyticsJob
<a name="API_GetCallAnalyticsJob"></a>

Provides information about the specified Call Analytics job.

To view the job's status, refer to `CallAnalyticsJobStatus`. If the status is `COMPLETED`, the job is finished. You can find your completed transcript at the URI specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.

If you enabled personally identifiable information (PII) redaction, the redacted transcript appears at the location specified in `RedactedTranscriptFileUri`.

If you chose to redact the audio in your media file, you can find your redacted media file at the location specified in `RedactedMediaFileUri`.

To get a list of your Call Analytics jobs, use the [ListCallAnalyticsJobs](API_ListCallAnalyticsJobs.md) operation.

## Request Syntax
<a name="API_GetCallAnalyticsJob_RequestSyntax"></a>

```
{
   "CallAnalyticsJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCallAnalyticsJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CallAnalyticsJobName](#API_GetCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-GetCallAnalyticsJob-request-CallAnalyticsJobName"></a>
The name of the Call Analytics job you want information about. Job names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_GetCallAnalyticsJob_ResponseSyntax"></a>

```
{
   "CallAnalyticsJob": { 
      "CallAnalyticsJobDetails": { 
         "Skipped": [ 
            { 
               "Feature": "string",
               "Message": "string",
               "ReasonCode": "string"
            }
         ]
      },
      "CallAnalyticsJobName": "string",
      "CallAnalyticsJobStatus": "string",
      "ChannelDefinitions": [ 
         { 
            "ChannelId": number,
            "ParticipantRole": "string"
         }
      ],
      "CompletionTime": number,
      "CreationTime": number,
      "DataAccessRoleArn": "string",
      "FailureReason": "string",
      "IdentifiedLanguageScore": number,
      "LanguageCode": "string",
      "Media": { 
         "MediaFileUri": "string",
         "RedactedMediaFileUri": "string"
      },
      "MediaFormat": "string",
      "MediaSampleRateHertz": number,
      "Settings": { 
         "ContentRedaction": { 
            "PiiEntityTypes": [ "string" ],
            "RedactionOutput": "string",
            "RedactionType": "string"
         },
         "LanguageIdSettings": { 
            "string" : { 
               "LanguageModelName": "string",
               "VocabularyFilterName": "string",
               "VocabularyName": "string"
            }
         },
         "LanguageModelName": "string",
         "LanguageOptions": [ "string" ],
         "Summarization": { 
            "GenerateAbstractiveSummary": boolean
         },
         "VocabularyFilterMethod": "string",
         "VocabularyFilterName": "string",
         "VocabularyName": "string"
      },
      "StartTime": number,
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "Transcript": { 
         "RedactedTranscriptFileUri": "string",
         "TranscriptFileUri": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetCallAnalyticsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CallAnalyticsJob](#API_GetCallAnalyticsJob_ResponseSyntax) **   <a name="transcribe-GetCallAnalyticsJob-response-CallAnalyticsJob"></a>
Provides detailed information about the specified Call Analytics job, including job status and, if applicable, failure reason.  
Type: [CallAnalyticsJob](API_CallAnalyticsJob.md) object

## Errors
<a name="API_GetCallAnalyticsJob_Errors"></a>

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
<a name="API_GetCallAnalyticsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetCallAnalyticsJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetCallAnalyticsJob) 