---
id: "@specs/aws/timestream-influxdb/docs/comparison-functions.least"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS least()"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# least()

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/comparison-functions.least
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# least()
<a name="comparison-functions.least"></a>

The **least()** function returns the smallest of the provided values. It returns `NULL` if any of the provided values are `NULL`. The syntax is as follows.

```
least(value1, value2, ..., valueN) 
```