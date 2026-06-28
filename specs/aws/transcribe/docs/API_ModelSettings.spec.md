---
id: "@specs/aws/transcribe/docs/API_ModelSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModelSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ModelSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ModelSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModelSettings
<a name="API_ModelSettings"></a>

Provides the name of the custom language model that was included in the specified transcription job.

Only use `ModelSettings` with the `LanguageModelName` sub-parameter if you're **not** using automatic language identification (` LanguageIdSettings `). If using `LanguageIdSettings` in your request, this parameter contains a `LanguageModelName` sub-parameter.

## Contents
<a name="API_ModelSettings_Contents"></a>

 ** LanguageModelName **   <a name="transcribe-Type-ModelSettings-LanguageModelName"></a>
The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.  
The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

## See Also
<a name="API_ModelSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ModelSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ModelSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ModelSettings) 