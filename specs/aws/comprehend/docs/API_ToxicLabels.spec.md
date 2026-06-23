---
id: "@specs/aws/comprehend/docs/API_ToxicLabels"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ToxicLabels"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ToxicLabels

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ToxicLabels
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ToxicLabels
<a name="API_ToxicLabels"></a>

**Important**  
Service availability notice: Amazon Comprehend topic modeling, event detection, and prompt safety classification features will no longer be available to new customers, effective April 30, 2026. For more information, see [Amazon Comprehend feature availability change](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-availability-change.html). 

Toxicity analysis result for one string. For more information about toxicity detection, see [Toxicity detection](https://docs.aws.amazon.com/comprehend/latest/dg/toxicity-detection.html) in the *Amazon Comprehend Developer Guide*.

## Contents
<a name="API_ToxicLabels_Contents"></a>

 ** Labels **   <a name="comprehend-Type-ToxicLabels-Labels"></a>
Array of toxic content types identified in the string.  
Type: Array of [ToxicContent](API_ToxicContent.md) objects  
Required: No

 ** Toxicity **   <a name="comprehend-Type-ToxicLabels-Toxicity"></a>
Overall toxicity score for the string. Value range is zero to one, where one is the highest confidence.  
Type: Float  
Required: No

## See Also
<a name="API_ToxicLabels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ToxicLabels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ToxicLabels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ToxicLabels) 