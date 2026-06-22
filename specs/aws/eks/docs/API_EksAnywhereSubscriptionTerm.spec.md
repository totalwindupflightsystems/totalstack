---
id: "@specs/aws/eks/docs/API_EksAnywhereSubscriptionTerm"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksAnywhereSubscriptionTerm"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# EksAnywhereSubscriptionTerm

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_EksAnywhereSubscriptionTerm
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksAnywhereSubscriptionTerm
<a name="API_EksAnywhereSubscriptionTerm"></a>

An object representing the term duration and term unit type of your subscription. This determines the term length of your subscription. Valid values are MONTHS for term unit and 12 or 36 for term duration, indicating a 12 month or 36 month subscription.

## Contents
<a name="API_EksAnywhereSubscriptionTerm_Contents"></a>

 ** duration **   <a name="AmazonEKS-Type-EksAnywhereSubscriptionTerm-duration"></a>
The duration of the subscription term. Valid values are 12 and 36, indicating a 12 month or 36 month subscription.  
Type: Integer  
Required: No

 ** unit **   <a name="AmazonEKS-Type-EksAnywhereSubscriptionTerm-unit"></a>
The term unit of the subscription. Valid value is `MONTHS`.  
Type: String  
Valid Values: `MONTHS`   
Required: No

## See Also
<a name="API_EksAnywhereSubscriptionTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/EksAnywhereSubscriptionTerm) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/EksAnywhereSubscriptionTerm) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/EksAnywhereSubscriptionTerm) 