---
id: "@specs/aws/emr/docs/API_SimpleScalingPolicyConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SimpleScalingPolicyConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SimpleScalingPolicyConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SimpleScalingPolicyConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SimpleScalingPolicyConfiguration
<a name="API_SimpleScalingPolicyConfiguration"></a>

An automatic scaling configuration, which describes how the policy adds or removes instances, the cooldown period, and the number of Amazon EC2 instances that will be added each time the CloudWatch metric alarm condition is satisfied.

## Contents
<a name="API_SimpleScalingPolicyConfiguration_Contents"></a>

 ** ScalingAdjustment **   <a name="EMR-Type-SimpleScalingPolicyConfiguration-ScalingAdjustment"></a>
The amount by which to scale in or scale out, based on the specified `AdjustmentType`. A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If `AdjustmentType` is set to `EXACT_CAPACITY`, the number should only be a positive integer. If `AdjustmentType` is set to `PERCENT_CHANGE_IN_CAPACITY`, the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.  
Type: Integer  
Required: Yes

 ** AdjustmentType **   <a name="EMR-Type-SimpleScalingPolicyConfiguration-AdjustmentType"></a>
The way in which Amazon EC2 instances are added (if `ScalingAdjustment` is a positive number) or terminated (if `ScalingAdjustment` is a negative number) each time the scaling activity is triggered. `CHANGE_IN_CAPACITY` is the default. `CHANGE_IN_CAPACITY` indicates that the Amazon EC2 instance count increments or decrements by `ScalingAdjustment`, which should be expressed as an integer. `PERCENT_CHANGE_IN_CAPACITY` indicates the instance count increments or decrements by the percentage specified by `ScalingAdjustment`, which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. `EXACT_CAPACITY` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by `ScalingAdjustment`, which should be expressed as a positive integer.  
Type: String  
Valid Values: `CHANGE_IN_CAPACITY | PERCENT_CHANGE_IN_CAPACITY | EXACT_CAPACITY`   
Required: No

 ** CoolDown **   <a name="EMR-Type-SimpleScalingPolicyConfiguration-CoolDown"></a>
The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.  
Type: Integer  
Required: No

## See Also
<a name="API_SimpleScalingPolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SimpleScalingPolicyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SimpleScalingPolicyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SimpleScalingPolicyConfiguration) 