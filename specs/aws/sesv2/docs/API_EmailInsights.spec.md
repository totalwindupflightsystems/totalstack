---
id: "@specs/aws/sesv2/docs/API_EmailInsights"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EmailInsights"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EmailInsights

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EmailInsights
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EmailInsights
<a name="API_EmailInsights"></a>

An email's insights contain metadata and delivery information about a specific email.

## Contents
<a name="API_EmailInsights_Contents"></a>

 ** Destination **   <a name="SES-Type-EmailInsights-Destination"></a>
The recipient of the email.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 320.  
Required: No

 ** Events **   <a name="SES-Type-EmailInsights-Events"></a>
A list of events associated with the sent email.  
Type: Array of [InsightsEvent](API_InsightsEvent.md) objects  
Required: No

 ** Isp **   <a name="SES-Type-EmailInsights-Isp"></a>
The recipient's ISP (e.g., `Gmail`, `Yahoo`, etc.).  
Type: String  
Required: No

## See Also
<a name="API_EmailInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EmailInsights) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EmailInsights) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EmailInsights) 