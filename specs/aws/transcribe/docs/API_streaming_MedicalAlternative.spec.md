---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalAlternative"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalAlternative"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalAlternative

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalAlternative
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalAlternative
<a name="API_streaming_MedicalAlternative"></a>

A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of `Items`, `Entities`, or `Transcript`.

## Contents
<a name="API_streaming_MedicalAlternative_Contents"></a>

 ** Entities **   <a name="transcribe-Type-streaming_MedicalAlternative-Entities"></a>
Contains entities identified as personal health information (PHI) in your transcription output.  
Type: Array of [MedicalEntity](API_streaming_MedicalEntity.md) objects  
Required: No

 ** Items **   <a name="transcribe-Type-streaming_MedicalAlternative-Items"></a>
Contains words, phrases, or punctuation marks in your transcription output.  
Type: Array of [MedicalItem](API_streaming_MedicalItem.md) objects  
Required: No

 ** Transcript **   <a name="transcribe-Type-streaming_MedicalAlternative-Transcript"></a>
Contains transcribed text.  
Type: String  
Required: No

## See Also
<a name="API_streaming_MedicalAlternative_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalAlternative) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalAlternative) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalAlternative) 