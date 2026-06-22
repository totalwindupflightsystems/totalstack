---
id: "@specs/aws/emr/docs/API_InstanceGroupTimeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceGroupTimeline"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceGroupTimeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceGroupTimeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceGroupTimeline
<a name="API_InstanceGroupTimeline"></a>

The timeline of the instance group lifecycle.

## Contents
<a name="API_InstanceGroupTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-InstanceGroupTimeline-CreationDateTime"></a>
The creation date and time of the instance group.  
Type: Timestamp  
Required: No

 ** EndDateTime **   <a name="EMR-Type-InstanceGroupTimeline-EndDateTime"></a>
The date and time when the instance group terminated.  
Type: Timestamp  
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-InstanceGroupTimeline-ReadyDateTime"></a>
The date and time when the instance group became ready to perform tasks.  
Type: Timestamp  
Required: No

## See Also
<a name="API_InstanceGroupTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroupTimeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroupTimeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroupTimeline) 