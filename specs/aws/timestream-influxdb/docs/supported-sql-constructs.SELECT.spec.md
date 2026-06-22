---
id: "@specs/aws/timestream-influxdb/docs/supported-sql-constructs.SELECT"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SELECT"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# SELECT

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/supported-sql-constructs.SELECT
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# SELECT
<a name="supported-sql-constructs.SELECT"></a>

**SELECT** statements can be used to retrieve data from one or more tables. Timestream's query language supports the following syntax for **SELECT** statements:

```
[ WITH with_query [, ...] ]
            SELECT [ ALL | DISTINCT ] select_expr [, ...]
            [ function (expression) OVER (
            [ PARTITION BY partition_expr_list ]
            [ ORDER BY order_list ]
            [ frame_clause ] )
            [ FROM from_item [, ...] ]
            [ WHERE condition ]
            [ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
            [ HAVING condition]
            [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
            [ ORDER BY order_list ]
            [ LIMIT [ count | ALL ] ]
```

where 
+ `function (expression)` is one of the supported [window functions](window-functions.md).
+ `partition_expr_list` is:

  ```
  expression | column_name [, expr_list ]
  ```
+ `order_list` is:

  ```
  expression | column_name [ ASC | DESC ] 
  [ NULLS FIRST | NULLS LAST ]
  [, order_list ]
  ```
+ `frame_clause` is:

  ```
  ROWS | RANGE
  { UNBOUNDED PRECEDING | expression PRECEDING | CURRENT ROW } |
  {BETWEEN
  { UNBOUNDED PRECEDING | expression { PRECEDING | FOLLOWING } |
  CURRENT ROW}
  AND
  { UNBOUNDED FOLLOWING | expression { PRECEDING | FOLLOWING } |
  CURRENT ROW }}
  ```
+ `from_item` is one of:

  ```
  table_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
  from_item join_type from_item [ ON join_condition | USING ( join_column [, ...] ) ]
  ```
+ `join_type` is one of:

  ```
  [ INNER ] JOIN
  LEFT [ OUTER ] JOIN
  RIGHT [ OUTER ] JOIN
  FULL [ OUTER ] JOIN
  ```
+ `grouping_element` is one of:

  ```
  ()
  expression
  ```