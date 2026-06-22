---
id: "@specs/aws/eks/docs/API_Certificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Certificate"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Certificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Certificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Certificate
<a name="API_Certificate"></a>

An object representing the `certificate-authority-data` for your cluster.

## Contents
<a name="API_Certificate_Contents"></a>

 ** data **   <a name="AmazonEKS-Type-Certificate-data"></a>
The Base64-encoded certificate data required to communicate with your cluster. Add this to the `certificate-authority-data` section of the `kubeconfig` file for your cluster.  
Type: String  
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Certificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Certificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Certificate) 