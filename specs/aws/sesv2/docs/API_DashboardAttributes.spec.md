---
id: "@specs/aws/sesv2/docs/API_DashboardAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DashboardAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DashboardAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DashboardAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DashboardAttributes
<a name="API_DashboardAttributes"></a>

An object containing additional settings for your VDM configuration as applicable to the Dashboard.

## Contents
<a name="API_DashboardAttributes_Contents"></a>

 ** EngagementMetrics **   <a name="SES-Type-DashboardAttributes-EngagementMetrics"></a>
Specifies the status of your VDM engagement metrics collection. Can be one of the following:  
+  `ENABLED` – Amazon SES enables engagement metrics for your account.
+  `DISABLED` – Amazon SES disables engagement metrics for your account.
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_DashboardAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DashboardAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DashboardAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DashboardAttributes) 