---
id: "@specs/aws/transcribe/docs/API_MedicalScribeChannelDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeChannelDefinition"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeChannelDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalScribeChannelDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeChannelDefinition
<a name="API_MedicalScribeChannelDefinition"></a>

Indicates which speaker is on which channel. The options are `CLINICIAN` and `PATIENT` 

## Contents
<a name="API_MedicalScribeChannelDefinition_Contents"></a>

 ** ChannelId **   <a name="transcribe-Type-MedicalScribeChannelDefinition-ChannelId"></a>
Specify the audio channel you want to define.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: Yes

 ** ParticipantRole **   <a name="transcribe-Type-MedicalScribeChannelDefinition-ParticipantRole"></a>
Specify the participant that you want to flag. The options are `CLINICIAN` and `PATIENT`   
Type: String  
Valid Values: `PATIENT | CLINICIAN`   
Required: Yes

## See Also
<a name="API_MedicalScribeChannelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalScribeChannelDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalScribeChannelDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalScribeChannelDefinition) 