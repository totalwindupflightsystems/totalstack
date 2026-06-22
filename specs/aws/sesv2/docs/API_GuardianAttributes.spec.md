---
id: "@specs/aws/sesv2/docs/API_GuardianAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GuardianAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GuardianAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GuardianAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GuardianAttributes
<a name="API_GuardianAttributes"></a>

An object containing additional settings for your VDM configuration as applicable to the Guardian.

## Contents
<a name="API_GuardianAttributes_Contents"></a>

 ** OptimizedSharedDelivery **   <a name="SES-Type-GuardianAttributes-OptimizedSharedDelivery"></a>
Specifies the status of your VDM optimized shared delivery. Can be one of the following:  
+  `ENABLED` – Amazon SES enables optimized shared delivery for your account.
+  `DISABLED` – Amazon SES disables optimized shared delivery for your account.
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_GuardianAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GuardianAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GuardianAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GuardianAttributes) 