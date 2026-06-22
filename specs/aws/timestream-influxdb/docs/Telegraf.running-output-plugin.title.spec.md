---
id: "@specs/aws/timestream-influxdb/docs/Telegraf.running-output-plugin.title"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Running Telegraf with the Timestream for LiveAnalytics output plugin"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Running Telegraf with the Timestream for LiveAnalytics output plugin

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Telegraf.running-output-plugin.title
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Running Telegraf with the Timestream for LiveAnalytics output plugin
<a name="Telegraf.running-output-plugin.title"></a>

You can follow the instructions below to run Telegraf with the Timestream for LiveAnalytics plugin.

1. Generate an example configuration using Telegraf.

   ```
   telegraf --section-filter agent:inputs:outputs --input-filter cpu:mem --output-filter timestream config > example.config
   ```

1. Create a database in Timestream [using the management console](console_timestream.md#console_timestream.db.using-console), [CLI](https://docs.aws.amazon.com/cli/latest/reference/timestream-write/create-database.html), or [SDKs](getting-started-sdks.md).

1. In the `example.config` file, add your database name by editing the following key under the `[[outputs.timestream]] ` section.

   ```
   database_name = "yourDatabaseNameHere"
   ```

1. By default, Telegraf will create a table. If you wish create a table manually, set `create_table_if_not_exists` to `false` and follow the instructions to create a table [using the management console](console_timestream.md#console_timestream.table.using-console), [CLI](https://docs.aws.amazon.com/cli/latest/reference/timestream-write/create-table.html), or [SDKs](getting-started-sdks.md).

1. In the *example.config* file, configure credentials under the `[[outputs.timestream]] ` section. The credentials should allow the following operations.

   ```
   timestream:DescribeEndpoints
   timestream:WriteRecords
   ```
**Note**  
If you leave `create_table_if_not_exists` set to `true`, include:  

   ```
   timestream:CreateTable
   ```
**Note**  
If you set `describe_database_on_start` to `true`, include the following.  

   ```
   timestream:DescribeDatabase
   ```

1. You can edit the rest of the configuration according to your preferences.

1. When you have finished editing the config file, run Telegraf with the following.

   ```
   ./telegraf --config example.config
   ```

1. Metrics should appear within a few seconds, depending on your agent configuration. You should also see the new tables, *cpu* and *mem*, in the Timestream console.