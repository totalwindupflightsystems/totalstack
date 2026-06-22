---
id: "@specs/aws/eks/docs/API_InsightCategorySpecificSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InsightCategorySpecificSummary"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# InsightCategorySpecificSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_InsightCategorySpecificSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InsightCategorySpecificSummary
<a name="API_InsightCategorySpecificSummary"></a>

Summary information that relates to the category of the insight. Currently only returned with certain insights having category `UPGRADE_READINESS`.

## Contents
<a name="API_InsightCategorySpecificSummary_Contents"></a>

 ** addonCompatibilityDetails **   <a name="AmazonEKS-Type-InsightCategorySpecificSummary-addonCompatibilityDetails"></a>
A list of `AddonCompatibilityDetail` objects for Amazon EKS add-ons.  
Type: Array of [AddonCompatibilityDetail](API_AddonCompatibilityDetail.md) objects  
Required: No

 ** deprecationDetails **   <a name="AmazonEKS-Type-InsightCategorySpecificSummary-deprecationDetails"></a>
The summary information about deprecated resource usage for an insight check in the `UPGRADE_READINESS` category.  
Type: Array of [DeprecationDetail](API_DeprecationDetail.md) objects  
Required: No

## See Also
<a name="API_InsightCategorySpecificSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/InsightCategorySpecificSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/InsightCategorySpecificSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/InsightCategorySpecificSummary) 