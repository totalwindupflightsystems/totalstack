---
id: "@specs/aws/eks/docs/API_InsightsFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InsightsFilter"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# InsightsFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_InsightsFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InsightsFilter
<a name="API_InsightsFilter"></a>

The criteria to use for the insights.

## Contents
<a name="API_InsightsFilter_Contents"></a>

 ** categories **   <a name="AmazonEKS-Type-InsightsFilter-categories"></a>
The categories to use to filter insights. The following lists the available categories:  
+  `UPGRADE_READINESS`: Amazon EKS identifies issues that could impact your ability to upgrade to new versions of Kubernetes. These are called upgrade insights.
+  `MISCONFIGURATION`: Amazon EKS identifies misconfiguration in your EKS Hybrid Nodes setup that could impair functionality of your cluster or workloads. These are called configuration insights.
Type: Array of strings  
Valid Values: `UPGRADE_READINESS | MISCONFIGURATION`   
Required: No

 ** kubernetesVersions **   <a name="AmazonEKS-Type-InsightsFilter-kubernetesVersions"></a>
The Kubernetes versions to use to filter the insights.  
Type: Array of strings  
Required: No

 ** statuses **   <a name="AmazonEKS-Type-InsightsFilter-statuses"></a>
The statuses to use to filter the insights.   
Type: Array of strings  
Valid Values: `PASSING | WARNING | ERROR | UNKNOWN`   
Required: No

## See Also
<a name="API_InsightsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/InsightsFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/InsightsFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/InsightsFilter) 