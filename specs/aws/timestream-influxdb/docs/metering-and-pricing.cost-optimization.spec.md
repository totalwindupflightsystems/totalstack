---
id: "@specs/aws/timestream-influxdb/docs/metering-and-pricing.cost-optimization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cost optimization"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Cost optimization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/metering-and-pricing.cost-optimization
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Cost optimization
<a name="metering-and-pricing.cost-optimization"></a>

To optimize the cost of writes, storage, and queries, use the following best practices with Amazon Timestream for LiveAnalytics:
+ Batch multiple time series events per write to reduce the number of write requests.
+ Consider using Multi-measure records, which allows you to write multiple time-series measures in a single write request and stores your data in a more compact manner. This reduces the number of write requests as well as data storage cost and query cost. 
+ Use common attributes with batching to batch more time series events per write to further reduce the number of write requests.
+ Set the data retention of the memory store to match your application's requirements for processing late-arriving data. Late-arriving data is incoming data with a timestamp earlier than the current time and outside the memory store retention period.
+ Set the data retention of the magnetic store to match your long term data storage requirements.
+ While writing queries, include only the measure and dimension names essential to query. Adding extraneous columns will increase data scans and therefore will also increase the query cost. We recommend that you review [query insights](using-query-insights.md) to assess the pruning efficiency of the included dimensions and measures.
+ Where possible, include a time range in the WHERE clause of your query. For example, if you only need the last one hour of data in your dataset, include a time predicate such as `time > ago(1h)`.
+ When a query accesses a subset of measures in a table, always include the measure names in the WHERE clause of the query.
+ If you've started running a query and realize that the query will not return the results you're looking for, cancel the query to save on cost.