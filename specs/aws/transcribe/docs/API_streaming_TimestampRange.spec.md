---
id: "@specs/aws/transcribe/docs/API_streaming_TimestampRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TimestampRange"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# TimestampRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_TimestampRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TimestampRange
<a name="API_streaming_TimestampRange"></a>

Contains the timestamp range (start time through end time) of a matched category.

## Contents
<a name="API_streaming_TimestampRange_Contents"></a>

 ** BeginOffsetMillis **   <a name="transcribe-Type-streaming_TimestampRange-BeginOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the category match.  
Type: Long  
Required: No

 ** EndOffsetMillis **   <a name="transcribe-Type-streaming_TimestampRange-EndOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the end of the category match.  
Type: Long  
Required: No

## See Also
<a name="API_streaming_TimestampRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/TimestampRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/TimestampRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/TimestampRange) 