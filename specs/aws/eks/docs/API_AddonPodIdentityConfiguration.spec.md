---
id: "@specs/aws/eks/docs/API_AddonPodIdentityConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonPodIdentityConfiguration"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonPodIdentityConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonPodIdentityConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonPodIdentityConfiguration
<a name="API_AddonPodIdentityConfiguration"></a>

Information about how to configure IAM for an add-on.

## Contents
<a name="API_AddonPodIdentityConfiguration_Contents"></a>

 ** recommendedManagedPolicies **   <a name="AmazonEKS-Type-AddonPodIdentityConfiguration-recommendedManagedPolicies"></a>
A suggested IAM Policy for the add-on.  
Type: Array of strings  
Required: No

 ** serviceAccount **   <a name="AmazonEKS-Type-AddonPodIdentityConfiguration-serviceAccount"></a>
The Kubernetes Service Account name used by the add-on.  
Type: String  
Required: No

## See Also
<a name="API_AddonPodIdentityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonPodIdentityConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonPodIdentityConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonPodIdentityConfiguration) 