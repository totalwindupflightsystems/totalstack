---
id: "@specs/aws/timestream-influxdb/docs/data-modeling"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Data modeling"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Data modeling

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/data-modeling
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Data modeling
<a name="data-modeling"></a>

Amazon Timestream for LiveAnalytics is designed to collect, store, and analyze time series data from applications and devices emitting a sequence of data with a timestamp. For optimal performance, the data being sent to Timestream for LiveAnalytics must have temporal characteristics and time must be a quintessential component of the data.

Timestream for LiveAnalytics provides you the flexibility to model your data in different ways to suit your application's requirements. In this section, we cover several of these patterns and provide guidelines for you to optimize your costs and performance. Familiarize yourself with key [Amazon Timestream for LiveAnalytics concepts](concepts.md) such as dimensions and measures. In this section, you will learn more about the following when deciding whether to create a single table or multiple tables to store data:
+ Which data to put in the same table vs. when you want to separate data across multiple tables and databases.
+ How to choose between Timestream for LiveAnalytics multi-measure records compared to single-measure records, and the benefits of modeling using multi-measure records especially when your application is tracking multiple measurements at the same time instant.
+ Which attributes to model as dimensions or as measures.
+ How to effectively use the measure name attributes to optimize your query latency.

**Topics**
+ [Single table vs. multiple tables](#data-modeling-singleVmultitable)
+ [Multi-measure records vs. single-measure records](#data-modeling-multiVsinglerecords)
+ [Dimensions and measures](#data-modeling-dimensionsmeasures)
+ [Using measure name with multi-measure records](#data-modeling-measurenamemulti)
+ [Recommendations for partitioning multi-measure records](#data-modeling-multi-measure-partitioning)

## Single table vs. multiple tables
<a name="data-modeling-singleVmultitable"></a>

As you are modeling your data in application, another important aspect is how to model the data into tables and databases. Databases and tables in Timestream for LiveAnalytics are abstractions for access control, specifying KMS keys, retention periods, and so on. Timestream for LiveAnalytics automatically partitions your data and is designed to scale resources to match the ingestion, storage, and query load and requirements for your applications.

A table in Timestream for LiveAnalytics can scale to petabytes of data stored and tens of gigabytes per second of data writes. Queries can process hundreds of terabytes per hour. Queries in Timestream for LiveAnalytics can span multiple tables and databases, providing joins and unions to provide seamless access to your data across multiple tables and databases. So scale of data or request volumes are usually not the primary concern when deciding how to organize your data in Timestream for LiveAnalytics. Below are some important considerations when deciding which data to co-locate in the same table compared to in different tables, or tables in different databases.
+ Data retention policies (memory store retention, magnetic store retention, etc.) are supported at the granularity of a table. Therefore, data that requires different retention policies needs to be in different tables.
+ AWS KMS keys that are used to encrypt your data are configured at the database level. Therefore, different encryption key requirements imply the data will need to be in different databases.
+ Timestream for LiveAnalytics supports resource-based access control at the granularity of tables and databases. Consider your access control requirements when deciding which data you write to the same table vs. different tables.
+ Be aware of the [limits](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html) on the number of dimensions, measure names, and multi-measure attribute names when deciding which data is stored in which table.
+ Consider your query workload and access patterns when deciding how you organize your data, as the query latency and ease of writing your queries will be dependent on that.
  + If you store data that you frequently query in the same table, that will generally ease the way you write your queries so that you can often avoid having to write joins, unions, or common table expressions. This also usually results in lower query latency. You can use predicates on dimensions and measure names to filter the data that is relevant to the queries.

    For instance, consider a case where you store data from devices located in six continents. If your queries frequently access data from across continents to get a global aggregated view, then storing data from these continents in the same table will result in easier to write queries. On the other hand, if you store data on different tables, you still can combine the data in the same query, however, you will need to write a query to union the data from across tables.
  + Timestream for LiveAnalytics uses adaptive partitioning and indexing on your data so queries only get charged for data that is relevant to your queries. For instance, if you have a table storing data from a million devices across six continents, if your query has predicates of the form `WHERE device_id = 'abcdef'` or `WHERE continent = 'North America'`, then queries are only charged for data for the device or for the continent.
  + Wherever possible, if you use measure name to separate out data in the same table that is not emitted at the same time or not frequently queried, then using predicates such as `WHERE measure_name = 'cpu'` in your query, not only do you get the metering benefits, Timestream for LiveAnalytics can also effectively eliminate partitions that do not have the measure name used in your query predicate. This enables you to store related data with different measure names in the same table without impacting query latency or costs, and avoids spreading the data into multiple tables. The measure name is essentially used to partition the data and prune partitions irrelevant to the query.

## Multi-measure records vs. single-measure records
<a name="data-modeling-multiVsinglerecords"></a>

Timestream for LiveAnalytics allows you to write data with multiple measures per record (multi-measure) or single measure per record (single-measure).

**Multi-measure records**

In many use cases, a device or an application you are tracking may emit multiple metrics or events at the same timestamp. In such cases, you can store all the metrics emitted at the same timestamp in the same multi-measure record. That is, all the measures stored in the same multi-measure record appear as different columns in the same row of data.

Consider, for instance, that your application is emitting metrics such as cpu, memory, and disk\_iops from a device measured at the same time instant. The following is an example of such a table where multiple metrics emitted at the same time instant are stored in the same row. You will that see two hosts are emitting the metrics once every second.


| Hostname | measure\_name | Time | cpu | Memory | disk\_iops | 
| --- | --- | --- | --- | --- | --- | 
| host-24Gju | metrics | 2021-12-01 19:00:00 | 35 | 54.9 | 38.2 | 
| host-24Gju | metrics | 2021-12-01 19:00:01 | 36 | 58 | 39 | 
| host-28Gju | metrics | 2021-12-01 19:00:00 | 15 | 55 | 92 | 
| host-28Gju | metrics | 2021-12-01 19:00:01 | 16 | 50 | 40 | 

**Single-measure records**

The single-measure records are suitable when your devices emit different metrics at different time periods, or you are using custom processing logic that emits metrics/events at different time periods (for instance, when a device's reading/state changes). Because every measure has a unique timestamp, the measures can be stored in their own records in Timestream for LiveAnalytics. For instance, consider an IoT sensor, which tracks soil temperature and moisture, that emits a record only when it detects a change from the previous reported entry. The following example provides an example of such data being emitted using single measure records.


| device\_id | measure\_name | Time | measure\_value::double | measure\_value::bigint | 
| --- | --- | --- | --- | --- | 
| sensor-sea478 | temperature |  2021-12-01 19:22:32 | 35 | NULL | 
| sensor-sea478 | temperature |  2021-12-01 18:07:51 | 36 | NULL | 
| sensor-sea478 | moisture |  2021-12-01 19:05:30 | NULL | 21 | 
| sensor-sea478 | moisture |  2021-12-01 19:00:01 | NULL | 23 | 

**Comparing single-measure and multi-measure records**

Timestream for LiveAnalytics provides you the flexibility to model your data as single-measure or multi-measure records depending on your application's requirements and characteristics. A single table can store both single-measure and multi-measure records if your application requirements so desire. In general, when your application is emitting multiple measures/events at the same time instant, then modeling the data as multi-measure records is usually recommended for performant data access and cost-effective data storage.

For instance, if you consider a [DevOps use case tracking metrics and events](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/perf-scale-workload) from hundreds of thousands of servers, each server periodically emits 20 metrics and 5 events, where the events and metrics are emitted at the same time instant. That data can be modeled either using single-measure records or using multi-measure records (see the [open-sourced data generator](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/perf-scale-workload) for the resulting schema). For this use case, modeling the data using multi-measure records compared to single-measure records results in:
+ *Ingestion metering* - Multi-measure records results in about *40 percent lower ingestion* bytes written. 
+ *Ingestion batching* - Multi-measure records result in bigger batches of data being sent, which implies the clients need fewer threads and fewer CPU to process the ingestion.
+ *Storage metering* - Multi-measure records result in about *8X lower storage*, resulting in significant storage savings for both memory and magnetic store.
+ *Query latency* - Multi-measure records results in lower query latency for most query types when compared to single-measure records.
+ *Query metered bytes* - For queries scanning less than 10 MB data, both single-measure and multi-measure records are comparable. For queries accessing a single measure and scanning > 10 MB data, single measure records usually results in lower bytes metered. For queries referencing three or more measures, multi-measure records result in lower bytes metered.
+ *Ease of expressing multi-measure queries* - When your queries reference multiple measures, modeling your data with multi-measure records results in easier to write and more compact queries. 

The previous factors will vary depending on how many metrics you are tracking, how many dimensions your data has, etc. While the preceding example provides some concrete data for one example, we see across many application scenarios and use cases where if your application emits multiple measures at the same instant, storing data as multi-measure records is more effective. Moreover, multi-measure records provide you the flexibility of data types and storing multiple other values as context (for example, storing request IDs, and additional timestamps, which is discussed later).

Note that a multi-measure record can also model sparse measures such as the previous example for single-measure records: you can use the `measure_name` to store the name of the measure and use a generic multi-measure attribute name, such as `value_double` to store `DOUBLE` measures, `value_bigint` to store `BIGINT` measures, `value_timestamp` to store additional `TIMESTAMP` values, and so on.

## Dimensions and measures
<a name="data-modeling-dimensionsmeasures"></a>

A table in Timestream for LiveAnalytics allows you to store *dimensions* (identifying attributes of the device/data you are storing) and *measures* (the metrics/values you are tracking); see [Amazon Timestream for LiveAnalytics concepts](concepts.md) for more details. As you are modeling your application on Timestream for LiveAnalytics, how you map your data into dimensions and measures impacts your ingestion and query latency. The following are guidelines on how to model your data as dimensions and measures that you can apply to your use case.

**Choosing dimensions**

Data that identifies the source that is sending the time series data is a natural fit for dimensions, which are attributes that don't change over time. For instance, if you have a server emitting metrics, then the attributes identifying the server, such as hostname, Region, rack, and Availability Zone, are candidates for dimensions. Similarly, for an IoT device with multiple sensors reporting time series data, attributes such as device ID and sensor ID are candidates for dimensions.

If you are writing data as multi-measure records, dimensions and multi-measure attributes appear as columns in the table when you do a `DESCRIBE` or run a `SELECT` statement on the table. Therefore, when writing your queries, you can freely use the dimensions and measures in the same query. However, as you construct your write record to ingest data, keep the following in mind as you choose which attributes are specified as dimensions and which ones are measure values:
+ The dimension names, dimension values, measure name, and timestamp uniquely identify the time series data. Timestream for LiveAnalytics uses this unique identifier to automatically de-duplicate data. That is, if Timestream for LiveAnalytics receives two data points with the same values of dimension names, dimension values, measure name, and timestamp, and the values have the same version number, then Timestream for LiveAnalytics de-duplicates. If the new write request has a lower version than the data already existing in Timestream for LiveAnalytics, the write request is rejected. If the new write request has a higher version, then the new value overwrites the old value. Therefore, how you choose your dimension values will impact this de-duplication behavior.
+ Dimension names and values cannot be updated, but measure value can be. Therefore, any data that might need updates is better modeled as measure values. For instance, if you have a machine on the factory floor whose color can change, you can model the color as a measure value, unless you also want to use the color as an identifying attribute that is needed for de-duplication. That is, measure values can be used to store attributes that only slowly change over time.

Note that a table in Timestream for LiveAnalytics does not limit the number of unique combinations of dimension names and values. For instance, you can have billions of such unique value combinations stored in a table. However, as you will see with the following examples, careful choice of dimensions and measures can significantly optimize your request latency, especially for queries.

**Unique IDs in dimensions**

If your application scenario requires you to store a unique identifier for every data point (for example, a request ID, a transaction ID, or a correlation ID), modeling the ID attribute as a measure value will result in significantly better query latency. When modeling your data with multi-measure records, the ID appears in the same row in context with your other dimensions and time series data, so your queries can continue to use them effectively. For instance, considering a [DevOps use case](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/perf-scale-workload) where every data point emitted by a server has a unique request ID attribute, modeling the request ID as a measure value results in up to 4x lower query latency across different query types, as opposed to modeling the unique request ID as a dimension.

You can use the similar analogy for attributes that are not entirely unique for every data point, but have hundreds of thousands or millions of unique values. You can model those attributes both as dimensions or measure values. You would want to model it as a dimension if the values are necessary for de-duplication on the write path as discussed earlier or you often use it as a predicate (for example, in the `WHERE` clause with an equality predicate on a value of that attribute such as `device_id = 'abcde'` where your application is tracking millions of devices) in your queries. 

**Richness of data types with multi-measure records**

Multi-measure records provide you the flexibility to effectively model your data. Data that you store in a multi-measure record appear as columns in the table similar to dimensions, thus providing the same ease of querying for dimension and measure values. You saw some of these patterns in the examples discussed earlier. Below you will find additional patterns to effectively use multi-measure records to meet your application's use cases.

Multi-measure records support attributes of data types `DOUBLE`, `BIGINT`, `VARCHAR`, `BOOLEAN`, and `TIMESTAMP`. Therefore, they naturally fit different types of attributes:
+ *Location information*: For instance, if you want to track a location (expressed as latitude and longitude), then modeling it as a multi-measure attribute will result in lower query latency compared to storing them as `VARCHAR` dimensions, especially when you have predicates on the latitudes and longitudes. 
+ *Multiple timestamps in a record*: If your application scenario requires you to track multiple timestamps for a time series record, you can model them as additional attributes in the multi-measure record. This pattern can be used to store data with future timestamps or past timestamps. Note that every record will still use the timestamp in the time column to partition, index, and uniquely identify a record.

In particular, if you have numeric data or timestamps on which you have predicates in the query, modeling those attributes as multi-measure attributes as opposed to dimensions will result in lower query latency. This is because when you model such data using the rich data types supported in multi-measure records, you can express the predicates using native data types instead of casting values from `VARCHAR` to another data type if you modeled such data as dimensions.

## Using measure name with multi-measure records
<a name="data-modeling-measurenamemulti"></a>

Tables in Timestream for LiveAnalytics support a special attribute (or column) called *measure name*. You specify a value for this attribute for every record you write to Timestream for LiveAnalytics. For single-measure records, it is natural to use the name of your metric (such as CPU or memory for server metrics, or temperature or pressure for sensor metrics). When using multi-measure records, attributes in a multi-measure record are named and these names become column names in the table. Therefore, cpu, memory, temperature, and pressure can become multi-measure attribute names. A natural question is how to effectively use the measure name.

Timestream for LiveAnalytics uses the values in the measure name attribute to partition and index the data. Therefore, if a table has multiple different measure names, and if the queries use those values as query predicates, then Timestream for LiveAnalytics can use its custom partitioning and indexing to prune out data that is not relevant to queries. For instance, if your table has `cpu` and `memory` measure names, and your query has a predicate `WHERE measure_name = 'cpu'`, Timestream for LiveAnalytics can effectively prune data for measure names not relevant to the query, for example, rows with measure name memory in this example. This pruning applies even when using measure names with multi-measure records. You can use the measure name attribute effectively as a partitioning attribute for a table. Measure name along with dimension names and values, and time are used to partition the data in a Timestream for LiveAnalytics table. Be aware of the [limits](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html) on the number of unique measure names allowed in a Timestream for LiveAnalytics table. Also note that a measure name is associated with a measure value data type as well. For example, a single measure name can only be associated with one type of measure value. That type can be one of `DOUBLE`, `BIGINT`, `BOOLEAN`, `VARCHAR`, or `MULTI`. Multi-measure records stored with a measure name will have the data type of `MULTI`. Since a single multi-measure record can store multiple metrics with different data types (`DOUBLE`, `BIGINT`, `VARCHAR`, `BOOLEAN`, and `TIMESTAMP`), you can associate data of different types in a multi-measure record. 

The following sections describe a few different examples of how the measure name attribute can be effectively used to group together different types of data in the same table. 

**IoT sensors reporting quality and value**

Consider you have an application monitoring data from IoT sensors. Each sensor tracks different measures, such as temperature and pressure. In addition to the actual values, the sensors also report the quality of the measurements, which is a measure of how accurate the reading is, and a unit for the measurement. Since quality, unit, and value are emitted together, they can be modeled as multi-measure records, as shown in the example data below where `device_id` is a dimension, and `quality`, `value`, and `unit` are multi-measure attributes:


| device\_id | measure\_name | Time | Quality | Value | Unit | 
| --- | --- | --- | --- | --- | --- | 
| sensor-sea478 | temperature | 2021-12-01 19:22:32 | 92 | 35 | c | 
| sensor-sea478 | temperature | 2021-12-01 18:07:51 | 93 | 34 | c | 
| sensor-sea478 | pressure | 2021-12-01 19:05:30 | 98 | 31 | psi | 
| sensor-sea478 | pressure | 2021-12-01 19:00:01 | 24 | 132 | psi | 

This approach allows you to combine the benefits of multi-measure records along with partitioning and pruning data using the values of measure name. If queries reference a single measure, such as temperature, then you can include a `measure_name` predicate in the query. The following is an example of such a query, which also projects the unit for measurements whose quality is above 90.

```
SELECT device_id, time, value AS temperature, unit
FROM db.table
WHERE time > ago(1h)
    AND measure_name = 'temperature'
    AND quality > 90
```

Using the `measure_name` predicate on the query enables Timestream for LiveAnalytics to effectively prune partitions and data that is not relevant to the query, thus improving your query latency.

It is also possible to have all of the metrics stored in the same multi-measure record if all the metrics are emitted at the same timestamp and/or multiple metrics are queried together in the same query. For instance, you can construct a multi-measure record with attributes such as temperature\_quality, temperature\_value, temperature\_unit, pressure\_quality, pressure\_value, and pressure\_unit. Many of the points discussed earlier about modeling data using single-measure vs. multi-measure records apply in your decision of how to model the data. Consider your query access patterns and how your data is generated to choose a model that optimizes your cost, ingestion and query latency, and ease of writing your queries.

**Different types of metrics in the same table**

Another use case where you can combine multi-measure records with measure name values is to model different types of data that are independently emitted from the same device. Consider the DevOps monitoring use case where servers are emitting two types of data: regularly emitted metrics and irregular events. An example of this approach is the schema discussed in the [data generator modeling a DevOps use case](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/perf-scale-workload). In this case, you can store the different types of data emitted from the same server in the same table by using different measure names. For instance, all the metrics that are emitted at the same time instant are stored with measure name metrics. All the events that are emitted at a different time instant from the metrics are stored with measure name events. The measure schema for the table (for example, output of `SHOW MEASURES` query) is:


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| events | multi | [{"data\_type":"varchar","dimension\_name":"availability\_zone"},{"data\_type":"varchar","dimension\_name":"microservice\_name"},{"data\_type":"varchar","dimension\_name":"instance\_name"},{"data\_type":"varchar","dimension\_name":"process\_name"},{"data\_type":"varchar","dimension\_name":"jdk\_version"},{"data\_type":"varchar","dimension\_name":"cell"},{"data\_type":"varchar","dimension\_name":"region"},{"data\_type":"varchar","dimension\_name":"silo"}] | 
| metrics | multi | [{"data\_type":"varchar","dimension\_name":"availability\_zone"},{"data\_type":"varchar","dimension\_name":"microservice\_name"},{"data\_type":"varchar","dimension\_name":"instance\_name"},{"data\_type":"varchar","dimension\_name":"os\_version"},{"data\_type":"varchar","dimension\_name":"cell"},{"data\_type":"varchar","dimension\_name":"region"},{"data\_type":"varchar","dimension\_name":"silo"},{"data\_type":"varchar","dimension\_name":"instance\_type"}] | 

In this case, you can see that the events and metrics also have different sets of dimensions, where events have different dimensions `jdk_version` and `process_name` while metrics have dimensions `instance_type` and `os_version`.

Using different measure names allow you to write queries with predicates such as `WHERE measure_name = 'metrics'` to get only the metrics. Also having all the data emitted from the same instance in the same table implies you can also write a simpler query with the `instance_name` predicate to get all data for that instance. For instance, a predicate of the form `WHERE instance_name = 'instance-1234'` without a `measure_name` predicate will return all data for a specific server instance.

## Recommendations for partitioning multi-measure records
<a name="data-modeling-multi-measure-partitioning"></a>

**Important**  
**This section is deprecated\!**  
These recommendations are out of date. Partitioning is now better controlled using [customer-defined partition keys](customer-defined-partition-keys.md). 

We have seen that there is a growing number of workloads in the time series ecosystem that require ingesting and storing massive amounts of data while simultaneously needing low latency query responses when accessing data by a high cardinality set of dimension values.

Because of such characteristics, recommendations in this section will be useful for customer workloads that have the following:
+ Adopted or want to adopt multi-measure records.
+ Expect to have a high volume of data coming into the system that will be stored for long periods.
+ Require low latency response times for their main access (query) patterns.
+ Know that the most important queries patterns involve a filtering condition of some sort in the predicate. This filtering condition is based around a high cardinality dimension. For example, consider events or aggregations by UserId, DeviceId, ServerID, host-name, and so forth.

In these cases, a single name for all the multi-measure measures will not help since our engine uses multi-measure names to partition the data and having a single value limits the partition advantage that you get. The partitioning for these records is mainly based on two dimensions. Let’s say time is on the x-axis and a hash of dimension names and the `measure_name` is on the y-axis. The `measure_name` in these cases works almost like a partitioning key.

Our recommendation is as follows:
+ When modeling your data for use cases like the one we mentioned, use a `measure_name` that is a direct derivative of your main query access pattern. For example:
  + Your use case requires tracking application performance and QoE from the end user point of view. This could also be tracking measurements for a single server or IoT device.
  + If you are querying and filtering by UserId, then you need, at ingestion time, to find the best way to associate `measure_name` to UserId.
  + Since a multi-measure table can only hold 8,192 different measure names, whatever formula is adopted should not generate more that 8,192 different values.
+ One approach that we have applied with success for string values is to apply a hashing algorithm to the string value. Then perform the modulo operation with the absolute value of the hash result and 8,192.

  ```
  measure_name = getMeasureName(UserId)
  int getMeasureName(value) {
      hash_value =  abs(hash(value))
      return hash_value % 8192
  }
  ```
+ We also added `abs()` to remove the sign eliminating the possibility for values to range from -8,192 to 8,192. This should be performed prior to the modulo operation.
+ By using this method your queries can run on a fraction of the time that would take to run on an unpartitioned data model.
+ When querying the data, make sure that you include a filtering condition in the predicate that uses the newly derived value of the `measure_name`. For example:
  + 

    ```
    SELECT * FROM {{your_database.your_table}} 
    WHERE host_name = 'Host-1235' time BETWEEN '2022-09-01' 
        AND '2022-09-18' 
        AND measure_name = (SELECT cast(abs(from_big_endian_64(xxhash64(CAST('HOST-1235' AS varbinary))))%8192 AS varchar))
    ```
  + This will minimize the total number of partitions scanned to get you data that will translate in faster queries over time.

Keep in mind that if you want to obtain the benefits from this partition schema, the hash needs to be calculated on the client side and passed to Timestream for LiveAnalytics as a static value to the query engine. The preceding example provides a way to validate that the generated hash can be resolved by the engine when needed.


| time | host\_name | location | server\_type | cpu\_usage | available\_memory | cpu\_temp | 
| --- | --- | --- | --- | --- | --- | --- | 
| 2022-09-07 21:48:44 .000000000 | host-1235 | us-east1 | 5.8xl | 55 | 16.2 | 78 | 
| R2022-09-07 21:48:44 .000000000 | host-3587 | us-west1 | 5.8xl | 62 | 18.1 | 81 | 
| 2022-09-07 21:48:45.000000000 | host-258743 | eu-central | 5.8xl | 88 | 9.4 | 91 | 
| 2022-09-07 21:48:45 .000000000 | host-35654 | us-east2 | 5.8xl | 29 | 24 | 54 | 
| R2022-09-07 21:48:45 .000000000 | host-254 | us-west1 | 5.8xl | 44 | 32 | 48 | 

To generate the associated `measure_name` following our recommendation, there are two paths that depend on your ingestion pattern.

1. *For batch ingestion of historical data*—You can add the transformation to your write code if you will use your own code for the batch process.

   Building on top of the preceding example.

   ```
           List<String> hosts = new ArrayList<>();
   
           hosts.add("host-1235");
           hosts.add("host-3587");
           hosts.add("host-258743");
           hosts.add("host-35654");
           hosts.add("host-254");
   
           for (String h: hosts){
               ByteBuffer buf2 = ByteBuffer.wrap(h.getBytes());
               partition = abs(hasher.hash(buf2, 0L)) % 8192;
               System.out.println(h + " - " + partition);
   
           }
   ```

   Output

   ```
   host-1235 - 6445
   host-3587 - 6399
   host-258743 - 640
   host-35654 - 2093
   host-254 - 7051
   ```

   Resulting dataset    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/data-modeling.html)

1. *For real-time ingestion*—You need to generate the `measure_name` in-flight as data is coming in.

In both cases, we recommend you test your hash generating algorithm at both ends (ingestion and querying) to make sure you are getting the same results.

Here are some code examples to generate the hashed value based on `host_name`.

**Example Python**  

```
>>> import xxhash
>>> from bitstring import BitArray
>>> b=xxhash.xxh64('HOST-ID-1235').digest()
>>> BitArray(b).int % 8192
### 3195
```

**Example Go**  

```
package main

import (
    "bytes"
    "fmt"
    "github.com/cespare/xxhash"
)

func main() {
    buf := bytes.NewBufferString("HOST-ID-1235")
    x := xxhash.New()
    x.Write(buf.Bytes())
    // convert unsigned integer to signed integer before taking mod
    fmt.Printf("%f\n", abs(int64(x.Sum64())) % 8192)
}

func abs(x int64) int64 {
    if (x < 0) {
        return -x
    }
    return x
}
```

**Example Java**  

```
import java.nio.ByteBuffer;

import net.jpountz.xxhash.XXHash64;

public class test {
    public static void main(String[] args) {
        XXHash64 hasher = net.jpountz.xxhash.XXHashFactory.fastestInstance().hash64();

        String host = "HOST-ID-1235";
        ByteBuffer buf = ByteBuffer.wrap(host.getBytes());

        Long result = Math.abs(hasher.hash(buf, 0L));
        Long partition = result % 8192;

        System.out.println(result);
        System.out.println(partition);
    }
}
```

**Example dependency in Maven**  

```
        <dependency>
            <groupId>net.jpountz.lz4</groupId>
            <artifactId>lz4</artifactId>
            <version>1.3.0</version>
        </dependency>
```