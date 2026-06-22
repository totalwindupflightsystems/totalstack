---
id: "@specs/aws/eks/docs/API_AddonNamespaceConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonNamespaceConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonNamespaceConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonNamespaceConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonNamespaceConfigRequest
<a name="API_AddonNamespaceConfigRequest"></a>

The namespace configuration request object for specifying a custom namespace when creating an addon.

## Contents
<a name="API_AddonNamespaceConfigRequest_Contents"></a>

 ** namespace **   <a name="AmazonEKS-Type-AddonNamespaceConfigRequest-namespace"></a>
The name of the Kubernetes namespace to install the addon in. Must be a valid RFC 1123 DNS label.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Required: No

## See Also
<a name="API_AddonNamespaceConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonNamespaceConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonNamespaceConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonNamespaceConfigRequest) 