---
id: "@specs/aws/sesv2/docs/API_BatchGetMetricDataQuery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchGetMetricDataQuery"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# BatchGetMetricDataQuery

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_BatchGetMetricDataQuery
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchGetMetricDataQuery
<a name="API_BatchGetMetricDataQuery"></a>

Represents a single metric data query to include in a batch.

## Contents
<a name="API_BatchGetMetricDataQuery_Contents"></a>

 ** EndDate **   <a name="SES-Type-BatchGetMetricDataQuery-EndDate"></a>
Represents the end date for the query interval.  
Type: Timestamp  
Required: Yes

 ** Id **   <a name="SES-Type-BatchGetMetricDataQuery-Id"></a>
The query identifier.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** Metric **   <a name="SES-Type-BatchGetMetricDataQuery-Metric"></a>
The queried metric. This can be one of the following:  
+  `SEND` – Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.
+  `COMPLAINT` – Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient
+  `PERMANENT_BOUNCE` – Permanent bounces - i.e. feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.
+  `TRANSIENT_BOUNCE` – Transient bounces - i.e. feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.
+  `OPEN` – Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
+  `CLICK` – Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.
+  `DELIVERY` – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.
+  `DELIVERY_OPEN` – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.
+  `DELIVERY_CLICK` – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.
+  `DELIVERY_COMPLAINT` – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.
Type: String  
Valid Values: `SEND | COMPLAINT | PERMANENT_BOUNCE | TRANSIENT_BOUNCE | OPEN | CLICK | DELIVERY | DELIVERY_OPEN | DELIVERY_CLICK | DELIVERY_COMPLAINT`   
Required: Yes

 ** Namespace **   <a name="SES-Type-BatchGetMetricDataQuery-Namespace"></a>
The query namespace - e.g. `VDM`   
Type: String  
Valid Values: `VDM`   
Required: Yes

 ** StartDate **   <a name="SES-Type-BatchGetMetricDataQuery-StartDate"></a>
Represents the start date for the query interval.  
Type: Timestamp  
Required: Yes

 ** Dimensions **   <a name="SES-Type-BatchGetMetricDataQuery-Dimensions"></a>
An object that contains mapping between `MetricDimensionName` and `MetricDimensionValue` to filter metrics by.  
Type: String to string map  
Map Entries: Maximum number of 3 items.  
Valid Keys: `EMAIL_IDENTITY | CONFIGURATION_SET | ISP`   
Required: No

## See Also
<a name="API_BatchGetMetricDataQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/BatchGetMetricDataQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/BatchGetMetricDataQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/BatchGetMetricDataQuery) 