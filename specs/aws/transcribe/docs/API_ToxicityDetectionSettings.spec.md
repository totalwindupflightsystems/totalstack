---
id: "@specs/aws/transcribe/docs/API_ToxicityDetectionSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ToxicityDetectionSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ToxicityDetectionSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ToxicityDetectionSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ToxicityDetectionSettings
<a name="API_ToxicityDetectionSettings"></a>

Contains `ToxicityCategories`, which is a required parameter if you want to enable toxicity detection (`ToxicityDetection`) in your transcription request.

## Contents
<a name="API_ToxicityDetectionSettings_Contents"></a>

 ** ToxicityCategories **   <a name="transcribe-Type-ToxicityDetectionSettings-ToxicityCategories"></a>
 If you include `ToxicityDetection` in your transcription request, you must also include `ToxicityCategories`. The only accepted value for this parameter is `ALL`.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `ALL`   
Required: Yes

## See Also
<a name="API_ToxicityDetectionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ToxicityDetectionSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ToxicityDetectionSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ToxicityDetectionSettings) 