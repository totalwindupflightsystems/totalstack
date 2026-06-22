---
id: "@specs/aws/emr/docs/API_ScalingAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScalingAction"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ScalingAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ScalingAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScalingAction
<a name="API_ScalingAction"></a>

The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

## Contents
<a name="API_ScalingAction_Contents"></a>

 ** SimpleScalingPolicyConfiguration **   <a name="EMR-Type-ScalingAction-SimpleScalingPolicyConfiguration"></a>
The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.  
Type: [SimpleScalingPolicyConfiguration](API_SimpleScalingPolicyConfiguration.md) object  
Required: Yes

 ** Market **   <a name="EMR-Type-ScalingAction-Market"></a>
Not available for instance groups. Instance groups use the market type specified for the group.  
Type: String  
Valid Values: `ON_DEMAND | SPOT`   
Required: No

## See Also
<a name="API_ScalingAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScalingAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScalingAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScalingAction) 