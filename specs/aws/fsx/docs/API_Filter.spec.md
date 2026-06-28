---
id: "@specs/aws/fsx/docs/API_Filter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Filter"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# Filter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_Filter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Filter
<a name="API_Filter"></a>

A filter used to restrict the results of describe calls. You can use multiple filters to return results that meet all applied filter requirements.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="FSx-Type-Filter-Name"></a>
The name for this filter.  
Type: String  
Valid Values: `file-system-id | backup-type | file-system-type | volume-id | data-repository-type | file-cache-id | file-cache-type`   
Required: No

 ** Values **   <a name="FSx-Type-Filter-Values"></a>
The values of the filter. These are all the values for any of the applied filters.  
Type: Array of strings  
Array Members: Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`   
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/Filter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/Filter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/Filter) 