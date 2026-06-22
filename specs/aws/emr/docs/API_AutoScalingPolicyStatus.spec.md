---
id: "@specs/aws/emr/docs/API_AutoScalingPolicyStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutoScalingPolicyStatus"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# AutoScalingPolicyStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_AutoScalingPolicyStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutoScalingPolicyStatus
<a name="API_AutoScalingPolicyStatus"></a>

The status of an automatic scaling policy. 

## Contents
<a name="API_AutoScalingPolicyStatus_Contents"></a>

 ** State **   <a name="EMR-Type-AutoScalingPolicyStatus-State"></a>
Indicates the status of the automatic scaling policy.  
Type: String  
Valid Values: `PENDING | ATTACHING | ATTACHED | DETACHING | DETACHED | FAILED`   
Required: No

 ** StateChangeReason **   <a name="EMR-Type-AutoScalingPolicyStatus-StateChangeReason"></a>
The reason for a change in status.  
Type: [AutoScalingPolicyStateChangeReason](API_AutoScalingPolicyStateChangeReason.md) object  
Required: No

## See Also
<a name="API_AutoScalingPolicyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AutoScalingPolicyStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AutoScalingPolicyStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AutoScalingPolicyStatus) 