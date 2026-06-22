---
id: "@specs/aws/eks/docs/API_AccessConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccessConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AccessConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AccessConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccessConfigResponse
<a name="API_AccessConfigResponse"></a>

The access configuration for the cluster.

## Contents
<a name="API_AccessConfigResponse_Contents"></a>

 ** authenticationMode **   <a name="AmazonEKS-Type-AccessConfigResponse-authenticationMode"></a>
The current authentication mode of the cluster.  
Type: String  
Valid Values: `API | API_AND_CONFIG_MAP | CONFIG_MAP`   
Required: No

 ** bootstrapClusterCreatorAdminPermissions **   <a name="AmazonEKS-Type-AccessConfigResponse-bootstrapClusterCreatorAdminPermissions"></a>
Specifies whether or not the cluster creator IAM principal was set as a cluster admin access entry during cluster creation time.  
Type: Boolean  
Required: No

## See Also
<a name="API_AccessConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AccessConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AccessConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AccessConfigResponse) 