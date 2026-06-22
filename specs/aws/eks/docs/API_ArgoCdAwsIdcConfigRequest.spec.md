---
id: "@specs/aws/eks/docs/API_ArgoCdAwsIdcConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArgoCdAwsIdcConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ArgoCdAwsIdcConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ArgoCdAwsIdcConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArgoCdAwsIdcConfigRequest
<a name="API_ArgoCdAwsIdcConfigRequest"></a>

Configuration for integrating Argo CD with IAM Identity CenterIAM; Identity Center. This allows you to use your organization's identity provider for authentication to Argo CD.

## Contents
<a name="API_ArgoCdAwsIdcConfigRequest_Contents"></a>

 ** idcInstanceArn **   <a name="AmazonEKS-Type-ArgoCdAwsIdcConfigRequest-idcInstanceArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity CenterIAM; Identity Center instance to use for authentication.  
Type: String  
Required: Yes

 ** idcRegion **   <a name="AmazonEKS-Type-ArgoCdAwsIdcConfigRequest-idcRegion"></a>
The Region where your IAM Identity CenterIAM; Identity Center instance is located.  
Type: String  
Required: No

## See Also
<a name="API_ArgoCdAwsIdcConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdAwsIdcConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdAwsIdcConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdAwsIdcConfigRequest) 