---
id: "@specs/aws/eks/docs/API_auth_Subject"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Subject"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Subject

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_auth_Subject
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Subject
<a name="API_auth_Subject"></a>

An object containing the name of the Kubernetes service account inside the cluster to associate the IAM credentials with.

## Contents
<a name="API_auth_Subject_Contents"></a>

 ** namespace **   <a name="AmazonEKS-Type-auth_Subject-namespace"></a>
The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the pods that use the service account must be in this namespace.  
Type: String  
Required: Yes

 ** serviceAccount **   <a name="AmazonEKS-Type-auth_Subject-serviceAccount"></a>
The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.  
Type: String  
Required: Yes

## See Also
<a name="API_auth_Subject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-auth-2023-11-26/Subject) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-auth-2023-11-26/Subject) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-auth-2023-11-26/Subject) 