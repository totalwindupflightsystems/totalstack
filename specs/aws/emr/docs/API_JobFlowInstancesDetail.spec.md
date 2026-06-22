---
id: "@specs/aws/emr/docs/API_JobFlowInstancesDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobFlowInstancesDetail"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# JobFlowInstancesDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_JobFlowInstancesDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobFlowInstancesDetail
<a name="API_JobFlowInstancesDetail"></a>

Specify the type of Amazon EC2 instances that the cluster (job flow) runs on.

## Contents
<a name="API_JobFlowInstancesDetail_Contents"></a>

 ** InstanceCount **   <a name="EMR-Type-JobFlowInstancesDetail-InstanceCount"></a>
The number of Amazon EC2 instances in the cluster. If the value is 1, the same instance serves as both the master and core and task node. If the value is greater than 1, one instance is the master node and all others are core and task nodes.  
Type: Integer  
Required: Yes

 ** MasterInstanceType **   <a name="EMR-Type-JobFlowInstancesDetail-MasterInstanceType"></a>
The Amazon EC2 master node instance type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** SlaveInstanceType **   <a name="EMR-Type-JobFlowInstancesDetail-SlaveInstanceType"></a>
The Amazon EC2 core and task node instance type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** Ec2KeyName **   <a name="EMR-Type-JobFlowInstancesDetail-Ec2KeyName"></a>
The name of an Amazon EC2 key pair that can be used to connect to the master node using SSH.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Ec2SubnetId **   <a name="EMR-Type-JobFlowInstancesDetail-Ec2SubnetId"></a>
For clusters launched within Amazon Virtual Private Cloud, this is the identifier of the subnet where the cluster was launched.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** HadoopVersion **   <a name="EMR-Type-JobFlowInstancesDetail-HadoopVersion"></a>
The Hadoop version for the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** InstanceGroups **   <a name="EMR-Type-JobFlowInstancesDetail-InstanceGroups"></a>
Details about the instance groups in a cluster.  
Type: Array of [InstanceGroupDetail](API_InstanceGroupDetail.md) objects  
Required: No

 ** KeepJobFlowAliveWhenNoSteps **   <a name="EMR-Type-JobFlowInstancesDetail-KeepJobFlowAliveWhenNoSteps"></a>
Specifies whether the cluster should remain available after completing all steps.  
Type: Boolean  
Required: No

 ** MasterInstanceId **   <a name="EMR-Type-JobFlowInstancesDetail-MasterInstanceId"></a>
The Amazon EC2 instance identifier of the master node.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** MasterPublicDnsName **   <a name="EMR-Type-JobFlowInstancesDetail-MasterPublicDnsName"></a>
The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NormalizedInstanceHours **   <a name="EMR-Type-JobFlowInstancesDetail-NormalizedInstanceHours"></a>
An approximation of the cost of the cluster, represented in m1.small/hours. This value is increased one time for every hour that an m1.small instance runs. Larger instances are weighted more heavily, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being increased incrementally four times. This result is only an approximation and does not reflect the actual billing rate.  
Type: Integer  
Required: No

 ** Placement **   <a name="EMR-Type-JobFlowInstancesDetail-Placement"></a>
The Amazon EC2 Availability Zone for the cluster.  
Type: [PlacementType](API_PlacementType.md) object  
Required: No

 ** TerminationProtected **   <a name="EMR-Type-JobFlowInstancesDetail-TerminationProtected"></a>
Specifies whether the Amazon EC2 instances in the cluster are protected from termination by API calls, user intervention, or in the event of a job-flow error.  
Type: Boolean  
Required: No

 ** UnhealthyNodeReplacement **   <a name="EMR-Type-JobFlowInstancesDetail-UnhealthyNodeReplacement"></a>
Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.  
Type: Boolean  
Required: No

## See Also
<a name="API_JobFlowInstancesDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/JobFlowInstancesDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/JobFlowInstancesDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/JobFlowInstancesDetail) 