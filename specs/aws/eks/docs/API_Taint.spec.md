---
id: "@specs/aws/eks/docs/API_Taint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Taint"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Taint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Taint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Taint
<a name="API_Taint"></a>

A property that allows a node to repel a `Pod`. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_Taint_Contents"></a>

 ** effect **   <a name="AmazonEKS-Type-Taint-effect"></a>
The effect of the taint.  
Type: String  
Valid Values: `NO_SCHEDULE | NO_EXECUTE | PREFER_NO_SCHEDULE`   
Required: No

 ** key **   <a name="AmazonEKS-Type-Taint-key"></a>
The key of the taint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Required: No

 ** value **   <a name="AmazonEKS-Type-Taint-value"></a>
The value of the taint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Required: No

## See Also
<a name="API_Taint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Taint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Taint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Taint) 