---
id: "@specs/aws/transcribe/docs/API_StartMedicalScribeJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartMedicalScribeJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartMedicalScribeJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_StartMedicalScribeJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartMedicalScribeJob
<a name="API_StartMedicalScribeJob"></a>

Transcribes patient-clinician conversations and generates clinical notes. 

 AWS HealthScribe automatically provides rich conversation transcripts, identifies speaker roles, classifies dialogues, extracts medical terms, and generates preliminary clinical notes. To learn more about these features, refer to [AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html).

To make a `StartMedicalScribeJob` request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the `Media` parameter.

You must include the following parameters in your `StartMedicalTranscriptionJob` request:
+  `DataAccessRoleArn`: The ARN of an IAM role with the these minimum permissions: read permission on input file Amazon S3 bucket specified in `Media`, write permission on the Amazon S3 bucket specified in `OutputBucketName`, and full permissions on the AWS KMS key specified in `OutputEncryptionKMSKeyId` (if set). The role should also allow `transcribe.amazonaws.com` to assume it. 
+  `Media` (`MediaFileUri`): The Amazon S3 location of your media file.
+  `MedicalScribeJobName`: A custom name you create for your MedicalScribe job that is unique within your AWS account.
+  `OutputBucketName`: The Amazon S3 bucket where you want your output files stored.
+  `Settings`: A `MedicalScribeSettings` object that must set exactly one of `ShowSpeakerLabels` or `ChannelIdentification` to true. If `ShowSpeakerLabels` is true, `MaxSpeakerLabels` must also be set. 
+  `ChannelDefinitions`: A `MedicalScribeChannelDefinitions` array should be set if and only if the `ChannelIdentification` value of `Settings` is set to true. 

## Request Syntax
<a name="API_StartMedicalScribeJob_RequestSyntax"></a>

```
{
   "ChannelDefinitions": [ 
      { 
         "ChannelId": {{number}},
         "ParticipantRole": "{{string}}"
      }
   ],
   "DataAccessRoleArn": "{{string}}",
   "KMSEncryptionContext": { 
      "{{string}}" : "{{string}}" 
   },
   "Media": { 
      "MediaFileUri": "{{string}}",
      "RedactedMediaFileUri": "{{string}}"
   },
   "MedicalScribeContext": { 
      "PatientContext": { 
         "Pronouns": "{{string}}"
      }
   },
   "MedicalScribeJobName": "{{string}}",
   "OutputBucketName": "{{string}}",
   "OutputEncryptionKMSKeyId": "{{string}}",
   "Settings": { 
      "ChannelIdentification": {{boolean}},
      "ClinicalNoteGenerationSettings": { 
         "NoteTemplate": "{{string}}"
      },
      "MaxSpeakerLabels": {{number}},
      "ShowSpeakerLabels": {{boolean}},
      "VocabularyFilterMethod": "{{string}}",
      "VocabularyFilterName": "{{string}}",
      "VocabularyName": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartMedicalScribeJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChannelDefinitions](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-ChannelDefinitions"></a>
Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set `ChannelId` of the first `ChannelDefinition` in the list to `0` (to indicate the first channel) and `ParticipantRole` to `CLINICIAN` (to indicate that it's the clinician speaking). Then you would set the `ChannelId` of the second `ChannelDefinition` in the list to `1` (to indicate the second channel) and `ParticipantRole` to `PATIENT` (to indicate that it's the patient speaking).   
Type: Array of [MedicalScribeChannelDefinition](API_MedicalScribeChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** [DataAccessRoleArn](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your AWS KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions your request fails.  
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.  
For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: Yes

 ** [KMSEncryptionContext](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-KMSEncryptionContext"></a>
A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see [AWS KMS encryption context](https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context) and [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html).  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

 ** [Media](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-Media"></a>
Describes the Amazon S3 location of the media file you want to use in your request.  
For information on supported media formats, refer to the `MediaFormat` parameter or the [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) section in the Amazon S3 Developer Guide.  
Type: [Media](API_Media.md) object  
Required: Yes

 ** [MedicalScribeContext](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-MedicalScribeContext"></a>
The `MedicalScribeContext` object that contains contextual information which is used during clinical note generation to add relevant context to the note.  
Type: [MedicalScribeContext](API_MedicalScribeContext.md) object  
Required: No

 ** [MedicalScribeJobName](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-MedicalScribeJobName"></a>
A unique name, chosen by you, for your Medical Scribe job.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account. If you try to create a new job with the same name as an existing job, you get a `ConflictException` error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [OutputBucketName](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-OutputBucketName"></a>
The name of the Amazon S3 bucket where you want your Medical Scribe output stored. Do not include the `S3://` prefix of the specified bucket.  
Note that the role specified in the `DataAccessRoleArn` request parameter must have permission to use the specified location. You can change Amazon S3 permissions using the [AWS Management Console](https://console.aws.amazon.com/s3). See also [Permissions Required for IAM User Roles](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user).  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`   
Required: Yes

 ** [OutputEncryptionKMSKeyId](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-OutputEncryptionKMSKeyId"></a>
The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your Medical Scribe output.  
KMS key ARNs have the format `arn:partition:kms:region:account:key/key-id`. For example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. For more information, see [ KMS key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN).  
If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).  
Note that the role making the [StartMedicalScribeJob](#API_StartMedicalScribeJob) request and the role specified in the `DataAccessRoleArn` request parameter (if present) must have permission to use the specified KMS key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`   
Required: No

 ** [Settings](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-Settings"></a>
Makes it possible to control how your Medical Scribe job is processed using a `MedicalScribeSettings` object. Specify `ChannelIdentification` if `ChannelDefinitions` are set. Enabled `ShowSpeakerLabels` if `ChannelIdentification` and `ChannelDefinitions` are not set. One and only one of `ChannelIdentification` and `ShowSpeakerLabels` must be set. If `ShowSpeakerLabels` is set, `MaxSpeakerLabels` must also be set. Use `Settings` to specify a vocabulary or vocabulary filter or both using `VocabularyName`, `VocabularyFilterName`. `VocabularyFilterMethod` must be specified if `VocabularyFilterName` is set.   
Type: [MedicalScribeSettings](API_MedicalScribeSettings.md) object  
Required: Yes

 ** [Tags](#API_StartMedicalScribeJob_RequestSyntax) **   <a name="transcribe-StartMedicalScribeJob-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to the Medical Scribe job.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_StartMedicalScribeJob_ResponseSyntax"></a>

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
<a name="API_StartMedicalScribeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MedicalScribeJob](#API_StartMedicalScribeJob_ResponseSyntax) **   <a name="transcribe-StartMedicalScribeJob-response-MedicalScribeJob"></a>
Provides detailed information about the current Medical Scribe job, including job status and, if applicable, failure reason.  
Type: [MedicalScribeJob](API_MedicalScribeJob.md) object

## Errors
<a name="API_StartMedicalScribeJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** ConflictException **   
A resource already exists with this name. Resource names must be unique within an AWS account.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_StartMedicalScribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/StartMedicalScribeJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/StartMedicalScribeJob) 