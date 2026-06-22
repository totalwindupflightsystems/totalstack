---
id: "@specs/aws/sesv2/docs/API_DomainDeliverabilityTrackingOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DomainDeliverabilityTrackingOption"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DomainDeliverabilityTrackingOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DomainDeliverabilityTrackingOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DomainDeliverabilityTrackingOption
<a name="API_DomainDeliverabilityTrackingOption"></a>

An object that contains information about the Deliverability dashboard subscription for a verified domain that you use to send email and currently has an active Deliverability dashboard subscription. If a Deliverability dashboard subscription is active for a domain, you gain access to reputation, inbox placement, and other metrics for the domain.

## Contents
<a name="API_DomainDeliverabilityTrackingOption_Contents"></a>

 ** Domain **   <a name="SES-Type-DomainDeliverabilityTrackingOption-Domain"></a>
A verified domain that’s associated with your AWS account and currently has an active Deliverability dashboard subscription.  
Type: String  
Required: No

 ** InboxPlacementTrackingOption **   <a name="SES-Type-DomainDeliverabilityTrackingOption-InboxPlacementTrackingOption"></a>
An object that contains information about the inbox placement data settings for the domain.  
Type: [InboxPlacementTrackingOption](API_InboxPlacementTrackingOption.md) object  
Required: No

 ** SubscriptionStartDate **   <a name="SES-Type-DomainDeliverabilityTrackingOption-SubscriptionStartDate"></a>
The date when you enabled the Deliverability dashboard for the domain.  
Type: Timestamp  
Required: No

## See Also
<a name="API_DomainDeliverabilityTrackingOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DomainDeliverabilityTrackingOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DomainDeliverabilityTrackingOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DomainDeliverabilityTrackingOption) 