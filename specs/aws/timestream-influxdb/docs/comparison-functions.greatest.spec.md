---
id: "@specs/aws/timestream-influxdb/docs/comparison-functions.greatest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS greatest()"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# greatest()

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/comparison-functions.greatest
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# greatest()
<a name="comparison-functions.greatest"></a>

The **greatest()** function returns the largest of the provided values. It returns `NULL` if any of the provided values are `NULL`. The syntax is as follows.

```
greatest(value1, value2, ..., valueN) 
```