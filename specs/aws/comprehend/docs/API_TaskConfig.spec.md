---
id: "@specs/aws/comprehend/docs/API_TaskConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TaskConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# TaskConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_TaskConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TaskConfig
<a name="API_TaskConfig"></a>

Configuration about the model associated with a flywheel.

## Contents
<a name="API_TaskConfig_Contents"></a>

 ** LanguageCode **   <a name="comprehend-Type-TaskConfig-LanguageCode"></a>
Language code for the language that the model supports.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: Yes

 ** DocumentClassificationConfig **   <a name="comprehend-Type-TaskConfig-DocumentClassificationConfig"></a>
Configuration required for a document classification model.  
Type: [DocumentClassificationConfig](API_DocumentClassificationConfig.md) object  
Required: No

 ** EntityRecognitionConfig **   <a name="comprehend-Type-TaskConfig-EntityRecognitionConfig"></a>
Configuration required for an entity recognition model.  
Type: [EntityRecognitionConfig](API_EntityRecognitionConfig.md) object  
Required: No

## See Also
<a name="API_TaskConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/TaskConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/TaskConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/TaskConfig) 