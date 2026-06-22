---
id: "@specs/aws/eks/docs/API_ComputeConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ComputeConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ComputeConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ComputeConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ComputeConfigResponse
<a name="API_ComputeConfigResponse"></a>

Indicates the status of the request to update the compute capability of your EKS Auto Mode cluster.

## Contents
<a name="API_ComputeConfigResponse_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-ComputeConfigResponse-enabled"></a>
Indicates if the compute capability is enabled on your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account.  
Type: Boolean  
Required: No

 ** nodePools **   <a name="AmazonEKS-Type-ComputeConfigResponse-nodePools"></a>
Indicates the current configuration of node pools in your EKS Auto Mode cluster. For more information, see EKS Auto Mode Node Pools in the *Amazon EKS User Guide*.  
Type: Array of strings  
Required: No

 ** nodeRoleArn **   <a name="AmazonEKS-Type-ComputeConfigResponse-nodeRoleArn"></a>
The ARN of the IAM Role EKS will assign to EC2 Managed Instances in your EKS Auto Mode cluster.  
Type: String  
Required: No

## See Also
<a name="API_ComputeConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ComputeConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ComputeConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ComputeConfigResponse) 