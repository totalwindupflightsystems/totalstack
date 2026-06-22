---
id: "@specs/aws/emr/docs/API_ScalingRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScalingRule"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ScalingRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ScalingRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScalingRule
<a name="API_ScalingRule"></a>

A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how Amazon EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

## Contents
<a name="API_ScalingRule_Contents"></a>

 ** Action **   <a name="EMR-Type-ScalingRule-Action"></a>
The conditions that trigger an automatic scaling activity.  
Type: [ScalingAction](API_ScalingAction.md) object  
Required: Yes

 ** Name **   <a name="EMR-Type-ScalingRule-Name"></a>
The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.  
Type: String  
Required: Yes

 ** Trigger **   <a name="EMR-Type-ScalingRule-Trigger"></a>
The CloudWatch alarm definition that determines when automatic scaling activity is triggered.  
Type: [ScalingTrigger](API_ScalingTrigger.md) object  
Required: Yes

 ** Description **   <a name="EMR-Type-ScalingRule-Description"></a>
A friendly, more verbose description of the automatic scaling rule.  
Type: String  
Required: No

## See Also
<a name="API_ScalingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScalingRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScalingRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScalingRule) 