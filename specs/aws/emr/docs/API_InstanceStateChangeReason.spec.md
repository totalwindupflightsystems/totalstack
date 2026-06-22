---
id: "@specs/aws/emr/docs/API_InstanceStateChangeReason"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceStateChangeReason"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceStateChangeReason

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceStateChangeReason
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceStateChangeReason
<a name="API_InstanceStateChangeReason"></a>

The details of the status change reason for the instance.

## Contents
<a name="API_InstanceStateChangeReason_Contents"></a>

 ** Code **   <a name="EMR-Type-InstanceStateChangeReason-Code"></a>
The programmable code for the state change reason.  
Type: String  
Valid Values: `INTERNAL_ERROR | VALIDATION_ERROR | INSTANCE_FAILURE | BOOTSTRAP_FAILURE | CLUSTER_TERMINATED`   
Required: No

 ** Message **   <a name="EMR-Type-InstanceStateChangeReason-Message"></a>
The status change reason description.  
Type: String  
Required: No

## See Also
<a name="API_InstanceStateChangeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceStateChangeReason) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceStateChangeReason) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceStateChangeReason) 