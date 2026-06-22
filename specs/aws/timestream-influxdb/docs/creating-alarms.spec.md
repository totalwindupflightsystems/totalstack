---
id: "@specs/aws/timestream-influxdb/docs/creating-alarms"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating alarms"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Creating alarms

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/creating-alarms
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Creating CloudWatch alarms to monitor Timestream for LiveAnalytics
<a name="creating-alarms"></a>

You can create an Amazon CloudWatch alarm for Timestream for LiveAnalytics that sends an Amazon Simple Notification Service (Amazon SNS) message when the alarm changes state. An alarm watches a single metric over a time period that you specify. It performs one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon SNS topic or Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms do not invoke actions simply because they are in a particular state. The state must have changed and been maintained for a specified number of periods.

For more information about creating CloudWatch alarms, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.