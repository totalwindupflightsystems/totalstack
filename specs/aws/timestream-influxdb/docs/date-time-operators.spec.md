---
id: "@specs/aws/timestream-influxdb/docs/date-time-operators"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Date / time operators"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Date / time operators

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/date-time-operators
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Date / time operators
<a name="date-time-operators"></a>

**Note**  
Timestream for LiveAnalytics does not support negative time values. Any operation resulting in negative time results in error.

Timestream for LiveAnalytics supports the following operations on `timestamps`, `dates`, and `intervals`.


| Operator | Description | 
| --- | --- | 
| \+ | Addition | 
| - | Subtraction | 

**Topics**
+ [Operations](#date-time-operators-operations)
+ [Addition](#date-time-operators-addition)
+ [Subtraction](#date-time-operators-subtraction)

## Operations
<a name="date-time-operators-operations"></a>

The result type of an operation is based on the operands. Interval literals such as `1day` and `3s` can be used.

```
SELECT date '2022-05-21' + interval '2' day
```

```
SELECT date '2022-05-21' + 2d
```

```
SELECT date '2022-05-21' + 2day
```

Example result for each: `2022-05-23`

Interval units include `second`, `minute`, `hour`, `day`, `week`, `month`, and `year`. But in some cases not all are applicable. For example seconds, minutes, and hours can not be added to or subtracted from a date.

```
SELECT interval '4' year + interval '2' month
```

Example result: `4-2`

```
SELECT typeof(interval '4' year + interval '2' month)
```

Example result: `interval year to month`

Result type of interval operations may be `'interval year to month'` or `'interval day to second'` depending on the operands. Intervals can be added to or subtracted from `dates` and `timestamps`. But a `date` or `timestamp` cannot be added to or subtracted from a `date` or `timestamp`. To find intervals or durations related to dates or timestamps, see `date_diff` and related functions in [Interval and duration](date-time-functions.md#date-time-functions-interval-duration).

## Addition
<a name="date-time-operators-addition"></a>

**Example**  

```
SELECT date '2022-05-21' + interval '2' day
```
Example result: `2022-05-23`

**Example**  

```
SELECT typeof(date '2022-05-21' + interval '2' day)
```
Example result: `date`

**Example**  

```
SELECT interval '2' year + interval '4' month
```
Example result: `2-4`

**Example**  

```
SELECT typeof(interval '2' year + interval '4' month)
```
Example result: `interval year to month`

## Subtraction
<a name="date-time-operators-subtraction"></a>

**Example**  

```
SELECT timestamp '2022-06-17 01:00' - interval '7' hour
```
Example result: `2022-06-16 18:00:00.000000000`

**Example**  

```
SELECT typeof(timestamp '2022-06-17 01:00' - interval '7' hour)
```
Example result: `timestamp`

**Example**  

```
SELECT interval '6' day - interval '4' hour
```
Example result: `5 20:00:00.000000000`

**Example**  

```
SELECT typeof(interval '6' day - interval '4' hour)
```
Example result: `interval day to second`