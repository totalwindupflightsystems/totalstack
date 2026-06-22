---
id: "@specs/aws/eks/docs/API_CapabilityConfigurationRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CapabilityConfigurationRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CapabilityConfigurationRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CapabilityConfigurationRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CapabilityConfigurationRequest
<a name="API_CapabilityConfigurationRequest"></a>

Configuration settings for a capability. The structure of this object varies depending on the capability type.

## Contents
<a name="API_CapabilityConfigurationRequest_Contents"></a>

 ** argoCd **   <a name="AmazonEKS-Type-CapabilityConfigurationRequest-argoCd"></a>
Configuration settings specific to Argo CD capabilities. This field is only used when creating or updating an Argo CD capability.  
Type: [ArgoCdConfigRequest](API_ArgoCdConfigRequest.md) object  
Required: No

## See Also
<a name="API_CapabilityConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CapabilityConfigurationRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CapabilityConfigurationRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CapabilityConfigurationRequest) 