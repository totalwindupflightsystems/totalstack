---
id: "@specs/aws/eks/docs/API_Insight"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Insight"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Insight

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Insight
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Insight
<a name="API_Insight"></a>

A check that provides recommendations to remedy potential upgrade-impacting issues.

## Contents
<a name="API_Insight_Contents"></a>

 ** additionalInfo **   <a name="AmazonEKS-Type-Insight-additionalInfo"></a>
Links to sources that provide additional context on the insight.  
Type: String to string map  
Required: No

 ** category **   <a name="AmazonEKS-Type-Insight-category"></a>
The category of the insight.  
Type: String  
Valid Values: `UPGRADE_READINESS | MISCONFIGURATION`   
Required: No

 ** categorySpecificSummary **   <a name="AmazonEKS-Type-Insight-categorySpecificSummary"></a>
Summary information that relates to the category of the insight. Currently only returned with certain insights having category `UPGRADE_READINESS`.  
Type: [InsightCategorySpecificSummary](API_InsightCategorySpecificSummary.md) object  
Required: No

 ** description **   <a name="AmazonEKS-Type-Insight-description"></a>
The description of the insight which includes alert criteria, remediation recommendation, and additional resources (contains Markdown).  
Type: String  
Required: No

 ** id **   <a name="AmazonEKS-Type-Insight-id"></a>
The ID of the insight.  
Type: String  
Required: No

 ** insightStatus **   <a name="AmazonEKS-Type-Insight-insightStatus"></a>
An object containing more detail on the status of the insight resource.  
Type: [InsightStatus](API_InsightStatus.md) object  
Required: No

 ** kubernetesVersion **   <a name="AmazonEKS-Type-Insight-kubernetesVersion"></a>
The Kubernetes minor version associated with an insight if applicable.  
Type: String  
Required: No

 ** lastRefreshTime **   <a name="AmazonEKS-Type-Insight-lastRefreshTime"></a>
The time Amazon EKS last successfully completed a refresh of this insight check on the cluster.  
Type: Timestamp  
Required: No

 ** lastTransitionTime **   <a name="AmazonEKS-Type-Insight-lastTransitionTime"></a>
The time the status of the insight last changed.  
Type: Timestamp  
Required: No

 ** name **   <a name="AmazonEKS-Type-Insight-name"></a>
The name of the insight.  
Type: String  
Required: No

 ** recommendation **   <a name="AmazonEKS-Type-Insight-recommendation"></a>
A summary of how to remediate the finding of this insight if applicable.   
Type: String  
Required: No

 ** resources **   <a name="AmazonEKS-Type-Insight-resources"></a>
The details about each resource listed in the insight check result.  
Type: Array of [InsightResourceDetail](API_InsightResourceDetail.md) objects  
Required: No

## See Also
<a name="API_Insight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Insight) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Insight) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Insight) 