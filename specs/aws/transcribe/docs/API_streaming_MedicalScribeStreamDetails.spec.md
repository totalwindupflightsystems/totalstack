---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeStreamDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeStreamDetails"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeStreamDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeStreamDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeStreamDetails
<a name="API_streaming_MedicalScribeStreamDetails"></a>

Contains details about a AWS HealthScribe streaming session.

## Contents
<a name="API_streaming_MedicalScribeStreamDetails_Contents"></a>

 ** ChannelDefinitions **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-ChannelDefinitions"></a>
The Channel Definitions of the HealthScribe streaming session.  
Type: Array of [MedicalScribeChannelDefinition](API_streaming_MedicalScribeChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** EncryptionSettings **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-EncryptionSettings"></a>
The Encryption Settings of the HealthScribe streaming session.  
Type: [MedicalScribeEncryptionSettings](API_streaming_MedicalScribeEncryptionSettings.md) object  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-LanguageCode"></a>
The Language Code of the HealthScribe streaming session.  
Type: String  
Valid Values: `en-US`   
Required: No

 ** MediaEncoding **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-MediaEncoding"></a>
The Media Encoding of the HealthScribe streaming session.  
Type: String  
Valid Values: `pcm | ogg-opus | flac`   
Required: No

 ** MediaSampleRateHertz **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-MediaSampleRateHertz"></a>
The sample rate (in hertz) of the HealthScribe streaming session.  
Type: Integer  
Valid Range: Minimum value of 16000. Maximum value of 48000.  
Required: No

 ** MedicalScribeContextProvided **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-MedicalScribeContextProvided"></a>
Indicates whether the `MedicalScribeContext` object was provided when the stream was started.  
Type: Boolean  
Required: No

 ** PostStreamAnalyticsResult **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-PostStreamAnalyticsResult"></a>
The result of post-stream analytics for the HealthScribe streaming session.  
Type: [MedicalScribePostStreamAnalyticsResult](API_streaming_MedicalScribePostStreamAnalyticsResult.md) object  
Required: No

 ** PostStreamAnalyticsSettings **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-PostStreamAnalyticsSettings"></a>
The post-stream analytics settings of the HealthScribe streaming session.  
Type: [MedicalScribePostStreamAnalyticsSettings](API_streaming_MedicalScribePostStreamAnalyticsSettings.md) object  
Required: No

 ** ResourceAccessRoleArn **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-ResourceAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the role used in the HealthScribe streaming session.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: No

 ** SessionId **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-SessionId"></a>
The identifier of the HealthScribe streaming session.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`   
Required: No

 ** StreamCreatedAt **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-StreamCreatedAt"></a>
The date and time when the HealthScribe streaming session was created.  
Type: Timestamp  
Required: No

 ** StreamEndedAt **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-StreamEndedAt"></a>
The date and time when the HealthScribe streaming session was ended.  
Type: Timestamp  
Required: No

 ** StreamStatus **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-StreamStatus"></a>
The streaming status of the HealthScribe streaming session.  
Possible Values:  
+  `IN_PROGRESS` 
+  `PAUSED` 
+  `FAILED` 
+  `COMPLETED` 
This status is specific to real-time streaming. A `COMPLETED` status doesn't mean that the post-stream analytics is complete. To get status of an analytics result, check the `Status` field for the analytics result within the `MedicalScribePostStreamAnalyticsResult`. For example, you can view the status of the `ClinicalNoteGenerationResult`. 
Type: String  
Valid Values: `IN_PROGRESS | PAUSED | FAILED | COMPLETED`   
Required: No

 ** VocabularyFilterMethod **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-VocabularyFilterMethod"></a>
The method of the vocabulary filter for the HealthScribe streaming session.  
Type: String  
Valid Values: `remove | mask | tag`   
Required: No

 ** VocabularyFilterName **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-VocabularyFilterName"></a>
The name of the vocabulary filter used for the HealthScribe streaming session .  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyName **   <a name="transcribe-Type-streaming_MedicalScribeStreamDetails-VocabularyName"></a>
The vocabulary name of the HealthScribe streaming session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

## See Also
<a name="API_streaming_MedicalScribeStreamDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeStreamDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeStreamDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeStreamDetails) 