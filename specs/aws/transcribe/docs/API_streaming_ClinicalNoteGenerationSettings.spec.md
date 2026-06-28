---
id: "@specs/aws/transcribe/docs/API_streaming_ClinicalNoteGenerationSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClinicalNoteGenerationSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ClinicalNoteGenerationSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_ClinicalNoteGenerationSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClinicalNoteGenerationSettings
<a name="API_streaming_ClinicalNoteGenerationSettings"></a>

The output configuration for aggregated transcript and clinical note generation.

## Contents
<a name="API_streaming_ClinicalNoteGenerationSettings_Contents"></a>

 ** OutputBucketName **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationSettings-OutputBucketName"></a>
The name of the Amazon S3 bucket where you want the output of AWS HealthScribe post-stream analytics stored. Don't include the `S3://` prefix of the specified bucket.   
HealthScribe outputs transcript and clinical note files under the prefix: `S3://$output-bucket-name/healthscribe-streaming/session-id/post-stream-analytics/clinical-notes`   
The role `ResourceAccessRoleArn` specified in the `MedicalScribeConfigurationEvent` must have permission to use the specified location. You can change Amazon S3 permissions using the [AWS Management Console](https://console.aws.amazon.com/s3). See also [Permissions Required for IAM User Roles ](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user) .   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`   
Required: Yes

 ** NoteTemplate **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationSettings-NoteTemplate"></a>
Specify one of the following templates to use for the clinical note summary. The default is `HISTORY_AND_PHYSICAL`.  
+ HISTORY\_AND\_PHYSICAL: Provides summaries for key sections of the clinical documentation. Examples of sections include Chief Complaint, History of Present Illness, Review of Systems, Past Medical History, Assessment, and Plan. 
+ GIRPP: Provides summaries based on the patients progress toward goals. Examples of sections include Goal, Intervention, Response, Progress, and Plan.
+ BIRP: Focuses on the patient's behavioral patterns and responses. Examples of sections include Behavior, Intervention, Response, and Plan.
+ SIRP: Emphasizes the situational context of therapy. Examples of sections include Situation, Intervention, Response, and Plan.
+ DAP: Provides a simplified format for clinical documentation. Examples of sections include Data, Assessment, and Plan.
+ BEHAVIORAL\_SOAP: Behavioral health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.
+ PHYSICAL\_SOAP: Physical health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.
Type: String  
Valid Values: `HISTORY_AND_PHYSICAL | GIRPP | DAP | SIRP | BIRP | BEHAVIORAL_SOAP | PHYSICAL_SOAP`   
Required: No

## See Also
<a name="API_streaming_ClinicalNoteGenerationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/ClinicalNoteGenerationSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/ClinicalNoteGenerationSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/ClinicalNoteGenerationSettings) 