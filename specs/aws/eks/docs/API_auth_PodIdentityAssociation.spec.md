---
id: "@specs/aws/eks/docs/API_auth_PodIdentityAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PodIdentityAssociation"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# PodIdentityAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_auth_PodIdentityAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PodIdentityAssociation
<a name="API_auth_PodIdentityAssociation"></a>

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

## Contents
<a name="API_auth_PodIdentityAssociation_Contents"></a>

 ** associationArn **   <a name="AmazonEKS-Type-auth_PodIdentityAssociation-associationArn"></a>
The Amazon Resource Name (ARN) of the EKS Pod Identity association.  
Type: String  
Required: Yes

 ** associationId **   <a name="AmazonEKS-Type-auth_PodIdentityAssociation-associationId"></a>
The ID of the association.  
Type: String  
Required: Yes

## See Also
<a name="API_auth_PodIdentityAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-auth-2023-11-26/PodIdentityAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-auth-2023-11-26/PodIdentityAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-auth-2023-11-26/PodIdentityAssociation) 