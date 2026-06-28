---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeConfigurationEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeConfigurationEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeConfigurationEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeConfigurationEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeConfigurationEvent
<a name="API_streaming_MedicalScribeConfigurationEvent"></a>

Specify details to configure the streaming session, including channel definitions, encryption settings, post-stream analytics settings, resource access role ARN and vocabulary settings. 

Whether you are starting a new session or resuming an existing session, your first event must be a `MedicalScribeConfigurationEvent`. If you are resuming a session, then this event must have the same configurations that you provided to start the session. 

## Contents
<a name="API_streaming_MedicalScribeConfigurationEvent_Contents"></a>

 ** PostStreamAnalyticsSettings **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-PostStreamAnalyticsSettings"></a>
Specify settings for post-stream analytics.  
Type: [MedicalScribePostStreamAnalyticsSettings](API_streaming_MedicalScribePostStreamAnalyticsSettings.md) object  
Required: Yes

 ** ResourceAccessRoleArn **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-ResourceAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 output bucket you specified, and use your AWS KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions, your request fails.   
 IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.   
For more information, see [AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-streaming.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`   
Required: Yes

 ** ChannelDefinitions **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-ChannelDefinitions"></a>
Specify which speaker is on which audio channel.  
Type: Array of [MedicalScribeChannelDefinition](API_streaming_MedicalScribeChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** EncryptionSettings **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-EncryptionSettings"></a>
Specify the encryption settings for your streaming session.  
Type: [MedicalScribeEncryptionSettings](API_streaming_MedicalScribeEncryptionSettings.md) object  
Required: No

 ** MedicalScribeContext **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-MedicalScribeContext"></a>
The `MedicalScribeContext` object that contains contextual information used to generate customized clinical notes.  
Type: [MedicalScribeContext](API_streaming_MedicalScribeContext.md) object  
Required: No

 ** VocabularyFilterMethod **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-VocabularyFilterMethod"></a>
Specify how you want your custom vocabulary filter applied to the streaming session.  
To replace words with `***`, specify `mask`.   
To delete words, specify `remove`.   
To flag words without changing them, specify `tag`.   
Type: String  
Valid Values: `remove | mask | tag`   
Required: No

 ** VocabularyFilterName **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-VocabularyFilterName"></a>
Specify the name of the custom vocabulary filter you want to include in your streaming session. Custom vocabulary filter names are case-sensitive.   
If you include `VocabularyFilterName` in the `MedicalScribeConfigurationEvent`, you must also include `VocabularyFilterMethod`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyName **   <a name="transcribe-Type-streaming_MedicalScribeConfigurationEvent-VocabularyName"></a>
Specify the name of the custom vocabulary you want to use for your streaming session. Custom vocabulary names are case-sensitive.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

## See Also
<a name="API_streaming_MedicalScribeConfigurationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeConfigurationEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeConfigurationEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeConfigurationEvent) 