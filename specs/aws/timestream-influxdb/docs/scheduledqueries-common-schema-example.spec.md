---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-common-schema-example"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Sample schema"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Sample schema

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-common-schema-example
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Scheduled queries sample schema
<a name="scheduledqueries-common-schema-example"></a>

In this example we will use a sample application mimicking a DevOps scenario monitoring metrics from a large fleet of servers. Users want to alert on anomalous resource usage, create dashboards on aggregate fleet behavior and utilization, and perform sophisticated analysis on recent and historical data to find correlations. The following diagram provides an illustration of the setup where a set of monitored instances emit metrics to Timestream for LiveAnalytics. Another set of concurrent users issues queries for alerts, dashboards, or ad-hoc analysis, where queries and ingestion run in parallel. 

![Monitored instances sending metrics to Timestream, with users querying for dashboards and alerts.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/schedquery_common_schema_example.png)


The application being monitored is modeled as a highly scaled-out service that is deployed in several regions across the globe. Each region is further subdivided into a number of scaling units called cells that have a level of isolation in terms of infrastructure within the region. Each cell is further subdivided into silos, which represent a level of software isolation. Each silo has five microservices that comprise one isolated instance of the service. Each microservice has several servers with different instance types and OS versions, which are deployed across three availability zones. These attributes that identify the servers emitting the metrics are modeled as [dimensions](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html) in Timestream for LiveAnalytics. In this architecture, we have a hierarchy of dimensions (such as region, cell, silo, and microservice\_name) and other dimensions that cut across the hierarchy (such as instance\_type and availability\_zone). 

The application emits a variety of metrics (such as cpu\_user and memory\_free) and events (such as task\_completed and gc\_reclaimed). Each metric or event is associated with eight dimensions (such as region or cell) that uniquely identify the server emitting it. Data is written with the 20 metrics stored together in a multi-measure record with measure name metrics and all the 5 events are stored together in another multi-measure record with measure name events. The data model, schema, and data generation can be found in the [open-sourced data generator](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/perf-scale-workload). In addition to the schema and data distributions, the data generator provides an example of using multiple writers to ingest data in parallel, using the ingestion scaling of Timestream for LiveAnalytics to ingest millions of measurements per second. Below we show the schema (table and measure schema) and some sample data from the data set.

