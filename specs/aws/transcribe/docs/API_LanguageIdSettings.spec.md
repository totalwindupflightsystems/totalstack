---
id: "@specs/aws/transcribe/docs/API_LanguageIdSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LanguageIdSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# LanguageIdSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_LanguageIdSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LanguageIdSettings
<a name="API_LanguageIdSettings"></a>

If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName`, `LanguageModelName`, and `VocabularyFilterName`). Note that multi-language identification (`IdentifyMultipleLanguages`) doesn't support custom language models.

 `LanguageIdSettings` supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.

It's recommended that you include `LanguageOptions` when using `LanguageIdSettings` to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in `en-US` but Amazon Transcribe determines that the language spoken in your media is `en-AU`, your custom vocabulary *is not* applied to your transcription. If you include `LanguageOptions` and include `en-US` as the only English language dialect, your custom vocabulary *is* applied to your transcription.

If you want to include a custom language model with your request but **do not** want to use automatic language identification, use instead the ` ModelSettings ` parameter with the `LanguageModelName` sub-parameter. If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but **do not** want to use automatic language identification, use instead the ` Settings ` parameter with the `VocabularyName` or `VocabularyFilterName` (or both) sub-parameter.

## Contents
<a name="API_LanguageIdSettings_Contents"></a>

 ** LanguageModelName **   <a name="transcribe-Type-LanguageIdSettings-LanguageModelName"></a>
The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.  
The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyFilterName **   <a name="transcribe-Type-LanguageIdSettings-VocabularyFilterName"></a>
The name of the custom vocabulary filter you want to use when processing your transcription job. Custom vocabulary filter names are case sensitive.  
The language of the specified custom vocabulary filter must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary filter isn't applied. There are no errors or warnings associated with a language mismatch.  
Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** VocabularyName **   <a name="transcribe-Type-LanguageIdSettings-VocabularyName"></a>
The name of the custom vocabulary you want to use when processing your transcription job. Custom vocabulary names are case sensitive.  
The language of the specified custom vocabulary must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary isn't applied. There are no errors or warnings associated with a language mismatch.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

## See Also
<a name="API_LanguageIdSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/LanguageIdSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/LanguageIdSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/LanguageIdSettings) 