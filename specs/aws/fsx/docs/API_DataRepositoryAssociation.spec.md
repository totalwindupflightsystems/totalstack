---
id: "@specs/aws/fsx/docs/API_DataRepositoryAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataRepositoryAssociation"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DataRepositoryAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DataRepositoryAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataRepositoryAssociation
<a name="API_DataRepositoryAssociation"></a>

The configuration of a data repository association that links an Amazon FSx for Lustre file system to an Amazon S3 bucket or an Amazon File Cache resource to an Amazon S3 bucket or an NFS file system. The data repository association configuration object is returned in the response of the following operations:
+  `CreateDataRepositoryAssociation` 
+  `UpdateDataRepositoryAssociation` 
+  `DescribeDataRepositoryAssociations` 

Data repository associations are supported on Amazon File Cache resources and all FSx for Lustre 2.12 and 2.15 file systems, excluding Intelligent-Tiering and `scratch_1` file systems.

## Contents
<a name="API_DataRepositoryAssociation_Contents"></a>

 ** AssociationId **   <a name="FSx-Type-DataRepositoryAssociation-AssociationId"></a>
The system-generated, unique ID of the data repository association.  
Type: String  
Length Constraints: Minimum length of 13. Maximum length of 23.  
Pattern: `^(dra-[0-9a-f]{8,})$`   
Required: No

 ** BatchImportMetaDataOnCreate **   <a name="FSx-Type-DataRepositoryAssociation-BatchImportMetaDataOnCreate"></a>
A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to `true`.  
 `BatchImportMetaDataOnCreate` is not supported for data repositories linked to an Amazon File Cache resource.
Type: Boolean  
Required: No

 ** CreationTime **   <a name="FSx-Type-DataRepositoryAssociation-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: No

 ** DataRepositoryPath **   <a name="FSx-Type-DataRepositoryAssociation-DataRepositoryPath"></a>
The path to the data repository that will be linked to the cache or file system.  
+ For Amazon File Cache, the path can be an NFS data repository that will be linked to the cache. The path can be in one of two formats:
  + If you are not using the `DataRepositorySubdirectories` parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format `nsf://nfs-domain-name/exportpath`. You can therefore link a single NFS Export to a single data repository association.
  + If you are using the `DataRepositorySubdirectories` parameter, the path is the domain name of the NFS file system in the format `nfs://filer-domain-name`, which indicates the root of the subdirectories specified with the `DataRepositorySubdirectories` parameter.
+ For Amazon File Cache, the path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).
+ For Amazon FSx for Lustre, the path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: No

 ** DataRepositorySubdirectories **   <a name="FSx-Type-DataRepositoryAssociation-DataRepositorySubdirectories"></a>
For Amazon File Cache, a list of NFS Exports that will be linked with an NFS data repository association. All the subdirectories must be on a single NFS file system. The Export paths are in the format `/exportpath1`. To use this parameter, you must configure `DataRepositoryPath` as the domain name of the NFS file system. The NFS file system domain name in effect is the root of the subdirectories. Note that `DataRepositorySubdirectories` is not supported for S3 data repositories.  
Type: Array of strings  
Array Members: Maximum number of 500 items.  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`   
Required: No

 ** FailureDetails **   <a name="FSx-Type-DataRepositoryAssociation-FailureDetails"></a>
Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED`.  
Type: [DataRepositoryFailureDetails](API_DataRepositoryFailureDetails.md) object  
Required: No

 ** FileCacheId **   <a name="FSx-Type-DataRepositoryAssociation-FileCacheId"></a>
The globally unique ID of the Amazon File Cache resource.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fc-[0-9a-f]{8,})$`   
Required: No

 ** FileCachePath **   <a name="FSx-Type-DataRepositoryAssociation-FileCachePath"></a>
A path on the Amazon File Cache that points to a high-level directory (such as `/ns1/`) or subdirectory (such as `/ns1/subdir/`) that will be mapped 1-1 with `DataRepositoryPath`. The leading forward slash in the path is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path `/ns1/`, then you cannot link another data repository with cache path `/ns1/ns2`.  
This path specifies the directory in your cache where files will be exported from. This cache directory can be linked to only one data repository (S3 or NFS) and no other data repository can be linked to the directory.  
The cache path can only be set to root (/) on an NFS DRA when `DataRepositorySubdirectories` is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.  
The cache path cannot be set to root (/) for an S3 DRA.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`   
Required: No

 ** FileSystemId **   <a name="FSx-Type-DataRepositoryAssociation-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: No

 ** FileSystemPath **   <a name="FSx-Type-DataRepositoryAssociation-FileSystemPath"></a>
A path on the Amazon FSx for Lustre file system that points to a high-level directory (such as `/ns1/`) or subdirectory (such as `/ns1/subdir/`) that will be mapped 1-1 with `DataRepositoryPath`. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path `/ns1/`, then you cannot link another data repository with file system path `/ns1/ns2`.  
This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.  
If you specify only a forward slash (`/`) as the file system path, you can link only one data repository to the file system. You can only specify "/" as the file system path for the first data repository associated with a file system.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`   
Required: No

 ** ImportedFileChunkSize **   <a name="FSx-Type-DataRepositoryAssociation-ImportedFileChunkSize"></a>
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system or cache.  
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 512000.  
Required: No

 ** Lifecycle **   <a name="FSx-Type-DataRepositoryAssociation-Lifecycle"></a>
Describes the state of a data repository association. The lifecycle can have the following values:  
+  `CREATING` - The data repository association between the file system or cache and the data repository is being created. The data repository is unavailable.
+  `AVAILABLE` - The data repository association is available for use.
+  `MISCONFIGURED` - The data repository association is misconfigured. Until the configuration is corrected, automatic import and automatic export will not work (only for Amazon FSx for Lustre).
+  `UPDATING` - The data repository association is undergoing a customer initiated update that might affect its availability.
+  `DELETING` - The data repository association is undergoing a customer initiated deletion.
+  `FAILED` - The data repository association is in a terminal state that cannot be recovered.
Type: String  
Valid Values: `CREATING | AVAILABLE | MISCONFIGURED | UPDATING | DELETING | FAILED`   
Required: No

 ** NFS **   <a name="FSx-Type-DataRepositoryAssociation-NFS"></a>
The configuration for an NFS data repository linked to an Amazon File Cache resource with a data repository association.  
Type: [NFSDataRepositoryConfiguration](API_NFSDataRepositoryConfiguration.md) object  
Required: No

 ** ResourceARN **   <a name="FSx-Type-DataRepositoryAssociation-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** S3 **   <a name="FSx-Type-DataRepositoryAssociation-S3"></a>
The configuration for an Amazon S3 data repository linked to an Amazon FSx for Lustre file system with a data repository association.  
Type: [S3DataRepositoryConfiguration](API_S3DataRepositoryConfiguration.md) object  
Required: No

 ** Tags **   <a name="FSx-Type-DataRepositoryAssociation-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_DataRepositoryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DataRepositoryAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DataRepositoryAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DataRepositoryAssociation) 