---
id: "@specs/aws/eks/docs/API_AddonCompatibilityDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonCompatibilityDetail"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonCompatibilityDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonCompatibilityDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonCompatibilityDetail
<a name="API_AddonCompatibilityDetail"></a>

The summary information about the Amazon EKS add-on compatibility for the next Kubernetes version for an insight check in the `UPGRADE_READINESS` category.

## Contents
<a name="API_AddonCompatibilityDetail_Contents"></a>

 ** compatibleVersions **   <a name="AmazonEKS-Type-AddonCompatibilityDetail-compatibleVersions"></a>
The list of compatible Amazon EKS add-on versions for the next Kubernetes version.  
Type: Array of strings  
Required: No

 ** name **   <a name="AmazonEKS-Type-AddonCompatibilityDetail-name"></a>
The name of the Amazon EKS add-on.  
Type: String  
Required: No

## See Also
<a name="API_AddonCompatibilityDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonCompatibilityDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonCompatibilityDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonCompatibilityDetail) 