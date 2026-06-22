---
id: "@specs/aws/eks/docs/API_ArgoCdConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArgoCdConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ArgoCdConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ArgoCdConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArgoCdConfigRequest
<a name="API_ArgoCdConfigRequest"></a>

Configuration settings for an Argo CD capability. This includes the Kubernetes namespace, IAM Identity CenterIAM; Identity Center integration, RBAC role mappings, and network access configuration.

## Contents
<a name="API_ArgoCdConfigRequest_Contents"></a>

 ** awsIdc **   <a name="AmazonEKS-Type-ArgoCdConfigRequest-awsIdc"></a>
Configuration for IAM Identity CenterIAM; Identity Center integration. When configured, users can authenticate to Argo CD using their IAM Identity CenterIAM; Identity Center credentials.  
Type: [ArgoCdAwsIdcConfigRequest](API_ArgoCdAwsIdcConfigRequest.md) object  
Required: Yes

 ** namespace **   <a name="AmazonEKS-Type-ArgoCdConfigRequest-namespace"></a>
The Kubernetes namespace where Argo CD resources will be created. If not specified, the default namespace is used.  
Type: String  
Required: No

 ** networkAccess **   <a name="AmazonEKS-Type-ArgoCdConfigRequest-networkAccess"></a>
Configuration for network access to the Argo CD capability's managed API server endpoint. By default, the Argo CD server is accessible via a public endpoint. You can optionally specify one or more VPC endpoint IDs to enable private connectivity from your VPCs. When VPC endpoints are configured, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.  
Type: [ArgoCdNetworkAccessConfigRequest](API_ArgoCdNetworkAccessConfigRequest.md) object  
Required: No

 ** rbacRoleMappings **   <a name="AmazonEKS-Type-ArgoCdConfigRequest-rbacRoleMappings"></a>
A list of role mappings that define which IAM Identity CenterIAM; Identity Center users or groups have which Argo CD roles. Each mapping associates an Argo CD role (`ADMIN`, `EDITOR`, or `VIEWER`) with one or more IAM Identity CenterIAM; Identity Center identities.  
Type: Array of [ArgoCdRoleMapping](API_ArgoCdRoleMapping.md) objects  
Required: No

## See Also
<a name="API_ArgoCdConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdConfigRequest) 