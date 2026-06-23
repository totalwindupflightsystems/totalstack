---
id: "@specs/aws/comprehend/docs/API_DatasetFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DatasetFilter"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DatasetFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DatasetFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DatasetFilter
<a name="API_DatasetFilter"></a>

Filter the datasets based on creation time or dataset status.

## Contents
<a name="API_DatasetFilter_Contents"></a>

 ** CreationTimeAfter **   <a name="comprehend-Type-DatasetFilter-CreationTimeAfter"></a>
Filter the datasets to include datasets created after the specified time.  
Type: Timestamp  
Required: No

 ** CreationTimeBefore **   <a name="comprehend-Type-DatasetFilter-CreationTimeBefore"></a>
Filter the datasets to include datasets created before the specified time.  
Type: Timestamp  
Required: No

 ** DatasetType **   <a name="comprehend-Type-DatasetFilter-DatasetType"></a>
Filter the datasets based on the dataset type.  
Type: String  
Valid Values: `TRAIN | TEST`   
Required: No

 ** Status **   <a name="comprehend-Type-DatasetFilter-Status"></a>
Filter the datasets based on the dataset status.  
Type: String  
Valid Values: `CREATING | COMPLETED | FAILED`   
Required: No

## See Also
<a name="API_DatasetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DatasetFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DatasetFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DatasetFilter) 