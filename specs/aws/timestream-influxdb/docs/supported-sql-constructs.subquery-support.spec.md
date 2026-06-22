---
id: "@specs/aws/timestream-influxdb/docs/supported-sql-constructs.subquery-support"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Subquery support"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Subquery support

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/supported-sql-constructs.subquery-support
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Subquery support
<a name="supported-sql-constructs.subquery-support"></a>

 Timestream supports subqueries in `EXISTS` and `IN` predicates. The `EXISTS` predicate determines if a subquery returns any rows. The `IN` predicate determines if values produced by the subquery match the values or expression of in IN clause. The Timestream query language supports correlated and other subqueries. 

```
SELECT t.c1
FROM (VALUES 1, 2, 3, 4, 5) AS t(c1)
WHERE EXISTS
(SELECT t.c2
 FROM (VALUES 1, 2, 3) AS t(c2)
 WHERE t.c1= t.c2
)
ORDER BY t.c1
```


| c1 | 
| --- | 
| 1 | 
| 2 | 
| 3 | 

```
SELECT t.c1
FROM (VALUES 1, 2, 3, 4, 5) AS t(c1)
WHERE t.c1 IN
(SELECT t.c2
 FROM (VALUES 2, 3, 4) AS t(c2)
)
ORDER BY t.c1
```


| c1 | 
| --- | 
| 2 | 
| 3 | 
| 4 | 