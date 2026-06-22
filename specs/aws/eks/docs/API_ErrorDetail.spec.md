---
id: "@specs/aws/eks/docs/API_ErrorDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ErrorDetail"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ErrorDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ErrorDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ErrorDetail
<a name="API_ErrorDetail"></a>

An object representing an error when an asynchronous operation fails.

## Contents
<a name="API_ErrorDetail_Contents"></a>

 ** errorCode **   <a name="AmazonEKS-Type-ErrorDetail-errorCode"></a>
A brief description of the error.   
+  **SubnetNotFound**: We couldn't find one of the subnets associated with the cluster.
+  **SecurityGroupNotFound**: We couldn't find one of the security groups associated with the cluster.
+  **EniLimitReached**: You have reached the elastic network interface limit for your account.
+  **IpNotAvailable**: A subnet associated with the cluster doesn't have any available IP addresses.
+  **AccessDenied**: You don't have permissions to perform the specified operation.
+  **OperationNotPermitted**: The service role associated with the cluster doesn't have the required access permissions for Amazon EKS.
+  **VpcIdNotFound**: We couldn't find the VPC associated with the cluster.
Type: String  
Valid Values: `SubnetNotFound | SecurityGroupNotFound | EniLimitReached | IpNotAvailable | AccessDenied | OperationNotPermitted | VpcIdNotFound | Unknown | NodeCreationFailure | PodEvictionFailure | InsufficientFreeAddresses | ClusterUnreachable | InsufficientNumberOfReplicas | ConfigurationConflict | AdmissionRequestDenied | UnsupportedAddonModification | K8sResourceNotFound`   
Required: No

 ** errorMessage **   <a name="AmazonEKS-Type-ErrorDetail-errorMessage"></a>
A more complete description of the error.  
Type: String  
Required: No

 ** resourceIds **   <a name="AmazonEKS-Type-ErrorDetail-resourceIds"></a>
An optional field that contains the resource IDs associated with the error.  
Type: Array of strings  
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ErrorDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ErrorDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ErrorDetail) 