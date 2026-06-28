---
id: "@specs/aws/transcribe/docs/API_AbsoluteTimeRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AbsoluteTimeRange"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# AbsoluteTimeRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_AbsoluteTimeRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AbsoluteTimeRange
<a name="API_AbsoluteTimeRange"></a>

A time range, in milliseconds, between two points in your media file.

You can use `StartTime` and `EndTime` to search a custom segment. For example, setting `StartTime` to 10000 and `EndTime` to 50000 only searches for your specified criteria in the audio contained between the 10,000 millisecond mark and the 50,000 millisecond mark of your media file. You must use `StartTime` and `EndTime` as a set; that is, if you include one, you must include both.

You can use also `First` to search from the start of the audio until the time that you specify, or `Last` to search from the time that you specify until the end of the audio. For example, setting `First` to 50000 only searches for your specified criteria in the audio contained between the start of the media file to the 50,000 millisecond mark. You can use `First` and `Last` independently of each other.

If you prefer to use percentage instead of milliseconds, see [RelativeTimeRange](API_RelativeTimeRange.md).

## Contents
<a name="API_AbsoluteTimeRange_Contents"></a>

 ** EndTime **   <a name="transcribe-Type-AbsoluteTimeRange-EndTime"></a>
The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime`.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 14400000.  
Required: No

 ** First **   <a name="transcribe-Type-AbsoluteTimeRange-First"></a>
The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 14400000.  
Required: No

 ** Last **   <a name="transcribe-Type-AbsoluteTimeRange-Last"></a>
The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 14400000.  
Required: No

 ** StartTime **   <a name="transcribe-Type-AbsoluteTimeRange-StartTime"></a>
The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime`.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 14400000.  
Required: No

## See Also
<a name="API_AbsoluteTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/AbsoluteTimeRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/AbsoluteTimeRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/AbsoluteTimeRange) 