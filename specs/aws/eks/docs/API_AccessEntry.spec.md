---
id: "@specs/aws/eks/docs/API_AccessEntry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccessEntry"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AccessEntry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AccessEntry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccessEntry
<a name="API_AccessEntry"></a>

An access entry allows an IAM principal (user or role) to access your cluster. Access entries can replace the need to maintain the `aws-auth` `ConfigMap` for authentication. For more information about access entries, see [Access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_AccessEntry_Contents"></a>

 ** accessEntryArn **   <a name="AmazonEKS-Type-AccessEntry-accessEntryArn"></a>
The ARN of the access entry.  
Type: String  
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-AccessEntry-clusterName"></a>
The name of your cluster.  
Type: String  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-AccessEntry-createdAt"></a>
The Unix epoch timestamp at object creation.  
Type: Timestamp  
Required: No

 ** kubernetesGroups **   <a name="AmazonEKS-Type-AccessEntry-kubernetesGroups"></a>
A `name` that you've specified in a Kubernetes `RoleBinding` or `ClusterRoleBinding` object so that Kubernetes authorizes the `principalARN` access to cluster objects.  
Type: Array of strings  
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-AccessEntry-modifiedAt"></a>
The Unix epoch timestamp for the last modification to the object.  
Type: Timestamp  
Required: No

 ** principalArn **   <a name="AmazonEKS-Type-AccessEntry-principalArn"></a>
The ARN of the IAM principal for the access entry. If you ever delete the IAM principal with this ARN, the access entry isn't automatically deleted. We recommend that you delete the access entry with an ARN for an IAM principal that you delete. If you don't delete the access entry and ever recreate the IAM principal, even if it has the same ARN, the access entry won't work. This is because even though the ARN is the same for the recreated IAM principal, the `roleID` or `userID` (you can see this with the AWS Security Token Service `GetCallerIdentity` API) is different for the recreated IAM principal than it was for the original IAM principal. Even though you don't see the IAM principal's `roleID` or `userID` for an access entry, Amazon EKS stores it with the access entry.  
Type: String  
Required: No

 ** tags **   <a name="AmazonEKS-Type-AccessEntry-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** type **   <a name="AmazonEKS-Type-AccessEntry-type"></a>
The type of the access entry.  
Type: String  
Required: No

 ** username **   <a name="AmazonEKS-Type-AccessEntry-username"></a>
The `name` of a user that can authenticate to your cluster.  
Type: String  
Required: No

## See Also
<a name="API_AccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AccessEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AccessEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AccessEntry) 