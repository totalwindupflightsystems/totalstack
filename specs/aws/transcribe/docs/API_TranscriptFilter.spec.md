---
id: "@specs/aws/transcribe/docs/API_TranscriptFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TranscriptFilter"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# TranscriptFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_TranscriptFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TranscriptFilter
<a name="API_TranscriptFilter"></a>

Flag the presence or absence of specific words or phrases detected in your Call Analytics transcription output.

Rules using `TranscriptFilter` are designed to match:
+ Custom words or phrases spoken by the agent, the customer, or both
+ Custom words or phrases **not** spoken by the agent, the customer, or either
+ Custom words or phrases that occur at a specific time frame

See [Rule criteria for post-call categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html#tca-rules-batch) and [Rule criteria for streaming categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html#tca-rules-stream) for usage examples.

## Contents
<a name="API_TranscriptFilter_Contents"></a>

 ** Targets **   <a name="transcribe-Type-TranscriptFilter-Targets"></a>
Specify the phrases that you want to flag.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `.*\S.*`   
Required: Yes

 ** TranscriptFilterType **   <a name="transcribe-Type-TranscriptFilter-TranscriptFilterType"></a>
Flag the presence or absence of an exact match to the phrases that you specify. For example, if you specify the phrase "speak to a manager" as your `Targets` value, only that exact phrase is flagged.  
Note that semantic matching is not supported. For example, if your customer says "speak to *the* manager", instead of "speak to *a* manager", your content is not flagged.  
Type: String  
Valid Values: `EXACT`   
Required: Yes

 ** AbsoluteTimeRange **   <a name="transcribe-Type-TranscriptFilter-AbsoluteTimeRange"></a>
Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified key words or phrases. See [AbsoluteTimeRange](API_AbsoluteTimeRange.md) for more detail.  
Type: [AbsoluteTimeRange](API_AbsoluteTimeRange.md) object  
Required: No

 ** Negate **   <a name="transcribe-Type-TranscriptFilter-Negate"></a>
Set to `TRUE` to flag the absence of the phrase that you specified in your request. Set to `FALSE` to flag the presence of the phrase that you specified in your request.  
Type: Boolean  
Required: No

 ** ParticipantRole **   <a name="transcribe-Type-TranscriptFilter-ParticipantRole"></a>
Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.  
Type: String  
Valid Values: `AGENT | CUSTOMER`   
Required: No

 ** RelativeTimeRange **   <a name="transcribe-Type-TranscriptFilter-RelativeTimeRange"></a>
Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified key words or phrases. See [RelativeTimeRange](API_RelativeTimeRange.md) for more detail.  
Type: [RelativeTimeRange](API_RelativeTimeRange.md) object  
Required: No

## See Also
<a name="API_TranscriptFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/TranscriptFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/TranscriptFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/TranscriptFilter) 