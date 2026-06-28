---
id: "@specs/aws/fsx/docs/API_FileCacheLustreConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileCacheLustreConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileCacheLustreConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileCacheLustreConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileCacheLustreConfiguration
<a name="API_FileCacheLustreConfiguration"></a>

The configuration for the Amazon File Cache resource.

## Contents
<a name="API_FileCacheLustreConfiguration_Contents"></a>

 ** DeploymentType **   <a name="FSx-Type-FileCacheLustreConfiguration-DeploymentType"></a>
The deployment type of the Amazon File Cache resource, which must be `CACHE_1`.  
Type: String  
Valid Values: `CACHE_1`   
Required: No

 ** LogConfiguration **   <a name="FSx-Type-FileCacheLustreConfiguration-LogConfiguration"></a>
The configuration for Lustre logging used to write the enabled logging events for your Amazon File Cache resource to Amazon CloudWatch Logs.  
Type: [LustreLogConfiguration](API_LustreLogConfiguration.md) object  
Required: No

 ** MetadataConfiguration **   <a name="FSx-Type-FileCacheLustreConfiguration-MetadataConfiguration"></a>
The configuration for a Lustre MDT (Metadata Target) storage volume.  
Type: [FileCacheLustreMetadataConfiguration](API_FileCacheLustreMetadataConfiguration.md) object  
Required: No

 ** MountName **   <a name="FSx-Type-FileCacheLustreConfiguration-MountName"></a>
You use the `MountName` value when mounting the cache. If you pass a cache ID to the `DescribeFileCaches` operation, it returns the the `MountName` value as part of the cache's description.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8.  
Pattern: `^([A-Za-z0-9_-]{1,8})$`   
Required: No

 ** PerUnitStorageThroughput **   <a name="FSx-Type-FileCacheLustreConfiguration-PerUnitStorageThroughput"></a>
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. Cache throughput capacity is equal to Storage capacity (TiB) \* PerUnitStorageThroughput (MB/s/TiB). The only supported value is `1000`.  
Type: Integer  
Valid Range: Minimum value of 12. Maximum value of 1000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-FileCacheLustreConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_FileCacheLustreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileCacheLustreConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileCacheLustreConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileCacheLustreConfiguration) 