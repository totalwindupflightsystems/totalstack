---
id: "@specs/aws/eks/docs/API_UpdateArgoCdConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateArgoCdConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateArgoCdConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateArgoCdConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateArgoCdConfig
<a name="API_UpdateArgoCdConfig"></a>

Configuration updates for an Argo CD capability. You only need to specify the fields you want to update.

## Contents
<a name="API_UpdateArgoCdConfig_Contents"></a>

 ** networkAccess **   <a name="AmazonEKS-Type-UpdateArgoCdConfig-networkAccess"></a>
Updated network access configuration for the Argo CD capability's managed API server endpoint. You can add or remove VPC endpoint associations to control which VPCs have private access to the Argo CD server.  
Type: [ArgoCdNetworkAccessConfigRequest](API_ArgoCdNetworkAccessConfigRequest.md) object  
Required: No

 ** rbacRoleMappings **   <a name="AmazonEKS-Type-UpdateArgoCdConfig-rbacRoleMappings"></a>
Updated RBAC role mappings for the Argo CD capability. You can add, update, or remove role mappings.  
Type: [UpdateRoleMappings](API_UpdateRoleMappings.md) object  
Required: No

## See Also
<a name="API_UpdateArgoCdConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateArgoCdConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateArgoCdConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateArgoCdConfig) 