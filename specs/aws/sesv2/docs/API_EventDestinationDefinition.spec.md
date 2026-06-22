---
id: "@specs/aws/sesv2/docs/API_EventDestinationDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventDestinationDefinition"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EventDestinationDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EventDestinationDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventDestinationDefinition
<a name="API_EventDestinationDefinition"></a>

An object that defines the event destination. Specifically, it defines which services receive events from emails sent using the configuration set that the event destination is associated with. Also defines the types of events that are sent to the event destination.

## Contents
<a name="API_EventDestinationDefinition_Contents"></a>

 ** CloudWatchDestination **   <a name="SES-Type-EventDestinationDefinition-CloudWatchDestination"></a>
An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.  
Type: [CloudWatchDestination](API_CloudWatchDestination.md) object  
Required: No

 ** Enabled **   <a name="SES-Type-EventDestinationDefinition-Enabled"></a>
If `true`, the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this `EventDestinationDefinition`.  
If `false`, the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.  
Type: Boolean  
Required: No

 ** EventBridgeDestination **   <a name="SES-Type-EventDestinationDefinition-EventBridgeDestination"></a>
An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.  
Type: [EventBridgeDestination](API_EventBridgeDestination.md) object  
Required: No

 ** KinesisFirehoseDestination **   <a name="SES-Type-EventDestinationDefinition-KinesisFirehoseDestination"></a>
An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.  
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object  
Required: No

 ** MatchingEventTypes **   <a name="SES-Type-EventDestinationDefinition-MatchingEventTypes"></a>
An array that specifies which events the Amazon SES API v2 should send to the destinations in this `EventDestinationDefinition`.  
Type: Array of strings  
Valid Values: `SEND | REJECT | BOUNCE | COMPLAINT | DELIVERY | OPEN | CLICK | RENDERING_FAILURE | DELIVERY_DELAY | SUBSCRIPTION`   
Required: No

 ** PinpointDestination **   <a name="SES-Type-EventDestinationDefinition-PinpointDestination"></a>
An object that defines an Amazon Pinpoint project destination for email events. You can send email event data to a Amazon Pinpoint project to view metrics using the Transactional Messaging dashboards that are built in to Amazon Pinpoint. For more information, see [Transactional Messaging Charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-transactional-messages.html) in the *Amazon Pinpoint User Guide*.  
Type: [PinpointDestination](API_PinpointDestination.md) object  
Required: No

 ** SnsDestination **   <a name="SES-Type-EventDestinationDefinition-SnsDestination"></a>
An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notifications when certain email events occur.  
Type: [SnsDestination](API_SnsDestination.md) object  
Required: No

## See Also
<a name="API_EventDestinationDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EventDestinationDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EventDestinationDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EventDestinationDefinition) 