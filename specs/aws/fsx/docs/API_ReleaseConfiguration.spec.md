---
id: "@specs/aws/fsx/docs/API_ReleaseConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ReleaseConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# ReleaseConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_ReleaseConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ReleaseConfiguration
<a name="API_ReleaseConfiguration"></a>

The configuration that specifies a minimum amount of time since last access for an exported file to be eligible for release from an Amazon FSx for Lustre file system. Only files that were last accessed before this point-in-time can be released. For example, if you specify a last accessed time criteria of 9 days, only files that were last accessed 9.00001 or more days ago can be released.

Only file data that has been exported to S3 can be released. Files that have not yet been exported to S3, such as new or changed files that have not been exported, are not eligible for release. When files are released, their metadata stays on the file system, so they can still be accessed later. Users and applications can access a released file by reading the file again, which restores data from Amazon S3 to the FSx for Lustre file system.

**Note**  
If a file meets the last accessed time criteria, its file or directory path must also be specified with the `Paths` parameter of the [CreateDataRepositoryTask](API_CreateDataRepositoryTask.md) operation in order for the file to be released.

## Contents
<a name="API_ReleaseConfiguration_Contents"></a>

 ** DurationSinceLastAccess **   <a name="FSx-Type-ReleaseConfiguration-DurationSinceLastAccess"></a>
Defines the point-in-time since an exported file was last accessed, in order for that file to be eligible for release. Only files that were last accessed before this point-in-time are eligible to be released from the file system.  
Type: [DurationSinceLastAccess](API_DurationSinceLastAccess.md) object  
Required: No

## See Also
<a name="API_ReleaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/ReleaseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/ReleaseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/ReleaseConfiguration) 