---
id: "@specs/aws/eks/docs/API_BlockStorage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlockStorage"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# BlockStorage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_BlockStorage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlockStorage
<a name="API_BlockStorage"></a>

Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.

## Contents
<a name="API_BlockStorage_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-BlockStorage-enabled"></a>
Indicates if the block storage capability is enabled on your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account.  
Type: Boolean  
Required: No

## See Also
<a name="API_BlockStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/BlockStorage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/BlockStorage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/BlockStorage) 