---
id: "@specs/aws/emr/docs/API_InstanceFleet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleet"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleet
<a name="API_InstanceFleet"></a>

Describes an instance fleet, which is a group of Amazon EC2 instances that host a particular node type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix of instance types and On-Demand and Spot Instances, which are provisioned to meet a defined target capacity. 

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleet_Contents"></a>

 ** Context **   <a name="EMR-Type-InstanceFleet-Context"></a>
Reserved.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Id **   <a name="EMR-Type-InstanceFleet-Id"></a>
The unique identifier of the instance fleet.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** InstanceFleetType **   <a name="EMR-Type-InstanceFleet-InstanceFleetType"></a>
The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.   
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: No

 ** InstanceTypeSpecifications **   <a name="EMR-Type-InstanceFleet-InstanceTypeSpecifications"></a>
An array of specifications for the instance types that comprise an instance fleet.  
Type: Array of [InstanceTypeSpecification](API_InstanceTypeSpecification.md) objects  
Required: No

 ** LaunchSpecifications **   <a name="EMR-Type-InstanceFleet-LaunchSpecifications"></a>
Describes the launch specification for an instance fleet.   
Type: [InstanceFleetProvisioningSpecifications](API_InstanceFleetProvisioningSpecifications.md) object  
Required: No

 ** Name **   <a name="EMR-Type-InstanceFleet-Name"></a>
A friendly name for the instance fleet.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ProvisionedOnDemandCapacity **   <a name="EMR-Type-InstanceFleet-ProvisionedOnDemandCapacity"></a>
The number of On-Demand units that have been provisioned for the instance fleet to fulfill `TargetOnDemandCapacity`. This provisioned capacity might be less than or greater than `TargetOnDemandCapacity`.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** ProvisionedSpotCapacity **   <a name="EMR-Type-InstanceFleet-ProvisionedSpotCapacity"></a>
The number of Spot units that have been provisioned for this instance fleet to fulfill `TargetSpotCapacity`. This provisioned capacity might be less than or greater than `TargetSpotCapacity`.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** ResizeSpecifications **   <a name="EMR-Type-InstanceFleet-ResizeSpecifications"></a>
The resize specification for the instance fleet.  
Type: [InstanceFleetResizingSpecifications](API_InstanceFleetResizingSpecifications.md) object  
Required: No

 ** Status **   <a name="EMR-Type-InstanceFleet-Status"></a>
The current status of the instance fleet.   
Type: [InstanceFleetStatus](API_InstanceFleetStatus.md) object  
Required: No

 ** TargetOnDemandCapacity **   <a name="EMR-Type-InstanceFleet-TargetOnDemandCapacity"></a>
The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand Instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand Instances as specified by [InstanceTypeConfig](API_InstanceTypeConfig.md). Each instance configuration has a specified `WeightedCapacity`. When an On-Demand Instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use [InstanceFleet:ProvisionedOnDemandCapacity](#EMR-Type-InstanceFleet-ProvisionedOnDemandCapacity) to determine the Spot capacity units that have been provisioned for the instance fleet.  
If not specified or set to 0, only Spot Instances are provisioned for the instance fleet using `TargetSpotCapacity`. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** TargetSpotCapacity **   <a name="EMR-Type-InstanceFleet-TargetSpotCapacity"></a>
The target capacity of Spot units for the instance fleet, which determines how many Spot Instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot Instances as specified by [InstanceTypeConfig](API_InstanceTypeConfig.md). Each instance configuration has a specified `WeightedCapacity`. When a Spot instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use [InstanceFleet:ProvisionedSpotCapacity](#EMR-Type-InstanceFleet-ProvisionedSpotCapacity) to determine the Spot capacity units that have been provisioned for the instance fleet.  
If not specified or set to 0, only On-Demand Instances are provisioned for the instance fleet. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_InstanceFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleet) 