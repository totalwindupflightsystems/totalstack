---
id: "@specs/aws/transcribe/docs/API_InterruptionFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InterruptionFilter"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# InterruptionFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_InterruptionFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InterruptionFilter
<a name="API_InterruptionFilter"></a>

Flag the presence or absence of interruptions in your Call Analytics transcription output.

Rules using `InterruptionFilter` are designed to match:
+ Instances where an agent interrupts a customer
+ Instances where a customer interrupts an agent
+ Either participant interrupting the other
+ A lack of interruptions

See [Rule criteria for post-call categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html#tca-rules-batch) for usage examples.

## Contents
<a name="API_InterruptionFilter_Contents"></a>

 ** AbsoluteTimeRange **   <a name="transcribe-Type-InterruptionFilter-AbsoluteTimeRange"></a>
Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for an interruption. See [AbsoluteTimeRange](API_AbsoluteTimeRange.md) for more detail.  
Type: [AbsoluteTimeRange](API_AbsoluteTimeRange.md) object  
Required: No

 ** Negate **   <a name="transcribe-Type-InterruptionFilter-Negate"></a>
Set to `TRUE` to flag speech that does not contain interruptions. Set to `FALSE` to flag speech that contains interruptions.  
Type: Boolean  
Required: No

 ** ParticipantRole **   <a name="transcribe-Type-InterruptionFilter-ParticipantRole"></a>
Specify the interrupter that you want to flag. Omitting this parameter is equivalent to specifying both participants.  
Type: String  
Valid Values: `AGENT | CUSTOMER`   
Required: No

 ** RelativeTimeRange **   <a name="transcribe-Type-InterruptionFilter-RelativeTimeRange"></a>
Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for an interruption. See [RelativeTimeRange](API_RelativeTimeRange.md) for more detail.  
Type: [RelativeTimeRange](API_RelativeTimeRange.md) object  
Required: No

 ** Threshold **   <a name="transcribe-Type-InterruptionFilter-Threshold"></a>
Specify the duration of the interruptions in milliseconds. For example, you can flag speech that contains more than 10,000 milliseconds of interruptions.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 14400000.  
Required: No

## See Also
<a name="API_InterruptionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/InterruptionFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/InterruptionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/InterruptionFilter) 