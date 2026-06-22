---
id: "@specs/aws/emr/docs/API_VolumeSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VolumeSpecification"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# VolumeSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_VolumeSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VolumeSpecification
<a name="API_VolumeSpecification"></a>

EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.

## Contents
<a name="API_VolumeSpecification_Contents"></a>

 ** SizeInGB **   <a name="EMR-Type-VolumeSpecification-SizeInGB"></a>
The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.  
Type: Integer  
Required: Yes

 ** VolumeType **   <a name="EMR-Type-VolumeSpecification-VolumeType"></a>
The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.  
Type: String  
Required: Yes

 ** Iops **   <a name="EMR-Type-VolumeSpecification-Iops"></a>
The number of I/O operations per second (IOPS) that the volume supports.  
Type: Integer  
Required: No

 ** Throughput **   <a name="EMR-Type-VolumeSpecification-Throughput"></a>
The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_VolumeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/VolumeSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/VolumeSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/VolumeSpecification) 