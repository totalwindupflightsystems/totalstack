---
id: "@specs/aws/timestream-influxdb/docs/optimize-query-using-query-insights"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Optimizing queries"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Optimizing queries

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/optimize-query-using-query-insights
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Optimizing queries using query insights response
<a name="optimize-query-using-query-insights"></a>

Say that you're using Amazon Timestream for LiveAnalytics to monitor energy consumption across various locations. Imagine that you've two tables in your database named `raw-metrics` and `aggregate-metrics`.

The `raw-metrics` table stores detailed energy data at the device level and contains the following columns:
+ Timestamp
+ State, for example, Washington
+ Device ID
+ Energy consumption

The data for this table is collected and stored at a minute-by-minute granularity. The table uses `State` as the CDPK.

The `aggregate-metrics` table stores the result of a scheduled query to aggregate the energy consumption data across all devices hourly. This table contains the following columns:
+ Timestamp
+ State, for example, Washington
+ Total energy consumption

The `aggregate-metrics` table stores this data at an hourly granularity. The table uses `State` as the CDPK.

**Topics**
+ [Querying energy consumption for the last 24 hours](#query-energy-consumption-data)
+ [Optimizing the query for temporal range](#optimize-query-temporal-range)
+ [Optimizing the query for spatial coverage](#optimize-query-spatial-coverage)
+ [Improved query performance](#improved-query-performance)

## Querying energy consumption for the last 24 hours
<a name="query-energy-consumption-data"></a>

Say that you want to extract the total energy consumed in Washington over the last 24 hours. To find this data, you can leverage the strengths of both the tables: `raw-metrics` and `aggregate-metrics`. The `aggregate-metrics` table provides hourly energy consumption data for the last 23 hours, while the `raw-metrics` table offers minute-granular data for the last one hour. By querying across both tables, you can get a complete and accurate picture of energy consumption in Washington over the last 24 hours.

```
SELECT am.time, am.state, am.total_energy_consumption, 
rm.time, rm.state, rm.device_id, rm.energy_consumption
FROM 
 "metrics"."aggregate-metrics" am
 LEFT JOIN "metrics"."raw-metrics" rm ON am.state = rm.state
WHERE rm.time >= ago(1h) and rm.time < now()
```

This example query is provided for illustrative purposes only and might not work as is. It's intended to demonstrate the concept, but you might need to modify it to fit your specific use case or environment.

After executing this query, you might notice that the query response time is slower than expected. To identify the root cause of this performance issue, you can use the query insights feature to analyze the query's performance and optimize its execution.

The following example shows the query insights response.

```
queryInsightsResponse={
                QuerySpatialCoverage: {
                    Max: {
                        Value: 1.0,
                        TableArn: arn:aws:timestream:{{us-east-1}}:{{123456789012}}:database/metrics/table/raw-metrics,
                        PartitionKey: [State]
                    }
                },
                QueryTemporalRange: {
                    Max: {
                        Value:31540000000000000 //365 days,
                        TableArn: arn:aws:timestream:{{us-east-1}}:{{123456789012}}:database/metrics/table/aggregate-metrics
                    }
                },
                QueryTableCount: 2,
                OutputRows: 83,
                OutputBytes: 590
```

The query insights response provides the following information:
+ **Temporal range**: The query scanned an excessive 365-day temporal range for the `aggregate-metrics` table. This indicates an inefficient use of temporal filtering.
+ **Spatial coverage**: The query scanned the entire spatial range (100%) of the `raw-metrics` table. This suggests that the spatial filtering isn't being utilized effectively.

If your query accesses more than one table, query insights provides the metrics for the table with most sub-optimal access pattern.

## Optimizing the query for temporal range
<a name="optimize-query-temporal-range"></a>

Based on the query insights response, you can optimize the query for temporal range as shown in the following example.

```
SELECT am.time, am.state, am.total_energy_consumption, 
rm.time, rm.state, rm.device_id, rm.energy_consumption
FROM 
  "metrics"."aggregate-metrics" am
  LEFT JOIN "metrics"."raw-metrics" rm ON am.state = rm.state
WHERE 
  am.time >=  ago(23h) and am.time < now()
  AND rm.time >=  ago(1h) and rm.time < now()
  AND rm.state = 'Washington'
```

If you run the `QueryInsights` command again, it returns the following response.

```
queryInsightsResponse={
                QuerySpatialCoverage: {
                    Max: {
                        Value: 1.0,
                        TableArn: arn:aws:timestream:{{us-east-1}}:{{123456789012}}:database/metrics/table/aggregate-metrics,
                        PartitionKey: [State]
                    }
                },
                QueryTemporalRange: {
                    Max: {
                        Value: 82800000000000 //23 hours,
                        TableArn: arn:aws:timestream:{{us-east-1}}:{{123456789012}}:database/metrics/table/aggregate-metrics
                    }
                },
                QueryTableCount: 2,
                OutputRows: 83,
                OutputBytes: 590
```

This response shows that the spatial coverage for the `aggregate-metrics` table is still 100%, which is inefficient. The following section shows how to optimze the query for spatial coverage.

## Optimizing the query for spatial coverage
<a name="optimize-query-spatial-coverage"></a>

Based on the query insights response, you can optimize the query for spatial coverage as shown in the following example.

```
SELECT am.time, am.state, am.total_energy_consumption, 
rm.time, rm.state, rm.device_id, rm.energy_consumption
FROM 
  "metrics"."aggregate-metrics" am
  LEFT JOIN "metrics"."raw-metrics" rm ON am.state = rm.state
WHERE 
  am.time >=  ago(23h) and am.time < now()
  AND am.state ='Washington'
  AND rm.time >=  ago(1h) and rm.time < now()
  AND rm.state = 'Washington'
```

If you run the `QueryInsights` command again, it returns the following response.

```
queryInsightsResponse={
                QuerySpatialCoverage: {
                    Max: {
                        Value: 0.02,
                        TableArn: arn:aws:timestream:{{us-east-1}}:{{123456789012}}:database/metrics/table/aggregate-metrics,
                        PartitionKey: [State]
                    }
                },
                QueryTemporalRange: {
                    Max: {
                        Value: 82800000000000 //23 hours,
                        TableArn: arn:aws:timestream:{{us-east-1}}:{{123456789012}}:database/metrics/table/aggregate-metrics
                    }
                },
                QueryTableCount: 2,
                OutputRows: 83,
                OutputBytes: 590
```

## Improved query performance
<a name="improved-query-performance"></a>

After optimizing the query, query insights provides the following information:
+ Temporal pruning for the `aggregate-metrics` table is 23 hours. This indicates that only 23 hours of the temporal range is scanned.
+ Spatial pruning for `aggregate-metrics` table is 0.02. This indicates that only 2% of the table's spatial range data is being scanned. The query scans a very small portion of the tables leading to fast performance and reduced resource utilization. The improved pruning efficiency indicates that the query is now optimized for performance.