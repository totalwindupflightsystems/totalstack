---
id: "@specs/aws/eks/docs/API_Provider"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Provider"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Provider

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Provider
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Provider
<a name="API_Provider"></a>

Identifies the AWS Key Management Service (AWS KMS) key used to encrypt the secrets.

## Contents
<a name="API_Provider_Contents"></a>

 ** keyArn **   <a name="AmazonEKS-Type-Provider-keyArn"></a>
Amazon Resource Name (ARN) or alias of the KMS key. The KMS key must be symmetric and created in the same AWS Region as the cluster. If the KMS key was created in a different account, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) must have access to the KMS key. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the * AWS Key Management Service Developer Guide*.  
Type: String  
Required: No

## See Also
<a name="API_Provider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Provider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Provider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Provider) 