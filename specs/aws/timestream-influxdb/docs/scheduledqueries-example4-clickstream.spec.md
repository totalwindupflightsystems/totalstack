---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-example4-clickstream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Comparison"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Comparison

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-example4-clickstream
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Comparing a query on a base table with a query of scheduled query results
<a name="scheduledqueries-example4-clickstream"></a>

In this Timestream query example, we use the following schema, example queries, and outputs to compare a query on a base table with a query on a derived table of scheduled query results. With a well-planned scheduled query, you can get a derived table with fewer rows and other characteristics that can lead to faster queries than would be possible on the original base table. 

For a video that describes this scenario, see [Improve query performance and reduce cost using scheduled queries in Amazon Timestream for LiveAnalytics](https://youtu.be/x8AgLhAydzY).

For this example, we use the following scenario:
+ **Region** – us-east-1
+ **Base table** – `"clickstream"."shopping"`
+ **Derived table** – `"clickstream"."aggregate"`

## Base table
<a name="scheduledqueries-example4-clickstream-base-table"></a>

The following describes the schema for the base table.


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| channel | varchar | MULTI | 
| description | varchar | MULTI | 
| event | varchar | DIMENSION | 
| ip\_address | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| product | varchar | MULTI | 
| product\_id | varchar | MULTI | 
| quantity | double | MULTI | 
| query | varchar | MULTI | 
| session\_id | varchar | DIMENSION | 
| user\_group | varchar | DIMENSION | 
| user\_id | varchar | DIMENSION | 

The following describes the measures for the base table. A *base table* refers to a table in Timestream that scheduled query is run on.
+ **measure\_name** – `metrics`
+ **data** – multi
+ **dimensions**:

  ```
  [ ( user_group, varchar ),( user_id, varchar ),( session_id, varchar ),( ip_address, varchar ),( event, varchar ) ]
  ```

## Query on a base table
<a name="scheduledqueries-example4-clickstream-base-table-query"></a>

The following is an ad-hoc query that gathers counts by a 5-minute aggregate in a given time range.

```
SELECT BIN(time, 5m) as time, 
channel, 
product_id,
SUM(quantity) as product_quantity 
FROM "clickstream"."shopping" 
WHERE BIN(time, 5m) BETWEEN '2023-05-11 10:10:00.000000000' AND '2023-05-11 10:30:00.000000000'
AND channel = 'Social media'
and product_id = '431412'
GROUP BY BIN(time, 5m),channel,product_id
```

Output:

```
duration:1.745 sec
Bytes scanned: 29.89 MB
Query Id: AEBQEANMHG7MHHBHCKJ3BSOE3QUGIDBGWCCP5I6J6YUW5CVJZ2M3JCJ27QRMM7A
Row count:5
```

## Scheduled query
<a name="scheduledqueries-example4-clickstream-scheduled-query"></a>

The following is a scheduled query that runs every 5 minutes.

```
SELECT BIN(time, 5m) as time, channel as measure_name, product_id, product, 
SUM(quantity) as product_quantity 
FROM "clickstream"."shopping" 
WHERE time BETWEEN BIN(@scheduled_runtime, 5m) - 10m AND BIN(@scheduled_runtime, 5m) - 5m 
AND channel = 'Social media' 
GROUP BY BIN(time, 5m), channel, product_id, product
```

## Query on a derived table
<a name="scheduledqueries-example4-clickstream-derived-table"></a>

The following is an ad-hoc query on a derived table. A *derived table* refers to a Timestream table that contains the results of a scheduled query.

```
SELECT time, measure_name, product_id,product_quantity 
FROM "clickstream"."aggregate"
WHERE time BETWEEN '2023-05-11 10:10:00.000000000' AND '2023-05-11 10:30:00.000000000'
AND measure_name = 'Social media'
and product_id = '431412'
```

Output:

```
duration: 0.2960 sec
Bytes scanned: 235.00 B
QueryID: AEBQEANMHHAAQU4FFTT6CFM6UYXTL4SMLZV22MFP4KV2Z7IRVOPLOMLDD6BR33Q
Row count: 5
```

## Comparison
<a name="scheduledqueries-example4-clickstream-comparison"></a>

The following is a comparison of the results of a query on a base table with a query on a derived table. The same query on a derived table that has aggregated results done through a scheduled query completes faster with fewer scanned bytes. 

These results show the value of using scheduled queries to aggregate data for faster queries.


|  | Query on base table | Query on derived table | 
| --- | --- | --- | 
| Duration | 1.745 sec | 0.2960 sec | 
| Bytes scanned | 29.89 MB | 235 bytes | 
| Row count | 5 | 5 | 