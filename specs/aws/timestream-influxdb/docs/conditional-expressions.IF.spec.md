---
id: "@specs/aws/timestream-influxdb/docs/conditional-expressions.IF"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IF statement"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# IF statement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/conditional-expressions.IF
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# The IF statement
<a name="conditional-expressions.IF"></a>

The **IF** statement evaluates a condition to be true or false and returns the appropriate value. Timestream supports the following two syntax representations for **IF**:

```
if(condition, true_value)
```

This syntax evaluates and returns `true_value` if condition is `true`; otherwise `null` is returned and `true_value` is not evaluated.

```
if(condition, true_value, false_value)
```

This syntax evaluates and returns `true_value` if condition is `true`, otherwise evaluates and returns `false_value`.

## Examples
<a name="conditional-expressions.IF.examples"></a>

```
SELECT
  if(true, 'example 1'),
  if(false, 'example 2'),
  if(true, 'example 3 true', 'example 3 false'),
  if(false, 'example 4 true', 'example 4 false')
```


| \_col0 | \_col1 | \_col2 | \_col3 | 
| --- | --- | --- | --- | 
| `example 1` | `-`<br />`null` | `example 3 true` | `example 4 false` | 