**Topics**
+ [Multi-measure records](#scheduledqueries-common-schema-example-mmr)
+ [Single-measure records](#scheduledqueries-common-schema-example-smr)

## Multi-measure records
<a name="scheduledqueries-common-schema-example-mmr"></a>

**Table Schema**

Below is the table schema once the data is ingested using multi-measure records. It is the output of DESCRIBE query. Assuming the data is ingested into a database raw\_data and table devops, below is the query.

```
DESCRIBE "raw_data"."devops"
```


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| availability\_zone | varchar | DIMENSION | 
| microservice\_name | varchar | DIMENSION | 
| instance\_name | varchar | DIMENSION | 
| process\_name | varchar | DIMENSION | 
| os\_version | varchar | DIMENSION | 
| jdk\_version | varchar | DIMENSION | 
| cell | varchar | DIMENSION | 
| region | varchar | DIMENSION | 
| silo | varchar | DIMENSION | 
| instance\_type | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| memory\_free | double | MULTI | 
| cpu\_steal | double | MULTI | 
| cpu\_iowait | double | MULTI | 
| cpu\_user | double | MULTI | 
| memory\_cached | double | MULTI | 
| disk\_io\_reads | double | MULTI | 
| cpu\_hi | double | MULTI | 
| latency\_per\_read | double | MULTI | 
| network\_bytes\_out | double | MULTI | 
| cpu\_idle | double | MULTI | 
| disk\_free | double | MULTI | 
| memory\_used | double | MULTI | 
| cpu\_system | double | MULTI | 
| file\_descriptors\_in\_use | double | MULTI | 
| disk\_used | double | MULTI | 
| cpu\_nice | double | MULTI | 
| disk\_io\_writes | double | MULTI | 
| cpu\_si | double | MULTI | 
| latency\_per\_write | double | MULTI | 
| network\_bytes\_in | double | MULTI | 
| task\_end\_state | varchar | MULTI | 
| gc\_pause | double | MULTI | 
| task\_completed | bigint | MULTI | 
| gc\_reclaimed | double | MULTI | 

**Measure Schema**

Below is the measure schema returned by the SHOW MEASURES query.

```
SHOW MEASURES FROM "raw_data"."devops"
```


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| events | multi | [{"data\_type":"varchar","dimension\_name":"availability\_zone"},{"data\_type":"varchar","dimension\_name":"microservice\_name"},{"data\_type":"varchar","dimension\_name":"instance\_name"},{"data\_type":"varchar","dimension\_name":"process\_name"},{"data\_type":"varchar","dimension\_name":"jdk\_version"},{"data\_type":"varchar","dimension\_name":"cell"},{"data\_type":"varchar","dimension\_name":"region"},{"data\_type":"varchar","dimension\_name":"silo"}] | 
| metrics | multi | [{"data\_type":"varchar","dimension\_name":"availability\_zone"},{"data\_type":"varchar","dimension\_name":"microservice\_name"},{"data\_type":"varchar","dimension\_name":"instance\_name"},{"data\_type":"varchar","dimension\_name":"os\_version"},{"data\_type":"varchar","dimension\_name":"cell"},{"data\_type":"varchar","dimension\_name":"region"},{"data\_type":"varchar","dimension\_name":"silo"},{"data\_type":"varchar","dimension\_name":"instance\_type"}] | 

**Example Data**


| region | Cell | Silo | availability\_zone | microservice\_name | instance\_name | instance\_type | os\_version | process\_name | jdk\_version | measure\_name | Time | cpu\_user | cpu\_system | cpu\_idle | cpu\_steal | cpu\_iowait | cpu\_nice | cpu\_hi | cpu\_si | memory\_used | memory\_cached | disk\_io\_reads | latency\_per\_read | disk\_io\_writes | latency\_per\_write | disk\_used | disk\_free | network\_bytes\_in | network\_bytes\_out | file\_descriptors\_in\_use | memory\_free | task\_end\_state | gc\_pause | task\_completed | gc\_reclaimed | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com | m5.8xlarge | AL2012 |  |  | metrics | 11/12/2021 12:43 | 62.8 | 0.408 | 34.2 | 0.972 | 0.0877 | 0.103 | 0.567 | 0.844 | 57.6 | 88.9 | 52.6 | 91.9 | 31.7 | 2.25 | 63.5 | 29.2 | 85.3 | 49.8 | 32.3 | 57.6 |  |  |  |  | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com | m5.8xlarge | AL2012 |  |  | metrics | 11/12/2021 12:41 | 56 | 0.923 | 39.9 | 0.799 | 0.532 | 0.655 | 0.851 | 0.317 | 90.5 | 31.9 | 56.6 | 37.1 | 25 | 93.3 | 52.2 | 33.1 | 7.14 | 53.7 | 65.9 | 20.4 |  |  |  |  | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com | m5.8xlarge | AL2012 |  |  | metrics | 11/12/2021 12:39 | 48.5 | 0.801 | 48.2 | 0.18 | 0.943 | 0.0316 | 0.844 | 0.54 | 97.4 | 41.4 | 55.1 | 32.7 | 86.2 | 33.7 | 72.7 | 61.5 | 80.8 | 5.15 | 44.3 | 8.5 |  |  |  |  | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com | m5.8xlarge | AL2012 |  |  | metrics | 11/12/2021 12:38 | 37.5 | 0.723 | 58.8 | 0.317 | 0.608 | 0.859 | 0.791 | 0.393 | 4.84 | 78.9 | 20.3 | 41.4 | 46.8 | 3.87 | 84.6 | 60.6 | 21.1 | 11.8 | 2.76 | 10 |  |  |  |  | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com | m5.8xlarge | AL2012 |  |  | metrics | 11/12/2021 12:36 | 58 | 0.786 | 38.7 | 0.219 | 0.436 | 0.829 | 0.331 | 0.734 | 51 | 36.8 | 81.8 | 50.5 | 77.9 | 17.8 | 82.3 | 64 | 7.69 | 66.5 | 56.2 | 31.3 |  |  |  |  | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com |  |  | host\_manager | JDK\_8 | events | 11/12/2021 12:43 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 75.8 | SUCCESS\_WITH\_NO\_RESULT | 85.5 | 348 | 64.8 | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com |  |  | host\_manager | JDK\_8 | events | 11/12/2021 12:41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 7.47 | SUCCESS\_WITH\_RESULT | 22.8 | 42 | 7.45 | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com |  |  | host\_manager | JDK\_8 | events | 11/12/2021 12:39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 64.1 | SUCCESS\_WITH\_RESULT | 6.77 | 249 | 72.3 | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com |  |  | host\_manager | JDK\_8 | events | 11/12/2021 12:38 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 23 | SUCCESS\_WITH\_RESULT | 53.3 | 138 | 99 | 
| us-east-2 | us-east-2-cell-1 | us-east-2-cell-1-silo-2 | us-east-2-1 | athena | i-zaZswmJk-athena-us-east-2-cell-1-silo-2-00000216.amazonaws.com |  |  | host\_manager | JDK\_8 | events | 11/12/2021 12:36 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 39.4 | SUCCESS\_WITH\_NO\_RESULT | 79.6 | 254 | 82.9 | 

## Single-measure records
<a name="scheduledqueries-common-schema-example-smr"></a>

Timestream for LiveAnalytics also allows you to ingest the data with one measure per time series record. Below are the schema details when ingested using single measure records.

**Table Schema**

Below is the table schema once the data is ingested using multi-measure records. It is the output of DESCRIBE query. Assuming the data is ingested into a database raw\_data and table devops, below is the query.

```
DESCRIBE "raw_data"."devops_single"
```


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| availability\_zone | varchar | DIMENSION | 
| microservice\_name | varchar | DIMENSION | 
| instance\_name | varchar | DIMENSION | 
| process\_name | varchar | DIMENSION | 
| os\_version | varchar | DIMENSION | 
| jdk\_version | varchar | DIMENSION | 
| cell | varchar | DIMENSION | 
| region | varchar | DIMENSION | 
| silo | varchar | DIMENSION | 
| instance\_type | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| measure\_value::double | double | MEASURE\_VALUE | 
| measure\_value::bigint | bigint | MEASURE\_VALUE | 
| measure\_value::varchar | varchar | MEASURE\_VALUE | 

**Measure Schema**

Below is the measure schema returned by the SHOW MEASURES query.

```
SHOW MEASURES FROM "raw_data"."devops_single"
```


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| cpu\_hi | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_idle | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_iowait | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_nice | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_si | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_steal | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_system | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| cpu\_user | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| disk\_free | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| disk\_io\_reads | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| disk\_io\_writes | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| disk\_used | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| file\_descriptors\_in\_use | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| gc\_pause | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'process\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'jdk\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}] | 
| gc\_reclaimed | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'process\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'jdk\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}] | 
| latency\_per\_read | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| latency\_per\_write | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| memory\_cached | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| memory\_free | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'process\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'jdk\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| memory\_used | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| network\_bytes\_in | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| network\_bytes\_out | double | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'os\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_type', 'data\_type': 'varchar'}] | 
| task\_completed | bigint | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'process\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'jdk\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}] | 
| task\_end\_state | varchar | [{'dimension\_name': 'availability\_zone', 'data\_type': 'varchar'}, {'dimension\_name': 'microservice\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'instance\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'process\_name', 'data\_type': 'varchar'}, {'dimension\_name': 'jdk\_version', 'data\_type': 'varchar'}, {'dimension\_name': 'cell', 'data\_type': 'varchar'}, {'dimension\_name': 'region', 'data\_type': 'varchar'}, {'dimension\_name': 'silo', 'data\_type': 'varchar'}] | 

