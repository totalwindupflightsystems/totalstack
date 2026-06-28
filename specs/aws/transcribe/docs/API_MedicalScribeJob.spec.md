---
id: "@specs/aws/transcribe/docs/API_MedicalScribeJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalScribeJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeJob
<a name="API_MedicalScribeJob"></a>

Provides detailed information about a Medical Scribe job.

To view the status of the specified Medical Scribe job, check the `MedicalScribeJobStatus` field. If the status is `COMPLETED`, the job is finished and you can find the results at the locations specified in `MedicalScribeOutput`. If the status is `FAILED`, `FailureReason` provides details on why your Medical Scribe job failed.

## Contents
<a name="API_MedicalScribeJob_Contents"></a>

 ** ChannelDefinitions **   <a name="transcribe-Type-MedicalScribeJob-ChannelDefinitions"></a>
Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set `ChannelId` of the first `ChannelDefinition` in the list to `0` (to indicate the first channel) and `ParticipantRole` to `CLINICIAN` (to indicate that it's the clinician speaking). Then you would set the `ChannelId` of the second `ChannelDefinition` in the list to `1` (to indicate the second channel) and `ParticipantRole` to `PATIENT` (to indicate that it's the patient speaking).   
Type: Array of [MedicalScribeChannelDefinition](API_MedicalScribeChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** CompletionTime **   <a name="transcribe-Type-MedicalScribeJob-CompletionTime"></a>
The date and time the specified Medical Scribe job finished processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** CreationTime **   <a name="transcribe-Type-MedicalScribeJob-CreationTime"></a>
The date and time the specified Medical Scribe job request was made.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** DataAccessRoleArn **   <a name="transcribe-Type-MedicalScribeJob-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your AWS KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions your request fails.  
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.  
For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: No

 ** FailureReason **   <a name="transcribe-Type-MedicalScribeJob-FailureReason"></a>
If `MedicalScribeJobStatus` is `FAILED`, `FailureReason` contains information about why the transcription job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-MedicalScribeJob-LanguageCode"></a>
The language code used to create your Medical Scribe job. US English (`en-US`) is the only supported language for Medical Scribe jobs.   
Type: String  
Valid Values: `en-US`   
Required: No

 ** Media **   <a name="transcribe-Type-MedicalScribeJob-Media"></a>
Describes the Amazon S3 location of the media file you want to use in your request.  
For information on supported media formats, refer to the `MediaFormat` parameter or the [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) section in the Amazon S3 Developer Guide.  
Type: [Media](API_Media.md) object  
Required: No

 ** MedicalScribeContextProvided **   <a name="transcribe-Type-MedicalScribeJob-MedicalScribeContextProvided"></a>
Indicates whether the `MedicalScribeContext` object was provided when the Medical Scribe job was started.  
Type: Boolean  
Required: No

 ** MedicalScribeJobName **   <a name="transcribe-Type-MedicalScribeJob-MedicalScribeJobName"></a>
The name of the Medical Scribe job. Job names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** MedicalScribeJobStatus **   <a name="transcribe-Type-MedicalScribeJob-MedicalScribeJobStatus"></a>
Provides the status of the specified Medical Scribe job.  
If the status is `COMPLETED`, the job is finished and you can find the results at the location specified in `MedicalScribeOutput` If the status is `FAILED`, `FailureReason` provides details on why your Medical Scribe job failed.  
Type: String  
Valid Values: `QUEUED | IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** MedicalScribeOutput **   <a name="transcribe-Type-MedicalScribeJob-MedicalScribeOutput"></a>
The location of the output of your Medical Scribe job. `ClinicalDocumentUri` holds the Amazon S3 URI for the Clinical Document and `TranscriptFileUri` holds the Amazon S3 URI for the Transcript.  
Type: [MedicalScribeOutput](API_MedicalScribeOutput.md) object  
Required: No

 ** Settings **   <a name="transcribe-Type-MedicalScribeJob-Settings"></a>
Makes it possible to control how your Medical Scribe job is processed using a `MedicalScribeSettings` object. Specify `ChannelIdentification` if `ChannelDefinitions` are set. Enabled `ShowSpeakerLabels` if `ChannelIdentification` and `ChannelDefinitions` are not set. One and only one of `ChannelIdentification` and `ShowSpeakerLabels` must be set. If `ShowSpeakerLabels` is set, `MaxSpeakerLabels` must also be set. Use `Settings` to specify a vocabulary or vocabulary filter or both using `VocabularyName`, `VocabularyFilterName`. `VocabularyFilterMethod` must be specified if `VocabularyFilterName` is set.   
Type: [MedicalScribeSettings](API_MedicalScribeSettings.md) object  
Required: No

 ** StartTime **   <a name="transcribe-Type-MedicalScribeJob-StartTime"></a>
The date and time your Medical Scribe job began processing.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.789000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** Tags **   <a name="transcribe-Type-MedicalScribeJob-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to the Medical Scribe job.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## See Also
<a name="API_MedicalScribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalScribeJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalScribeJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalScribeJob) 