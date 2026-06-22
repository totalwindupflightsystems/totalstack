---
id: "@specs/aws/sesv2/docs/API_IspPlacement"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IspPlacement"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# IspPlacement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_IspPlacement
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IspPlacement
<a name="API_IspPlacement"></a>

An object that describes how email sent during the predictive inbox placement test was handled by a certain email provider.

## Contents
<a name="API_IspPlacement_Contents"></a>

 ** IspName **   <a name="SES-Type-IspPlacement-IspName"></a>
The name of the email provider that the inbox placement data applies to.  
Type: String  
Required: No

 ** PlacementStatistics **   <a name="SES-Type-IspPlacement-PlacementStatistics"></a>
An object that contains inbox placement metrics for a specific email provider.  
Type: [PlacementStatistics](API_PlacementStatistics.md) object  
Required: No

## See Also
<a name="API_IspPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/IspPlacement) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/IspPlacement) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/IspPlacement) 