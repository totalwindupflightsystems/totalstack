---
id: "@specs/aws/eks/docs/API_AddonInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonInfo"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonInfo
<a name="API_AddonInfo"></a>

Information about an add-on.

## Contents
<a name="API_AddonInfo_Contents"></a>

 ** addonName **   <a name="AmazonEKS-Type-AddonInfo-addonName"></a>
The name of the add-on.  
Type: String  
Required: No

 ** addonVersions **   <a name="AmazonEKS-Type-AddonInfo-addonVersions"></a>
An object representing information about available add-on versions and compatible Kubernetes versions.  
Type: Array of [AddonVersionInfo](API_AddonVersionInfo.md) objects  
Required: No

 ** defaultNamespace **   <a name="AmazonEKS-Type-AddonInfo-defaultNamespace"></a>
The default Kubernetes namespace where this addon is typically installed if no custom namespace is specified.  
Type: String  
Required: No

 ** marketplaceInformation **   <a name="AmazonEKS-Type-AddonInfo-marketplaceInformation"></a>
Information about the add-on from the AWS Marketplace.  
Type: [MarketplaceInformation](API_MarketplaceInformation.md) object  
Required: No

 ** owner **   <a name="AmazonEKS-Type-AddonInfo-owner"></a>
The owner of the add-on.  
Type: String  
Required: No

 ** publisher **   <a name="AmazonEKS-Type-AddonInfo-publisher"></a>
The publisher of the add-on.  
Type: String  
Required: No

 ** type **   <a name="AmazonEKS-Type-AddonInfo-type"></a>
The type of the add-on.  
Type: String  
Required: No

## See Also
<a name="API_AddonInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonInfo) 