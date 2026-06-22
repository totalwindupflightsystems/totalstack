---
id: "@specs/aws/sesv2/docs/API_InsightsEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InsightsEvent"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# InsightsEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_InsightsEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InsightsEvent
<a name="API_InsightsEvent"></a>

An object containing details about a specific event.

## Contents
<a name="API_InsightsEvent_Contents"></a>

 ** Details **   <a name="SES-Type-InsightsEvent-Details"></a>
Details about bounce or complaint events.  
Type: [EventDetails](API_EventDetails.md) object  
Required: No

 ** Timestamp **   <a name="SES-Type-InsightsEvent-Timestamp"></a>
The timestamp of the event.  
Type: Timestamp  
Required: No

 ** Type **   <a name="SES-Type-InsightsEvent-Type"></a>
The type of event:  
+  `SEND` - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.) 
+  `DELIVERY` - SES successfully delivered the email to the recipient's mail server. Excludes deliveries to the mailbox simulator, and those from emails addressed to more than one recipient. 
+  `BOUNCE` - Feedback received for delivery failures. Additional details about the bounce are provided in the `Details` object. Excludes bounces from the mailbox simulator, and those from emails addressed to more than one recipient. 
+  `COMPLAINT` - Complaint received for the email. Additional details about the complaint are provided in the `Details` object. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient. 
+  `OPEN` - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
+  `CLICK` - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.
Type: String  
Valid Values: `SEND | REJECT | BOUNCE | COMPLAINT | DELIVERY | OPEN | CLICK | RENDERING_FAILURE | DELIVERY_DELAY | SUBSCRIPTION`   
Required: No

## See Also
<a name="API_InsightsEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/InsightsEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/InsightsEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/InsightsEvent) 