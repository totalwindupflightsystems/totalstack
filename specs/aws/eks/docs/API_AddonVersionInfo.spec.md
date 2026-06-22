---
id: "@specs/aws/eks/docs/API_AddonVersionInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonVersionInfo"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonVersionInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonVersionInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonVersionInfo
<a name="API_AddonVersionInfo"></a>

Information about an add-on version.

## Contents
<a name="API_AddonVersionInfo_Contents"></a>

 ** addonVersion **   <a name="AmazonEKS-Type-AddonVersionInfo-addonVersion"></a>
The version of the add-on.  
Type: String  
Required: No

 ** architecture **   <a name="AmazonEKS-Type-AddonVersionInfo-architecture"></a>
The architectures that the version supports.  
Type: Array of strings  
Required: No

 ** compatibilities **   <a name="AmazonEKS-Type-AddonVersionInfo-compatibilities"></a>
An object representing the compatibilities of a version.  
Type: Array of [Compatibility](API_Compatibility.md) objects  
Required: No

 ** computeTypes **   <a name="AmazonEKS-Type-AddonVersionInfo-computeTypes"></a>
Indicates the compute type of the add-on version.  
Type: Array of strings  
Required: No

 ** requiresConfiguration **   <a name="AmazonEKS-Type-AddonVersionInfo-requiresConfiguration"></a>
Whether the add-on requires configuration.  
Type: Boolean  
Required: No

 ** requiresIamPermissions **   <a name="AmazonEKS-Type-AddonVersionInfo-requiresIamPermissions"></a>
Indicates if the add-on requires IAM Permissions to operate, such as networking permissions.  
Type: Boolean  
Required: No

## See Also
<a name="API_AddonVersionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonVersionInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonVersionInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonVersionInfo) 