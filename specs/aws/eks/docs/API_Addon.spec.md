---
id: "@specs/aws/eks/docs/API_Addon"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Addon"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Addon

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Addon
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Addon
<a name="API_Addon"></a>

An Amazon EKS add-on. For more information, see [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_Addon_Contents"></a>

 ** addonArn **   <a name="AmazonEKS-Type-Addon-addonArn"></a>
The Amazon Resource Name (ARN) of the add-on.  
Type: String  
Required: No

 ** addonName **   <a name="AmazonEKS-Type-Addon-addonName"></a>
The name of the add-on.  
Type: String  
Required: No

 ** addonVersion **   <a name="AmazonEKS-Type-Addon-addonVersion"></a>
The version of the add-on.  
Type: String  
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-Addon-clusterName"></a>
The name of your cluster.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: No

 ** configurationValues **   <a name="AmazonEKS-Type-Addon-configurationValues"></a>
The configuration values that you provided.  
Type: String  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-Addon-createdAt"></a>
The Unix epoch timestamp at object creation.  
Type: Timestamp  
Required: No

 ** health **   <a name="AmazonEKS-Type-Addon-health"></a>
An object that represents the health of the add-on.  
Type: [AddonHealth](API_AddonHealth.md) object  
Required: No

 ** marketplaceInformation **   <a name="AmazonEKS-Type-Addon-marketplaceInformation"></a>
Information about an Amazon EKS add-on from the AWS Marketplace.  
Type: [MarketplaceInformation](API_MarketplaceInformation.md) object  
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-Addon-modifiedAt"></a>
The Unix epoch timestamp for the last modification to the object.  
Type: Timestamp  
Required: No

 ** namespaceConfig **   <a name="AmazonEKS-Type-Addon-namespaceConfig"></a>
The namespace configuration for the addon. This specifies the Kubernetes namespace where the addon is installed.  
Type: [AddonNamespaceConfigResponse](API_AddonNamespaceConfigResponse.md) object  
Required: No

 ** owner **   <a name="AmazonEKS-Type-Addon-owner"></a>
The owner of the add-on.  
Type: String  
Required: No

 ** podIdentityAssociations **   <a name="AmazonEKS-Type-Addon-podIdentityAssociations"></a>
An array of EKS Pod Identity associations owned by the add-on. Each association maps a role to a service account in a namespace in the cluster.  
For more information, see [Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide*.  
Type: Array of strings  
Required: No

 ** publisher **   <a name="AmazonEKS-Type-Addon-publisher"></a>
The publisher of the add-on.  
Type: String  
Required: No

 ** serviceAccountRoleArn **   <a name="AmazonEKS-Type-Addon-serviceAccountRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that's bound to the Kubernetes `ServiceAccount` object that the add-on uses.  
Type: String  
Required: No

 ** status **   <a name="AmazonEKS-Type-Addon-status"></a>
The status of the add-on.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | DELETING | DELETE_FAILED | DEGRADED | UPDATE_FAILED`   
Required: No

 ** tags **   <a name="AmazonEKS-Type-Addon-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_Addon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Addon) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Addon) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Addon) 