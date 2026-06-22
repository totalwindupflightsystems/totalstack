---
id: "@specs/aws/timestream-influxdb/docs/configuration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring Timestream for LiveAnalytics"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Configuring Timestream for LiveAnalytics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/configuration
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Configuring Amazon Timestream for LiveAnalytics
<a name="configuration"></a>

Configure the data retention period for the memory store and the magnetic store to match the data processing, storage, query performance, and cost requirements.
+ Set the data retention of the memory store to match your application's requirements for processing late-arriving data. Late-arriving data is incoming data with a timestamp earlier than the current time. It is emitted from resources that batch events for a time period before sending the data to Timestream for LiveAnalytics, and also from resources with intermittent connectivity e.g. an IoT sensor that is online intermittently.
+ If you expect late-arriving data to occasionally arrive with timestamps earlier than the memory store retention, you should enable magnetic store writes for your table. Once you set the EnableMagneticStoreWrites in MagneticStoreWritesProperties for a table, the table will accept data with timestamp earlier than your memory store retention but within your magnetic store retention period.
+ Consider the characteristics of queries that you plan to run on Timestream for LiveAnalytics such as the types of queries, frequency, time range, and performance requirements. This is because the memory store and magnetic store are optimized for different scenarios. The memory store is optimized for fast point-in-time queries that process small amounts of recent data sent to Timestream for LiveAnalytics. The magnetic store is optimized for fast analytical queries that process medium to large volumes of data sent to Timestream for LiveAnalytics.
+ Your data retention period should also be influenced by the cost requirements of your system.

  For example, consider a scenario where the late-arriving data threshold for your application is 2 hours and your applications send many queries that process a day's-worth, week's-worth, or month's-worth of data. In that case, you may want to configure a smaller retention period for the memory store (2-3 hours) and allow more data to flow to the magnetic store given the magnetic store is optimized for fast analytical queries.

Understand the impact of increasing or decreasing the data retention period of the memory store and the magnetic store of an existing table.
+ When you decrease the retention period of the memory store, the data is moved from the memory store to the magnetic store, and this data transfer is permanent. Timestream for LiveAnalytics does not retrieve data from the magnetic store to populate the memory store. When you decrease the retention period of the magnetic store, the data is deleted from the system, and the data deletion is permanent.
+ When you increase the retention period of the memory store or the magnetic store, the change takes effect for data being sent to Timestream for LiveAnalytics from that point onwards. Timestream for LiveAnalytics does not retrieve data from the magnetic store to populate the memory store. For example, if the retention period of the memory store was initially set to 2 hours and then increased to 24 hours, it will take 22 hours for the memory store to contain 24 hours worth of data.