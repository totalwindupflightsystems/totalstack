---
id: "@specs/aws/sesv2/docs/API_DomainDeliverabilityCampaign"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DomainDeliverabilityCampaign"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DomainDeliverabilityCampaign

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DomainDeliverabilityCampaign
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DomainDeliverabilityCampaign
<a name="API_DomainDeliverabilityCampaign"></a>

An object that contains the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (`PutDeliverabilityDashboardOption` operation).

## Contents
<a name="API_DomainDeliverabilityCampaign_Contents"></a>

 ** CampaignId **   <a name="SES-Type-DomainDeliverabilityCampaign-CampaignId"></a>
The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.  
Type: String  
Required: No

 ** DeleteRate **   <a name="SES-Type-DomainDeliverabilityCampaign-DeleteRate"></a>
The percentage of email messages that were deleted by recipients, without being opened first. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.  
Type: Double  
Required: No

 ** Esps **   <a name="SES-Type-DomainDeliverabilityCampaign-Esps"></a>
The major email providers who handled the email message.  
Type: Array of strings  
Required: No

 ** FirstSeenDateTime **   <a name="SES-Type-DomainDeliverabilityCampaign-FirstSeenDateTime"></a>
The first time when the email message was delivered to any recipient's inbox. This value can help you determine how long it took for a campaign to deliver an email message.  
Type: Timestamp  
Required: No

 ** FromAddress **   <a name="SES-Type-DomainDeliverabilityCampaign-FromAddress"></a>
The verified email address that the email message was sent from.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** ImageUrl **   <a name="SES-Type-DomainDeliverabilityCampaign-ImageUrl"></a>
The URL of an image that contains a snapshot of the email message that was sent.  
Type: String  
Required: No

 ** InboxCount **   <a name="SES-Type-DomainDeliverabilityCampaign-InboxCount"></a>
The number of email messages that were delivered to recipients’ inboxes.  
Type: Long  
Required: No

 ** LastSeenDateTime **   <a name="SES-Type-DomainDeliverabilityCampaign-LastSeenDateTime"></a>
The last time when the email message was delivered to any recipient's inbox. This value can help you determine how long it took for a campaign to deliver an email message.  
Type: Timestamp  
Required: No

 ** ProjectedVolume **   <a name="SES-Type-DomainDeliverabilityCampaign-ProjectedVolume"></a>
The projected number of recipients that the email message was sent to.  
Type: Long  
Required: No

 ** ReadDeleteRate **   <a name="SES-Type-DomainDeliverabilityCampaign-ReadDeleteRate"></a>
The percentage of email messages that were opened and then deleted by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.  
Type: Double  
Required: No

 ** ReadRate **   <a name="SES-Type-DomainDeliverabilityCampaign-ReadRate"></a>
The percentage of email messages that were opened by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.  
Type: Double  
Required: No

 ** SendingIps **   <a name="SES-Type-DomainDeliverabilityCampaign-SendingIps"></a>
The IP addresses that were used to send the email message.  
Type: Array of strings  
Required: No

 ** SpamCount **   <a name="SES-Type-DomainDeliverabilityCampaign-SpamCount"></a>
The number of email messages that were delivered to recipients' spam or junk mail folders.  
Type: Long  
Required: No

 ** Subject **   <a name="SES-Type-DomainDeliverabilityCampaign-Subject"></a>
The subject line, or title, of the email message.  
Type: String  
Required: No

## See Also
<a name="API_DomainDeliverabilityCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DomainDeliverabilityCampaign) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DomainDeliverabilityCampaign) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DomainDeliverabilityCampaign) 