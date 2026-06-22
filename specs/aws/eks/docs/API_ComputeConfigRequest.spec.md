---
id: "@specs/aws/eks/docs/API_ComputeConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ComputeConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ComputeConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ComputeConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ComputeConfigRequest
<a name="API_ComputeConfigRequest"></a>

Request to update the configuration of the compute capability of your EKS Auto Mode cluster. For example, enable the capability. For more information, see EKS Auto Mode compute capability in the *Amazon EKS User Guide*.

## Contents
<a name="API_ComputeConfigRequest_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-ComputeConfigRequest-enabled"></a>
Request to enable or disable the compute capability on your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account.  
Type: Boolean  
Required: No

 ** nodePools **   <a name="AmazonEKS-Type-ComputeConfigRequest-nodePools"></a>
Configuration for node pools that defines the compute resources for your EKS Auto Mode cluster. For more information, see EKS Auto Mode Node Pools in the *Amazon EKS User Guide*.  
Type: Array of strings  
Required: No

 ** nodeRoleArn **   <a name="AmazonEKS-Type-ComputeConfigRequest-nodeRoleArn"></a>
The ARN of the IAM Role EKS will assign to EC2 Managed Instances in your EKS Auto Mode cluster. This value cannot be changed after the compute capability of EKS Auto Mode is enabled. For more information, see the IAM Reference in the *Amazon EKS User Guide*.  
Type: String  
Required: No

## See Also
<a name="API_ComputeConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ComputeConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ComputeConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ComputeConfigRequest) 