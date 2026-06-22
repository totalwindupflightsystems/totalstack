---
id: "@specs/aws/eks/docs/API_AccessPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccessPolicy"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AccessPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AccessPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccessPolicy
<a name="API_AccessPolicy"></a>

An access policy includes permissions that allow Amazon EKS to authorize an IAM principal to work with Kubernetes objects on your cluster. The policies are managed by Amazon EKS, but they're not IAM policies. You can't view the permissions in the policies using the API. The permissions for many of the policies are similar to the Kubernetes `cluster-admin`, `admin`, `edit`, and `view` cluster roles. For more information about these cluster roles, see [User-facing roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) in the Kubernetes documentation. To view the contents of the policies, see [Access policy permissions](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html#access-policy-permissions) in the *Amazon EKS User Guide*.

## Contents
<a name="API_AccessPolicy_Contents"></a>

 ** arn **   <a name="AmazonEKS-Type-AccessPolicy-arn"></a>
The ARN of the access policy.  
Type: String  
Required: No

 ** name **   <a name="AmazonEKS-Type-AccessPolicy-name"></a>
The name of the access policy.  
Type: String  
Required: No

## See Also
<a name="API_AccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AccessPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AccessPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AccessPolicy) 