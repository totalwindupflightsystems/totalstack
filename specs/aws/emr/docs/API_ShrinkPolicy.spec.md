---
id: "@specs/aws/emr/docs/API_ShrinkPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ShrinkPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ShrinkPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ShrinkPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ShrinkPolicy
<a name="API_ShrinkPolicy"></a>

Policy for customizing shrink operations. Allows configuration of decommissioning timeout and targeted instance shrinking.

## Contents
<a name="API_ShrinkPolicy_Contents"></a>

 ** DecommissionTimeout **   <a name="EMR-Type-ShrinkPolicy-DecommissionTimeout"></a>
The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.  
Type: Integer  
Required: No

 ** InstanceResizePolicy **   <a name="EMR-Type-ShrinkPolicy-InstanceResizePolicy"></a>
Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.  
Type: [InstanceResizePolicy](API_InstanceResizePolicy.md) object  
Required: No

## See Also
<a name="API_ShrinkPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ShrinkPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ShrinkPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ShrinkPolicy) 