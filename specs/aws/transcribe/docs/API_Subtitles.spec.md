---
id: "@specs/aws/transcribe/docs/API_Subtitles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Subtitles"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Subtitles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_Subtitles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Subtitles
<a name="API_Subtitles"></a>

Generate subtitles for your media file with your transcription request.

You can choose a start index of 0 or 1, and you can specify either WebVTT or SubRip (or both) as your output format.

Note that your subtitle files are placed in the same location as your transcription output.

## Contents
<a name="API_Subtitles_Contents"></a>

 ** Formats **   <a name="transcribe-Type-Subtitles-Formats"></a>
Specify the output format for your subtitle file; if you select both WebVTT (`vtt`) and SubRip (`srt`) formats, two output files are generated.  
Type: Array of strings  
Valid Values: `vtt | srt`   
Required: No

 ** OutputStartIndex **   <a name="transcribe-Type-Subtitles-OutputStartIndex"></a>
Specify the starting value that is assigned to the first subtitle segment.  
The default start index for Amazon Transcribe is `0`, which differs from the more widely used standard of `1`. If you're uncertain which value to use, we recommend choosing `1`, as this may improve compatibility with other services.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_Subtitles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/Subtitles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/Subtitles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/Subtitles) 