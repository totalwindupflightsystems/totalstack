---
id: "@specs/aws/timestream-influxdb/docs/conditional-expressions.NULLIF"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NULLIF statement"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# NULLIF statement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/conditional-expressions.NULLIF
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# The NULLIF statement
<a name="conditional-expressions.NULLIF"></a>

The **IF** statement evaluates a condition to be true or false and returns the appropriate value. Timestream supports the following two syntax representations for **IF**:

**NULLIF** returns null if `value1` equals `value2`; otherwise it returns `value1`. The syntax is as follows:

```
nullif(value1, value2)
```