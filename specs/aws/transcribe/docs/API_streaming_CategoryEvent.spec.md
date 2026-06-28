---
id: "@specs/aws/transcribe/docs/API_streaming_CategoryEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CategoryEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CategoryEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_CategoryEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CategoryEvent
<a name="API_streaming_CategoryEvent"></a>

Provides information on any `TranscriptFilterType` categories that matched your transcription output. Matches are identified for each segment upon completion of that segment.

## Contents
<a name="API_streaming_CategoryEvent_Contents"></a>

 ** MatchedCategories **   <a name="transcribe-Type-streaming_CategoryEvent-MatchedCategories"></a>
Lists the categories that were matched in your audio segment.  
Type: Array of strings  
Required: No

 ** MatchedDetails **   <a name="transcribe-Type-streaming_CategoryEvent-MatchedDetails"></a>
Contains information about the matched categories, including category names and timestamps.  
Type: String to [PointsOfInterest](API_streaming_PointsOfInterest.md) object map  
Required: No

## See Also
<a name="API_streaming_CategoryEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CategoryEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CategoryEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CategoryEvent) 