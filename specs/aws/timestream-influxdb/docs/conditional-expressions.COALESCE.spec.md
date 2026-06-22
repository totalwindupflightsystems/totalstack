---
id: "@specs/aws/timestream-influxdb/docs/conditional-expressions.COALESCE"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS COALESCE statement"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# COALESCE statement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/conditional-expressions.COALESCE
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# The COALESCE statement
<a name="conditional-expressions.COALESCE"></a>

 **COALESCE** returns the first non-null value in an argument list. The syntax is as follows:

```
coalesce(value1, value2[,...])
```