---
id: "@specs/aws/transcribe/docs/API_MedicalScribeOutput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeOutput"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeOutput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_MedicalScribeOutput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeOutput
<a name="API_MedicalScribeOutput"></a>

The location of the output of your Medical Scribe job. `ClinicalDocumentUri` holds the Amazon S3 URI for the Clinical Document and `TranscriptFileUri` holds the Amazon S3 URI for the Transcript.

## Contents
<a name="API_MedicalScribeOutput_Contents"></a>

 ** ClinicalDocumentUri **   <a name="transcribe-Type-MedicalScribeOutput-ClinicalDocumentUri"></a>
Holds the Amazon S3 URI for the Clinical Document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: Yes

 ** TranscriptFileUri **   <a name="transcribe-Type-MedicalScribeOutput-TranscriptFileUri"></a>
Holds the Amazon S3 URI for the Transcript.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `(s3://|http(s*)://).+`   
Required: Yes

## See Also
<a name="API_MedicalScribeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/MedicalScribeOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/MedicalScribeOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/MedicalScribeOutput) 