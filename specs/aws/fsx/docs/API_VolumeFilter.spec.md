---
id: "@specs/aws/fsx/docs/API_VolumeFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VolumeFilter"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# VolumeFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_VolumeFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VolumeFilter
<a name="API_VolumeFilter"></a>

A filter used to restrict the results of describe calls for Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volumes. You can use multiple filters to return results that meet all applied filter requirements.

## Contents
<a name="API_VolumeFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-VolumeFilter-Name"></a>
The name for this filter.  
Type: String  
Valid Values: `file-system-id | storage-virtual-machine-id`   
Required: No

 ** Values **   <a name="FSx-Type-VolumeFilter-Values"></a>
The values of the filter. These are all the values for any of the applied filters.  
Type: Array of strings  
Array Members: Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`   
Required: No

## See Also
<a name="API_VolumeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/VolumeFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/VolumeFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/VolumeFilter) 