---
id: "@specs/aws/comprehend/docs/API_DatasetEntityRecognizerEntityList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetEntityRecognizerEntityList"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetEntityRecognizerEntityList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetEntityRecognizerEntityList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetEntityRecognizerEntityList
<a name="API_DatasetEntityRecognizerEntityList"></a>

Describes the dataset entity list for an entity recognizer model.

For more information on how the input file is formatted, see [Preparing training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-training-data-cer.html) in the Comprehend Developer Guide. 

## Contents
<a name="API_DatasetEntityRecognizerEntityList_Contents"></a>

 ** S3Uri **   <a name="comprehend-Type-DatasetEntityRecognizerEntityList-S3Uri"></a>
Specifies the Amazon S3 location where the entity list is located.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

## See Also
<a name="API_DatasetEntityRecognizerEntityList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetEntityRecognizerEntityList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetEntityRecognizerEntityList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetEntityRecognizerEntityList) 