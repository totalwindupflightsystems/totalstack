---
id: "@specs/aws/emr/docs/API_ScalingTrigger"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScalingTrigger"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ScalingTrigger

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ScalingTrigger
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScalingTrigger
<a name="API_ScalingTrigger"></a>

The conditions that trigger an automatic scaling activity.

## Contents
<a name="API_ScalingTrigger_Contents"></a>

 ** CloudWatchAlarmDefinition **   <a name="EMR-Type-ScalingTrigger-CloudWatchAlarmDefinition"></a>
The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.  
Type: [CloudWatchAlarmDefinition](API_CloudWatchAlarmDefinition.md) object  
Required: Yes

## See Also
<a name="API_ScalingTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScalingTrigger) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScalingTrigger) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScalingTrigger) 