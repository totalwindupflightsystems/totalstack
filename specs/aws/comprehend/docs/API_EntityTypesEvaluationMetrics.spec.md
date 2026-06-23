---
id: "@specs/aws/comprehend/docs/API_EntityTypesEvaluationMetrics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EntityTypesEvaluationMetrics"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# EntityTypesEvaluationMetrics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_EntityTypesEvaluationMetrics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EntityTypesEvaluationMetrics
<a name="API_EntityTypesEvaluationMetrics"></a>

Detailed information about the accuracy of an entity recognizer for a specific entity type. 

## Contents
<a name="API_EntityTypesEvaluationMetrics_Contents"></a>

 ** F1Score **   <a name="comprehend-Type-EntityTypesEvaluationMetrics-F1Score"></a>
A measure of how accurate the recognizer results are for a specific entity type in the test data. It is derived from the `Precision` and `Recall` values. The `F1Score` is the harmonic average of the two scores. The highest score is 1, and the worst score is 0.   
Type: Double  
Required: No

 ** Precision **   <a name="comprehend-Type-EntityTypesEvaluationMetrics-Precision"></a>
A measure of the usefulness of the recognizer results for a specific entity type in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones.   
Type: Double  
Required: No

 ** Recall **   <a name="comprehend-Type-EntityTypesEvaluationMetrics-Recall"></a>
A measure of how complete the recognizer results are for a specific entity type in the test data. High recall means that the recognizer returned most of the relevant results.  
Type: Double  
Required: No

## See Also
<a name="API_EntityTypesEvaluationMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/EntityTypesEvaluationMetrics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/EntityTypesEvaluationMetrics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/EntityTypesEvaluationMetrics) 