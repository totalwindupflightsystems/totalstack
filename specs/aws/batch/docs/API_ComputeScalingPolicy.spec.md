---
id: "@specs/aws/batch/docs/API_ComputeScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ComputeScalingPolicy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ComputeScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ComputeScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ComputeScalingPolicy
<a name="API_ComputeScalingPolicy"></a>

An object that represents a scaling policy for a compute environment.

## Contents
<a name="API_ComputeScalingPolicy_Contents"></a>

 ** minScaleDownDelayMinutes **   <a name="Batch-Type-ComputeScalingPolicy-minScaleDownDelayMinutes"></a>
The minimum time (in minutes) that AWS Batch keeps instances running in the compute environment after their jobs complete. For each instance, the delay period begins when the last job finishes. If no new jobs are placed on the instance during this delay, AWS Batch terminates the instance once the delay expires.  
Valid Range: Minimum value of 20. Maximum value of 10080. Use 0 to unset and disable the scale down delay.  
Idle instances retained during the scale-down delay period are billable at standard EC2 pricing.
The scale down delay does not apply to:  
+ Instances being replaced during infrastructure updates
+ Newly launched instances that have not yet run any jobs
+ Spot instances reclaimed due to interruption
Type: Integer  
Required: No

## See Also
<a name="API_ComputeScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ComputeScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ComputeScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ComputeScalingPolicy) 