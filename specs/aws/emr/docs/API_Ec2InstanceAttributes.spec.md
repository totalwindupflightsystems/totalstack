---
id: "@specs/aws/emr/docs/API_Ec2InstanceAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Ec2InstanceAttributes"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Ec2InstanceAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Ec2InstanceAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Ec2InstanceAttributes
<a name="API_Ec2InstanceAttributes"></a>

Provides information about the Amazon EC2 instances in a cluster grouped by category. For example, key name, subnet ID, IAM instance profile, and so on.

## Contents
<a name="API_Ec2InstanceAttributes_Contents"></a>

 ** AdditionalMasterSecurityGroups **   <a name="EMR-Type-Ec2InstanceAttributes-AdditionalMasterSecurityGroups"></a>
A list of additional Amazon EC2 security group IDs for the master node.  
Type: Array of strings  
Required: No

 ** AdditionalSlaveSecurityGroups **   <a name="EMR-Type-Ec2InstanceAttributes-AdditionalSlaveSecurityGroups"></a>
A list of additional Amazon EC2 security group IDs for the core and task nodes.  
Type: Array of strings  
Required: No

 ** Ec2AvailabilityZone **   <a name="EMR-Type-Ec2InstanceAttributes-Ec2AvailabilityZone"></a>
The Availability Zone in which the cluster will run.   
Type: String  
Required: No

 ** Ec2KeyName **   <a name="EMR-Type-Ec2InstanceAttributes-Ec2KeyName"></a>
The name of the Amazon EC2 key pair to use when connecting with SSH into the master node as a user named "hadoop".  
Type: String  
Required: No

 ** Ec2SubnetId **   <a name="EMR-Type-Ec2InstanceAttributes-Ec2SubnetId"></a>
Set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value, and your account supports EC2-Classic, the cluster launches in EC2-Classic.  
Type: String  
Required: No

 ** EmrManagedMasterSecurityGroup **   <a name="EMR-Type-Ec2InstanceAttributes-EmrManagedMasterSecurityGroup"></a>
The identifier of the Amazon EC2 security group for the master node.  
Type: String  
Required: No

 ** EmrManagedSlaveSecurityGroup **   <a name="EMR-Type-Ec2InstanceAttributes-EmrManagedSlaveSecurityGroup"></a>
The identifier of the Amazon EC2 security group for the core and task nodes.  
Type: String  
Required: No

 ** IamInstanceProfile **   <a name="EMR-Type-Ec2InstanceAttributes-IamInstanceProfile"></a>
The IAM role that was specified when the cluster was launched. The Amazon EC2 instances of the cluster assume this role.  
Type: String  
Required: No

 ** RequestedEc2AvailabilityZones **   <a name="EMR-Type-Ec2InstanceAttributes-RequestedEc2AvailabilityZones"></a>
Applies to clusters configured with the instance fleets option. Specifies one or more Availability Zones in which to launch Amazon EC2 cluster instances when the EC2-Classic network configuration is supported. Amazon EMR chooses the Availability Zone with the best fit from among the list of `RequestedEc2AvailabilityZones`, and then launches all cluster instances within that Availability Zone. If you do not specify this value, Amazon EMR chooses the Availability Zone for you. `RequestedEc2SubnetIDs` and `RequestedEc2AvailabilityZones` cannot be specified together.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** RequestedEc2SubnetIds **   <a name="EMR-Type-Ec2InstanceAttributes-RequestedEc2SubnetIds"></a>
Applies to clusters configured with the instance fleets option. Specifies the unique identifier of one or more Amazon EC2 subnets in which to launch Amazon EC2 cluster instances. Subnets must exist within the same VPC. Amazon EMR chooses the Amazon EC2 subnet with the best fit from among the list of `RequestedEc2SubnetIds`, and then launches all cluster instances within that Subnet. If this value is not specified, and the account and Region support EC2-Classic networks, the cluster launches instances in the EC2-Classic network and uses `RequestedEc2AvailabilityZones` instead of this setting. If EC2-Classic is not supported, and no Subnet is specified, Amazon EMR chooses the subnet for you. `RequestedEc2SubnetIDs` and `RequestedEc2AvailabilityZones` cannot be specified together.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ServiceAccessSecurityGroup **   <a name="EMR-Type-Ec2InstanceAttributes-ServiceAccessSecurityGroup"></a>
The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.  
Type: String  
Required: No

## See Also
<a name="API_Ec2InstanceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Ec2InstanceAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Ec2InstanceAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Ec2InstanceAttributes) 