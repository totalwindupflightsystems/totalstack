---
id: "@specs/aws/timestream-influxdb/docs/queries"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Queries"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Queries

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/queries
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Queries
<a name="queries"></a>

With Timestream for Live Analytics, you can easily store and analyze metrics for DevOps, sensor data for IoT applications, and industrial telemetry data for equipment maintenance, as well as many other use cases. The purpose-built, adaptive query engine in Timestream for Live Analytics allows you to access data across storage tiers using a single SQL statement. It transparently accesses and combines data across storage tiers without requiring you to specify the data location. You can use SQL to query data in Timestream for Live Analytics to retrieve time series data from one or more tables. You can access the metadata information for databases and tables. Timestream for Live Analytics SQL also supports built-in functions for time series analytics. You can refer to the [Query language reference](reference.md) reference for additional details. 

Timestream for Live Analytics is designed to have a fully decoupled data ingestion, storage, and query architecture where each component can scale independently of other components (allowing it to offer virtually infinite scale for an application's needs). This means that Timestream for Live Analytics does not "tip over" when your applications send hundreds of terabytes of data per day or run millions of queries processing small or large amounts of data. As your data grows over time, the query latency in Timestream for Live Analytics remains mostly unchanged. This is because the Timestream for Live Analytics query architecture can leverage massive amounts of parallelism to process larger data volumes and automatically scale to match query throughput needs of an application. 

## Data model
<a name="datamodel"></a>

 Timestream supports two data models for queries—the flat model and the time series model. 

**Note**  
Data in Timestream is stored using the flat model and it is the default model for querying data. The time series model is a query-time concept and is used for time series analytics.
+  [Flat model](#flatmodel) 
+  [Time series model](#timeseriesmodel) 

### Flat model
<a name="flatmodel"></a>

 The flat model is Timestream's default data model for queries. It represents time series data in a tabular format. The dimension names, time, measure names and measure values appear as columns. Each row in the table is an atomic data point corresponding to a measurement at a specific time within a time series. Timestream databases, tables, and columns have some naming constraints. Those are described in [Service limits](ts-limits.md#system-limits).

 The table below shows an illustrative example for how Timestream stores data representing the CPU utilization, memory utilization, and network activity of EC2 instances, when the data is sent as a single-measure record. In this case, the dimensions are the region, availability zone, virtual private cloud, and instance IDs of the EC2 instances. The measures are the CPU utilization, memory utilization, and the incoming network data for the EC2 instances. The columns region, az, vpc, and instance\_id contain the dimension values. The column time contains the timestamp for each record. The column measure\_name contains the names of the measures represented by cpu-utilization, memory\_utilization, and network\_bytes\_in. The columns measure\_value::double contains measurements emitted as doubles (e.g. CPU utilization and memory utilization). The column measure\_value::bigint contains measurements emitted as integers e.g. the incoming network data. 


| Time | region | az | vpc | instance\_id | measure\_name | measure\_value::double | measure\_value::bigint | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| 2019-12-04 19:00:00.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  cpu\_utilization  |  35.0  |  null  | 
| 2019-12-04 19:00:01.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  cpu\_utilization  |  38.2  |  null  | 
| 2019-12-04 19:00:02.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  cpu\_utilization  |  45.3  |  null  | 
| 2019-12-04 19:00:00.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  memory\_utilization  |  54.9  |  null  | 
| 2019-12-04 19:00:01.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  memory\_utilization  |  42.6  |  null  | 
| 2019-12-04 19:00:02.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  memory\_utilization  |  33.3  |  null  | 
| 2019-12-04 19:00:00.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  network\_bytes  |  34,400  |  null  | 
| 2019-12-04 19:00:01.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  network\_bytes  |  1,500  |  null  | 
| 2019-12-04 19:00:02.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  network\_bytes  |  6,000  |  null  | 

The table below shows an illustrative example for how Timestream stores data representing the CPU utilization, memory utilization, and network activity of EC2 instances, when the data is sent as a multi-measure record.


| Time | region | az | vpc | instance\_id | measure\_name | cpu\_utilization | memory\_utilization | network\_bytes | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 2019-12-04 19:00:00.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  metrics  |  35.0  |  54.9  |  34,400  | 
| 2019-12-04 19:00:01.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  metrics  |  38.2  |  42.6  |  1,500  | 
| 2019-12-04 19:00:02.000000000 |  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  metrics  |  45.3  |  33.3  |  6,600  | 

### Time series model
<a name="timeseriesmodel"></a>

 The time series model is a query time construct used for time series analytics. It represents data as an ordered sequence of (time, measure value) pairs. Timestream supports time series functions such as interpolation to enable you to fill the gaps in your data. To use these functions, you must convert your data into the time series model using functions such as create\_time\_series. Refer to [Query language reference](reference.md) for more details. 

 Using the earlier example of the EC2 instance, here is the CPU utilization data expressed as a timeseries. 


| region | az | vpc | instance\_id | cpu\_utilization | 
| --- | --- | --- | --- | --- | 
|  us-east-1  |  us-east-1d  |  vpc-1a2b3c4d  |  i-1234567890abcdef0  |  [{time: 2019-12-04 19:00:00.000000000, value: 35}, {time: 2019-12-04 19:00:01.000000000, value: 38.2}, {time: 2019-12-04 19:00:02.000000000, value: 45.3}]  | 