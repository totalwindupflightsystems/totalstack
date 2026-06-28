---
id: "@specs/aws/transcribe/docs/API_streaming_CharacterOffsets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CharacterOffsets"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CharacterOffsets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_CharacterOffsets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CharacterOffsets
<a name="API_streaming_CharacterOffsets"></a>

Provides the location, using character count, in your transcript where a match is identified. For example, the location of an issue or a category match within a segment.

## Contents
<a name="API_streaming_CharacterOffsets_Contents"></a>

 ** Begin **   <a name="transcribe-Type-streaming_CharacterOffsets-Begin"></a>
Provides the character count of the first character where a match is identified. For example, the first character associated with an issue or a category match in a segment transcript.  
Type: Integer  
Required: No

 ** End **   <a name="transcribe-Type-streaming_CharacterOffsets-End"></a>
Provides the character count of the last character where a match is identified. For example, the last character associated with an issue or a category match in a segment transcript.  
Type: Integer  
Required: No

## See Also
<a name="API_streaming_CharacterOffsets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CharacterOffsets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CharacterOffsets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CharacterOffsets) 