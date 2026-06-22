---
id: "@specs/aws/eks/docs/API_CapabilityHealth"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CapabilityHealth"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CapabilityHealth

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CapabilityHealth
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CapabilityHealth
<a name="API_CapabilityHealth"></a>

Health information for a capability, including any issues that may be affecting its operation.

## Contents
<a name="API_CapabilityHealth_Contents"></a>

 ** issues **   <a name="AmazonEKS-Type-CapabilityHealth-issues"></a>
A list of issues affecting the capability. If this list is empty, the capability is healthy.  
Type: Array of [CapabilityIssue](API_CapabilityIssue.md) objects  
Required: No

## See Also
<a name="API_CapabilityHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CapabilityHealth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CapabilityHealth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CapabilityHealth) 