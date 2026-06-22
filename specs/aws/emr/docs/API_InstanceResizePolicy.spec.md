---
id: "@specs/aws/emr/docs/API_InstanceResizePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceResizePolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceResizePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceResizePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceResizePolicy
<a name="API_InstanceResizePolicy"></a>

Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.

## Contents
<a name="API_InstanceResizePolicy_Contents"></a>

 ** InstancesToProtect **   <a name="EMR-Type-InstanceResizePolicy-InstancesToProtect"></a>
Specific list of instances to be protected when shrinking an instance group.  
Type: Array of strings  
Required: No

 ** InstancesToTerminate **   <a name="EMR-Type-InstanceResizePolicy-InstancesToTerminate"></a>
Specific list of instances to be terminated when shrinking an instance group.  
Type: Array of strings  
Required: No

 ** InstanceTerminationTimeout **   <a name="EMR-Type-InstanceResizePolicy-InstanceTerminationTimeout"></a>
Decommissioning timeout override for the specific list of instances to be terminated.  
Type: Integer  
Required: No

## See Also
<a name="API_InstanceResizePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceResizePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceResizePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceResizePolicy) 