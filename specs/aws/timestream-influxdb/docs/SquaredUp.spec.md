---
id: "@specs/aws/timestream-influxdb/docs/SquaredUp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SquaredUp"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# SquaredUp

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/SquaredUp
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Using SquaredUp to work with Amazon Timestream
<a name="SquaredUp"></a>

[SquaredUp](https://SquaredUp.com/) is an observability platform that integrates with Amazon Timestream. You can use SquaredUp's intuitive dashboard designer to visualize, analyze, and monitor your time-series data. Dashboards can be shared publicly or privately, and notification channels can be created to alert you when the health state of a monitor changes.

## Using SquaredUp with Amazon Timestream
<a name="SquaredUp-using"></a>

1. [Sign up](https://app.squaredup.com/?signup=true) for [SquaredUp](https://squaredup.com/) and get started for free.

1. Add an [AWS data source](https://squaredup.com/cloud/pluginsetup-aws).

1. Create a dashboard tile that uses the [Timestream Query](https://squaredup.com/cloud/AWS-Timestream-Query) data stream.

1. Optionally, enable monitoring for the tile, create a notification channel, or share the dashboard publicly or privately.

1. Optionally create other tiles to see your Timestream data alongside data from your other monitoring and observability tools.