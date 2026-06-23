---
id: "@specs/aws/comprehend/docs/API_DatasetInputDataConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetInputDataConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetInputDataConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetInputDataConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetInputDataConfig
<a name="API_DatasetInputDataConfig"></a>

Specifies the format and location of the input data for the dataset.

## Contents
<a name="API_DatasetInputDataConfig_Contents"></a>

 ** AugmentedManifests **   <a name="comprehend-Type-DatasetInputDataConfig-AugmentedManifests"></a>
A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.   
Type: Array of [DatasetAugmentedManifestsListItem](API_DatasetAugmentedManifestsListItem.md) objects  
Required: No

 ** DataFormat **   <a name="comprehend-Type-DatasetInputDataConfig-DataFormat"></a>
 `COMPREHEND_CSV`: The data format is a two-column CSV file, where the first column contains labels and the second column contains documents.  
 `AUGMENTED_MANIFEST`: The data format   
Type: String  
Valid Values: `COMPREHEND_CSV | AUGMENTED_MANIFEST`   
Required: No

 ** DocumentClassifierInputDataConfig **   <a name="comprehend-Type-DatasetInputDataConfig-DocumentClassifierInputDataConfig"></a>
The input properties for training a document classifier model.   
For more information on how the input file is formatted, see [Preparing training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html) in the Comprehend Developer Guide.   
Type: [DatasetDocumentClassifierInputDataConfig](API_DatasetDocumentClassifierInputDataConfig.md) object  
Required: No

 ** EntityRecognizerInputDataConfig **   <a name="comprehend-Type-DatasetInputDataConfig-EntityRecognizerInputDataConfig"></a>
The input properties for training an entity recognizer model.  
Type: [DatasetEntityRecognizerInputDataConfig](API_DatasetEntityRecognizerInputDataConfig.md) object  
Required: No

## See Also
<a name="API_DatasetInputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetInputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetInputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetInputDataConfig) 