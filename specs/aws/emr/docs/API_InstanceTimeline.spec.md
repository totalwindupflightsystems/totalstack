---
id: "@specs/aws/emr/docs/API_InstanceTimeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceTimeline"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceTimeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceTimeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceTimeline
<a name="API_InstanceTimeline"></a>

The timeline of the instance lifecycle.

## Contents
<a name="API_InstanceTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-InstanceTimeline-CreationDateTime"></a>
The creation date and time of the instance.  
Type: Timestamp  
Required: No

 ** EndDateTime **   <a name="EMR-Type-InstanceTimeline-EndDateTime"></a>
The date and time when the instance was terminated.  
Type: Timestamp  
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-InstanceTimeline-ReadyDateTime"></a>
The date and time when the instance was ready to perform tasks.  
Type: Timestamp  
Required: No

## See Also
<a name="API_InstanceTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceTimeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceTimeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceTimeline) 