---
id: "@specs/aws/comprehend/docs/API_DatasetAugmentedManifestsListItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetAugmentedManifestsListItem"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetAugmentedManifestsListItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetAugmentedManifestsListItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetAugmentedManifestsListItem
<a name="API_DatasetAugmentedManifestsListItem"></a>

An augmented manifest file that provides training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

## Contents
<a name="API_DatasetAugmentedManifestsListItem_Contents"></a>

 ** AttributeNames **   <a name="comprehend-Type-DatasetAugmentedManifestsListItem-AttributeNames"></a>
The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.  
If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.  
If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

 ** S3Uri **   <a name="comprehend-Type-DatasetAugmentedManifestsListItem-S3Uri"></a>
The Amazon S3 location of the augmented manifest file.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** AnnotationDataS3Uri **   <a name="comprehend-Type-DatasetAugmentedManifestsListItem-AnnotationDataS3Uri"></a>
The S3 prefix to the annotation files that are referred in the augmented manifest file.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** DocumentType **   <a name="comprehend-Type-DatasetAugmentedManifestsListItem-DocumentType"></a>
The type of augmented manifest. If you don't specify, the default is PlainTextDocument.   
 `PLAIN_TEXT_DOCUMENT` A document type that represents any unicode text that is encoded in UTF-8.  
Type: String  
Valid Values: `PLAIN_TEXT_DOCUMENT | SEMI_STRUCTURED_DOCUMENT`   
Required: No

 ** SourceDocumentsS3Uri **   <a name="comprehend-Type-DatasetAugmentedManifestsListItem-SourceDocumentsS3Uri"></a>
The S3 prefix to the source files (PDFs) that are referred to in the augmented manifest file.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

## See Also
<a name="API_DatasetAugmentedManifestsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetAugmentedManifestsListItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetAugmentedManifestsListItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetAugmentedManifestsListItem) 