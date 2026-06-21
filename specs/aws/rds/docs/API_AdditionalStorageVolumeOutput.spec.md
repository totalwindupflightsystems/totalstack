---
id: "@specs/aws/rds/docs/API_AdditionalStorageVolumeOutput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AdditionalStorageVolumeOutput"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# AdditionalStorageVolumeOutput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_AdditionalStorageVolumeOutput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AdditionalStorageVolumeOutput
<a name="API_AdditionalStorageVolumeOutput"></a>

Contains information about an additional storage volume for a DB instance.

## Contents
<a name="API_AdditionalStorageVolumeOutput_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

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
The storage throughput value for the additional storage volume, in mebibytes per second (MiBps).  
Type: Integer  
Required: No

 ** StorageType **   
The storage type for the additional storage volume.  
Valid Values: `GP3 | IO2`   
Type: String  
Required: No

 ** StorageVolumeStatus **   
The status of the additional storage volume.  
Valid Values: `ACTIVE | CREATING | DELETING | MODIFYING | NOT-IN-USE | STORAGE-OPTIMIZATION | VOLUME-FULL`   
Type: String  
Required: No

 ** VolumeName **   
The name of the additional storage volume.  
Type: String  
Required: No

## See Also
<a name="API_AdditionalStorageVolumeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AdditionalStorageVolumeOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AdditionalStorageVolumeOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AdditionalStorageVolumeOutput) 