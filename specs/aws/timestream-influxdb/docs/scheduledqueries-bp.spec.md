---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-bp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scheduled queries"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Scheduled queries

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-bp
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Scheduled queries
<a name="scheduledqueries-bp"></a>

Scheduled queries help you optimize your dashboards by pre-computing some fleet-wide aggregate statistics. So a natural question to ask is how do you take your use case and identify which results to pre-compute and how to use these results stored in a derived table to create your dashboard. The first step in this process is to identify which panels to pre-compute. Below are some high-level guidelines:
+ Consider the bytes scanned by the queries that are used to populate the panels, the frequency of dashboard reload, and number of concurrent users who would load these dashboards. You should start with the dashboards loaded most frequently and scanning significant amounts of data. The first two dashboards in the [aggregate dashboard](https://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-example1.html) example as well as the aggregate dashboard in the [drill down](https://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-example2.html) example are good examples of such dashboards. 
+ Consider which computations are being [repeatedly used](https://docs.aws.amazon.com/timestream/latest/developerguide/cheduledqueries-example3.html). While it is possible to create a scheduled query for every panel and every variable value used in the panel, you can significantly optimize your costs and the number of scheduled queries by looking for avenues to use one computation to pre-compute the data necessary for multiple panels. 
+ Consider the frequency of your scheduled queries to refresh the materialized results in the derived table. You would want to analyze how frequently a dashboard is refreshed vs. the time window that is queried in a dashboard vs. the time binning used in the pre-computation as well as the panels in the dashboards. For instance, if a dashboard that is plotting hourly aggregates for the past few days is only refreshed once in a few hours, you might want to configure your scheduled queries to only refresh once every 30 mins or an hour. On the other hand, if you have a dashboard that plots per minute aggregates and is refreshed every minute or so, you would want your scheduled queries to refresh the results every minute or few minutes.
+ Consider which query patterns can be further optimized (both from a query cost and query latency perspective) using scheduled queries. For instance, when computing the unique dimension values frequently used as variables in dashboards, or returning the last data point emitted from a sensor or the first data point emitted from a sensor after a certain date, etc. Some of these [example patterns](https://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-patterns.html) are discussed in this guide.

The preceding considerations will have a significant impact on your savings when you move your dashboard to query the derived tables, the freshness of data in your dashboards, and the cost incurred by the scheduled queries.