---
id: "@specs/aws/sesv2/docs/API_EventDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EventDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EventDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventDestination
<a name="API_EventDestination"></a>

In the Amazon SES API v2, *events* include message sends, deliveries, opens, clicks, bounces, complaints and delivery delays. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

## Contents
<a name="API_EventDestination_Contents"></a>

 ** MatchingEventTypes **   <a name="SES-Type-EventDestination-MatchingEventTypes"></a>
The types of events that Amazon SES sends to the specified event destinations.  
+  `SEND` - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)
+  `REJECT` - SES accepted the email, but determined that it contained a virus and didn’t attempt to deliver it to the recipient’s mail server.
+  `BOUNCE` - (*Hard bounce*) The recipient's mail server permanently rejected the email. (*Soft bounces* are only included when SES fails to deliver the email after retrying for a period of time.)
+  `COMPLAINT` - The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam.
+  `DELIVERY` - SES successfully delivered the email to the recipient's mail server.
+  `OPEN` - The recipient received the message and opened it in their email client.
+  `CLICK` - The recipient clicked one or more links in the email.
+  `RENDERING_FAILURE` - The email wasn't sent because of a template rendering issue. This event type can occur when template data is missing, or when there is a mismatch between template parameters and data. (This event type only occurs when you send email using the [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) or [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendBulkEmail.html](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendBulkEmail.html) API operations.) 
+  `DELIVERY_DELAY` - The email couldn't be delivered to the recipient’s mail server because a temporary issue occurred. Delivery delays can occur, for example, when the recipient's inbox is full, or when the receiving email server experiences a transient issue.
+  `SUBSCRIPTION` - The email was successfully delivered, but the recipient updated their subscription preferences by clicking on an *unsubscribe* link as part of your [subscription management](https://docs.aws.amazon.com/ses/latest/dg/sending-email-subscription-management.html).
Type: Array of strings  
Valid Values: `SEND | REJECT | BOUNCE | COMPLAINT | DELIVERY | OPEN | CLICK | RENDERING_FAILURE | DELIVERY_DELAY | SUBSCRIPTION`   
Required: Yes

 ** Name **   <a name="SES-Type-EventDestination-Name"></a>
A name that identifies the event destination.  
Type: String  
Required: Yes

 ** CloudWatchDestination **   <a name="SES-Type-EventDestination-CloudWatchDestination"></a>
An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.  
Type: [CloudWatchDestination](API_CloudWatchDestination.md) object  
Required: No

 ** Enabled **   <a name="SES-Type-EventDestination-Enabled"></a>
If `true`, the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this `EventDestinationDefinition`.  
If `false`, the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.  
Type: Boolean  
Required: No

 ** EventBridgeDestination **   <a name="SES-Type-EventDestination-EventBridgeDestination"></a>
An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.  
Type: [EventBridgeDestination](API_EventBridgeDestination.md) object  
Required: No

 ** KinesisFirehoseDestination **   <a name="SES-Type-EventDestination-KinesisFirehoseDestination"></a>
An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.  
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object  
Required: No

 ** PinpointDestination **   <a name="SES-Type-EventDestination-PinpointDestination"></a>
An object that defines an Amazon Pinpoint project destination for email events. You can send email event data to a Amazon Pinpoint project to view metrics using the Transactional Messaging dashboards that are built in to Amazon Pinpoint. For more information, see [Transactional Messaging Charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-transactional-messages.html) in the *Amazon Pinpoint User Guide*.  
Type: [PinpointDestination](API_PinpointDestination.md) object  
Required: No

 ** SnsDestination **   <a name="SES-Type-EventDestination-SnsDestination"></a>
An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notifications when certain email events occur.  
Type: [SnsDestination](API_SnsDestination.md) object  
Required: No

## See Also
<a name="API_EventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EventDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EventDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EventDestination) 