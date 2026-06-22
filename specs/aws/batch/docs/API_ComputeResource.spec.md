---
id: "@specs/aws/batch/docs/API_ComputeResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ComputeResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ComputeResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ComputeResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ComputeResource
<a name="API_ComputeResource"></a>

An object that represents an AWS Batch compute resource. For more information, see [Compute environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_ComputeResource_Contents"></a>

 ** maxvCpus **   <a name="Batch-Type-ComputeResource-maxvCpus"></a>
The maximum number of vCPUs that a compute environment can support.  
With any allocation strategy except `BEST_FIT` using On-Demand (`EC2`) compute resources, AWS Batch might need to exceed `maxvCpus` to meet your capacity requirements. In this event, AWS Batch never exceeds `maxvCpus` by more than a single instance.
Type: Integer  
Required: Yes

 ** type **   <a name="Batch-Type-ComputeResource-type"></a>
The type of compute environment: `EC2`, `SPOT`, `FARGATE`, or `FARGATE_SPOT`. For more information, see [Compute environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.  
 If you choose `SPOT`, you must also specify an Amazon EC2 Spot Fleet role with the `spotIamFleetRole` parameter. For more information, see [Amazon EC2 spot fleet role](https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html) in the * AWS Batch User Guide*.  
Multi-node parallel jobs aren't supported on Spot Instances.
Type: String  
Valid Values: `EC2 | SPOT | FARGATE | FARGATE_SPOT`   
Required: Yes

 ** allocationStrategy **   <a name="Batch-Type-ComputeResource-allocationStrategy"></a>
The allocation strategy to use for the compute resource if not enough instances of the best fitting instance type can be allocated. This might be because of availability of the instance type in the Region or [Amazon EC2 service limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html). For more information, see [Allocation strategies](https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html) in the * AWS Batch User Guide*.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
This parameter is required for Amazon EKS compute environments. For Amazon ECS compute environments, if this parameter isn't specified, the `BEST_FIT` allocation strategy is used by default.  
BEST\_FIT (default)  
 AWS Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, AWS Batch waits for the additional instances to be available. If there aren't enough instances available or the user is reaching [Amazon EC2 service limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html), additional jobs aren't run until the currently running jobs are completed. This allocation strategy keeps costs lower but can limit scaling. If you're using Spot Fleets with `BEST_FIT`, the Spot Fleet IAM Role must be specified. Compute resources that use a `BEST_FIT` allocation strategy don't support infrastructure updates and can't update some parameters. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.  
BEST\_FIT\_PROGRESSIVE  
 AWS Batch selects additional instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types with lower cost vCPUs. If additional instances of the previously selected instance types aren't available, AWS Batch selects new instance types.  
BEST\_FIT\_PROGRESSIVE\_ORDERED  
This is an advanced allocation strategy only for customers who want to control which instance types are preferred during scaling.  
Placing large instance types at the top of the list may result in **over-provisioning** for small jobs. Placing small instance types at the top may cause the compute environment to reach Amazon EC2 instance count limits before reaching `maxvCpus`.
 AWS Batch selects instance types in the order they appear in the `instanceTypes` list. When an instance family is specified, sizes within that family are expanded using `BEST_FIT_PROGRESSIVE` logic—preferring sizes that best fit the jobs, with larger sizes as fallback. Instance types that cannot meet the resource requirements of the jobs are skipped. This strategy is only available for On-Demand Instance (`EC2`) compute resources.  
If an instance family and an explicit instance type from that family both appear in `instanceTypes`, the explicit type takes its listed position and is excluded from the family expansion. For example, in `["m7a.4xlarge", "m7a", "m6a"]`, `m7a.4xlarge` is always placed first and is excluded from the `m7a` family expansion.  
SPOT\_CAPACITY\_OPTIMIZED  
 AWS Batch selects one or more instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources.  
SPOT\_PRICE\_CAPACITY\_OPTIMIZED  
The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price. This allocation strategy is only available for Spot Instance compute resources.  
SPOT\_CAPACITY\_OPTIMIZED\_PRIORITIZED  
This is an advanced allocation strategy for customers who want to influence instance type selection during scaling. This strategy optimizes for **capacity first**, and honors instance type priorities on a best-effort basis (priorities are honored when they do not significantly reduce available Spot capacity).  
Placing large instance types at the top of the list may result in **over-provisioning** for small jobs. Placing small instance types at the top may cause the compute environment to reach Amazon EC2 instance count limits before reaching `maxvCpus`.
 AWS Batch selects instance types in the order they appear in the `instanceTypes` list, but **optimizes for capacity first**. The customer-defined priority is honored on a best-effort basis. When Spot Instance capacity pools are similarly available, priority order is respected. When capacity is constrained, AWS Batch selects from the most available pools regardless of priority to minimize the likelihood of Spot Instance interruptions. This strategy is only available for Spot Instance compute resources.
With any allocation strategy except `BEST_FIT` using On-Demand (`EC2`) compute resources, AWS Batch might need to exceed `maxvCpus` to meet your capacity requirements. In this event, AWS Batch never exceeds `maxvCpus` by more than a single instance.  
Type: String  
Valid Values: `BEST_FIT | BEST_FIT_PROGRESSIVE | BEST_FIT_PROGRESSIVE_ORDERED | SPOT_CAPACITY_OPTIMIZED | SPOT_PRICE_CAPACITY_OPTIMIZED | SPOT_CAPACITY_OPTIMIZED_PRIORITIZED`   
Required: No

 ** bidPercentage **   <a name="Batch-Type-ComputeResource-bidPercentage"></a>
The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price. For most use cases, we recommend leaving this field empty.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: Integer  
Required: No

 ** desiredvCpus **   <a name="Batch-Type-ComputeResource-desiredvCpus"></a>
The desired number of vCPUS in the compute environment. AWS Batch modifies this value between the minimum and maximum values based on job queue demand.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: Integer  
Required: No

 ** ec2Configuration **   <a name="Batch-Type-ComputeResource-ec2Configuration"></a>
Provides information that's used to select Amazon Machine Images (AMIs) for Amazon EC2 instances in the compute environment. If `Ec2Configuration` isn't specified, the default is `ECS_AL2023` for EC2 (ECS) compute environments and `EKS_AL2023` for EKS compute environments.  
One or two values can be provided.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: Array of [Ec2Configuration](API_Ec2Configuration.md) objects  
Required: No

 ** ec2KeyPair **   <a name="Batch-Type-ComputeResource-ec2KeyPair"></a>
The Amazon EC2 key pair that's used for instances launched in the compute environment. You can use this key pair to log in to your instances with SSH.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: String  
Required: No

 ** imageId **   <a name="Batch-Type-ComputeResource-imageId"></a>
 *This member has been deprecated.*   
The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. This parameter is overridden by the `imageIdOverride` member of the `Ec2Configuration` structure.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2023 AMI. For more information, see [Amazon ECS-optimized Amazon Linux 2023 AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String  
Required: No

 ** instanceRole **   <a name="Batch-Type-ComputeResource-instanceRole"></a>
The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. This parameter is required for Amazon EC2 instances types. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ` ecsInstanceRole ` or `arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole `. For more information, see [Amazon ECS instance role](https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html) in the * AWS Batch User Guide*.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: String  
Required: No

 ** instanceTypes **   <a name="Batch-Type-ComputeResource-instanceTypes"></a>
The instances types that can be launched. You can specify instance families to launch any instance type within those families (for example, `c5` or `p3`), or you can specify specific sizes within a family (such as `c5.8xlarge`).  
 AWS Batch can select the instance type for you if you choose one of the following:  
+  `default_x86_64` to choose x86 based instance types (from the `m6i`, `c6i`, `r6i`, and `c7i` instance families) that matches the resource demands of the job queue.
+  `default_arm64` to choose ARM based instance types (from the `m6g`, `c6g`, `r6g`, and `c7g` instance families) that matches the resource demands of the job queue.
+  `optimal` Semantically equivalent to `default_x86_64`, see [Optimal instance type configuration to receive automatic instance family updates](https://docs.aws.amazon.com/batch/latest/userguide/optimal-default-instance-troubleshooting.html) for details.
Instance family availability varies by AWS Region. For example, some AWS Regions may not have any fourth generation instance families but have fifth and sixth generation instance families.  
When using `default_x86_64` or `default_arm64` instance bundles, AWS Batch selects instance families based on a balance of cost-effectiveness and performance. While newer generation instances often provide better price-performance, AWS Batch may choose an earlier generation instance family if it provides the optimal combination of availability, cost, and performance for your workload. For example, in an AWS Region where both c6i and c7i instances are available, AWS Batch might select c6i instances if they offer better cost-effectiveness for your specific job requirements. For more information on AWS Batch instance types and AWS Region availability, see [Instance type compute table](https://docs.aws.amazon.com/batch/latest/userguide/instance-type-compute-table.html) in the * AWS Batch User Guide*.  
 AWS Batch periodically updates your instances in default bundles to newer, more cost-effective options. Updates happen automatically without requiring any action from you. Your workloads continue running during updates with no interruption 
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment.
Type: Array of strings  
Required: No

 ** launchTemplate **   <a name="Batch-Type-ComputeResource-launchTemplate"></a>
The launch template to use for your compute resources. Any other compute resource parameters that you specify in a [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see [Launch template support](https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html) in the * AWS Batch User Guide*.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object  
Required: No

 ** minvCpus **   <a name="Batch-Type-ComputeResource-minvCpus"></a>
The minimum number of vCPUs that a compute environment should maintain (even if the compute environment is `DISABLED`).  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: Integer  
Required: No

 ** placementGroup **   <a name="Batch-Type-ComputeResource-placementGroup"></a>
The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide for Linux Instances*.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: String  
Required: No

 ** scalingPolicy **   <a name="Batch-Type-ComputeResource-scalingPolicy"></a>
The scaling policy configuration for the compute environment.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: [ComputeScalingPolicy](API_ComputeScalingPolicy.md) object  
Required: No

 ** securityGroupIds **   <a name="Batch-Type-ComputeResource-securityGroupIds"></a>
The Amazon EC2 security groups that are associated with instances launched in the compute environment. One or more security groups must be specified, either in `securityGroupIds` or using a launch template referenced in `launchTemplate`. This parameter is required for jobs that are running on Fargate resources and must contain at least one security group. Fargate doesn't support launch templates. If security groups are specified using both `securityGroupIds` and `launchTemplate`, the values in `securityGroupIds` are used.  
Type: Array of strings  
Required: No

 ** spotIamFleetRole **   <a name="Batch-Type-ComputeResource-spotIamFleetRole"></a>
The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a `SPOT` compute environment. This role is required if the allocation strategy set to `BEST_FIT` or if the allocation strategy isn't specified. For more information, see [Amazon EC2 spot fleet role](https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html) in the * AWS Batch User Guide*.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
To tag your Spot Instances on creation, the Spot Fleet IAM role specified here must use the newer **AmazonEC2SpotFleetTaggingRole** managed policy. The previously recommended **AmazonEC2SpotFleetRole** managed policy doesn't have the required permissions to tag Spot Instances. For more information, see [Spot instances not tagged on creation](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#spot-instance-no-tag) in the * AWS Batch User Guide*.
Type: String  
Required: No

 ** subnets **   <a name="Batch-Type-ComputeResource-subnets"></a>
The VPC subnets where the compute resources are launched. These subnets must be within the same VPC. Fargate compute resources can contain up to 16 subnets. For more information, see [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) in the *Amazon VPC User Guide*. This parameter is required for compute environments using `EC2`, `SPOT`, `FARGATE`, or `FARGATE_SPOT` compute resources.  
 AWS Batch on Amazon EC2 and AWS Batch on Amazon EKS support Local Zones. For more information, see [ Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones) in the *Amazon EC2 User Guide for Linux Instances*, [Amazon EKS and AWS Local Zones](https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html) in the *Amazon EKS User Guide* and [ Amazon ECS clusters in Local Zones, Wavelength Zones, and AWS Outposts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html#clusters-local-zones) in the *Amazon ECS Developer Guide*.  
 AWS Batch on Fargate doesn't currently support Local Zones.
Type: Array of strings  
Required: No

 ** tags **   <a name="Batch-Type-ComputeResource-tags"></a>
Key-value pair tags to be applied to Amazon EC2 resources that are launched in the compute environment. For AWS Batch, these take the form of `"String1": "String2"`, where `String1` is the tag key and `String2` is the tag value (for example, `{ "Name": "Batch Instance - C4OnDemand" }`). This is helpful for recognizing your AWS Batch instances in the Amazon EC2 console. Updating these tags requires an infrastructure update to the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*. These tags aren't seen when using the AWS Batch `ListTagsForResource` API operation.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
Type: String to string map  
Required: No

## See Also
<a name="API_ComputeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ComputeResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ComputeResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ComputeResource) 