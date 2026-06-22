---
id: "@specs/aws/eks/docs/API_WarmPoolConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WarmPoolConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# WarmPoolConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_WarmPoolConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WarmPoolConfig
<a name="API_WarmPoolConfig"></a>

The configuration for an Amazon EC2 Auto Scaling warm pool attached to an Amazon EKS managed node group. Warm pools maintain pre-initialized EC2 instances alongside your Auto Scaling group that have already completed the bootup initialization process and can be kept in a `Stopped`, `Running`, or `Hibernated` state.

## Contents
<a name="API_WarmPoolConfig_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-WarmPoolConfig-enabled"></a>
Specifies whether to attach warm pools on the managed node group. Set to `true` to enable the warm pool, or `false` to disable and remove it. If not specified during an update, the current value is preserved.  
Type: Boolean  
Required: No

 ** maxGroupPreparedCapacity **   <a name="AmazonEKS-Type-WarmPoolConfig-maxGroupPreparedCapacity"></a>
The maximum total number of instances across the warm pool and Auto Scaling group combined. This value controls the total prepared capacity available for your node group.  
Type: Integer  
Required: No

 ** minSize **   <a name="AmazonEKS-Type-WarmPoolConfig-minSize"></a>
The minimum number of instances to maintain in the warm pool. Default: `0`. Size your warm pool based on scaling patterns to balance cost and availability. Start with 10-20% of expected peak capacity.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** poolState **   <a name="AmazonEKS-Type-WarmPoolConfig-poolState"></a>
The desired state for warm pool instances. Default: `Stopped`. Valid values are `Stopped` (most cost-effective with EBS storage costs only), `Running` (fastest transition time with full EC2 costs), and `Hibernated` (balance between cost and speed, only supported on specific instance types). Warm pool instances in the `Hibernated` state are not supported with Bottlerocket AMIs.  
Type: String  
Valid Values: `STOPPED | RUNNING | HIBERNATED`   
Required: No

 ** reuseOnScaleIn **   <a name="AmazonEKS-Type-WarmPoolConfig-reuseOnScaleIn"></a>
Indicates whether instances should return to the warm pool during scale-in events instead of being terminated. Default: `false`. Enable this to reduce costs by reusing instances. This feature is not supported for Bottlerocket AMIs.  
Type: Boolean  
Required: No

## See Also
<a name="API_WarmPoolConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/WarmPoolConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/WarmPoolConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/WarmPoolConfig) 