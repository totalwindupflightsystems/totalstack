---
id: "@specs/aws/emr/docs/API_Cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Cluster
<a name="API_Cluster"></a>

The detailed description of the cluster.

## Contents
<a name="API_Cluster_Contents"></a>

 ** Applications **   <a name="EMR-Type-Cluster-Applications"></a>
The applications installed on this cluster.  
Type: Array of [Application](API_Application.md) objects  
Required: No

 ** AutoScalingRole **   <a name="EMR-Type-Cluster-AutoScalingRole"></a>
An IAM role for automatic scaling policies. The default role is `EMR_AutoScaling_DefaultRole`. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** AutoTerminate **   <a name="EMR-Type-Cluster-AutoTerminate"></a>
Specifies whether the cluster should terminate after completing all steps.  
Type: Boolean  
Required: No

 ** ClusterArn **   <a name="EMR-Type-Cluster-ClusterArn"></a>
The Amazon Resource Name of the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** Configurations **   <a name="EMR-Type-Cluster-Configurations"></a>
Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** CustomAmiId **   <a name="EMR-Type-Cluster-CustomAmiId"></a>
Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EbsRootVolumeIops **   <a name="EMR-Type-Cluster-EbsRootVolumeIops"></a>
The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.  
Type: Integer  
Required: No

 ** EbsRootVolumeSize **   <a name="EMR-Type-Cluster-EbsRootVolumeSize"></a>
The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.  
Type: Integer  
Required: No

 ** EbsRootVolumeThroughput **   <a name="EMR-Type-Cluster-EbsRootVolumeThroughput"></a>
The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.  
Type: Integer  
Required: No

 ** Ec2InstanceAttributes **   <a name="EMR-Type-Cluster-Ec2InstanceAttributes"></a>
Provides information about the Amazon EC2 instances in a cluster grouped by category. For example, key name, subnet ID, IAM instance profile, and so on.  
Type: [Ec2InstanceAttributes](API_Ec2InstanceAttributes.md) object  
Required: No

 ** ExtendedSupport **   <a name="EMR-Type-Cluster-ExtendedSupport"></a>
Reserved.  
Type: Boolean  
Required: No

 ** Id **   <a name="EMR-Type-Cluster-Id"></a>
The unique identifier for the cluster.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** InstanceCollectionType **   <a name="EMR-Type-Cluster-InstanceCollectionType"></a>
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.
The instance group configuration of the cluster. A value of `INSTANCE_GROUP` indicates a uniform instance group configuration. A value of `INSTANCE_FLEET` indicates an instance fleets configuration.  
Type: String  
Valid Values: `INSTANCE_FLEET | INSTANCE_GROUP`   
Required: No

 ** KerberosAttributes **   <a name="EMR-Type-Cluster-KerberosAttributes"></a>
Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see [Use Kerberos Authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html) in the *Amazon EMR Management Guide*.  
Type: [KerberosAttributes](API_KerberosAttributes.md) object  
Required: No

 ** LogEncryptionKmsKeyId **   <a name="EMR-Type-Cluster-LogEncryptionKmsKeyId"></a>
 The AWS KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0.   
Type: String  
Required: No

 ** LogUri **   <a name="EMR-Type-Cluster-LogUri"></a>
The path to the Amazon S3 location where logs for this cluster are stored.  
Type: String  
Required: No

 ** MasterPublicDnsName **   <a name="EMR-Type-Cluster-MasterPublicDnsName"></a>
The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.  
Type: String  
Required: No

 ** MonitoringConfiguration **   <a name="EMR-Type-Cluster-MonitoringConfiguration"></a>
Contains Cloudwatch log configuration metadata and settings.  
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object  
Required: No

 ** Name **   <a name="EMR-Type-Cluster-Name"></a>
The name of the cluster. This parameter can't contain the characters <, >, $, \|, or ` (backtick).  
Type: String  
Required: No

 ** NormalizedInstanceHours **   <a name="EMR-Type-Cluster-NormalizedInstanceHours"></a>
An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.  
Type: Integer  
Required: No

 ** OSReleaseLabel **   <a name="EMR-Type-Cluster-OSReleaseLabel"></a>
