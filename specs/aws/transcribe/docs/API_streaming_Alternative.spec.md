---
id: "@specs/aws/transcribe/docs/API_streaming_Alternative"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Alternative"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Alternative

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_Alternative
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Alternative
<a name="API_streaming_Alternative"></a>

A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of `Items`, `Entities`, or `Transcript`.

## Contents
<a name="API_streaming_Alternative_Contents"></a>

 ** Entities **   <a name="transcribe-Type-streaming_Alternative-Entities"></a>
Contains entities identified as personally identifiable information (PII) in your transcription output.  
Type: Array of [Entity](API_streaming_Entity.md) objects  
Required: No

 ** Items **   <a name="transcribe-Type-streaming_Alternative-Items"></a>
Contains words, phrases, or punctuation marks in your transcription output.  
Type: Array of [Item](API_streaming_Item.md) objects  
Required: No

 ** Transcript **   <a name="transcribe-Type-streaming_Alternative-Transcript"></a>
Contains transcribed text.  
Type: String  
Required: No

## See Also
<a name="API_streaming_Alternative_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/Alternative) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/Alternative) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/Alternative) 