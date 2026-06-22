---
id: "@specs/aws/emr/docs/API_SpotProvisioningSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SpotProvisioningSpecification"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SpotProvisioningSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SpotProvisioningSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SpotProvisioningSpecification
<a name="API_SpotProvisioningSpecification"></a>

The launch specification for Spot Instances in the instance fleet, which determines the defined duration, provisioning timeout behavior, and allocation strategy.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. Spot Instance allocation strategy is available in Amazon EMR releases 5.12.1 and later.

**Note**  
Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022. 

## Contents
<a name="API_SpotProvisioningSpecification_Contents"></a>

 ** TimeoutAction **   <a name="EMR-Type-SpotProvisioningSpecification-TimeoutAction"></a>
The action to take when `TargetSpotCapacity` has not been fulfilled when the `TimeoutDurationMinutes` has expired; that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are `TERMINATE_CLUSTER` and `SWITCH_TO_ON_DEMAND`. SWITCH\_TO\_ON\_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.  
Type: String  
Valid Values: `SWITCH_TO_ON_DEMAND | TERMINATE_CLUSTER`   
Required: Yes

 ** TimeoutDurationMinutes **   <a name="EMR-Type-SpotProvisioningSpecification-TimeoutDurationMinutes"></a>
The Spot provisioning timeout period in minutes. If Spot Instances are not provisioned within this time period, the `TimeOutAction` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** AllocationStrategy **   <a name="EMR-Type-SpotProvisioningSpecification-AllocationStrategy"></a>
Specifies one of the following strategies to launch Spot Instance fleets: `capacity-optimized`, `price-capacity-optimized`, `lowest-price`, or `diversified`, and `capacity-optimized-prioritized`. For more information on the provisioning strategies, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html) in the *Amazon EC2 User Guide for Linux Instances*.  
When you launch a Spot Instance fleet with the old console, it automatically launches with the `capacity-optimized` strategy. You can't change the allocation strategy from the old console.
Type: String  
Valid Values: `capacity-optimized | price-capacity-optimized | lowest-price | diversified | capacity-optimized-prioritized`   
Required: No

 ** BlockDurationMinutes **   <a name="EMR-Type-SpotProvisioningSpecification-BlockDurationMinutes"></a>
The defined duration for Spot Instances (also known as Spot blocks) in minutes. When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates.   
Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022. 
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_SpotProvisioningSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SpotProvisioningSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SpotProvisioningSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SpotProvisioningSpecification) 