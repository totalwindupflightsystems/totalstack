---
id: "@specs/aws/eks/docs/API_CreateAccessConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAccessConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateAccessConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateAccessConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAccessConfigRequest
<a name="API_CreateAccessConfigRequest"></a>

The access configuration information for the cluster.

## Contents
<a name="API_CreateAccessConfigRequest_Contents"></a>

 ** authenticationMode **   <a name="AmazonEKS-Type-CreateAccessConfigRequest-authenticationMode"></a>
The desired authentication mode for the cluster. If you create a cluster by using the EKS API, AWS SDKs, or AWS CloudFormation, the default is `CONFIG_MAP`. If you create the cluster by using the AWS Management Console, the default value is `API_AND_CONFIG_MAP`.  
Type: String  
Valid Values: `API | API_AND_CONFIG_MAP | CONFIG_MAP`   
Required: No

 ** bootstrapClusterCreatorAdminPermissions **   <a name="AmazonEKS-Type-CreateAccessConfigRequest-bootstrapClusterCreatorAdminPermissions"></a>
Specifies whether or not the cluster creator IAM principal was set as a cluster admin access entry during cluster creation time. The default value is `true`.  
Type: Boolean  
Required: No

## See Also
<a name="API_CreateAccessConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateAccessConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateAccessConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateAccessConfigRequest) 