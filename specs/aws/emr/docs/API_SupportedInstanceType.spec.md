---
id: "@specs/aws/emr/docs/API_SupportedInstanceType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SupportedInstanceType"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SupportedInstanceType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SupportedInstanceType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SupportedInstanceType
<a name="API_SupportedInstanceType"></a>

An instance type that the specified Amazon EMR release supports.

## Contents
<a name="API_SupportedInstanceType_Contents"></a>

 ** Architecture **   <a name="EMR-Type-SupportedInstanceType-Architecture"></a>
The CPU architecture, for example `X86_64` or `AARCH64`.  
Type: String  
Required: No

 ** EbsOptimizedAvailable **   <a name="EMR-Type-SupportedInstanceType-EbsOptimizedAvailable"></a>
Indicates whether the `SupportedInstanceType` supports Amazon EBS optimization.  
Type: Boolean  
Required: No

 ** EbsOptimizedByDefault **   <a name="EMR-Type-SupportedInstanceType-EbsOptimizedByDefault"></a>
Indicates whether the `SupportedInstanceType` uses Amazon EBS optimization by default.  
Type: Boolean  
Required: No

 ** EbsStorageOnly **   <a name="EMR-Type-SupportedInstanceType-EbsStorageOnly"></a>
Indicates whether the `SupportedInstanceType` only supports Amazon EBS.  
Type: Boolean  
Required: No

 ** InstanceFamilyId **   <a name="EMR-Type-SupportedInstanceType-InstanceFamilyId"></a>
The Amazon EC2 family and generation for the `SupportedInstanceType`.  
Type: String  
Required: No

 ** Is64BitsOnly **   <a name="EMR-Type-SupportedInstanceType-Is64BitsOnly"></a>
Indicates whether the `SupportedInstanceType` only supports 64-bit architecture.  
Type: Boolean  
Required: No

 ** MemoryGB **   <a name="EMR-Type-SupportedInstanceType-MemoryGB"></a>
The amount of memory that is available to Amazon EMR from the `SupportedInstanceType`. The kernel and hypervisor software consume some memory, so this value might be lower than the overall memory for the instance type.  
Type: Float  
Required: No

 ** NumberOfDisks **   <a name="EMR-Type-SupportedInstanceType-NumberOfDisks"></a>
Number of disks for the `SupportedInstanceType`. This value is `0` for Amazon EBS-only instance types.  
Type: Integer  
Required: No

 ** StorageGB **   <a name="EMR-Type-SupportedInstanceType-StorageGB"></a>
 `StorageGB` represents the storage capacity of the `SupportedInstanceType`. This value is `0` for Amazon EBS-only instance types.  
Type: Integer  
Required: No

 ** Type **   <a name="EMR-Type-SupportedInstanceType-Type"></a>
The [Amazon EC2 instance type](http://aws.amazon.com/ec2/instance-types/), for example `m5.xlarge`, of the `SupportedInstanceType`.  
Type: String  
Required: No

 ** VCPU **   <a name="EMR-Type-SupportedInstanceType-VCPU"></a>
The number of vCPUs available for the `SupportedInstanceType`.  
Type: Integer  
Required: No

## See Also
<a name="API_SupportedInstanceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SupportedInstanceType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SupportedInstanceType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SupportedInstanceType) 