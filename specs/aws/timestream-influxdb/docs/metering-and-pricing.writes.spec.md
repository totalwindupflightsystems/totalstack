---
id: "@specs/aws/timestream-influxdb/docs/metering-and-pricing.writes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Writes"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Writes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/metering-and-pricing.writes
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Writes
<a name="metering-and-pricing.writes"></a>

 The write size of each time series event is calculated as the sum of the size of the timestamp and one or more dimension names, dimension values, measure names, and measure values. The size of the timestamp is 8 bytes. The size of dimension names, dimension values, and measure names are the length of the UTF-8 encoded bytes of the string representing each dimension name, dimension value, and measure name. The size of the measure value depends on the data type. It is 1 byte for the boolean data type, 8 bytes for bigint and double, and the length of the UTF-8 encoded bytes for strings. Each write is counted in units of 1 KiB. 

Two example calculations are provided below:

**Topics**
+ [Calculating the write size of a time series event](#metering-and-pricing.writes.write-size-one-event)
+ [Calculating the number of writes](#metering-and-pricing.writes.write-size-multiple-events)

## Calculating the write size of a time series event
<a name="metering-and-pricing.writes.write-size-one-event"></a>

Consider a time series event representing the CPU utilization of an EC2 instance as shown below:


| Time | region | az | vpc | Hostname | measure\_name | measure\_value::double | 
| --- | --- | --- | --- | --- | --- | --- | 
| 1602983435238563000 | us-east-1 | 1d | vpc-1a2b3c4d | host-24Gju | cpu\_utilization | 35.0 | 

The write size of the time series event can be calculated as:
+ time = 8 bytes
+ first dimension = 15 bytes (`region`\+`us-east-1`)
+ second dimension = 4 bytes (`az`\+`1d`)
+ third dimension = 15 bytes (`vpc`\+`vpc-1a2b3c4d`)
+ fourth dimension = 18 bytes (`hostname`\+`host-24Gju`)
+ name of the measure = 15 bytes (`cpu_utilization`)
+ value of the measure = 8 bytes

**Write size of the time series event = 83 bytes**

## Calculating the number of writes
<a name="metering-and-pricing.writes.write-size-multiple-events"></a>

Now consider 100 EC2 instances, similar to the instance described in [Calculating the write size of a time series event](#metering-and-pricing.writes.write-size-one-event), emitting metrics every 5 seconds. The total monthly writes for the EC2 instances will vary based on how many time series events exist per write and if common attributes are being used while batching time series events. An example of calculating total monthly writes is provided for each of the following scenarios:

**Topics**
+ [One time series event per write](#metering-and-pricing.writes.write-size-multiple-events.one-event-per-write)
+ [Batching time series events in a write](#metering-and-pricing.writes.write-size-multiple-events.batching-events)
+ [Batching time series events and using common attributes in a write](#metering-and-pricing.writes.write-size-multiple-events.batching-events-and-using-common-attrbs)

### One time series event per write
<a name="metering-and-pricing.writes.write-size-multiple-events.one-event-per-write"></a>

If each write contains only one time series event, the total monthly writes are calculated as:
+ 100 time series events = 100 writes every 5 seconds
+ x 12 writes/minute = 1,200 writes
+ x 60 minutes/hour = 72,000 writes
+ x 24 hours/day = 1,728,000 writes
+ x 30 days/month = 51,840,000 writes

**Total monthly writes = 51,840,000**

### Batching time series events in a write
<a name="metering-and-pricing.writes.write-size-multiple-events.batching-events"></a>

Given each write is measured in units of 1 KB, a write can contain a batch of 12 time series events (998 bytes) and the total monthly writes are calculated as:
+ 100 time series events = 9 writes (12 time series events per write) every 5 seconds
+ x 12 writes/minute = 108 writes
+ x 60 minutes/hour = 6,480 writes
+ x 24 hours/day = 155,520 writes
+ x 30 days/month = 4,665,600 writes

**Total monthly writes = 4,665,600**

### Batching time series events and using common attributes in a write
<a name="metering-and-pricing.writes.write-size-multiple-events.batching-events-and-using-common-attrbs"></a>

If the region, az, vpc, and measure name are common across 100 EC2 instances, the common values can be specified just once per write and are referred to as common attributes. In this case, the size of common attributes is 52 bytes, and the size of the time series events is 27 bytes. Given each write is measured in units of 1 KiB, a write can contain 36 time series events and common attributes, and the total monthly writes are calculated as:
+ 100 time series events = 3 writes (36 time series events per write) every 5 seconds
+ x 12 writes/minute = 36 writes
+ x 60 minutes/hour = 2,160 writes
+ x 24 hours/day = 51,840 writes
+ x 30 days/month = 1,555,200 writes

**Total monthly writes = 1,555,200**

**Note**  
Due to usage of batching, common attributes and rounding of the writes to units of 1KB, the storage size of the time series events may be different than write size.