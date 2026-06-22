---
id: "@specs/aws/timestream-influxdb/docs/supported-sql-constructs.DESCRIBE"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DESCRIBE statements"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# DESCRIBE statements

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/supported-sql-constructs.DESCRIBE
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# DESCRIBE statements
<a name="supported-sql-constructs.DESCRIBE"></a>

You can view the metadata for a table by using the `DESCRIBE` statement. The syntax is as follows:

```
DESCRIBE database.table
```

where `table` contains the table name. The describe statement returns the column names and data types for the table.