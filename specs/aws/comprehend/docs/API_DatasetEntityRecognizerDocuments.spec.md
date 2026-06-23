---
id: "@specs/aws/comprehend/docs/API_DatasetEntityRecognizerDocuments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetEntityRecognizerDocuments"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetEntityRecognizerDocuments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetEntityRecognizerDocuments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetEntityRecognizerDocuments
<a name="API_DatasetEntityRecognizerDocuments"></a>

Describes the documents submitted with a dataset for an entity recognizer model.

## Contents
<a name="API_DatasetEntityRecognizerDocuments_Contents"></a>

 ** S3Uri **   <a name="comprehend-Type-DatasetEntityRecognizerDocuments-S3Uri"></a>
 Specifies the Amazon S3 location where the documents for the dataset are located.   
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** InputFormat **   <a name="comprehend-Type-DatasetEntityRecognizerDocuments-InputFormat"></a>
 Specifies how the text in an input file should be processed. This is optional, and the default is ONE\_DOC\_PER\_LINE. ONE\_DOC\_PER\_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE\_DOC\_PER\_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.  
Type: String  
Valid Values: `ONE_DOC_PER_FILE | ONE_DOC_PER_LINE`   
Required: No

## See Also
<a name="API_DatasetEntityRecognizerDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetEntityRecognizerDocuments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetEntityRecognizerDocuments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetEntityRecognizerDocuments) 