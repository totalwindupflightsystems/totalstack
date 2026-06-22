---
id: "@specs/aws/emr/docs/API_ClusterSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterSummary"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ClusterSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ClusterSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterSummary
<a name="API_ClusterSummary"></a>

The summary description of the cluster.

## Contents
<a name="API_ClusterSummary_Contents"></a>

 ** ClusterArn **   <a name="EMR-Type-ClusterSummary-ClusterArn"></a>
The Amazon Resource Name of the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** Id **   <a name="EMR-Type-ClusterSummary-Id"></a>
The unique identifier for the cluster.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** Name **   <a name="EMR-Type-ClusterSummary-Name"></a>
The name of the cluster.  
Type: String  
Required: No

 ** NormalizedInstanceHours **   <a name="EMR-Type-ClusterSummary-NormalizedInstanceHours"></a>
An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.  
Type: Integer  
Required: No

 ** OutpostArn **   <a name="EMR-Type-ClusterSummary-OutpostArn"></a>
 The Amazon Resource Name (ARN) of the Outpost where the cluster is launched.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** Status **   <a name="EMR-Type-ClusterSummary-Status"></a>
The details about the current status of the cluster.  
Type: [ClusterStatus](API_ClusterStatus.md) object  
Required: No

## See Also
<a name="API_ClusterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ClusterSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ClusterSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ClusterSummary) 