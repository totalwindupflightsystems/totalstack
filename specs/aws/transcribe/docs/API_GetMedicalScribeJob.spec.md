---
id: "@specs/aws/transcribe/docs/API_GetMedicalScribeJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMedicalScribeJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetMedicalScribeJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_GetMedicalScribeJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMedicalScribeJob
<a name="API_GetMedicalScribeJob"></a>

Provides information about the specified Medical Scribe job.

To view the status of the specified medical transcription job, check the `MedicalScribeJobStatus` field. If the status is `COMPLETED`, the job is finished. You can find the results at the location specified in `MedicalScribeOutput`. If the status is `FAILED`, `FailureReason` provides details on why your Medical Scribe job failed.

To get a list of your Medical Scribe jobs, use the [ListMedicalScribeJobs](API_ListMedicalScribeJobs.md) operation.

## Request Syntax
<a name="API_GetMedicalScribeJob_RequestSyntax"></a>

```
{
   "MedicalScribeJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMedicalScribeJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MedicalScribeJobName](#API_GetMedicalScribeJob_RequestSyntax) **   <a name="transcribe-GetMedicalScribeJob-request-MedicalScribeJobName"></a>
The name of the Medical Scribe job you want information about. Job names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_GetMedicalScribeJob_ResponseSyntax"></a>

```
{
   "MedicalScribeJob": { 
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
      "LanguageCode": "string",
      "Media": { 
         "MediaFileUri": "string",
         "RedactedMediaFileUri": "string"
      },
      "MedicalScribeContextProvided": boolean,
      "MedicalScribeJobName": "string",
      "MedicalScribeJobStatus": "string",
      "MedicalScribeOutput": { 
         "ClinicalDocumentUri": "string",
         "TranscriptFileUri": "string"
      },
      "Settings": { 
         "ChannelIdentification": boolean,
         "ClinicalNoteGenerationSettings": { 
            "NoteTemplate": "string"
         },
         "MaxSpeakerLabels": number,
         "ShowSpeakerLabels": boolean,
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
      ]
   }
}
```

## Response Elements
<a name="API_GetMedicalScribeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MedicalScribeJob](#API_GetMedicalScribeJob_ResponseSyntax) **   <a name="transcribe-GetMedicalScribeJob-response-MedicalScribeJob"></a>
Provides detailed information about the specified Medical Scribe job, including job status and, if applicable, failure reason  
Type: [MedicalScribeJob](API_MedicalScribeJob.md) object

## Errors
<a name="API_GetMedicalScribeJob_Errors"></a>

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
<a name="API_GetMedicalScribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetMedicalScribeJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetMedicalScribeJob) 