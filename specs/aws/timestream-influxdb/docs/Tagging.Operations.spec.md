---
id: "@specs/aws/timestream-influxdb/docs/Tagging.Operations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tagging operations"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Tagging operations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Tagging.Operations
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Tagging operations
<a name="Tagging.Operations"></a>

You can add, list, edit, or delete tags for databases and tables using the Amazon Timestream for LiveAnalytics console, query language, or the AWS Command Line Interface (AWS CLI). 

**Topics**
+ [Adding tags to new or existing databases and tables using the console](#Tagging.Operations.using-console)

## Adding tags to new or existing databases and tables using the console
<a name="Tagging.Operations.using-console"></a>

You can use the Timestream for LiveAnalytics console to add tags to new databases, tables and scheduled queries when you create them. You can also add, edit, or delete tags for existing tables.

**To tag databases when creating them (console)**

1. Open the Timestream console at [https://console.aws.amazon.com/timestream](https://console.aws.amazon.com/timestream).

1. In the navigation pane, choose **Databases**, and then choose **Create database**.

1. On the **Create database** page, provide a name for the database. Enter a key and value for the tag, and then choose **Add new tag**.

1. Choose **Create database**.

**To tag tables when creating them (console)**

1. Open the Timestream console at [https://console.aws.amazon.com/timestream](https://console.aws.amazon.com/timestream).

1. In the navigation pane, choose **Tables**, and then choose **Create table**.

1. On the **Create Timestream for LiveAnalytics table** page, provide a name for the table. Enter a key and value for the tag, and choose **Add new tag**. 

1. Choose **Create table**.

**To tag scheduled queries when creating them (console)**

1. Open the Timestream console at [https://console.aws.amazon.com/timestream](https://console.aws.amazon.com/timestream).

1. In the navigation pane, choose **Scheduled queries**, and then choose **Create scheduled query**.

1. On the **Step 3. Configure query settings** page, choose **Add new tag**. Enter a key and value for the tag. Choose **Add new tag** to add additional tags.

1. Choose **Next**.

**To tag existing resources (console)**

1. Open the Timestream console at [https://console.aws.amazon.com/timestream](https://console.aws.amazon.com/timestream).

1. In the navigation pane, choose **Databases**, **Tables** or **Scheduled queries**.

1. Choose a database or table in the list. Then choose **Manage tags** to add, edit, or delete your tags.

For information about tag structure, see [Tagging restrictions](TaggingRestrictions.md). 