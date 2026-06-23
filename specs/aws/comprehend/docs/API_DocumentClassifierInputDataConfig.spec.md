---
id: "@specs/aws/comprehend/docs/API_DocumentClassifierInputDataConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentClassifierInputDataConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentClassifierInputDataConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentClassifierInputDataConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentClassifierInputDataConfig
<a name="API_DocumentClassifierInputDataConfig"></a>

The input properties for training a document classifier. 

For more information on how the input file is formatted, see [Preparing training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html) in the Comprehend Developer Guide. 

## Contents
<a name="API_DocumentClassifierInputDataConfig_Contents"></a>

 ** AugmentedManifests **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-AugmentedManifests"></a>
A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.  
This parameter is required if you set `DataFormat` to `AUGMENTED_MANIFEST`.  
Type: Array of [AugmentedManifestsListItem](API_AugmentedManifestsListItem.md) objects  
Required: No

 ** DataFormat **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-DataFormat"></a>
The format of your training data:  
+  `COMPREHEND_CSV`: A two-column CSV file, where labels are provided in the first column, and documents are provided in the second. If you use this value, you must provide the `S3Uri` parameter in your request.
+  `AUGMENTED_MANIFEST`: A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its associated labels. 

  If you use this value, you must provide the `AugmentedManifests` parameter in your request.
If you don't specify a value, Amazon Comprehend uses `COMPREHEND_CSV` as the default.  
Type: String  
Valid Values: `COMPREHEND_CSV | AUGMENTED_MANIFEST`   
Required: No

 ** DocumentReaderConfig **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-DocumentReaderConfig"></a>
Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.   
 By default, Amazon Comprehend performs the following actions to extract text from files, based on the input file type:   
+  **Word files** - Amazon Comprehend parser extracts the text. 
+  **Digital PDF files** - Amazon Comprehend parser extracts the text. 
+  **Image files and scanned PDF files** - Amazon Comprehend uses the Amazon Textract `DetectDocumentText` API to extract the text. 
 `DocumentReaderConfig` does not apply to plain text files or Word files.  
 For image files and PDF documents, you can override these default actions using the fields listed below. For more information, see [ Setting text extraction options](https://docs.aws.amazon.com/comprehend/latest/dg/idp-set-textract-options.html) in the Comprehend Developer Guide.   
Type: [DocumentReaderConfig](API_DocumentReaderConfig.md) object  
Required: No

 ** Documents **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-Documents"></a>
The S3 location of the training documents. This parameter is required in a request to create a native document model.  
Type: [DocumentClassifierDocuments](API_DocumentClassifierDocuments.md) object  
Required: No

 ** DocumentType **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-DocumentType"></a>
The type of input documents for training the model. Provide plain-text documents to create a plain-text model, and provide semi-structured documents to create a native document model.  
Type: String  
Valid Values: `PLAIN_TEXT_DOCUMENT | SEMI_STRUCTURED_DOCUMENT`   
Required: No

 ** LabelDelimiter **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-LabelDelimiter"></a>
Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (\|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.  
Type: String  
Length Constraints: Fixed length of 1.  
Pattern: `^[ ~!@#$%^*\-_+=|\\:;\t>?/]$`   
Required: No

 ** S3Uri **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-S3Uri"></a>
The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.  
For example, if you use the URI `S3://bucketName/prefix`, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.  
This parameter is required if you set `DataFormat` to `COMPREHEND_CSV`.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** TestS3Uri **   <a name="comprehend-Type-DocumentClassifierInputDataConfig-TestS3Uri"></a>
This specifies the Amazon S3 location that contains the test annotations for the document classifier. The URI must be in the same AWS Region as the API endpoint that you are calling.   
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

## See Also
<a name="API_DocumentClassifierInputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentClassifierInputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentClassifierInputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentClassifierInputDataConfig) 