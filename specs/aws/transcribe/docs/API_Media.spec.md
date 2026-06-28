---
id: "@specs/aws/transcribe/docs/API_Media"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Media"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Media

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_Media
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Media
<a name="API_Media"></a>

Describes the Amazon S3 location of the media file you want to use in your request.

For information on supported media formats, refer to the `MediaFormat` parameter or the [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) section in the Amazon S3 Developer Guide.

## Contents
<a name="API_Media_Contents"></a>

 ** MediaFileUri **   <a name="transcribe-Type-Media-MediaFileUri"></a>
The Amazon S3 location of the media file you want to transcribe. For example:  
+  `s3://DOC-EXAMPLE-BUCKET/my-media-file.flac` 
+  `s3://DOC-EXAMPLE-BUCKET/media-files/my-media-file.flac` 
Note that the Amazon S3 bucket that contains your input media must be located in the same AWS Region where you're making your transcription request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

 ** RedactedMediaFileUri **   <a name="transcribe-Type-Media-RedactedMediaFileUri"></a>
The Amazon S3 location of the media file you want to redact. For example:  
+  `s3://DOC-EXAMPLE-BUCKET/my-media-file.flac` 
+  `s3://DOC-EXAMPLE-BUCKET/media-files/my-media-file.flac` 
Note that the Amazon S3 bucket that contains your input media must be located in the same AWS Region where you're making your transcription request.  
 `RedactedMediaFileUri` produces a redacted audio file in addition to a redacted transcript. It is only supported for Call Analytics (`StartCallAnalyticsJob`) transcription requests.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

## See Also
<a name="API_Media_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/Media) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/Media) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/Media) 