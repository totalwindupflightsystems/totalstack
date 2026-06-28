---
id: "@specs/aws/fsx/docs/API_AutoImportPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutoImportPolicy"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# AutoImportPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_AutoImportPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutoImportPolicy
<a name="API_AutoImportPolicy"></a>

Describes the data repository association's automatic import policy. The AutoImportPolicy defines how Amazon FSx keeps your file metadata and directory listings up to date by importing changes to your Amazon FSx for Lustre file system as you modify objects in a linked S3 bucket.

The `AutoImportPolicy` is only supported on Amazon FSx for Lustre file systems with a data repository association.

## Contents
<a name="API_AutoImportPolicy_Contents"></a>

 ** Events **   <a name="FSx-Type-AutoImportPolicy-Events"></a>
The `AutoImportPolicy` can have the following event values:  
+  `NEW` - Amazon FSx automatically imports metadata of files added to the linked S3 bucket that do not currently exist in the FSx file system.
+  `CHANGED` - Amazon FSx automatically updates file metadata and invalidates existing file content on the file system as files change in the data repository.
+  `DELETED` - Amazon FSx automatically deletes files on the file system as corresponding files are deleted in the data repository.
You can define any combination of event types for your `AutoImportPolicy`.  
Type: Array of strings  
Array Members: Maximum number of 3 items.  
Valid Values: `NEW | CHANGED | DELETED`   
Required: No

## See Also
<a name="API_AutoImportPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/AutoImportPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/AutoImportPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/AutoImportPolicy) 