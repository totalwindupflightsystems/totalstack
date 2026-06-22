---
id: "@specs/aws/eks/docs/API_InsightSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InsightSummary"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# InsightSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_InsightSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InsightSummary
<a name="API_InsightSummary"></a>

The summarized description of the insight.

## Contents
<a name="API_InsightSummary_Contents"></a>

 ** category **   <a name="AmazonEKS-Type-InsightSummary-category"></a>
The category of the insight.  
Type: String  
Valid Values: `UPGRADE_READINESS | MISCONFIGURATION`   
Required: No

 ** description **   <a name="AmazonEKS-Type-InsightSummary-description"></a>
The description of the insight which includes alert criteria, remediation recommendation, and additional resources (contains Markdown).  
Type: String  
Required: No

 ** id **   <a name="AmazonEKS-Type-InsightSummary-id"></a>
The ID of the insight.  
Type: String  
Required: No

 ** insightStatus **   <a name="AmazonEKS-Type-InsightSummary-insightStatus"></a>
An object containing more detail on the status of the insight.  
Type: [InsightStatus](API_InsightStatus.md) object  
Required: No

 ** kubernetesVersion **   <a name="AmazonEKS-Type-InsightSummary-kubernetesVersion"></a>
The Kubernetes minor version associated with an insight if applicable.   
Type: String  
Required: No

 ** lastRefreshTime **   <a name="AmazonEKS-Type-InsightSummary-lastRefreshTime"></a>
The time Amazon EKS last successfully completed a refresh of this insight check on the cluster.  
Type: Timestamp  
Required: No

 ** lastTransitionTime **   <a name="AmazonEKS-Type-InsightSummary-lastTransitionTime"></a>
The time the status of the insight last changed.  
Type: Timestamp  
Required: No

 ** name **   <a name="AmazonEKS-Type-InsightSummary-name"></a>
The name of the insight.  
Type: String  
Required: No

## See Also
<a name="API_InsightSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/InsightSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/InsightSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/InsightSummary) 