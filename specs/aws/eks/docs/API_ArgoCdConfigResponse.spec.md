---
id: "@specs/aws/eks/docs/API_ArgoCdConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArgoCdConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ArgoCdConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ArgoCdConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArgoCdConfigResponse
<a name="API_ArgoCdConfigResponse"></a>

The response object containing Argo CD configuration details, including the server URL that you use to access the Argo CD web interface and API.

## Contents
<a name="API_ArgoCdConfigResponse_Contents"></a>

 ** awsIdc **   <a name="AmazonEKS-Type-ArgoCdConfigResponse-awsIdc"></a>
The IAM Identity CenterIAM; Identity Center integration configuration.  
Type: [ArgoCdAwsIdcConfigResponse](API_ArgoCdAwsIdcConfigResponse.md) object  
Required: No

 ** namespace **   <a name="AmazonEKS-Type-ArgoCdConfigResponse-namespace"></a>
The Kubernetes namespace where Argo CD resources are monitored by your Argo CD Capability.  
Type: String  
Required: No

 ** networkAccess **   <a name="AmazonEKS-Type-ArgoCdConfigResponse-networkAccess"></a>
The network access configuration for the Argo CD capability's managed API server endpoint. If VPC endpoint IDs are specified, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.  
Type: [ArgoCdNetworkAccessConfigResponse](API_ArgoCdNetworkAccessConfigResponse.md) object  
Required: No

 ** rbacRoleMappings **   <a name="AmazonEKS-Type-ArgoCdConfigResponse-rbacRoleMappings"></a>
The list of role mappings that define which IAM Identity CenterIAM; Identity Center users or groups have which Argo CD roles.  
Type: Array of [ArgoCdRoleMapping](API_ArgoCdRoleMapping.md) objects  
Required: No

 ** serverUrl **   <a name="AmazonEKS-Type-ArgoCdConfigResponse-serverUrl"></a>
The URL of the Argo CD server. Use this URL to access the Argo CD web interface and API.  
Type: String  
Required: No

## See Also
<a name="API_ArgoCdConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdConfigResponse) 