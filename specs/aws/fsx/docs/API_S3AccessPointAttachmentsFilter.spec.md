---
id: "@specs/aws/fsx/docs/API_S3AccessPointAttachmentsFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3AccessPointAttachmentsFilter"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# S3AccessPointAttachmentsFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_S3AccessPointAttachmentsFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3AccessPointAttachmentsFilter
<a name="API_S3AccessPointAttachmentsFilter"></a>

A set of Name and Values pairs used to view a select set of S3 access point attachments.

## Contents
<a name="API_S3AccessPointAttachmentsFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-S3AccessPointAttachmentsFilter-Name"></a>
The name of the filter.  
Type: String  
Valid Values: `file-system-id | volume-id | type`   
Required: No

 ** Values **   <a name="FSx-Type-S3AccessPointAttachmentsFilter-Values"></a>
The values of the filter.  
Type: Array of strings  
Array Members: Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`   
Required: No

## See Also
<a name="API_S3AccessPointAttachmentsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPointAttachmentsFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPointAttachmentsFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPointAttachmentsFilter) 