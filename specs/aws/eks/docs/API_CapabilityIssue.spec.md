---
id: "@specs/aws/eks/docs/API_CapabilityIssue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CapabilityIssue"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CapabilityIssue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CapabilityIssue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CapabilityIssue
<a name="API_CapabilityIssue"></a>

An issue affecting a capability's health or operation.

## Contents
<a name="API_CapabilityIssue_Contents"></a>

 ** code **   <a name="AmazonEKS-Type-CapabilityIssue-code"></a>
A code identifying the type of issue. This can be used to programmatically handle specific issue types.  
Type: String  
Valid Values: `AccessDenied | ClusterUnreachable`   
Required: No

 ** message **   <a name="AmazonEKS-Type-CapabilityIssue-message"></a>
A human-readable message describing the issue and potential remediation steps.  
Type: String  
Required: No

## See Also
<a name="API_CapabilityIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CapabilityIssue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CapabilityIssue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CapabilityIssue) 