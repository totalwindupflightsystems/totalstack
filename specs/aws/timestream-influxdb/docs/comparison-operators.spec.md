---
id: "@specs/aws/timestream-influxdb/docs/comparison-operators"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Comparison operators"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Comparison operators

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/comparison-operators
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Comparison operators
<a name="comparison-operators"></a>

Timestream for LiveAnalytics supports the following comparison operators.


| Operator | Description | 
| --- | --- | 
| < | Less than | 
| > | Greater than | 
| <= | Less than or equal to | 
| >= | Greater than or equal to | 
| = | Equal | 
| <> | Not equal | 
| \!= | Not equal | 

**Note**  
The `BETWEEN` operator tests if a value is within a specified range. The syntax is as follows:  

  ```
  BETWEEN min AND max
  ```
The presence of `NULL` in a `BETWEEN` or `NOT BETWEEN` statement will result in the statement evaluating to `NULL`.
`IS NULL `and `IS NOT NULL` operators test whether a value is null (undefined). Using `NULL` with `IS NULL` evaluates to true.
In SQL, a `NULL` value signifies an unknown value.