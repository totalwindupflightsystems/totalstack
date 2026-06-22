---
id: "@specs/aws/eks/docs/API_ArgoCdNetworkAccessConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArgoCdNetworkAccessConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ArgoCdNetworkAccessConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ArgoCdNetworkAccessConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArgoCdNetworkAccessConfigRequest
<a name="API_ArgoCdNetworkAccessConfigRequest"></a>

Configuration for network access to the Argo CD capability's managed API server endpoint. When VPC endpoint IDs are specified, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.

## Contents
<a name="API_ArgoCdNetworkAccessConfigRequest_Contents"></a>

 ** vpceIds **   <a name="AmazonEKS-Type-ArgoCdNetworkAccessConfigRequest-vpceIds"></a>
A list of VPC endpoint IDs to associate with the managed Argo CD API server endpoint. Each VPC endpoint provides private connectivity from a specific VPC to the Argo CD server. You can specify multiple VPC endpoint IDs to enable access from multiple VPCs.  
Type: Array of strings  
Required: No

## See Also
<a name="API_ArgoCdNetworkAccessConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdNetworkAccessConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdNetworkAccessConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdNetworkAccessConfigRequest) 