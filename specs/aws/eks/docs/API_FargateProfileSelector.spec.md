---
id: "@specs/aws/eks/docs/API_FargateProfileSelector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FargateProfileSelector"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# FargateProfileSelector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_FargateProfileSelector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FargateProfileSelector
<a name="API_FargateProfileSelector"></a>

An object representing an AWS Fargate profile selector.

## Contents
<a name="API_FargateProfileSelector_Contents"></a>

 ** labels **   <a name="AmazonEKS-Type-FargateProfileSelector-labels"></a>
The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.  
Type: String to string map  
Required: No

 ** namespace **   <a name="AmazonEKS-Type-FargateProfileSelector-namespace"></a>
The Kubernetes `namespace` that the selector should match.  
Type: String  
Required: No

## See Also
<a name="API_FargateProfileSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/FargateProfileSelector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/FargateProfileSelector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/FargateProfileSelector) 