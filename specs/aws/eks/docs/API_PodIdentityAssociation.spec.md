---
id: "@specs/aws/eks/docs/API_PodIdentityAssociation"
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
> **spec:id:** @specs/aws/eks/docs/API_PodIdentityAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PodIdentityAssociation
<a name="API_PodIdentityAssociation"></a>

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

## Contents
<a name="API_PodIdentityAssociation_Contents"></a>

 ** associationArn **   <a name="AmazonEKS-Type-PodIdentityAssociation-associationArn"></a>
The Amazon Resource Name (ARN) of the association.  
Type: String  
Required: No

 ** associationId **   <a name="AmazonEKS-Type-PodIdentityAssociation-associationId"></a>
The ID of the association.  
Type: String  
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-PodIdentityAssociation-clusterName"></a>
The name of the cluster that the association is in.  
Type: String  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-PodIdentityAssociation-createdAt"></a>
The timestamp that the association was created at.  
Type: Timestamp  
Required: No

 ** disableSessionTags **   <a name="AmazonEKS-Type-PodIdentityAssociation-disableSessionTags"></a>
The state of the automatic sessions tags. The value of *true* disables these tags.  
EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to AWS resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see [List of session tags added by EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags) in the *Amazon EKS User Guide*.  
Type: Boolean  
Required: No

 ** externalId **   <a name="AmazonEKS-Type-PodIdentityAssociation-externalId"></a>
The unique identifier for this EKS Pod Identity association for a target IAM role. You put this value in the trust policy of the target role, in a `Condition` to match the `sts.ExternalId`. This ensures that the target role can only be assumed by this association. This prevents the *confused deputy problem*. For more information about the confused deputy problem, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.  
If you want to use the same target role with multiple associations or other roles, use independent statements in the trust policy to allow `sts:AssumeRole` access from each role.  
Type: String  
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-PodIdentityAssociation-modifiedAt"></a>
The most recent timestamp that the association was modified at.  
Type: Timestamp  
Required: No

 ** namespace **   <a name="AmazonEKS-Type-PodIdentityAssociation-namespace"></a>
The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the Pods that use the service account must be in this namespace.  
Type: String  
Required: No

 ** ownerArn **   <a name="AmazonEKS-Type-PodIdentityAssociation-ownerArn"></a>
If defined, the EKS Pod Identity association is owned by an Amazon EKS add-on.  
Type: String  
Required: No

 ** policy **   <a name="AmazonEKS-Type-PodIdentityAssociation-policy"></a>
An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.  
Type: String  
Required: No

 ** roleArn **   <a name="AmazonEKS-Type-PodIdentityAssociation-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.  
Type: String  
Required: No

 ** serviceAccount **   <a name="AmazonEKS-Type-PodIdentityAssociation-serviceAccount"></a>
The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.  
Type: String  
Required: No

 ** tags **   <a name="AmazonEKS-Type-PodIdentityAssociation-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
The following basic restrictions apply to tags:  
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** targetRoleArn **   <a name="AmazonEKS-Type-PodIdentityAssociation-targetRoleArn"></a>
The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.  
Type: String  
Required: No

## See Also
<a name="API_PodIdentityAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/PodIdentityAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/PodIdentityAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/PodIdentityAssociation) 