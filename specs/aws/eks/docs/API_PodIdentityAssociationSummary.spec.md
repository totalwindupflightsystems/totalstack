---
id: "@specs/aws/eks/docs/API_PodIdentityAssociationSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PodIdentityAssociationSummary"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# PodIdentityAssociationSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_PodIdentityAssociationSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PodIdentityAssociationSummary
<a name="API_PodIdentityAssociationSummary"></a>

The summarized description of the association.

Each summary is simplified by removing these fields compared to the full [https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html):
+ The IAM role: `roleArn` 
+ The timestamp that the association was created at: `createdAt` 
+ The most recent timestamp that the association was modified at:. `modifiedAt` 
+ The tags on the association: `tags` 

## Contents
<a name="API_PodIdentityAssociationSummary_Contents"></a>

 ** associationArn **   <a name="AmazonEKS-Type-PodIdentityAssociationSummary-associationArn"></a>
The Amazon Resource Name (ARN) of the association.  
Type: String  
Required: No

 ** associationId **   <a name="AmazonEKS-Type-PodIdentityAssociationSummary-associationId"></a>
The ID of the association.  
Type: String  
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-PodIdentityAssociationSummary-clusterName"></a>
The name of the cluster that the association is in.  
Type: String  
Required: No

 ** namespace **   <a name="AmazonEKS-Type-PodIdentityAssociationSummary-namespace"></a>
The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the Pods that use the service account must be in this namespace.  
Type: String  
Required: No

 ** ownerArn **   <a name="AmazonEKS-Type-PodIdentityAssociationSummary-ownerArn"></a>
If defined, the association is owned by an Amazon EKS add-on.  
Type: String  
Required: No

 ** serviceAccount **   <a name="AmazonEKS-Type-PodIdentityAssociationSummary-serviceAccount"></a>
The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.  
Type: String  
Required: No

## See Also
<a name="API_PodIdentityAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/PodIdentityAssociationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/PodIdentityAssociationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/PodIdentityAssociationSummary) 