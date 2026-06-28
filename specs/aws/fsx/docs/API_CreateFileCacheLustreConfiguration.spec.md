---
id: "@specs/aws/fsx/docs/API_CreateFileCacheLustreConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileCacheLustreConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileCacheLustreConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileCacheLustreConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileCacheLustreConfiguration
<a name="API_CreateFileCacheLustreConfiguration"></a>

The Amazon File Cache configuration for the cache that you are creating.

## Contents
<a name="API_CreateFileCacheLustreConfiguration_Contents"></a>

 ** DeploymentType **   <a name="FSx-Type-CreateFileCacheLustreConfiguration-DeploymentType"></a>
Specifies the cache deployment type, which must be `CACHE_1`.  
Type: String  
Valid Values: `CACHE_1`   
Required: Yes

 ** MetadataConfiguration **   <a name="FSx-Type-CreateFileCacheLustreConfiguration-MetadataConfiguration"></a>
The configuration for a Lustre MDT (Metadata Target) storage volume.  
Type: [FileCacheLustreMetadataConfiguration](API_FileCacheLustreMetadataConfiguration.md) object  
Required: Yes

 ** PerUnitStorageThroughput **   <a name="FSx-Type-CreateFileCacheLustreConfiguration-PerUnitStorageThroughput"></a>
Provisions the amount of read and write throughput for each 1 tebibyte (TiB) of cache storage capacity, in MB/s/TiB. The only supported value is `1000`.  
Type: Integer  
Valid Range: Minimum value of 12. Maximum value of 1000.  
Required: Yes

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-CreateFileCacheLustreConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_CreateFileCacheLustreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileCacheLustreConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileCacheLustreConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileCacheLustreConfiguration) 