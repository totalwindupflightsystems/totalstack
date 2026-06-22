---
id: "@specs/aws/emr/docs/API_ManagedScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ManagedScalingPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ManagedScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ManagedScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ManagedScalingPolicy
<a name="API_ManagedScalingPolicy"></a>

 Managed scaling policy for an Amazon EMR cluster. The policy specifies the limits for resources that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration. 

## Contents
<a name="API_ManagedScalingPolicy_Contents"></a>

 ** ComputeLimits **   <a name="EMR-Type-ManagedScalingPolicy-ComputeLimits"></a>
The Amazon EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.  
Type: [ComputeLimits](API_ComputeLimits.md) object  
Required: No

 ** ScalingStrategy **   <a name="EMR-Type-ManagedScalingPolicy-ScalingStrategy"></a>
Determines whether a custom scaling utilization performance index can be set. Possible values include *ADVANCED* or *DEFAULT*.  
Type: String  
Valid Values: `DEFAULT | ADVANCED`   
Required: No

 ** UtilizationPerformanceIndex **   <a name="EMR-Type-ManagedScalingPolicy-UtilizationPerformanceIndex"></a>
An integer value that represents an advanced scaling strategy. Setting a higher value optimizes for performance. Setting a lower value optimizes for resource conservation. Setting the value to 50 balances performance and resource conservation. Possible values are 1, 25, 50, 75, and 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_ManagedScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ManagedScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ManagedScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ManagedScalingPolicy) 