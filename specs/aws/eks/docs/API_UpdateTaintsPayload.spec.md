---
id: "@specs/aws/eks/docs/API_UpdateTaintsPayload"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateTaintsPayload"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateTaintsPayload

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateTaintsPayload
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateTaintsPayload
<a name="API_UpdateTaintsPayload"></a>

An object representing the details of an update to a taints payload. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_UpdateTaintsPayload_Contents"></a>

 ** addOrUpdateTaints **   <a name="AmazonEKS-Type-UpdateTaintsPayload-addOrUpdateTaints"></a>
Kubernetes taints to be added or updated.  
Type: Array of [Taint](API_Taint.md) objects  
Required: No

 ** removeTaints **   <a name="AmazonEKS-Type-UpdateTaintsPayload-removeTaints"></a>
Kubernetes taints to remove.  
Type: Array of [Taint](API_Taint.md) objects  
Required: No

## See Also
<a name="API_UpdateTaintsPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateTaintsPayload) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateTaintsPayload) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateTaintsPayload) 