**Example Data**


| availability\_zone | microservice\_name | instance\_name | process\_name | os\_version | jdk\_version | Cell | region | Silo | instance\_type | measure\_name | Time | measure\_value::double | measure\_value::bigint | measure\_value::varchar | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_hi | 34:57.2 | 0.87169 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_idle | 34:57.2 | 3.46266 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_iowait | 34:57.2 | 0.10226 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_nice | 34:57.2 | 0.63013 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_si | 34:57.2 | 0.16441 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_steal | 34:57.2 | 0.10729 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_system | 34:57.2 | 0.45709 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | cpu\_user | 34:57.2 | 94.20448 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | disk\_free | 34:57.2 | 72.51895 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | disk\_io\_reads | 34:57.2 | 81.73383 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | disk\_io\_writes | 34:57.2 | 77.11665 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | disk\_used | 34:57.2 | 89.42235 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | file\_descriptors\_in\_use | 34:57.2 | 30.08254 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com | server |  | JDK\_8 | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 |  | gc\_pause | 34:57.2 | 60.28679 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com | server |  | JDK\_8 | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 |  | gc\_reclaimed | 34:57.2 | 75.28839 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | latency\_per\_read | 34:57.2 | 8.07605 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | latency\_per\_write | 34:57.2 | 58.11223 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | memory\_cached | 34:57.2 | 87.56481 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com | server |  | JDK\_8 | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 |  | memory\_free | 34:57.2 | 18.95768 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | memory\_free | 34:57.2 | 97.20523 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | memory\_used | 34:57.2 | 12.37723 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | network\_bytes\_in | 34:57.2 | 31.02065 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com |  | AL2012 |  | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 | r5.4xlarge | network\_bytes\_out | 34:57.2 | 0.51424 |  |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com | server |  | JDK\_8 | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 |  | task\_completed | 34:57.2 |  | 69 |  | 
| eu-west-1-1 | hercules | i-zaZswmJk-hercules-eu-west-1-cell-9-silo-2-00000027.amazonaws.com | server |  | JDK\_8 | eu-west-1-cell-9 | eu-west-1 | eu-west-1-cell-9-silo-2 |  | task\_end\_state | 34:57.2 |  |  | SUCCESS\_WITH\_RESULT | 