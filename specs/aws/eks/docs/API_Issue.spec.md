---
id: "@specs/aws/eks/docs/API_Issue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Issue"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Issue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Issue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Issue
<a name="API_Issue"></a>

An object representing an issue with an Amazon EKS resource.

## Contents
<a name="API_Issue_Contents"></a>

 ** code **   <a name="AmazonEKS-Type-Issue-code"></a>
A brief description of the error.  
+  **AccessDenied**: Amazon EKS or one or more of your managed nodes is failing to authenticate or authorize with your Kubernetes cluster API server.
+  **AsgInstanceLaunchFailures**: Your Auto Scaling group is experiencing failures while attempting to launch instances.
+  **AutoScalingGroupNotFound**: We couldn't find the Auto Scaling group associated with the managed node group. You may be able to recreate an Auto Scaling group with the same settings to recover.
+  **ClusterUnreachable**: Amazon EKS or one or more of your managed nodes is unable to to communicate with your Kubernetes cluster API server. This can happen if there are network disruptions or if API servers are timing out processing requests. 
+  **Ec2InstanceTypeDoesNotExist**: One or more of the supplied Amazon EC2 instance types do not exist. Amazon EKS checked for the instance types that you provided in this AWS Region, and one or more aren't available.
+  **Ec2LaunchTemplateNotFound**: We couldn't find the Amazon EC2 launch template for your managed node group. You may be able to recreate a launch template with the same settings to recover.
+  **Ec2LaunchTemplateVersionMismatch**: The Amazon EC2 launch template version for your managed node group does not match the version that Amazon EKS created. You may be able to revert to the version that Amazon EKS created to recover.
+  **Ec2SecurityGroupDeletionFailure**: We could not delete the remote access security group for your managed node group. Remove any dependencies from the security group.
+  **Ec2SecurityGroupNotFound**: We couldn't find the cluster security group for the cluster. You must recreate your cluster.
+  **Ec2SubnetInvalidConfiguration**: One or more Amazon EC2 subnets specified for a node group do not automatically assign public IP addresses to instances launched into it. If you want your instances to be assigned a public IP address, then you need to enable the `auto-assign public IP address` setting for the subnet. See [Modifying the public `IPv4` addressing attribute for your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#subnet-public-ip) in the *Amazon VPC User Guide*.
+  **IamInstanceProfileNotFound**: We couldn't find the IAM instance profile for your managed node group. You may be able to recreate an instance profile with the same settings to recover.
+  **IamNodeRoleNotFound**: We couldn't find the IAM role for your managed node group. You may be able to recreate an IAM role with the same settings to recover.
+  **InstanceLimitExceeded**: Your AWS account is unable to launch any more instances of the specified instance type. You may be able to request an Amazon EC2 instance limit increase to recover.
+  **InsufficientFreeAddresses**: One or more of the subnets associated with your managed node group does not have enough available IP addresses for new nodes.
+  **InternalFailure**: These errors are usually caused by an Amazon EKS server-side issue.
+  **NodeCreationFailure**: Your launched instances are unable to register with your Amazon EKS cluster. Common causes of this failure are insufficient [node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) permissions or lack of outbound internet access for the nodes. 
Type: String  
Valid Values: `AutoScalingGroupNotFound | AutoScalingGroupInvalidConfiguration | Ec2SecurityGroupNotFound | Ec2SecurityGroupDeletionFailure | Ec2LaunchTemplateNotFound | Ec2LaunchTemplateVersionMismatch | Ec2SubnetNotFound | Ec2SubnetInvalidConfiguration | IamInstanceProfileNotFound | Ec2SubnetMissingIpv6Assignment | IamLimitExceeded | IamNodeRoleNotFound | NodeCreationFailure | AsgInstanceLaunchFailures | InstanceLimitExceeded | InsufficientFreeAddresses | AccessDenied | InternalFailure | ClusterUnreachable | AmiIdNotFound | AutoScalingGroupOptInRequired | AutoScalingGroupRateLimitExceeded | Ec2LaunchTemplateDeletionFailure | Ec2LaunchTemplateInvalidConfiguration | Ec2LaunchTemplateMaxLimitExceeded | Ec2SubnetListTooLong | IamThrottling | NodeTerminationFailure | PodEvictionFailure | SourceEc2LaunchTemplateNotFound | LimitExceeded | Unknown | AutoScalingGroupInstanceRefreshActive | KubernetesLabelInvalid | Ec2LaunchTemplateVersionMaxLimitExceeded | Ec2InstanceTypeDoesNotExist`   
Required: No

 ** message **   <a name="AmazonEKS-Type-Issue-message"></a>
The error message associated with the issue.  
Type: String  
Required: No

 ** resourceIds **   <a name="AmazonEKS-Type-Issue-resourceIds"></a>
The AWS resources that are afflicted by this issue.  
Type: Array of strings  
Required: No

## See Also
<a name="API_Issue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Issue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Issue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Issue) 