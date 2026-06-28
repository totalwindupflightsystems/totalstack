---
id: "@specs/aws/transcribe/docs/API_GetMedicalTranscriptionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMedicalTranscriptionJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetMedicalTranscriptionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_GetMedicalTranscriptionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMedicalTranscriptionJob
<a name="API_GetMedicalTranscriptionJob"></a>

Provides information about the specified medical transcription job.

To view the status of the specified medical transcription job, check the `TranscriptionJobStatus` field. If the status is `COMPLETED`, the job is finished. You can find the results at the location specified in `TranscriptFileUri`. If the status is `FAILED`, `FailureReason` provides details on why your transcription job failed.

To get a list of your medical transcription jobs, use the [ListMedicalTranscriptionJobs](API_ListMedicalTranscriptionJobs.md) operation.

## Request Syntax
<a name="API_GetMedicalTranscriptionJob_RequestSyntax"></a>

```
{
   "MedicalTranscriptionJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMedicalTranscriptionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MedicalTranscriptionJobName](#API_GetMedicalTranscriptionJob_RequestSyntax) **   <a name="transcribe-GetMedicalTranscriptionJob-request-MedicalTranscriptionJobName"></a>
The name of the medical transcription job you want information about. Job names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_GetMedicalTranscriptionJob_ResponseSyntax"></a>

```
{
   "MedicalTranscriptionJob": { 
      "CompletionTime": number,
      "ContentIdentificationType": "string",
      "CreationTime": number,
      "FailureReason": "string",
      "LanguageCode": "string",
      "Media": { 
         "MediaFileUri": "string",
         "RedactedMediaFileUri": "string"
      },
      "MediaFormat": "string",
      "MediaSampleRateHertz": number,
      "MedicalTranscriptionJobName": "string",
      "Settings": { 
         "ChannelIdentification": boolean,
         "MaxAlternatives": number,
         "MaxSpeakerLabels": number,
         "ShowAlternatives": boolean,
         "ShowSpeakerLabels": boolean,
         "VocabularyName": "string"
      },
      "Specialty": "string",
      "StartTime": number,
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "Transcript": { 
         "TranscriptFileUri": "string"
      },
      "TranscriptionJobStatus": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_GetMedicalTranscriptionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MedicalTranscriptionJob](#API_GetMedicalTranscriptionJob_ResponseSyntax) **   <a name="transcribe-GetMedicalTranscriptionJob-response-MedicalTranscriptionJob"></a>
Provides detailed information about the specified medical transcription job, including job status and, if applicable, failure reason.  
Type: [MedicalTranscriptionJob](API_MedicalTranscriptionJob.md) object

## Errors
<a name="API_GetMedicalTranscriptionJob_Errors"></a>

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
<a name="API_GetMedicalTranscriptionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetMedicalTranscriptionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetMedicalTranscriptionJob) 