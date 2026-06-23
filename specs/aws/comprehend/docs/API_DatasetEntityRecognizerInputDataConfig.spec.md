---
id: "@specs/aws/comprehend/docs/API_DatasetEntityRecognizerInputDataConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetEntityRecognizerInputDataConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetEntityRecognizerInputDataConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetEntityRecognizerInputDataConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetEntityRecognizerInputDataConfig
<a name="API_DatasetEntityRecognizerInputDataConfig"></a>

Specifies the format and location of the input data. You must provide either the `Annotations` parameter or the `EntityList` parameter.

## Contents
<a name="API_DatasetEntityRecognizerInputDataConfig_Contents"></a>

 ** Documents **   <a name="comprehend-Type-DatasetEntityRecognizerInputDataConfig-Documents"></a>
The format and location of the training documents for your custom entity recognizer.  
Type: [DatasetEntityRecognizerDocuments](API_DatasetEntityRecognizerDocuments.md) object  
Required: Yes

 ** Annotations **   <a name="comprehend-Type-DatasetEntityRecognizerInputDataConfig-Annotations"></a>
The S3 location of the annotation documents for your custom entity recognizer.  
Type: [DatasetEntityRecognizerAnnotations](API_DatasetEntityRecognizerAnnotations.md) object  
Required: No

 ** EntityList **   <a name="comprehend-Type-DatasetEntityRecognizerInputDataConfig-EntityList"></a>
The S3 location of the entity list for your custom entity recognizer.  
Type: [DatasetEntityRecognizerEntityList](API_DatasetEntityRecognizerEntityList.md) object  
Required: No

## See Also
<a name="API_DatasetEntityRecognizerInputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetEntityRecognizerInputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetEntityRecognizerInputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetEntityRecognizerInputDataConfig) 