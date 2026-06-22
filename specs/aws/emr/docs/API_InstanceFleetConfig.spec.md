---
id: "@specs/aws/emr/docs/API_InstanceFleetConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleetConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleetConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleetConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleetConfig
<a name="API_InstanceFleetConfig"></a>

The configuration that defines an instance fleet.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleetConfig_Contents"></a>

 ** InstanceFleetType **   <a name="EMR-Type-InstanceFleetConfig-InstanceFleetType"></a>
The node type that the instance fleet hosts. Valid values are MASTER, CORE, and TASK.  
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: Yes

 ** Context **   <a name="EMR-Type-InstanceFleetConfig-Context"></a>
Reserved.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** InstanceTypeConfigs **   <a name="EMR-Type-InstanceFleetConfig-InstanceTypeConfigs"></a>
The instance type configurations that define the Amazon EC2 instances in the instance fleet.  
Type: Array of [InstanceTypeConfig](API_InstanceTypeConfig.md) objects  
Required: No

 ** LaunchSpecifications **   <a name="EMR-Type-InstanceFleetConfig-LaunchSpecifications"></a>
The launch specification for the instance fleet.  
Type: [InstanceFleetProvisioningSpecifications](API_InstanceFleetProvisioningSpecifications.md) object  
Required: No

 ** Name **   <a name="EMR-Type-InstanceFleetConfig-Name"></a>
The friendly name of the instance fleet.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ResizeSpecifications **   <a name="EMR-Type-InstanceFleetConfig-ResizeSpecifications"></a>
The resize specification for the instance fleet.  
Type: [InstanceFleetResizingSpecifications](API_InstanceFleetResizingSpecifications.md) object  
Required: No

 ** TargetOnDemandCapacity **   <a name="EMR-Type-InstanceFleetConfig-TargetOnDemandCapacity"></a>
The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand Instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand Instances as specified by [InstanceTypeConfig](API_InstanceTypeConfig.md). Each instance configuration has a specified `WeightedCapacity`. When an On-Demand Instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.  
If not specified or set to 0, only Spot Instances are provisioned for the instance fleet using `TargetSpotCapacity`. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** TargetSpotCapacity **   <a name="EMR-Type-InstanceFleetConfig-TargetSpotCapacity"></a>
The target capacity of Spot units for the instance fleet, which determines how many Spot Instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot Instances as specified by [InstanceTypeConfig](API_InstanceTypeConfig.md). Each instance configuration has a specified `WeightedCapacity`. When a Spot Instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.  
If not specified or set to 0, only On-Demand Instances are provisioned for the instance fleet. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_InstanceFleetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetConfig) 