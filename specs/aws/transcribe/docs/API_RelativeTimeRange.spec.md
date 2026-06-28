---
id: "@specs/aws/transcribe/docs/API_RelativeTimeRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RelativeTimeRange"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# RelativeTimeRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_RelativeTimeRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RelativeTimeRange
<a name="API_RelativeTimeRange"></a>

A time range, in percentage, between two points in your media file.

You can use `StartPercentage` and `EndPercentage` to search a custom segment. For example, setting `StartPercentage` to 10 and `EndPercentage` to 50 only searches for your specified criteria in the audio contained between the 10 percent mark and the 50 percent mark of your media file.

You can use also `First` to search from the start of the media file until the time that you specify. Or use `Last` to search from the time that you specify until the end of the media file. For example, setting `First` to 10 only searches for your specified criteria in the audio contained in the first 10 percent of the media file.

If you prefer to use milliseconds instead of percentage, see [AbsoluteTimeRange](API_AbsoluteTimeRange.md).

## Contents
<a name="API_RelativeTimeRange_Contents"></a>

 ** EndPercentage **   <a name="transcribe-Type-RelativeTimeRange-EndPercentage"></a>
The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** First **   <a name="transcribe-Type-RelativeTimeRange-First"></a>
The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** Last **   <a name="transcribe-Type-RelativeTimeRange-Last"></a>
The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** StartPercentage **   <a name="transcribe-Type-RelativeTimeRange-StartPercentage"></a>
The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

## See Also
<a name="API_RelativeTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/RelativeTimeRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/RelativeTimeRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/RelativeTimeRange) 