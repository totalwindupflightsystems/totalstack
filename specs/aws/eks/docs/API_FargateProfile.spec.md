---
id: "@specs/aws/eks/docs/API_FargateProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FargateProfile"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# FargateProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_FargateProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FargateProfile
<a name="API_FargateProfile"></a>

An object representing an AWS Fargate profile.

## Contents
<a name="API_FargateProfile_Contents"></a>

 ** clusterName **   <a name="AmazonEKS-Type-FargateProfile-clusterName"></a>
The name of your cluster.  
Type: String  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-FargateProfile-createdAt"></a>
The Unix epoch timestamp at object creation.  
Type: Timestamp  
Required: No

 ** fargateProfileArn **   <a name="AmazonEKS-Type-FargateProfile-fargateProfileArn"></a>
The full Amazon Resource Name (ARN) of the Fargate profile.  
Type: String  
Required: No

 ** fargateProfileName **   <a name="AmazonEKS-Type-FargateProfile-fargateProfileName"></a>
The name of the Fargate profile.  
Type: String  
Required: No

 ** health **   <a name="AmazonEKS-Type-FargateProfile-health"></a>
The health status of the Fargate profile. If there are issues with your Fargate profile's health, they are listed here.  
Type: [FargateProfileHealth](API_FargateProfileHealth.md) object  
Required: No

 ** podExecutionRoleArn **   <a name="AmazonEKS-Type-FargateProfile-podExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the `Pod` execution role to use for any `Pod` that matches the selectors in the Fargate profile. For more information, see [`Pod` execution role](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

 ** selectors **   <a name="AmazonEKS-Type-FargateProfile-selectors"></a>
The selectors to match for a `Pod` to use this Fargate profile.  
Type: Array of [FargateProfileSelector](API_FargateProfileSelector.md) objects  
Required: No

 ** status **   <a name="AmazonEKS-Type-FargateProfile-status"></a>
The current status of the Fargate profile.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | CREATE_FAILED | DELETE_FAILED`   
Required: No

 ** subnets **   <a name="AmazonEKS-Type-FargateProfile-subnets"></a>
The IDs of subnets to launch a `Pod` into.  
Type: Array of strings  
Required: No

 ** tags **   <a name="AmazonEKS-Type-FargateProfile-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_FargateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/FargateProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/FargateProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/FargateProfile) 