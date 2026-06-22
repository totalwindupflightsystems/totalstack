---
id: "@specs/aws/eks/docs/API_Capability"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Capability"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Capability

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Capability
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Capability
<a name="API_Capability"></a>

An object representing a managed capability in an Amazon EKS cluster. This includes all configuration, status, and health information for the capability.

## Contents
<a name="API_Capability_Contents"></a>

 ** arn **   <a name="AmazonEKS-Type-Capability-arn"></a>
The Amazon Resource Name (ARN) of the capability.  
Type: String  
Required: No

 ** capabilityName **   <a name="AmazonEKS-Type-Capability-capabilityName"></a>
The unique name of the capability within the cluster.  
Type: String  
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-Capability-clusterName"></a>
The name of the Amazon EKS cluster that contains this capability.  
Type: String  
Required: No

 ** configuration **   <a name="AmazonEKS-Type-Capability-configuration"></a>
The configuration settings for the capability. The structure varies depending on the capability type.  
Type: [CapabilityConfigurationResponse](API_CapabilityConfigurationResponse.md) object  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-Capability-createdAt"></a>
The Unix epoch timestamp in seconds for when the capability was created.  
Type: Timestamp  
Required: No

 ** deletePropagationPolicy **   <a name="AmazonEKS-Type-Capability-deletePropagationPolicy"></a>
The delete propagation policy for the capability. Currently, the only supported value is `RETAIN`, which keeps all resources managed by the capability when the capability is deleted.  
Type: String  
Valid Values: `RETAIN`   
Required: No

 ** health **   <a name="AmazonEKS-Type-Capability-health"></a>
Health information for the capability, including any issues that may be affecting its operation.  
Type: [CapabilityHealth](API_CapabilityHealth.md) object  
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-Capability-modifiedAt"></a>
The Unix epoch timestamp in seconds for when the capability was last modified.  
Type: Timestamp  
Required: No

 ** roleArn **   <a name="AmazonEKS-Type-Capability-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with AWS services.  
Type: String  
Required: No

 ** status **   <a name="AmazonEKS-Type-Capability-status"></a>
The current status of the capability. Valid values include:  
+  `CREATING` – The capability is being created.
+  `ACTIVE` – The capability is running and available.
+  `UPDATING` – The capability is being updated.
+  `DELETING` – The capability is being deleted.
+  `CREATE_FAILED` – The capability creation failed.
+  `UPDATE_FAILED` – The capability update failed.
+  `DELETE_FAILED` – The capability deletion failed.
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | DELETING | DELETE_FAILED | ACTIVE | DEGRADED`   
Required: No

 ** tags **   <a name="AmazonEKS-Type-Capability-tags"></a>
The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.  
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

 ** type **   <a name="AmazonEKS-Type-Capability-type"></a>
The type of capability. Valid values are `ACK`, `ARGOCD`, or `KRO`.  
Type: String  
Valid Values: `ACK | KRO | ARGOCD`   
Required: No

 ** version **   <a name="AmazonEKS-Type-Capability-version"></a>
The version of the capability software that is currently running.  
Type: String  
Required: No

## See Also
<a name="API_Capability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Capability) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Capability) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Capability) 