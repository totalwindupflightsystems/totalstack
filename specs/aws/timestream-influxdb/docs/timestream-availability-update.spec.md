---
id: "@specs/aws/timestream-influxdb/docs/timestream-availability-update"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Timestream for LiveAnalytics availability change"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon Timestream for LiveAnalytics availability change

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/timestream-availability-update
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Timestream for LiveAnalytics availability change
<a name="timestream-availability-update"></a>

Since time-series applications have unique requirements and characteristics, we offer a broad framework to help you evaluate various alternatives before diving into specific implementation details. This high-level guidance serves as a foundation for your decision-making process, with more detailed steps and practical implementations to be covered in subsequent sections.

## Alternative services evaluation
<a name="alternative-services"></a>

**Use-case fits into Amazon Timestream for InfluxDB**  
We recommend [Timestream for InfluxDB](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html), if your Timestream for LiveAnalytics table has less than 10 million cardinality ([series keys](https://docs.influxdata.com/influxdb/v2/reference/key-concepts/data-elements/#series)), meaning the unique combinations of [Amazon Timestream for LiveAnalytics concepts](concepts.md) or if you can reduce your table's cardinality under 10 million. Timestream for InfluxDB gives you access to the capabilities of the open source version of InfluxDB. Choosing this path provides existing time-series functionality such as time-series analytics functions provided by [Flux](https://docs.influxdata.com/influxdb/v2/query-data/flux/), tasks (equivalent to [Scheduled queries](scheduled-query.md)) and other similar functions offered by Timestream for LiveAnalytics. Timestream for InfluxDB also provides [InfluxQL](https://docs.influxdata.com/influxdb/v2/query-data/influxql/) (an SQL-like query language) to interact with InfluxDB for querying and analyzing your time-series data.

**Prefer using SQL instead of InfluxQL**  
We recommend implementing Amazon Aurora or RDS PostgreSQL. These databases offer full SQL functionality while providing effective [time-series data management](https://docs.aws.amazon.com//AmazonRDS/latest/UserGuide/PostgreSQL_Partitions.html) capabilities. Time-series analytics can either be implemented using the built-in database functions where available, or managed at the application layer.

**Require high-scale data ingestion (exceeding 1 million records per second)**  
We recommend using Amazon DynamoDB or other AWS [NoSQL](https://aws.amazon.com/nosql/) databases. These databases can be selected based on your specific application needs. Time-series analytics can either be implemented using the built-in database functions where available, or managed at the application layer.

Before beginning your data migration to the chosen alternate AWS service, it is crucial to assess several key factors that will significantly influence your migration strategy and its ultimate success. These evaluations will help shape your approach, identify potential challenges, and ensure a smoother transition during the migration process.

**Data selection and retention considerations**

Assess your data migration scope by defining exact retention requirements. Consider whether you need to migrate the complete historical dataset, recent data only (such as the last 30, 60, or 90 days), or specific time-series data segments. This decision should be guided by three key factors: regulatory compliance requirements, analytical needs of your business, and practical considerations around migration complexity and costs.

**Query pattern compatibility analysis**

Query compatibility between your source (Timestream for LiveAnalytics) and target service requires thorough evaluation, as time-series databases handle query languages and features differently. Conduct comprehensive testing to identify syntax differences, functional gaps, and performance variations between systems. Test all business-critical queries or if possible all queries that your applications rely on to ensure they will function correctly after migration and are performant.

**Data transformation planning**

Before migrating, pay close attention to schema mapping to ensure proper data alignment and structural consistency between source and target systems, and accurate data type conversions specifically tailored for time-series data. These components work together to ensure data quality, optimize performance, and maintain functionality across different system architectures. In addition, consider any specialized indexing patterns and system-specific optimizations to guarantee efficient data access and retrieval.

**Continuity and downtime management**

Since data migration inherently causes operational disruption, developing a comprehensive switchover strategy is crucial for success. Few best practices to consider in the migration plan to minimize downtime are:
+ Implement temporary parallel processing systems where possible to maintain business continuity.
+ Schedule migrations during low-traffic periods such as weekends or overnight hours.
+ Establish well-tested rollback procedures for quick recovery in case of unexpected issues.