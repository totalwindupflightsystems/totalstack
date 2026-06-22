---
id: "@specs/aws/emr/docs/API_Instance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Instance"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Instance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Instance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Instance
<a name="API_Instance"></a>

Represents an Amazon EC2 instance provisioned as part of cluster.

## Contents
<a name="API_Instance_Contents"></a>

 ** EbsVolumes **   <a name="EMR-Type-Instance-EbsVolumes"></a>
The list of Amazon EBS volumes that are attached to this instance.  
Type: Array of [EbsVolume](API_EbsVolume.md) objects  
Required: No

 ** Ec2InstanceId **   <a name="EMR-Type-Instance-Ec2InstanceId"></a>
The unique identifier of the instance in Amazon EC2.  
Type: String  
Required: No

 ** Id **   <a name="EMR-Type-Instance-Id"></a>
The unique identifier for the instance in Amazon EMR.  
Type: String  
Required: No

 ** InstanceFleetId **   <a name="EMR-Type-Instance-InstanceFleetId"></a>
The unique identifier of the instance fleet to which an Amazon EC2 instance belongs.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** InstanceGroupId **   <a name="EMR-Type-Instance-InstanceGroupId"></a>
The identifier of the instance group to which this instance belongs.  
Type: String  
Required: No

 ** InstanceType **   <a name="EMR-Type-Instance-InstanceType"></a>
The Amazon EC2 instance type, for example `m3.xlarge`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Market **   <a name="EMR-Type-Instance-Market"></a>
The instance purchasing option. Valid values are `ON_DEMAND` or `SPOT`.   
Type: String  
Valid Values: `ON_DEMAND | SPOT`   
Required: No

 ** PrivateDnsName **   <a name="EMR-Type-Instance-PrivateDnsName"></a>
The private DNS name of the instance.  
Type: String  
Required: No

 ** PrivateIpAddress **   <a name="EMR-Type-Instance-PrivateIpAddress"></a>
The private IP address of the instance.  
Type: String  
Required: No

 ** PublicDnsName **   <a name="EMR-Type-Instance-PublicDnsName"></a>
The public DNS name of the instance.  
Type: String  
Required: No

 ** PublicIpAddress **   <a name="EMR-Type-Instance-PublicIpAddress"></a>
The public IP address of the instance.  
Type: String  
Required: No

 ** Status **   <a name="EMR-Type-Instance-Status"></a>
The current status of the instance.  
Type: [InstanceStatus](API_InstanceStatus.md) object  
Required: No

## See Also
<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Instance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Instance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Instance) 