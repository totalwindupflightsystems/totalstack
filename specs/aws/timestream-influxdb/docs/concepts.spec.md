---
id: "@specs/aws/timestream-influxdb/docs/concepts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Concepts"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Concepts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/concepts
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Timestream for LiveAnalytics concepts
<a name="concepts"></a>

 Time series data is a sequence of data points recorded over a time interval. This type of data is used for measuring events that change over time. Examples include the following.
+ Stock prices over time
+ Temperature measurements over time
+ CPU utilization of an EC2 instance over time

 With time series data, each data point consists of a timestamp, one or more attributes, and the event that changes over time. This data can be used to derive insights into the performance and health of an application, detect anomalies, and identify optimization opportunities. For example, DevOps engineers might want to view data that measures changes in infrastructure performance metrics. Manufacturers might want to track IoT sensor data that measures changes in equipment across a facility. Online marketers might want to analyze clickstream data that captures how a user navigates a website over time. Because time series data is generated from multiple sources in extremely high volumes, it needs to be cost-effectively collected in near real time, and therefore requires efficient storage that helps organize and analyze the data. 

 Following are the key concepts of Timestream for LiveAnalytics. 
+ **Time series** - *A sequence of one or more data points (or records) recorded over a time interval. * Examples are the price of a stock over time, the CPU or memory utilization of an EC2 instance over time, and the temperature/pressure reading of an IoT sensor over time.
+ **Record** - *A single data point in a time series.*
+ **Dimension** - *An attribute that describes the meta-data of a time series.* A dimension consists of a dimension name and a dimension value. Consider the following examples: 
  + When considering a stock exchange as a dimension, the dimension name is "stock exchange" and the dimension value is "NYSE"
  + When considering an AWS Region as a dimension, the dimension name is "region" and the dimension value is "us-east-1"
  + For an IoT sensor, the dimension name is "device ID" and the dimension value is "12345"
+ **Measure** - *The actual value being measured by the record. * Examples are the stock price, the CPU or memory utilization, and the temperature or humidity reading. Measures consist of measure names and measure values. Consider the following examples: 
  + For a stock price, the measure name is "stock price" and the measure value is the actual stock price at a point in time. 
  + For CPU utilization, the measure name is "CPU utilization" and the measure value is the actual CPU utilization.

  Measures can be modeled in Timestream for LiveAnalytics as multi-measure or single-measure records. For more information, see [Multi-measure records vs. single-measure records](data-modeling.md#data-modeling-multiVsinglerecords).
+ **Timestamp** - *Indicates when a measure was collected for a given record.* Timestream for LiveAnalytics supports timestamps with nanosecond granularity. 
+ **Table** - *A container for a set of related time series.* 
+ **Database** - *A top level container for tables.* 

## A summary of Timestream for LiveAnalytics concepts
<a name="w2aab7c17c12c13"></a>

 A **database** contains 0 or more **tables**. Each **table** contains 0 or more **time series**. Each **time series** consists of a sequence of **records** over a given time interval at a specified **granularity**. Each **time series** can be described using its meta-data or **dimensions**, its data or **measures**, and its **timestamps**. 

![Database hierarchy showing tables containing series with dimensions, timestamps, and measure values.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/concepts_simple.png)
