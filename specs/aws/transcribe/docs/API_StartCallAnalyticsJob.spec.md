---
id: "@specs/aws/transcribe/docs/API_StartCallAnalyticsJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartCallAnalyticsJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# StartCallAnalyticsJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_StartCallAnalyticsJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartCallAnalyticsJob
<a name="API_StartCallAnalyticsJob"></a>

Transcribes the audio from a customer service call and applies any additional Request Parameters you choose to include in your request.

In addition to many standard transcription features, Call Analytics provides you with call characteristics, call summarization, speaker sentiment, and optional redaction of your text transcript and your audio file. You can also apply custom categories to flag specified conditions. To learn more about these features and insights, refer to [Analyzing call center audio with Call Analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html).

If you want to apply categories to your Call Analytics job, you must create them before submitting your job request. Categories cannot be retroactively applied to a job. To create a new category, use the [CreateCallAnalyticsCategory](API_CreateCallAnalyticsCategory.md) operation. To learn more about Call Analytics categories, see [Creating categories for post-call transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html) and [Creating categories for real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html).

To make a `StartCallAnalyticsJob` request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the `Media` parameter.

Job queuing is available for Call Analytics jobs. If you pass a `DataAccessRoleArn` in your request and you exceed your Concurrent Job Limit, your job will automatically be added to a queue to be processed once your concurrent job count is below the limit.

You must include the following parameters in your `StartCallAnalyticsJob` request:
+  `region`: The AWS Region where you are making your request. For a list of AWS Regions supported with Amazon Transcribe, refer to [Amazon Transcribe endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html).
+  `CallAnalyticsJobName`: A custom name that you create for your transcription job that's unique within your AWS account.
+  `Media` (`MediaFileUri` or `RedactedMediaFileUri`): The Amazon S3 location of your media file.

**Note**  
With Call Analytics, you can redact the audio contained in your media file by including `RedactedMediaFileUri`, instead of `MediaFileUri`, to specify the location of your input audio. If you choose to redact your audio, you can find your redacted media at the location specified in the `RedactedMediaFileUri` field of your response.

## Request Syntax
<a name="API_StartCallAnalyticsJob_RequestSyntax"></a>

```
{
   "CallAnalyticsJobName": "{{string}}",
   "ChannelDefinitions": [ 
      { 
         "ChannelId": {{number}},
         "ParticipantRole": "{{string}}"
      }
   ],
   "DataAccessRoleArn": "{{string}}",
   "Media": { 
      "MediaFileUri": "{{string}}",
      "RedactedMediaFileUri": "{{string}}"
   },
   "OutputEncryptionKMSKeyId": "{{string}}",
   "OutputLocation": "{{string}}",
   "Settings": { 
      "ContentRedaction": { 
         "PiiEntityTypes": [ "{{string}}" ],
         "RedactionOutput": "{{string}}",
         "RedactionType": "{{string}}"
      },
      "LanguageIdSettings": { 
         "{{string}}" : { 
            "LanguageModelName": "{{string}}",
            "VocabularyFilterName": "{{string}}",
            "VocabularyName": "{{string}}"
         }
      },
      "LanguageModelName": "{{string}}",
      "LanguageOptions": [ "{{string}}" ],
      "Summarization": { 
         "GenerateAbstractiveSummary": {{boolean}}
      },
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
<a name="API_StartCallAnalyticsJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CallAnalyticsJobName](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-CallAnalyticsJobName"></a>
A unique name, chosen by you, for your Call Analytics job.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account. If you try to create a new job with the same name as an existing job, you get a `ConflictException` error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [ChannelDefinitions](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-ChannelDefinitions"></a>
Makes it possible to specify which speaker is on which channel. For example, if your agent is the first participant to speak, you would set `ChannelId` to `0` (to indicate the first channel) and `ParticipantRole` to `AGENT` (to indicate that it's the agent speaking).  
Type: Array of [ChannelDefinition](API_ChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** [DataAccessRoleArn](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.  
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.  
For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: No

 ** [Media](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-Media"></a>
Describes the Amazon S3 location of the media file you want to use in your Call Analytics request.  
Type: [Media](API_Media.md) object  
Required: Yes

 ** [OutputEncryptionKMSKeyId](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-OutputEncryptionKMSKeyId"></a>
The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your Call Analytics output.  
KMS key ARNs have the format `arn:partition:kms:region:account:key/key-id`. For example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. For more information, see [ KMS key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN).  
If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).  
Note that the role making the [StartCallAnalyticsJob](#API_StartCallAnalyticsJob) request and the role specified in the `DataAccessRoleArn` request parameter (if present) must have permission to use the specified KMS key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`   
Required: No

 ** [OutputLocation](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-OutputLocation"></a>
The Amazon S3 location where you want your Call Analytics transcription output stored. You can use any of the following formats to specify the output location:  

1. s3://DOC-EXAMPLE-BUCKET

1. s3://DOC-EXAMPLE-BUCKET/my-output-folder/

1. s3://DOC-EXAMPLE-BUCKET/my-output-folder/my-call-analytics-job.json
Unless you specify a file name (option 3), the name of your output file has a default value that matches the name you specified for your transcription job using the `CallAnalyticsJobName` parameter.  
You can specify a KMS key to encrypt your output using the `OutputEncryptionKMSKeyId` parameter. If you do not specify a KMS key, Amazon Transcribe uses the default Amazon S3 key for server-side encryption.  
If you do not specify `OutputLocation`, your transcript is placed in a service-managed Amazon S3 bucket and you are provided with a URI to access your transcript.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

 ** [Settings](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-Settings"></a>
Specify additional optional settings in your [StartCallAnalyticsJob](#API_StartCallAnalyticsJob) request, including content redaction; allows you to apply custom language models, vocabulary filters, and custom vocabularies to your Call Analytics job.  
Type: [CallAnalyticsJobSettings](API_CallAnalyticsJobSettings.md) object  
Required: No

 ** [Tags](#API_StartCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-StartCallAnalyticsJob-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to a new call analytics job at the time you start this new job.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_StartCallAnalyticsJob_ResponseSyntax"></a>

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
<a name="API_StartCallAnalyticsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CallAnalyticsJob](#API_StartCallAnalyticsJob_ResponseSyntax) **   <a name="transcribe-StartCallAnalyticsJob-response-CallAnalyticsJob"></a>
Provides detailed information about the current Call Analytics job, including job status and, if applicable, failure reason.  
Type: [CallAnalyticsJob](API_CallAnalyticsJob.md) object

## Errors
<a name="API_StartCallAnalyticsJob_Errors"></a>

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
<a name="API_StartCallAnalyticsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/StartCallAnalyticsJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/StartCallAnalyticsJob) 