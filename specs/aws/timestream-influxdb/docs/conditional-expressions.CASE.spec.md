---
id: "@specs/aws/timestream-influxdb/docs/conditional-expressions.CASE"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CASE statement"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# CASE statement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/conditional-expressions.CASE
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# The CASE statement
<a name="conditional-expressions.CASE"></a>

The **CASE** statement searches each value expression from left to right until it finds one that equals `expression`. If it finds a match, the result for the matching value is returned. If no match is found, the result from the `ELSE` clause is returned if it exists; otherwise `null` is returned. The syntax is as follows:

```
CASE expression
    WHEN value THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
```

 Timestream also supports the following syntax for **CASE** statements. In this syntax, the "searched" form evaluates each boolean condition from left to right until one is `true` and returns the matching result. If no conditions are `true`, the result from the `ELSE` clause is returned if it exists; otherwise `null` is returned. See below for the alternate syntax: 

```
CASE
    WHEN condition THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
```