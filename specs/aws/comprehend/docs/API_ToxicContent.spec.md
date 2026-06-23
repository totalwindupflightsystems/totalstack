---
id: "@specs/aws/comprehend/docs/API_ToxicContent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ToxicContent"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ToxicContent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ToxicContent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ToxicContent
<a name="API_ToxicContent"></a>

**Important**  
Service availability notice: Amazon Comprehend topic modeling, event detection, and prompt safety classification features will no longer be available to new customers, effective April 30, 2026. For more information, see [Amazon Comprehend feature availability change](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-availability-change.html). 

Toxic content analysis result for one string. For more information about toxicity detection, see [Toxicity detection](https://docs.aws.amazon.com/comprehend/latest/dg/toxicity-detection.html) in the *Amazon Comprehend Developer Guide* 

## Contents
<a name="API_ToxicContent_Contents"></a>

 ** Name **   <a name="comprehend-Type-ToxicContent-Name"></a>
The name of the toxic content type.  
Type: String  
Valid Values: `GRAPHIC | HARASSMENT_OR_ABUSE | HATE_SPEECH | INSULT | PROFANITY | SEXUAL | VIOLENCE_OR_THREAT`   
Required: No

 ** Score **   <a name="comprehend-Type-ToxicContent-Score"></a>
 Model confidence in the detected content type. Value range is zero to one, where one is highest confidence.  
Type: Float  
Required: No

## See Also
<a name="API_ToxicContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ToxicContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ToxicContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ToxicContent) 