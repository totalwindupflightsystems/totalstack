---
id: "@specs/aws/eks/docs/API_ClusterIssue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterIssue"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ClusterIssue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ClusterIssue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterIssue
<a name="API_ClusterIssue"></a>

An issue with your Amazon EKS cluster.

## Contents
<a name="API_ClusterIssue_Contents"></a>

 ** code **   <a name="AmazonEKS-Type-ClusterIssue-code"></a>
The error code of the issue.  
Type: String  
Valid Values: `AccessDenied | ClusterUnreachable | ConfigurationConflict | InternalFailure | ResourceLimitExceeded | ResourceNotFound | IamRoleNotFound | VpcNotFound | InsufficientFreeAddresses | Ec2ServiceNotSubscribed | Ec2SubnetNotFound | Ec2SecurityGroupNotFound | KmsGrantRevoked | KmsKeyNotFound | KmsKeyMarkedForDeletion | KmsKeyDisabled | StsRegionalEndpointDisabled | UnsupportedVersion | Other`   
Required: No

 ** message **   <a name="AmazonEKS-Type-ClusterIssue-message"></a>
A description of the issue.  
Type: String  
Required: No

 ** resourceIds **   <a name="AmazonEKS-Type-ClusterIssue-resourceIds"></a>
The resource IDs that the issue relates to.  
Type: Array of strings  
Required: No

## See Also
<a name="API_ClusterIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ClusterIssue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ClusterIssue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ClusterIssue) 