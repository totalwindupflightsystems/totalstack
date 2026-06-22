---
id: "@specs/aws/eks/docs/API_Nodegroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Nodegroup"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Nodegroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Nodegroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Nodegroup
<a name="API_Nodegroup"></a>

An object representing an Amazon EKS managed node group.

## Contents
<a name="API_Nodegroup_Contents"></a>

 ** amiType **   <a name="AmazonEKS-Type-Nodegroup-amiType"></a>
If the node group was deployed using a launch template with a custom AMI, then this is `CUSTOM`. For node groups that weren't deployed using a launch template, this is the AMI type that was specified in the node group configuration.  
Type: String  
Valid Values: `AL2_x86_64 | AL2_x86_64_GPU | AL2_ARM_64 | CUSTOM | BOTTLEROCKET_ARM_64 | BOTTLEROCKET_x86_64 | BOTTLEROCKET_ARM_64_FIPS | BOTTLEROCKET_x86_64_FIPS | BOTTLEROCKET_ARM_64_NVIDIA | BOTTLEROCKET_x86_64_NVIDIA | BOTTLEROCKET_ARM_64_NVIDIA_FIPS | BOTTLEROCKET_x86_64_NVIDIA_FIPS | WINDOWS_CORE_2019_x86_64 | WINDOWS_FULL_2019_x86_64 | WINDOWS_CORE_2022_x86_64 | WINDOWS_FULL_2022_x86_64 | WINDOWS_CORE_2025_x86_64 | WINDOWS_FULL_2025_x86_64 | AL2023_x86_64_STANDARD | AL2023_ARM_64_STANDARD | AL2023_x86_64_NEURON | AL2023_x86_64_NVIDIA | AL2023_ARM_64_NVIDIA`   
Required: No

 ** capacityType **   <a name="AmazonEKS-Type-Nodegroup-capacityType"></a>
The capacity type of your managed node group.  
Type: String  
Valid Values: `ON_DEMAND | SPOT | CAPACITY_BLOCK`   
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-Nodegroup-clusterName"></a>
The name of your cluster.  
Type: String  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-Nodegroup-createdAt"></a>
The Unix epoch timestamp at object creation.  
Type: Timestamp  
Required: No

 ** diskSize **   <a name="AmazonEKS-Type-Nodegroup-diskSize"></a>
If the node group wasn't deployed with a launch template, then this is the disk size in the node group configuration. If the node group was deployed with a launch template, then this is `null`.  
Type: Integer  
Required: No

 ** health **   <a name="AmazonEKS-Type-Nodegroup-health"></a>
The health status of the node group. If there are issues with your node group's health, they are listed here.  
Type: [NodegroupHealth](API_NodegroupHealth.md) object  
Required: No

 ** instanceTypes **   <a name="AmazonEKS-Type-Nodegroup-instanceTypes"></a>
If the node group wasn't deployed with a launch template, then this is the instance type that is associated with the node group. If the node group was deployed with a launch template, then this is `null`.  
Type: Array of strings  
Required: No

 ** labels **   <a name="AmazonEKS-Type-Nodegroup-labels"></a>
The Kubernetes `labels` applied to the nodes in the node group.  
Only `labels` that are applied with the Amazon EKS API are shown here. There may be other Kubernetes `labels` applied to the nodes in this group.
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 63.  
Value Length Constraints: Minimum length of 1. Maximum length of 63.  
Required: No

 ** launchTemplate **   <a name="AmazonEKS-Type-Nodegroup-launchTemplate"></a>
If a launch template was used to create the node group, then this is the launch template that was used.  
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object  
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-Nodegroup-modifiedAt"></a>
The Unix epoch timestamp for the last modification to the object.  
Type: Timestamp  
Required: No

 ** nodegroupArn **   <a name="AmazonEKS-Type-Nodegroup-nodegroupArn"></a>
The Amazon Resource Name (ARN) associated with the managed node group.  
Type: String  
Required: No

 ** nodegroupName **   <a name="AmazonEKS-Type-Nodegroup-nodegroupName"></a>
The name associated with an Amazon EKS managed node group.  
Type: String  
Required: No

 ** nodeRepairConfig **   <a name="AmazonEKS-Type-Nodegroup-nodeRepairConfig"></a>
The node auto repair configuration for the node group.  
Type: [NodeRepairConfig](API_NodeRepairConfig.md) object  
Required: No

 ** nodeRole **   <a name="AmazonEKS-Type-Nodegroup-nodeRole"></a>
The IAM role associated with your node group. The Amazon EKS node `kubelet` daemon makes calls to AWS APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies.  
Type: String  
Required: No

 ** releaseVersion **   <a name="AmazonEKS-Type-Nodegroup-releaseVersion"></a>
If the node group was deployed using a launch template with a custom AMI, then this is the AMI ID that was specified in the launch template. For node groups that weren't deployed using a launch template, this is the version of the Amazon EKS optimized AMI that the node group was deployed with.  
Type: String  
Required: No

 ** remoteAccess **   <a name="AmazonEKS-Type-Nodegroup-remoteAccess"></a>
If the node group wasn't deployed with a launch template, then this is the remote access configuration that is associated with the node group. If the node group was deployed with a launch template, then this is `null`.  
Type: [RemoteAccessConfig](API_RemoteAccessConfig.md) object  
Required: No

 ** resources **   <a name="AmazonEKS-Type-Nodegroup-resources"></a>
The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.  
Type: [NodegroupResources](API_NodegroupResources.md) object  
Required: No

 ** scalingConfig **   <a name="AmazonEKS-Type-Nodegroup-scalingConfig"></a>
The scaling configuration details for the Auto Scaling group that is associated with your node group.  
Type: [NodegroupScalingConfig](API_NodegroupScalingConfig.md) object  
Required: No

 ** status **   <a name="AmazonEKS-Type-Nodegroup-status"></a>
The current status of the managed node group.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | DELETE_FAILED | DEGRADED`   
Required: No

 ** subnets **   <a name="AmazonEKS-Type-Nodegroup-subnets"></a>
The subnets that were specified for the Auto Scaling group that is associated with your node group.  
Type: Array of strings  
Required: No

 ** tags **   <a name="AmazonEKS-Type-Nodegroup-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** taints **   <a name="AmazonEKS-Type-Nodegroup-taints"></a>
The Kubernetes taints to be applied to the nodes in the node group when they are created. Effect is one of `No_Schedule`, `Prefer_No_Schedule`, or `No_Execute`. Kubernetes taints can be used together with tolerations to control how workloads are scheduled to your nodes. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html).  
Type: Array of [Taint](API_Taint.md) objects  
Required: No

 ** updateConfig **   <a name="AmazonEKS-Type-Nodegroup-updateConfig"></a>
The node group update configuration.  
Type: [NodegroupUpdateConfig](API_NodegroupUpdateConfig.md) object  
Required: No

 ** version **   <a name="AmazonEKS-Type-Nodegroup-version"></a>
The Kubernetes version of the managed node group.  
Type: String  
Required: No

 ** warmPoolConfig **   <a name="AmazonEKS-Type-Nodegroup-warmPoolConfig"></a>
The warm pool configuration attached to the node group. Amazon EKS manages warm pools throughout the node group lifecycle using the `AWSServiceRoleForAmazonEKSNodegroup` service-linked role to create, update, and delete warm pool resources.  
Type: [WarmPoolConfig](API_WarmPoolConfig.md) object  
Required: No

## See Also
<a name="API_Nodegroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Nodegroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Nodegroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Nodegroup) 