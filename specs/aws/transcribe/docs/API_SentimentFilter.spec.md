---
id: "@specs/aws/transcribe/docs/API_SentimentFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SentimentFilter"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# SentimentFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_SentimentFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SentimentFilter
<a name="API_SentimentFilter"></a>

Flag the presence or absence of specific sentiments detected in your Call Analytics transcription output.

Rules using `SentimentFilter` are designed to match:
+ The presence or absence of a positive sentiment felt by the customer, agent, or both at specified points in the call
+ The presence or absence of a negative sentiment felt by the customer, agent, or both at specified points in the call
+ The presence or absence of a neutral sentiment felt by the customer, agent, or both at specified points in the call
+ The presence or absence of a mixed sentiment felt by the customer, the agent, or both at specified points in the call

See [Rule criteria for post-call categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html#tca-rules-batch) for usage examples.

## Contents
<a name="API_SentimentFilter_Contents"></a>

 ** Sentiments **   <a name="transcribe-Type-SentimentFilter-Sentiments"></a>
Specify the sentiments that you want to flag.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL | MIXED`   
Required: Yes

 ** AbsoluteTimeRange **   <a name="transcribe-Type-SentimentFilter-AbsoluteTimeRange"></a>
Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified sentiments. See [AbsoluteTimeRange](API_AbsoluteTimeRange.md) for more detail.  
Type: [AbsoluteTimeRange](API_AbsoluteTimeRange.md) object  
Required: No

 ** Negate **   <a name="transcribe-Type-SentimentFilter-Negate"></a>
Set to `TRUE` to flag the sentiments that you didn't include in your request. Set to `FALSE` to flag the sentiments that you specified in your request.  
Type: Boolean  
Required: No

 ** ParticipantRole **   <a name="transcribe-Type-SentimentFilter-ParticipantRole"></a>
Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.  
Type: String  
Valid Values: `AGENT | CUSTOMER`   
Required: No

 ** RelativeTimeRange **   <a name="transcribe-Type-SentimentFilter-RelativeTimeRange"></a>
Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified sentiments. See [RelativeTimeRange](API_RelativeTimeRange.md) for more detail.  
Type: [RelativeTimeRange](API_RelativeTimeRange.md) object  
Required: No

## See Also
<a name="API_SentimentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/SentimentFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/SentimentFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/SentimentFilter) 