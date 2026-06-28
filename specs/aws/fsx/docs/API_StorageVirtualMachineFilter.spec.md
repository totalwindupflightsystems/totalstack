---
id: "@specs/aws/fsx/docs/API_StorageVirtualMachineFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StorageVirtualMachineFilter"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# StorageVirtualMachineFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_StorageVirtualMachineFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StorageVirtualMachineFilter
<a name="API_StorageVirtualMachineFilter"></a>

A filter used to restrict the results of describe calls for Amazon FSx for NetApp ONTAP storage virtual machines (SVMs). You can use multiple filters to return results that meet all applied filter requirements.

## Contents
<a name="API_StorageVirtualMachineFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-StorageVirtualMachineFilter-Name"></a>
The name for this filter.  
Type: String  
Valid Values: `file-system-id`   
Required: No

 ** Values **   <a name="FSx-Type-StorageVirtualMachineFilter-Values"></a>
The values of the filter. These are all the values for any of the applied filters.  
Type: Array of strings  
Array Members: Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`   
Required: No

## See Also
<a name="API_StorageVirtualMachineFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/StorageVirtualMachineFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/StorageVirtualMachineFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/StorageVirtualMachineFilter) 