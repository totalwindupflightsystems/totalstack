---
id: "@specs/aws/emr/docs/API_InstanceGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceGroup"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceGroup
<a name="API_InstanceGroup"></a>

This entity represents an instance group, which is a group of instances that have common purpose. For example, CORE instance group is used for HDFS.

## Contents
<a name="API_InstanceGroup_Contents"></a>

 ** AutoScalingPolicy **   <a name="EMR-Type-InstanceGroup-AutoScalingPolicy"></a>
An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy.  
Type: [AutoScalingPolicyDescription](API_AutoScalingPolicyDescription.md) object  
Required: No

 ** BidPrice **   <a name="EMR-Type-InstanceGroup-BidPrice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.  
Type: String  
Required: No

 ** Configurations **   <a name="EMR-Type-InstanceGroup-Configurations"></a>
Amazon EMR releases 4.x or later.
The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** ConfigurationsVersion **   <a name="EMR-Type-InstanceGroup-ConfigurationsVersion"></a>
The version number of the requested configuration specification for this instance group.  
Type: Long  
Required: No

 ** CustomAmiId **   <a name="EMR-Type-InstanceGroup-CustomAmiId"></a>
The custom AMI ID to use for the provisioned instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EbsBlockDevices **   <a name="EMR-Type-InstanceGroup-EbsBlockDevices"></a>
The EBS block devices that are mapped to this instance group.  
Type: Array of [EbsBlockDevice](API_EbsBlockDevice.md) objects  
Required: No

 ** EbsOptimized **   <a name="EMR-Type-InstanceGroup-EbsOptimized"></a>
If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O.  
Type: Boolean  
Required: No

 ** Id **   <a name="EMR-Type-InstanceGroup-Id"></a>
The identifier of the instance group.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** InstanceGroupType **   <a name="EMR-Type-InstanceGroup-InstanceGroupType"></a>
The type of the instance group. Valid values are MASTER, CORE or TASK.  
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: No

 ** InstanceType **   <a name="EMR-Type-InstanceGroup-InstanceType"></a>
The Amazon EC2 instance type for all instances in the instance group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LastSuccessfullyAppliedConfigurations **   <a name="EMR-Type-InstanceGroup-LastSuccessfullyAppliedConfigurations"></a>
A list of configurations that were successfully applied for an instance group last time.  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** LastSuccessfullyAppliedConfigurationsVersion **   <a name="EMR-Type-InstanceGroup-LastSuccessfullyAppliedConfigurationsVersion"></a>
The version number of a configuration specification that was successfully applied for an instance group last time.   
Type: Long  
Required: No

 ** Market **   <a name="EMR-Type-InstanceGroup-Market"></a>
The marketplace to provision instances for this group. Valid values are ON\_DEMAND or SPOT.  
Type: String  
Valid Values: `ON_DEMAND | SPOT`   
Required: No

 ** Name **   <a name="EMR-Type-InstanceGroup-Name"></a>
The name of the instance group.  
Type: String  
Required: No

 ** RequestedInstanceCount **   <a name="EMR-Type-InstanceGroup-RequestedInstanceCount"></a>
The target number of instances for the instance group.  
Type: Integer  
Required: No

 ** RunningInstanceCount **   <a name="EMR-Type-InstanceGroup-RunningInstanceCount"></a>
The number of instances currently running in this instance group.  
Type: Integer  
Required: No

 ** ShrinkPolicy **   <a name="EMR-Type-InstanceGroup-ShrinkPolicy"></a>
Policy for customizing shrink operations.  
Type: [ShrinkPolicy](API_ShrinkPolicy.md) object  
Required: No

 ** Status **   <a name="EMR-Type-InstanceGroup-Status"></a>
The current status of the instance group.  
Type: [InstanceGroupStatus](API_InstanceGroupStatus.md) object  
Required: No

## See Also
<a name="API_InstanceGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroup) 