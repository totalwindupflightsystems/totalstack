---
id: "@specs/aws/emr/docs/API_JobFlowInstancesConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobFlowInstancesConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# JobFlowInstancesConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_JobFlowInstancesConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobFlowInstancesConfig
<a name="API_JobFlowInstancesConfig"></a>

A description of the Amazon EC2 instance on which the cluster (job flow) runs. A valid JobFlowInstancesConfig must contain either InstanceGroups or InstanceFleets. They cannot be used together. You may also have MasterInstanceType, SlaveInstanceType, and InstanceCount (all three must be present), but we don't recommend this configuration.

## Contents
<a name="API_JobFlowInstancesConfig_Contents"></a>

 ** AdditionalMasterSecurityGroups **   <a name="EMR-Type-JobFlowInstancesConfig-AdditionalMasterSecurityGroups"></a>
A list of additional Amazon EC2 security group IDs for the master node.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** AdditionalSlaveSecurityGroups **   <a name="EMR-Type-JobFlowInstancesConfig-AdditionalSlaveSecurityGroups"></a>
A list of additional Amazon EC2 security group IDs for the core and task nodes.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Ec2KeyName **   <a name="EMR-Type-JobFlowInstancesConfig-Ec2KeyName"></a>
The name of the Amazon EC2 key pair that can be used to connect to the master node using SSH as the user called "hadoop."  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Ec2SubnetId **   <a name="EMR-Type-JobFlowInstancesConfig-Ec2SubnetId"></a>
Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Ec2SubnetIds **   <a name="EMR-Type-JobFlowInstancesConfig-Ec2SubnetIds"></a>
Applies to clusters that use the instance fleet configuration. When multiple Amazon EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EmrManagedMasterSecurityGroup **   <a name="EMR-Type-JobFlowInstancesConfig-EmrManagedMasterSecurityGroup"></a>
The identifier of the Amazon EC2 security group for the master node. If you specify `EmrManagedMasterSecurityGroup`, you must also specify `EmrManagedSlaveSecurityGroup`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EmrManagedSlaveSecurityGroup **   <a name="EMR-Type-JobFlowInstancesConfig-EmrManagedSlaveSecurityGroup"></a>
The identifier of the Amazon EC2 security group for the core and task nodes. If you specify `EmrManagedSlaveSecurityGroup`, you must also specify `EmrManagedMasterSecurityGroup`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** HadoopVersion **   <a name="EMR-Type-JobFlowInstancesConfig-HadoopVersion"></a>
Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are "0.18" (no longer maintained), "0.20" (no longer maintained), "0.20.205" (no longer maintained), "1.0.3", "2.2.0", or "2.4.0". If you do not set this value, the default of 0.18 is used, unless the `AmiVersion` parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** InstanceCount **   <a name="EMR-Type-JobFlowInstancesConfig-InstanceCount"></a>
The number of Amazon EC2 instances in the cluster.  
Type: Integer  
Required: No

 ** InstanceFleets **   <a name="EMR-Type-JobFlowInstancesConfig-InstanceFleets"></a>
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.
Describes the Amazon EC2 instances and instance configurations for clusters that use the instance fleet configuration.  
Type: Array of [InstanceFleetConfig](API_InstanceFleetConfig.md) objects  
Required: No

 ** InstanceGroups **   <a name="EMR-Type-JobFlowInstancesConfig-InstanceGroups"></a>
Configuration for the instance groups in a cluster.  
Type: Array of [InstanceGroupConfig](API_InstanceGroupConfig.md) objects  
Required: No

 ** KeepJobFlowAliveWhenNoSteps **   <a name="EMR-Type-JobFlowInstancesConfig-KeepJobFlowAliveWhenNoSteps"></a>
Specifies whether the cluster should remain available after completing all steps. Defaults to `false`. For more information about configuring cluster termination, see [Control Cluster Termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html) in the *EMR Management Guide*.  
Type: Boolean  
Required: No

 ** MasterInstanceType **   <a name="EMR-Type-JobFlowInstancesConfig-MasterInstanceType"></a>
The Amazon EC2 instance type of the master node.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Placement **   <a name="EMR-Type-JobFlowInstancesConfig-Placement"></a>
The Availability Zone in which the cluster runs.  
Type: [PlacementType](API_PlacementType.md) object  
Required: No

 ** ServiceAccessSecurityGroup **   <a name="EMR-Type-JobFlowInstancesConfig-ServiceAccessSecurityGroup"></a>
The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** SlaveInstanceType **   <a name="EMR-Type-JobFlowInstancesConfig-SlaveInstanceType"></a>
The Amazon EC2 instance type of the core and task nodes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** TerminationProtected **   <a name="EMR-Type-JobFlowInstancesConfig-TerminationProtected"></a>
Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.  
Type: Boolean  
Required: No

 ** UnhealthyNodeReplacement **   <a name="EMR-Type-JobFlowInstancesConfig-UnhealthyNodeReplacement"></a>
Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.  
Type: Boolean  
Required: No

## See Also
<a name="API_JobFlowInstancesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/JobFlowInstancesConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/JobFlowInstancesConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/JobFlowInstancesConfig) 