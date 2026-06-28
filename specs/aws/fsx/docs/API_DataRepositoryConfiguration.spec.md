---
id: "@specs/aws/fsx/docs/API_DataRepositoryConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataRepositoryConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DataRepositoryConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DataRepositoryConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataRepositoryConfiguration
<a name="API_DataRepositoryConfiguration"></a>

The data repository configuration object for Lustre file systems returned in the response of the `CreateFileSystem` operation.

This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see [DataRepositoryAssociation](API_DataRepositoryAssociation.md).

## Contents
<a name="API_DataRepositoryConfiguration_Contents"></a>

 ** AutoImportPolicy **   <a name="FSx-Type-DataRepositoryConfiguration-AutoImportPolicy"></a>
Describes the file system's linked S3 data repository's `AutoImportPolicy`. The AutoImportPolicy configures how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:  
+  `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
+  `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. 
+  `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
+  `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.
Type: String  
Valid Values: `NONE | NEW | NEW_CHANGED | NEW_CHANGED_DELETED`   
Required: No

 ** ExportPath **   <a name="FSx-Type-DataRepositoryConfiguration-ExportPath"></a>
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: No

 ** FailureDetails **   <a name="FSx-Type-DataRepositoryConfiguration-FailureDetails"></a>
Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED`.  
Type: [DataRepositoryFailureDetails](API_DataRepositoryFailureDetails.md) object  
Required: No

 ** ImportedFileChunkSize **   <a name="FSx-Type-DataRepositoryConfiguration-ImportedFileChunkSize"></a>
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.  
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 512000.  
Required: No

 ** ImportPath **   <a name="FSx-Type-DataRepositoryConfiguration-ImportPath"></a>
The import path to the Amazon S3 bucket (and optional prefix) that you're using as the data repository for your FSx for Lustre file system, for example `s3://import-bucket/optional-prefix`. If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: No

 ** Lifecycle **   <a name="FSx-Type-DataRepositoryConfiguration-Lifecycle"></a>
Describes the state of the file system's S3 durable data repository, if it is configured with an S3 repository. The lifecycle can have the following values:  
+  `CREATING` - The data repository configuration between the FSx file system and the linked S3 data repository is being created. The data repository is unavailable.
+  `AVAILABLE` - The data repository is available for use.
+  `MISCONFIGURED` - Amazon FSx cannot automatically import updates from the S3 bucket until the data repository configuration is corrected. For more information, see [Troubleshooting a Misconfigured linked S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html#troubleshooting-misconfigured-data-repository). 
+  `UPDATING` - The data repository is undergoing a customer initiated update and availability may be impacted.
+  `FAILED` - The data repository is in a terminal state that cannot be recovered.
Type: String  
Valid Values: `CREATING | AVAILABLE | MISCONFIGURED | UPDATING | DELETING | FAILED`   
Required: No

## See Also
<a name="API_DataRepositoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DataRepositoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DataRepositoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DataRepositoryConfiguration) 