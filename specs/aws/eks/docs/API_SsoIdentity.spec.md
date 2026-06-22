---
id: "@specs/aws/eks/docs/API_SsoIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SsoIdentity"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# SsoIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_SsoIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SsoIdentity
<a name="API_SsoIdentity"></a>

An IAM Identity CenterIAM; Identity Center identity (user or group) that can be assigned permissions in a capability.

## Contents
<a name="API_SsoIdentity_Contents"></a>

 ** id **   <a name="AmazonEKS-Type-SsoIdentity-id"></a>
The unique identifier of the IAM Identity CenterIAM; Identity Center user or group.  
Type: String  
Required: Yes

 ** type **   <a name="AmazonEKS-Type-SsoIdentity-type"></a>
The type of identity. Valid values are `SSO_USER` or `SSO_GROUP`.  
Type: String  
Valid Values: `SSO_USER | SSO_GROUP`   
Required: Yes

## See Also
<a name="API_SsoIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/SsoIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/SsoIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/SsoIdentity) 