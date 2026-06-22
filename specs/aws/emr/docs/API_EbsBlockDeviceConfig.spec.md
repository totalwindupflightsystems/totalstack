---
id: "@specs/aws/emr/docs/API_EbsBlockDeviceConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EbsBlockDeviceConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# EbsBlockDeviceConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_EbsBlockDeviceConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EbsBlockDeviceConfig
<a name="API_EbsBlockDeviceConfig"></a>

Configuration of requested EBS block device associated with the instance group with count of volumes that are associated to every instance.

## Contents
<a name="API_EbsBlockDeviceConfig_Contents"></a>

 ** VolumeSpecification **   <a name="EMR-Type-EbsBlockDeviceConfig-VolumeSpecification"></a>
EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.  
Type: [VolumeSpecification](API_VolumeSpecification.md) object  
Required: Yes

 ** VolumesPerInstance **   <a name="EMR-Type-EbsBlockDeviceConfig-VolumesPerInstance"></a>
Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group  
Type: Integer  
Required: No

## See Also
<a name="API_EbsBlockDeviceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/EbsBlockDeviceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/EbsBlockDeviceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/EbsBlockDeviceConfig) 