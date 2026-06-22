---
id: "@specs/aws/timestream-influxdb/docs/query-insights-optimize-data-access-pattern"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Optimizing data access"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Optimizing data access

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/query-insights-optimize-data-access-pattern
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Optimizing data access in Amazon Timestream
<a name="query-insights-optimize-data-access-pattern"></a>

You can optimize the data access patterns in Amazon Timestream using the Timestream partitioning scheme or data organization techniques.

**Topics**
+ [Timestream partitioning scheme](#query-insights-optimize-data-access-partitioning-scheme)
+ [Data organization](#query-insights-optimize-data-access-data-org)

## Timestream partitioning scheme
<a name="query-insights-optimize-data-access-partitioning-scheme"></a>

Amazon Timestream uses a highly scalable partitioning scheme where each Timestream table can have hundreds, thousands, or even millions of independent partitions. A highly available partition tracking and indexing service manages the partitioning, minimizing the impact of failures and making the system more resilient.

![Timestream partitioning scheme](http://docs.aws.amazon.com/timestream/latest/developerguide/images/QueryInsights/ts-partitioning-scheme.png)


## Data organization
<a name="query-insights-optimize-data-access-data-org"></a>

Timestream stores each data point it ingests in a single partition. As you ingest data into a Timestream table, Timestream automatically creates partitions based on the timestamps, partition key, and other context attributes in the data. In addition to partitioning the data on time (temporal partitioning), Timestream also partitions the data based on the selected partitioning key and other dimensions (spatial partitioning). This approach is designed to distribute write traffic and allow for effective pruning of data for queries.

The query insights feature provides valuable insights into the pruning efficiency of the query, which includes query spatial coverage and query temporal coverage.

**Topics**
+ [QuerySpatialCoverage](#query-insights-data-org-query-spatial-cvg)
+ [QueryTemporalCoverage](#query-insights-data-org-query-temporal-cvg)

### QuerySpatialCoverage
<a name="query-insights-data-org-query-spatial-cvg"></a>

The [QuerySpatialCoverage](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_QuerySpatialCoverage.html) metric provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning. This information can help you identify areas of improvement in the partitioning strategy to enhance spatial pruning. The value for the `QuerySpatialCoverage` metric ranges between 0 and 1. The lower the value of the metric, the more optimal the query pruning on the spatial axis. For example, a value of 0.1 indicates that the query scans 10% of the spatial axis. A value of 1 indicates that the query scans 100% of the spatial axis.

**Example Using query insights to analyze a query's spatial coverage**  
Say that you've a Timestream database that stores weather data. Assume that the temperature is recorded every hour from weather stations located across different states in United States. Imagine that you choose `State` as the [customer-defined partitioning key](customer-defined-partition-keys.md) (CDPK) to partition the data by state.  
Suppose that you execute a query to retrieve the average temperature for all weather stations in California between 2 PM and 4 PM on a specific day. The following example shows the query for this scenario.  

```
SELECT AVG(temperature) 
FROM "weather_data"."hourly_weather"
WHERE time >= '2024-10-01 14:00:00' AND time < '2024-10-01 16:00:00' 
  AND state = 'CA';
```
Using the query insights feature, you can analyze the query's spatial coverage. Imagine that the `QuerySpatialCoverage` metric returns a value of 0.02. This means that the query only scanned 2% of the spatial axis, which is efficient. In this case, the query was able to effectively prune the spatial range, only retrieving data from California and ignoring data from other states.  
On the contrary, if the `QuerySpatialCoverage` metric returned a value of 0.8, it would indicate that the query scanned 80% of the spatial axis, which is less efficient. This might suggest that the partitioning strategy needs to be refined to improve spatial pruning. For example, you can select the partition key as city or region instead of a state. By analyzing the `QuerySpatialCoverage` metric, you can identify opportunities to optimize your partitioning strategy and improve the performance of your queries.

The following image shows poor spatial pruning.

![Result provided by the QuerySpatialCoverage metric that shows poor spatial pruning.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/QueryInsights/QuerySpatialCoverageMetricResult.png)


To improve spatial pruning efficiency, you can do one or both of the following:
+ Add `measure_name`, the default paritioning key, or use the CDPK predicates in your query.
+ If you've already added the attributes mentioned in the previous point, remove functions around these attributes or clauses, such as `LIKE`.

### QueryTemporalCoverage
<a name="query-insights-data-org-query-temporal-cvg"></a>

The `QueryTemporalCoverage` metric provides insights into the temporal range scanned by the executed query, including the table with the largest time range scanned. The value for the `QueryTemporalCoverage` metric is time range represented in nanoseconds. The lower the value of this metric, the more optimal the query pruning on the temporal range. For example, a query scanning last few minutes of data is more performant than a query scanning the entire time range of the table.

**Example**  
Say that you've a Timestream database that stores IoT sensor data, with measurements taken every minute from devices located in a manufacturing plant. Assume that you've partitioned your data by `device_ID`.  
Suppose that you execute a query to retrieve the average sensor reading for a specific device over the last 30 minutes. The following example shows the query for this scenario.  

```
SELECT AVG(sensor_reading) 
FROM "sensor_data"."factory_1"
WHERE device_id = 'DEV_123' 
  AND time >= NOW() - INTERVAL 30 MINUTE and time < NOW();
```
Using the query insights feature, you can analyze the temporal range scanned by the query. Imagine the `QueryTemporalCoverage` metric returns a value of 1800000000000 nanoseconds (30 minutes). This means that the query only scanned the last 30 minutes of data, which is a relatively narrow temporal range. This is a good sign because it indicates that the query was able to effectively prune the temporal partitioning and only retrieved the requested data.  
On the contrary, if the `QueryTemporalCoverage` metric returned a value of 1 year in nanoseconds, it indicates that the query scanned one year of time range in the table, which is less efficient. This might suggest that the query is not optimized for temporal pruning, and you could improve it by adding time filters.

The following image shows poor temporal pruning.

![Result provided by the QueryTemporalCoverage metric that shows poor temporal pruning.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/QueryInsights/QueryTemporalCoverageMetricResult.png)


To improve temporal pruning, we recommend that you do one or all of the following:
+ Add the missing time predicates in the query and make sure that the time predicates are pruning the desired time window.
+ Remove functions, such as `MAX()`, around the time predicates.
+ Add time predicates to all the sub queries. This is important if your sub queries are joining large tables or performing complex operations.