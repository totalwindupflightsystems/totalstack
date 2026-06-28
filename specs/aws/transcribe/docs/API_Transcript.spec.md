---
id: "@specs/aws/transcribe/docs/API_Transcript"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Transcript"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Transcript

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_Transcript
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Transcript
<a name="API_Transcript"></a>

Provides you with the Amazon S3 URI you can use to access your transcript.

## Contents
<a name="API_Transcript_Contents"></a>

 ** RedactedTranscriptFileUri **   <a name="transcribe-Type-Transcript-RedactedTranscriptFileUri"></a>
The Amazon S3 location of your redacted transcript. You can use this URI to access or download your transcript.  
If you included `OutputBucketName` in your transcription job request, this is the URI of that bucket. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.  
If you didn't include `OutputBucketName` in your transcription job request, your transcript is stored in a service-managed bucket, and `RedactedTranscriptFileUri` provides you with a temporary URI you can use for secure access to your transcript.  
Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an `AccesDenied` error, you can get a new temporary URI by running a `GetTranscriptionJob` or `ListTranscriptionJob` request.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

 ** TranscriptFileUri **   <a name="transcribe-Type-Transcript-TranscriptFileUri"></a>
The Amazon S3 location of your transcript. You can use this URI to access or download your transcript.  
If you included `OutputBucketName` in your transcription job request, this is the URI of that bucket. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.  
If you didn't include `OutputBucketName` in your transcription job request, your transcript is stored in a service-managed bucket, and `TranscriptFileUri` provides you with a temporary URI you can use for secure access to your transcript.  
Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an `AccesDenied` error, you can get a new temporary URI by running a `GetTranscriptionJob` or `ListTranscriptionJob` request.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

## See Also
<a name="API_Transcript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/Transcript) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/Transcript) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/Transcript) 