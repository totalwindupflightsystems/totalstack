---
id: "@specs/aws/fsx/docs/API_AutoExportPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutoExportPolicy"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# AutoExportPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_AutoExportPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutoExportPolicy
<a name="API_AutoExportPolicy"></a>

Describes a data repository association's automatic export policy. The `AutoExportPolicy` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.

The `AutoExportPolicy` is only supported on Amazon FSx for Lustre file systems with a data repository association.

## Contents
<a name="API_AutoExportPolicy_Contents"></a>

 ** Events **   <a name="FSx-Type-AutoExportPolicy-Events"></a>
The `AutoExportPolicy` can have the following event values:  
+  `NEW` - New files and directories are automatically exported to the data repository as they are added to the file system.
+  `CHANGED` - Changes to files and directories on the file system are automatically exported to the data repository.
+  `DELETED` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.
You can define any combination of event types for your `AutoExportPolicy`.  
Type: Array of strings  
Array Members: Maximum number of 3 items.  
Valid Values: `NEW | CHANGED | DELETED`   
Required: No

## See Also
<a name="API_AutoExportPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/AutoExportPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/AutoExportPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/AutoExportPolicy) 