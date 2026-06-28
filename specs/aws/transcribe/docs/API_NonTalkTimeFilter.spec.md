---
id: "@specs/aws/transcribe/docs/API_NonTalkTimeFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NonTalkTimeFilter"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# NonTalkTimeFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_NonTalkTimeFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NonTalkTimeFilter
<a name="API_NonTalkTimeFilter"></a>

Flag the presence or absence of periods of silence in your Call Analytics transcription output.

Rules using `NonTalkTimeFilter` are designed to match:
+ The presence of silence at specified periods throughout the call
+ The presence of speech at specified periods throughout the call

See [Rule criteria for post-call categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html#tca-rules-batch) for usage examples.

## Contents
<a name="API_NonTalkTimeFilter_Contents"></a>

 ** AbsoluteTimeRange **   <a name="transcribe-Type-NonTalkTimeFilter-AbsoluteTimeRange"></a>
Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for a period of silence. See [AbsoluteTimeRange](API_AbsoluteTimeRange.md) for more detail.  
Type: [AbsoluteTimeRange](API_AbsoluteTimeRange.md) object  
Required: No

 ** Negate **   <a name="transcribe-Type-NonTalkTimeFilter-Negate"></a>
Set to `TRUE` to flag periods of speech. Set to `FALSE` to flag periods of silence  
Type: Boolean  
Required: No

 ** RelativeTimeRange **   <a name="transcribe-Type-NonTalkTimeFilter-RelativeTimeRange"></a>
Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for a period of silence. See [RelativeTimeRange](API_RelativeTimeRange.md) for more detail.  
Type: [RelativeTimeRange](API_RelativeTimeRange.md) object  
Required: No

 ** Threshold **   <a name="transcribe-Type-NonTalkTimeFilter-Threshold"></a>
Specify the duration, in milliseconds, of the period of silence that you want to flag. For example, you can flag a silent period that lasts 30,000 milliseconds.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 14400000.  
Required: No

## See Also
<a name="API_NonTalkTimeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/NonTalkTimeFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/NonTalkTimeFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/NonTalkTimeFilter) 