The Amazon Linux release specified in a cluster launch RunJobFlow request. If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.  
Type: String  
Required: No

 ** OutpostArn **   <a name="EMR-Type-Cluster-OutpostArn"></a>
 The Amazon Resource Name (ARN) of the Outpost where the cluster is launched.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** PlacementGroups **   <a name="EMR-Type-Cluster-PlacementGroups"></a>
Placement group configured for an Amazon EMR cluster.  
Type: Array of [PlacementGroupConfig](API_PlacementGroupConfig.md) objects  
Required: No

 ** ReleaseLabel **   <a name="EMR-Type-Cluster-ReleaseLabel"></a>
The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form `emr-x.x.x`, where x.x.x is an Amazon EMR release version such as `emr-5.14.0`. For more information about Amazon EMR release versions and included application versions and features, see [https://docs.aws.amazon.com/emr/latest/ReleaseGuide/](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/). The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use `AmiVersion`.  
Type: String  
Required: No

 ** RepoUpgradeOnBoot **   <a name="EMR-Type-Cluster-RepoUpgradeOnBoot"></a>
Applies only when `CustomAmiID` is used. Specifies the type of updates that the Amazon Linux AMI package repositories apply when an instance boots using the AMI.  
Type: String  
Valid Values: `SECURITY | NONE`   
Required: No

 ** RequestedAmiVersion **   <a name="EMR-Type-Cluster-RequestedAmiVersion"></a>
The AMI version requested for this cluster.  
Type: String  
Required: No

 ** RunningAmiVersion **   <a name="EMR-Type-Cluster-RunningAmiVersion"></a>
The AMI version running on this cluster.  
Type: String  
Required: No

 ** ScaleDownBehavior **   <a name="EMR-Type-Cluster-ScaleDownBehavior"></a>
The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.  
Type: String  
Valid Values: `TERMINATE_AT_INSTANCE_HOUR | TERMINATE_AT_TASK_COMPLETION`   
Required: No

 ** SecurityConfiguration **   <a name="EMR-Type-Cluster-SecurityConfiguration"></a>
The name of the security configuration applied to the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ServiceRole **   <a name="EMR-Type-Cluster-ServiceRole"></a>
The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf.  
Type: String  
Required: No

 ** Status **   <a name="EMR-Type-Cluster-Status"></a>
The current status details about the cluster.  
Type: [ClusterStatus](API_ClusterStatus.md) object  
Required: No

 ** StepConcurrencyLevel **   <a name="EMR-Type-Cluster-StepConcurrencyLevel"></a>
Specifies the number of steps that can be executed concurrently.  
Type: Integer  
Required: No

 ** Tags **   <a name="EMR-Type-Cluster-Tags"></a>
A list of tags associated with a cluster.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TerminationProtected **   <a name="EMR-Type-Cluster-TerminationProtected"></a>
Indicates whether Amazon EMR will lock the cluster to prevent the Amazon EC2 instances from being terminated by an API call or user intervention, or in the event of a cluster error.  
Type: Boolean  
Required: No

 ** UnhealthyNodeReplacement **   <a name="EMR-Type-Cluster-UnhealthyNodeReplacement"></a>
Indicates whether Amazon EMR should gracefully replace Amazon EC2 core instances that have degraded within the cluster.  
Type: Boolean  
Required: No

 ** VisibleToAllUsers **   <a name="EMR-Type-Cluster-VisibleToAllUsers"></a>
Indicates whether the cluster is visible to IAM principals in the AWS account associated with the cluster. When `true`, IAM principals in the AWS account can perform Amazon EMR cluster actions on the cluster that their IAM policies allow. When `false`, only the IAM principal that created the cluster and the AWS account root user can perform Amazon EMR actions, regardless of IAM permissions policies attached to other IAM principals.  
The default value is `true` if a value is not provided when creating a cluster using the Amazon EMR API [RunJobFlow](API_RunJobFlow.md) command, the AWS CLI [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html) command, or the AWS Management Console.  
Type: Boolean  
Required: No

## See Also
<a name="API_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Cluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Cluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Cluster) 