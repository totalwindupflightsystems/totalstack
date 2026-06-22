---
id: "@specs/aws/emr/docs/API_ScalingConstraints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScalingConstraints"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ScalingConstraints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ScalingConstraints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScalingConstraints
<a name="API_ScalingConstraints"></a>

The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activities triggered by automatic scaling rules will not cause an instance group to grow above or below these limits.

## Contents
<a name="API_ScalingConstraints_Contents"></a>

 ** MaxCapacity **   <a name="EMR-Type-ScalingConstraints-MaxCapacity"></a>
The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.  
Type: Integer  
Required: Yes

 ** MinCapacity **   <a name="EMR-Type-ScalingConstraints-MinCapacity"></a>
The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.  
Type: Integer  
Required: Yes

## See Also
<a name="API_ScalingConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScalingConstraints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScalingConstraints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScalingConstraints) 