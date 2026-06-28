---
id: "@specs/aws/transcribe/docs/API_MedicalTranscript"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalTranscript"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalTranscript

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalTranscript
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalTranscript
<a name="API_MedicalTranscript"></a>

Provides you with the Amazon S3 URI you can use to access your transcript.

## Contents
<a name="API_MedicalTranscript_Contents"></a>

 ** TranscriptFileUri **   <a name="transcribe-Type-MedicalTranscript-TranscriptFileUri"></a>
The Amazon S3 location of your transcript. You can use this URI to access or download your transcript.  
Note that this is the Amazon S3 location you specified in your request using the `OutputBucketName` parameter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: No

## See Also
<a name="API_MedicalTranscript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalTranscript) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalTranscript) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalTranscript) 