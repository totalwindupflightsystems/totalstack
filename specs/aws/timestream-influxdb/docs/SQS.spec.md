---
id: "@specs/aws/timestream-influxdb/docs/SQS"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon SQS"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon SQS

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/SQS
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon SQS
<a name="SQS"></a>

## Using EventBridge Pipes to send Amazon SQS data to Timestream
<a name="SQS-via-pipes"></a>

You can use EventBridge Pipes to send data from a Amazon SQS queue to a Amazon Timestream for LiveAnalytics table.

Pipes are intended for point-to-point integrations between supported sources and targets, with support for advanced transformations and enrichment. Pipes reduce the need for specialized knowledge and integration code when developing event-driven architectures. To set up a pipe, you choose the source, add optional filtering, define optional enrichment, and choose the target for the event data.

![A source sends events to an EventBridge pipe, which filters and routes matching events to the target.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/pipes-overview_shared_architecture.png)


For more information on EventBridge Pipes, see [EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) in the *EventBridge User Guide*. For information on configuring a pipe to deliver events to a Amazon Timestream for LiveAnalytics table, see [EventBridge Pipes target specifics](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-targets-specifics.html#pipes-targets-specifics-timestream).