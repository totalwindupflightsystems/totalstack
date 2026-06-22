---
id: "@specs/aws/sesv2/docs/API_GuardianOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GuardianOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GuardianOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GuardianOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GuardianOptions
<a name="API_GuardianOptions"></a>

An object containing additional settings for your VDM configuration as applicable to the Guardian.

## Contents
<a name="API_GuardianOptions_Contents"></a>

 ** OptimizedSharedDelivery **   <a name="SES-Type-GuardianOptions-OptimizedSharedDelivery"></a>
Specifies the status of your VDM optimized shared delivery. Can be one of the following:  
+  `ENABLED` – Amazon SES enables optimized shared delivery for the configuration set.
+  `DISABLED` – Amazon SES disables optimized shared delivery for the configuration set.
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_GuardianOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GuardianOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GuardianOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GuardianOptions) 