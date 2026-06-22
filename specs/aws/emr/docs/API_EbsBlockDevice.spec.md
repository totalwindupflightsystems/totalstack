---
id: "@specs/aws/emr/docs/API_EbsBlockDevice"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EbsBlockDevice"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# EbsBlockDevice

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_EbsBlockDevice
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EbsBlockDevice
<a name="API_EbsBlockDevice"></a>

Configuration of requested EBS block device associated with the instance group.

## Contents
<a name="API_EbsBlockDevice_Contents"></a>

 ** Device **   <a name="EMR-Type-EbsBlockDevice-Device"></a>
The device name that is exposed to the instance, such as /dev/sdh.  
Type: String  
Required: No

 ** VolumeSpecification **   <a name="EMR-Type-EbsBlockDevice-VolumeSpecification"></a>
EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.  
Type: [VolumeSpecification](API_VolumeSpecification.md) object  
Required: No

## See Also
<a name="API_EbsBlockDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/EbsBlockDevice) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/EbsBlockDevice) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/EbsBlockDevice) 