---
id: "@specs/aws/lightsail/docs/amazon-lightsail-notifications"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Metric notifications"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Metric notifications

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-notifications
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure metric notifications for Lightsail resources
<a name="amazon-lightsail-notifications"></a>

You can configure Lightsail to notify you when a metric for one of your instances, databases, load balancers, or content delivery network (CDN) distributions crosses a specified threshold. Notifications can be in the form of a banner displayed in the Lightsail console, an email sent to an address you specify, or an SMS text message sent to a mobile phone number you specify. For more information on how to review your contacts pending verification for notifications, see [Review email contacts pending verification](amazon-lightsail-alarm-notifications.md#amazon-lightsail-alarm-notifications-review-contacts).

To get notifications, you must configure an alarm that monitors a metric for one of your resources. For example, you can configure an alarm that notifies you when your instance's outgoing network traffic is greater than 500 kilobytes during a specified length of time. For more information, see [Metric alarms](amazon-lightsail-alarms.md).

When an alarm is triggered, a notification banner is displayed in the Lightsail console. To be notified by email and SMS text message, you must add your email address and mobile phone number as notification contacts in each AWS Region where you want to monitor your resources. For more information, see [Add notification contacts](amazon-lightsail-adding-editing-notification-contacts.md).

**Note**  
SMS text messaging is not supported in all AWS Regions in which you can create Lightsail resources, and text messages cannot be sent to some countries and regions of the world. For more information, see [Add notification contacts](amazon-lightsail-adding-editing-notification-contacts.md).

If don't receive notifications when you expect to be notified, then there are a few things you should check to confirm that your notification contacts are configured correctly. To learn more, see [Troubleshoot notifications](amazon-lightsail-troubleshooting-notifications.md).

To stop receiving notifications, you can remove your email and mobile phone from Lightsail. For more information, see [Delete or disable metric alarms](amazon-lightsail-deleting-notification-contacts.md). You can also disable or delete an alarm to stop receiving notifications for a specific alarm. For more information, see [Delete or disable metric alarms](amazon-lightsail-deleting-health-metric-alarms.md).