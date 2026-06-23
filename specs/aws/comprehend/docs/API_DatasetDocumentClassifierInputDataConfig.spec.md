---
id: "@specs/aws/comprehend/docs/API_DatasetDocumentClassifierInputDataConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetDocumentClassifierInputDataConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetDocumentClassifierInputDataConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetDocumentClassifierInputDataConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetDocumentClassifierInputDataConfig
<a name="API_DatasetDocumentClassifierInputDataConfig"></a>

Describes the dataset input data configuration for a document classifier model.

For more information on how the input file is formatted, see [Preparing training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html) in the Comprehend Developer Guide. 

## Contents
<a name="API_DatasetDocumentClassifierInputDataConfig_Contents"></a>

 ** S3Uri **   <a name="comprehend-Type-DatasetDocumentClassifierInputDataConfig-S3Uri"></a>
The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.  
For example, if you use the URI `S3://bucketName/prefix`, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.  
This parameter is required if you set `DataFormat` to `COMPREHEND_CSV`.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** LabelDelimiter **   <a name="comprehend-Type-DatasetDocumentClassifierInputDataConfig-LabelDelimiter"></a>
Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (\|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.  
Type: String  
Length Constraints: Fixed length of 1.  
Pattern: `^[ ~!@#$%^*\-_+=|\\:;\t>?/]$`   
Required: No

## See Also
<a name="API_DatasetDocumentClassifierInputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetDocumentClassifierInputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetDocumentClassifierInputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetDocumentClassifierInputDataConfig) 