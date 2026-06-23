---
id: "@specs/aws/comprehend/docs/API_DatasetProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetProperties"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetProperties
<a name="API_DatasetProperties"></a>

Properties associated with the dataset.

## Contents
<a name="API_DatasetProperties_Contents"></a>

 ** CreationTime **   <a name="comprehend-Type-DatasetProperties-CreationTime"></a>
Creation time of the dataset.  
Type: Timestamp  
Required: No

 ** DatasetArn **   <a name="comprehend-Type-DatasetProperties-DatasetArn"></a>
The ARN of the dataset.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*/dataset/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** DatasetName **   <a name="comprehend-Type-DatasetProperties-DatasetName"></a>
The name of the dataset.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`   
Required: No

 ** DatasetS3Uri **   <a name="comprehend-Type-DatasetProperties-DatasetS3Uri"></a>
The S3 URI where the dataset is stored.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** DatasetType **   <a name="comprehend-Type-DatasetProperties-DatasetType"></a>
The dataset type (training data or test data).  
Type: String  
Valid Values: `TRAIN | TEST`   
Required: No

 ** Description **   <a name="comprehend-Type-DatasetProperties-Description"></a>
Description of the dataset.  
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** EndTime **   <a name="comprehend-Type-DatasetProperties-EndTime"></a>
Time when the data from the dataset becomes available in the data lake.  
Type: Timestamp  
Required: No

 ** Message **   <a name="comprehend-Type-DatasetProperties-Message"></a>
A description of the status of the dataset.  
Type: String  
Required: No

 ** NumberOfDocuments **   <a name="comprehend-Type-DatasetProperties-NumberOfDocuments"></a>
The number of documents in the dataset.  
Type: Long  
Required: No

 ** Status **   <a name="comprehend-Type-DatasetProperties-Status"></a>
The dataset status. While the system creates the dataset, the status is `CREATING`. When the dataset is ready to use, the status changes to `COMPLETED`.   
Type: String  
Valid Values: `CREATING | COMPLETED | FAILED`   
Required: No

## See Also
<a name="API_DatasetProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetProperties) 