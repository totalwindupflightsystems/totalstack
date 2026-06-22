---
id: "@specs/aws/eks/docs/API_CapabilitySummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CapabilitySummary"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CapabilitySummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CapabilitySummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CapabilitySummary
<a name="API_CapabilitySummary"></a>

A summary of a capability, containing basic information without the full configuration details. This is returned by the `ListCapabilities` operation.

## Contents
<a name="API_CapabilitySummary_Contents"></a>

 ** arn **   <a name="AmazonEKS-Type-CapabilitySummary-arn"></a>
The Amazon Resource Name (ARN) of the capability.  
Type: String  
Required: No

 ** capabilityName **   <a name="AmazonEKS-Type-CapabilitySummary-capabilityName"></a>
The unique name of the capability within the cluster.  
Type: String  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-CapabilitySummary-createdAt"></a>
The Unix epoch timestamp in seconds for when the capability was created.  
Type: Timestamp  
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-CapabilitySummary-modifiedAt"></a>
The Unix epoch timestamp in seconds for when the capability was last modified.  
Type: Timestamp  
Required: No

 ** status **   <a name="AmazonEKS-Type-CapabilitySummary-status"></a>
The current status of the capability.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | DELETING | DELETE_FAILED | ACTIVE | DEGRADED`   
Required: No

 ** type **   <a name="AmazonEKS-Type-CapabilitySummary-type"></a>
The type of capability. Valid values are `ACK`, `ARGOCD`, or `KRO`.  
Type: String  
Valid Values: `ACK | KRO | ARGOCD`   
Required: No

 ** version **   <a name="AmazonEKS-Type-CapabilitySummary-version"></a>
The version of the capability software that is currently running.  
Type: String  
Required: No

## See Also
<a name="API_CapabilitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CapabilitySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CapabilitySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CapabilitySummary) 