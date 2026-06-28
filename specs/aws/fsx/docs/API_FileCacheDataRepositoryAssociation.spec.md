---
id: "@specs/aws/fsx/docs/API_FileCacheDataRepositoryAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileCacheDataRepositoryAssociation"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileCacheDataRepositoryAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileCacheDataRepositoryAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileCacheDataRepositoryAssociation
<a name="API_FileCacheDataRepositoryAssociation"></a>

The configuration for a data repository association (DRA) to be created during the Amazon File Cache resource creation. The DRA links the cache to either an Amazon S3 bucket or prefix, or a Network File System (NFS) data repository that supports the NFSv3 protocol.

The DRA does not support automatic import or automatic export.

## Contents
<a name="API_FileCacheDataRepositoryAssociation_Contents"></a>

 ** DataRepositoryPath **   <a name="FSx-Type-FileCacheDataRepositoryAssociation-DataRepositoryPath"></a>
The path to the S3 or NFS data repository that links to the cache. You must provide one of the following paths:  
+ The path can be an NFS data repository that links to the cache. The path can be in one of two formats:
  + If you are not using the `DataRepositorySubdirectories` parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format `nfs://nfs-domain-name/exportpath`. You can therefore link a single NFS Export to a single data repository association.
  + If you are using the `DataRepositorySubdirectories` parameter, the path is the domain name of the NFS file system in the format `nfs://filer-domain-name`, which indicates the root of the subdirectories specified with the `DataRepositorySubdirectories` parameter.
+ The path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: Yes

 ** FileCachePath **   <a name="FSx-Type-FileCacheDataRepositoryAssociation-FileCachePath"></a>
A path on the cache that points to a high-level directory (such as `/ns1/`) or subdirectory (such as `/ns1/subdir/`) that will be mapped 1-1 with `DataRepositoryPath`. The leading forward slash in the name is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path `/ns1/`, then you cannot link another data repository with cache path `/ns1/ns2`.  
This path specifies where in your cache files will be exported from. This cache directory can be linked to only one data repository, and no data repository other can be linked to the directory.  
The cache path can only be set to root (/) on an NFS DRA when `DataRepositorySubdirectories` is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.  
The cache path cannot be set to root (/) for an S3 DRA.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`   
Required: Yes

 ** DataRepositorySubdirectories **   <a name="FSx-Type-FileCacheDataRepositoryAssociation-DataRepositorySubdirectories"></a>
A list of NFS Exports that will be linked with this data repository association. The Export paths are in the format `/exportpath1`. To use this parameter, you must configure `DataRepositoryPath` as the domain name of the NFS file system. The NFS file system domain name in effect is the root of the subdirectories. Note that `DataRepositorySubdirectories` is not supported for S3 data repositories.  
Type: Array of strings  
Array Members: Maximum number of 500 items.  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`   
Required: No

 ** NFS **   <a name="FSx-Type-FileCacheDataRepositoryAssociation-NFS"></a>
The configuration for a data repository association that links an Amazon File Cache resource to an NFS data repository.  
Type: [FileCacheNFSConfiguration](API_FileCacheNFSConfiguration.md) object  
Required: No

## See Also
<a name="API_FileCacheDataRepositoryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileCacheDataRepositoryAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileCacheDataRepositoryAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileCacheDataRepositoryAssociation) 