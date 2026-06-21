---
id: "@specs/aws/rds/docs/API_AdditionalStorageVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AdditionalStorageVolume"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# AdditionalStorageVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_AdditionalStorageVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AdditionalStorageVolume
<a name="API_AdditionalStorageVolume"></a>

Contains details about an additional storage volume for a DB instance. RDS support additional storage volumes for RDS for Oracle and RDS for SQL Server.

## Contents
<a name="API_AdditionalStorageVolume_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** VolumeName **   
The name of the additional storage volume.  
Valid Values: `RDSDBDATA2 | RDSDBDATA3 | RDSDBDATA4`   
Type: String  
Required: Yes

 ** AllocatedStorage **   
The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).  
Type: Integer  
Required: No

 ** IOPS **   
The number of I/O operations per second (IOPS) provisioned for the additional storage volume.  
Type: Integer  
Required: No

 ** MaxAllocatedStorage **   
The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume.  
Type: Integer  
Required: No

 ** StorageThroughput **   
The storage throughput value for the additional storage volume, in mebibytes per second (MiBps). This setting applies only to the General Purpose SSD (`gp3`) storage type.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type for the additional storage volume.  
Valid Values: `GP3 | IO2`   
Type: String  
Required: No

## See Also
<a name="API_AdditionalStorageVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AdditionalStorageVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AdditionalStorageVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AdditionalStorageVolume) 