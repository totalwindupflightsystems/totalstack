---
id: "@specs/aws/sesv2/docs/API_ExportMetric"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExportMetric"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ExportMetric

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ExportMetric
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExportMetric
<a name="API_ExportMetric"></a>

An object that contains a mapping between a `Metric` and `MetricAggregation`.

## Contents
<a name="API_ExportMetric_Contents"></a>

 ** Aggregation **   <a name="SES-Type-ExportMetric-Aggregation"></a>
The aggregation to apply to a metric, can be one of the following:  
+  `VOLUME` - The volume of events for this metric.
+  `RATE` - The rate for this metric relative to the `SEND` metric volume.
Type: String  
Valid Values: `RATE | VOLUME`   
Required: No

 ** Name **   <a name="SES-Type-ExportMetric-Name"></a>
The metric to export, can be one of the following:  
+  `SEND` - Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.
+  `COMPLAINT` - Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient
+  `PERMANENT_BOUNCE` - Permanent bounces - i.e., feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.
+  `TRANSIENT_BOUNCE` - Transient bounces - i.e., feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.
+  `OPEN` - Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
+  `CLICK` - Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.
+  `DELIVERY` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.
+  `DELIVERY_OPEN` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.
+  `DELIVERY_CLICK` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.
+  `DELIVERY_COMPLAINT` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.
Type: String  
Valid Values: `SEND | COMPLAINT | PERMANENT_BOUNCE | TRANSIENT_BOUNCE | OPEN | CLICK | DELIVERY | DELIVERY_OPEN | DELIVERY_CLICK | DELIVERY_COMPLAINT`   
Required: No

## See Also
<a name="API_ExportMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ExportMetric) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ExportMetric) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ExportMetric) 