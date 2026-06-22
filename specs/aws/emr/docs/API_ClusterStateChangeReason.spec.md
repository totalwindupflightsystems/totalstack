---
id: "@specs/aws/emr/docs/API_ClusterStateChangeReason"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterStateChangeReason"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ClusterStateChangeReason

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ClusterStateChangeReason
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterStateChangeReason
<a name="API_ClusterStateChangeReason"></a>

The reason that the cluster changed to its current state.

## Contents
<a name="API_ClusterStateChangeReason_Contents"></a>

 ** Code **   <a name="EMR-Type-ClusterStateChangeReason-Code"></a>
The programmatic code for the state change reason.  
Type: String  
Valid Values: `INTERNAL_ERROR | VALIDATION_ERROR | INSTANCE_FAILURE | INSTANCE_FLEET_TIMEOUT | BOOTSTRAP_FAILURE | USER_REQUEST | STEP_FAILURE | ALL_STEPS_COMPLETED`   
Required: No

 ** Message **   <a name="EMR-Type-ClusterStateChangeReason-Message"></a>
The descriptive message for the state change reason.  
Type: String  
Required: No

## See Also
<a name="API_ClusterStateChangeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ClusterStateChangeReason) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ClusterStateChangeReason) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ClusterStateChangeReason) 