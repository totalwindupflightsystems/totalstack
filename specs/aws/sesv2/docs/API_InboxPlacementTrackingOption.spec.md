---
id: "@specs/aws/sesv2/docs/API_InboxPlacementTrackingOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InboxPlacementTrackingOption"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# InboxPlacementTrackingOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_InboxPlacementTrackingOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InboxPlacementTrackingOption
<a name="API_InboxPlacementTrackingOption"></a>

An object that contains information about the inbox placement data settings for a verified domain that’s associated with your AWS account. This data is available only if you enabled the Deliverability dashboard for the domain.

## Contents
<a name="API_InboxPlacementTrackingOption_Contents"></a>

 ** Global **   <a name="SES-Type-InboxPlacementTrackingOption-Global"></a>
Specifies whether inbox placement data is being tracked for the domain.  
Type: Boolean  
Required: No

 ** TrackedIsps **   <a name="SES-Type-InboxPlacementTrackingOption-TrackedIsps"></a>
An array of strings, one for each major email provider that the inbox placement data applies to.  
Type: Array of strings  
Required: No

## See Also
<a name="API_InboxPlacementTrackingOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/InboxPlacementTrackingOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/InboxPlacementTrackingOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/InboxPlacementTrackingOption) 