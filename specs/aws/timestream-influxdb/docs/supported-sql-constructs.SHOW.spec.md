---
id: "@specs/aws/timestream-influxdb/docs/supported-sql-constructs.SHOW"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SHOW statements"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# SHOW statements

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/supported-sql-constructs.SHOW
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# SHOW statements
<a name="supported-sql-constructs.SHOW"></a>

You can view all the databases in an account by using the `SHOW DATABASES` statement. The syntax is as follows:

```
SHOW DATABASES [LIKE pattern]
```

where the `LIKE` clause can be used to filter database names.

You can view all the tables in an account by using the `SHOW TABLES` statement. The syntax is as follows:

```
SHOW TABLES [FROM database] [LIKE pattern]
```

where the `FROM` clause can be used to filter database names and the `LIKE` clause can be used to filter table names.

You can view all the measures for a table by using the `SHOW MEASURES` statement. The syntax is as follows:

```
SHOW MEASURES FROM database.table [LIKE pattern]
```

where the `FROM` clause will be used to specify the database and table name and the `LIKE` clause can be used to filter measure names.