---
id: "@specs/aws/eks/docs/API_AddonPodIdentityAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonPodIdentityAssociations"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonPodIdentityAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonPodIdentityAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonPodIdentityAssociations
<a name="API_AddonPodIdentityAssociations"></a>

A type of EKS Pod Identity association owned by an Amazon EKS add-on.

Each association maps a role to a service account in a namespace in the cluster.

For more information, see [Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_AddonPodIdentityAssociations_Contents"></a>

 ** roleArn **   <a name="AmazonEKS-Type-AddonPodIdentityAssociations-roleArn"></a>
The ARN of an IAM Role.  
Type: String  
Required: Yes

 ** serviceAccount **   <a name="AmazonEKS-Type-AddonPodIdentityAssociations-serviceAccount"></a>
The name of a Kubernetes Service Account.  
Type: String  
Required: Yes

## See Also
<a name="API_AddonPodIdentityAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonPodIdentityAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonPodIdentityAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonPodIdentityAssociations) 