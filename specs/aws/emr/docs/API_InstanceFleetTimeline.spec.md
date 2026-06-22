---
id: "@specs/aws/emr/docs/API_InstanceFleetTimeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleetTimeline"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleetTimeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleetTimeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleetTimeline
<a name="API_InstanceFleetTimeline"></a>

Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleetTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-InstanceFleetTimeline-CreationDateTime"></a>
The time and date the instance fleet was created.  
Type: Timestamp  
Required: No

 ** EndDateTime **   <a name="EMR-Type-InstanceFleetTimeline-EndDateTime"></a>
The time and date the instance fleet terminated.  
Type: Timestamp  
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-InstanceFleetTimeline-ReadyDateTime"></a>
The time and date the instance fleet was ready to run jobs.  
Type: Timestamp  
Required: No

## See Also
<a name="API_InstanceFleetTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetTimeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetTimeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetTimeline) 