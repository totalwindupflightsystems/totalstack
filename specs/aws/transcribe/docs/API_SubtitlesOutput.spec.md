---
id: "@specs/aws/transcribe/docs/API_SubtitlesOutput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubtitlesOutput"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# SubtitlesOutput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_SubtitlesOutput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubtitlesOutput
<a name="API_SubtitlesOutput"></a>

Provides information about your subtitle file, including format, start index, and Amazon S3 location.

## Contents
<a name="API_SubtitlesOutput_Contents"></a>

 ** Formats **   <a name="transcribe-Type-SubtitlesOutput-Formats"></a>
Provides the format of your subtitle files. If your request included both WebVTT (`vtt`) and SubRip (`srt`) formats, both formats are shown.  
Type: Array of strings  
Valid Values: `vtt | srt`   
Required: No

 ** OutputStartIndex **   <a name="transcribe-Type-SubtitlesOutput-OutputStartIndex"></a>
Provides the start index value for your subtitle files. If you did not specify a value in your request, the default value of `0` is used.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** SubtitleFileUris **   <a name="transcribe-Type-SubtitlesOutput-SubtitleFileUris"></a>
The Amazon S3 location of your transcript. You can use this URI to access or download your subtitle file. Your subtitle file is stored in the same location as your transcript. If you specified both WebVTT and SubRip subtitle formats, two URIs are provided.  
If you included `OutputBucketName` in your transcription job request, this is the URI of that bucket. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.  
If you didn't include `OutputBucketName` in your transcription job request, your subtitle file is stored in a service-managed bucket, and `TranscriptFileUri` provides you with a temporary URI you can use for secure access to your subtitle file.  
Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an `AccesDenied` error, you can get a new temporary URI by running a `GetTranscriptionJob` or `ListTranscriptionJob` request.
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

## See Also
<a name="API_SubtitlesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/SubtitlesOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/SubtitlesOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/SubtitlesOutput) 