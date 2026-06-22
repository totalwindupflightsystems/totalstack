---
id: "@specs/aws/emr/docs/API_ClusterStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterStatus"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ClusterStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ClusterStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterStatus
<a name="API_ClusterStatus"></a>

The detailed status of the cluster.

## Contents
<a name="API_ClusterStatus_Contents"></a>

 ** ErrorDetails **   <a name="EMR-Type-ClusterStatus-ErrorDetails"></a>
A list of tuples that provides information about the errors that caused a cluster to terminate. This structure can contain up to 10 different `ErrorDetail` tuples.  
Type: Array of [ErrorDetail](API_ErrorDetail.md) objects  
Required: No

 ** State **   <a name="EMR-Type-ClusterStatus-State"></a>
The current state of the cluster.  
Type: String  
Valid Values: `STARTING | BOOTSTRAPPING | RUNNING | WAITING | TERMINATING | TERMINATED | TERMINATED_WITH_ERRORS`   
Required: No

 ** StateChangeReason **   <a name="EMR-Type-ClusterStatus-StateChangeReason"></a>
The reason for the cluster status change.  
Type: [ClusterStateChangeReason](API_ClusterStateChangeReason.md) object  
Required: No

 ** Timeline **   <a name="EMR-Type-ClusterStatus-Timeline"></a>
A timeline that represents the status of a cluster over the lifetime of the cluster.  
Type: [ClusterTimeline](API_ClusterTimeline.md) object  
Required: No

## See Also
<a name="API_ClusterStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ClusterStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ClusterStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ClusterStatus) 