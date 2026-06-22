---
id: "@specs/aws/timestream-influxdb/docs/metering-and-pricing.queries"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Queries"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Queries

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/metering-and-pricing.queries
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Queries
<a name="metering-and-pricing.queries"></a>

Queries are charged based on the duration of [Timestream compute units (TCUs)](tcu.md) used by your application in TCU-hours as specified on the [Amazon Timestream pricing](https://aws.amazon.com/timestream/pricing/) page. Amazon Timestream for LiveAnalytics' query engine prunes irrelevant data while processing a query. Queries with projections and predicates including time ranges, measure names, and/or dimension names enable the query processing engine to prune a significant amount of data and help with lowering query costs.