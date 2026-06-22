---
id: "@specs/aws/eks/docs/API_StorageConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StorageConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# StorageConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_StorageConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StorageConfigRequest
<a name="API_StorageConfigRequest"></a>

Request to update the configuration of the storage capability of your EKS Auto Mode cluster. For example, enable the capability. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.

## Contents
<a name="API_StorageConfigRequest_Contents"></a>

 ** blockStorage **   <a name="AmazonEKS-Type-StorageConfigRequest-blockStorage"></a>
Request to configure EBS Block Storage settings for your EKS Auto Mode cluster.  
Type: [BlockStorage](API_BlockStorage.md) object  
Required: No

## See Also
<a name="API_StorageConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/StorageConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/StorageConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/StorageConfigRequest) 