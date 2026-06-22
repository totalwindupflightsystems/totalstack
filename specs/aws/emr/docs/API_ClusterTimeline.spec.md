---
id: "@specs/aws/emr/docs/API_ClusterTimeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterTimeline"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ClusterTimeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ClusterTimeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterTimeline
<a name="API_ClusterTimeline"></a>

Represents the timeline of the cluster's lifecycle.

## Contents
<a name="API_ClusterTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-ClusterTimeline-CreationDateTime"></a>
The creation date and time of the cluster.  
Type: Timestamp  
Required: No

 ** EndDateTime **   <a name="EMR-Type-ClusterTimeline-EndDateTime"></a>
The date and time when the cluster was terminated.  
Type: Timestamp  
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-ClusterTimeline-ReadyDateTime"></a>
The date and time when the cluster was ready to run steps.  
Type: Timestamp  
Required: No

## See Also
<a name="API_ClusterTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ClusterTimeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ClusterTimeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ClusterTimeline) 