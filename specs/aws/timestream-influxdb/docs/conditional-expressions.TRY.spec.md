---
id: "@specs/aws/timestream-influxdb/docs/conditional-expressions.TRY"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TRY statement"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# TRY statement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/conditional-expressions.TRY
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# The TRY statement
<a name="conditional-expressions.TRY"></a>

The **TRY** function evaluates an expression and handles certain types of errors by returning `null`. The syntax is as follows:

```
try(expression)
```