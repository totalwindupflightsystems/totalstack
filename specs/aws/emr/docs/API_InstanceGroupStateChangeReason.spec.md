---
id: "@specs/aws/emr/docs/API_InstanceGroupStateChangeReason"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceGroupStateChangeReason"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceGroupStateChangeReason

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceGroupStateChangeReason
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceGroupStateChangeReason
<a name="API_InstanceGroupStateChangeReason"></a>

The status change reason details for the instance group.

## Contents
<a name="API_InstanceGroupStateChangeReason_Contents"></a>

 ** Code **   <a name="EMR-Type-InstanceGroupStateChangeReason-Code"></a>
The programmable code for the state change reason.  
Type: String  
Valid Values: `INTERNAL_ERROR | VALIDATION_ERROR | INSTANCE_FAILURE | CLUSTER_TERMINATED`   
Required: No

 ** Message **   <a name="EMR-Type-InstanceGroupStateChangeReason-Message"></a>
The status change reason description.  
Type: String  
Required: No

## See Also
<a name="API_InstanceGroupStateChangeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroupStateChangeReason) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroupStateChangeReason) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroupStateChangeReason) 