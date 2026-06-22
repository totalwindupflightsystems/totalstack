---
id: "@specs/aws/timestream-influxdb/docs/batch-load-using-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using batch load with the console"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Using batch load with the console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/batch-load-using-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Using batch load with the console
<a name="batch-load-using-console"></a>

Following are steps for using batch load with the AWS Management Console. You can download a sample CSV at [sample CSV](samples/batch-load-sample-file.csv.zip).

**Topics**
+ [Access batch load](#console_timestream.access-batch-load.using-console)
+ [Create a batch load task](#console_timestream.create-batch-load.using-console)
+ [Resume a batch load task](#console_timestream.resume-batch-load.using-console)
+ [Using the visual builder](#batch-load-using-visual-builder)

## Access batch load
<a name="console_timestream.access-batch-load.using-console"></a>

Follow these steps to access batch load using the AWS Management Console.

1. Open the [Amazon Timestream console](https://console.aws.amazon.com/timestream).

1. In the navigation pane, choose **Management Tools**, and then choose **Batch load tasks**.

1. From here, you can view the list of batch load tasks and drill into a given task for more details. You can also create and resume tasks.

## Create a batch load task
<a name="console_timestream.create-batch-load.using-console"></a>

Follow these steps to create a batch load task using the AWS Management Console.

1. Open the [Amazon Timestream console](https://console.aws.amazon.com/timestream).

1. In the navigation pane, choose **Management Tools**, and then choose **Batch load tasks**.

1. Choose **Create batch load task**.

1. In **Import destination**, choose the following.
   + **Target database** – Select the name of the database created in [Create a database](console_timestream.md#console_timestream.db.using-console).
   + **Target table** – Select the name of the table created in [Create a table](console_timestream.md#console_timestream.table.using-console).

   If necessary, you can add a table from this panel with the **Create new table** button.

1. From **Data source S3 location** in **Data source**, select the S3 bucket where the source data is stored. Use the **Browse S3** button to view S3 resources the active AWS account has access to, or enter the S3 location URL. The data source must be located in the same region.

1. In **File format settings** (expandable section), you can use the default settings to parse input data. You can also choose **Advanced settings**. From there you can choose **CSV format parameters**, and select parameters to parse input data. For information about these parameters, see [CSV format parameters](batch-load-preparing-data-file.md#batch-load-data-file-options).

1. From **Configure data model mapping**, configure the data model. For additional data model guidance, see [Data model mappings for batch load](batch-load-data-model-mappings.md)
   + From **Data model mapping**, choose **Mapping configuration input**, and choose one of the following.
     + **Visual builder** – To map data visually, choose **TargetMultiMeasureName** or **MeasureNameColumn**. Then from **Visual builder**, map the columns.

       Visual builder automatically detects and loads the source column headers from the data source file when a single CSV file is selected as the data source. Choose the attribute and data type to create your mapping.

       For information about using the visual builder, see [Using the visual builder](#batch-load-using-visual-builder).
     + **JSON editor** – A freeform JSON editor for configuring your data model. Choose this option if you're familiar with Timestream for LiveAnalytics and want to build advanced data model mappings.
     + **JSON file from S3** – Select a JSON model file you have stored in S3. Choose this option if you've already configured a data model and want to reuse it for additional batch loads.

1. From **Error logs S3 location** in **Error log report**, select the S3 location that will be used to report errors. For information about how to use this report, see [Using batch load error reports](batch-load-using-error-reports.md).

1. For **Encryption key type**, choose one of the following.
   + **Amazon S3-managed key (SSE-S3)** – An encryption key that Amazon S3 creates, manages, and uses for you.
   + **AWS KMS key (SSE-KMS)** – An encryption key protected by AWS Key Management Service (AWS KMS).

1. Choose **Next**.

1. On the **Review and create page**, review the settings and edit as necessary.
**Note**  
You can't change batch load task settings after the task has been created. Task completion times will vary based on the amount of data being imported.

1. Choose **Create batch load task**.

## Resume a batch load task
<a name="console_timestream.resume-batch-load.using-console"></a>

When you select a batch load task with a status of "Progress stopped" which is still resumable, you are prompted to resume the task. There is also a banner with a **Resume task** button when you view the details for those tasks. Resumable tasks have a "resume by" date. After that date expires, tasks cannot be resumed.

## Using the visual builder
<a name="batch-load-using-visual-builder"></a>

You can use the visual builder to map source data columns one or more CSV file(s) stored in an S3 bucket to destination columns in a Timestream for LiveAnalytics table.

**Note**  
Your role will need the `SelectObjectContent` permission for the file. Without this, you will need to add and delete columns manually.

### Auto load source columns mode
<a name="batch-load-using-visual-builder-auto-load"></a>

Timestream for LiveAnalytics can automatically scan the source CSV file for column names if you specify one bucket only. When there are no existing mappings, you can choose **Import source columns**.

1. With the **Visual builder** option selected from the **Mapping configuration input settings**, set the Timestamp time input. `Milliseconds` is the default setting.

1. Click the **Load source columns** button to import the column headers found in the source data file. The table will be populated with the source column header names from the data source file.

1. Choose the **Target table column name**, **Timestream attribute type**, and **Data type** for each source column.

   For details about these columns and possible values, see [Mapping fields](#batch-load-using-visual-builder-mapping-fields).

1. Use the drag-to-fill feature to set the value for multiple columns at once.

### Manually add source columns
<a name="batch-load-using-visual-builder-manually-add"></a>

If you're using a bucket or CSV prefix and not a single CSV, you can add and delete column mappings from the visual editor with the **Add column mapping** and **Delete column mapping** buttons. There is also a button to reset mappings.

### Mapping fields
<a name="batch-load-using-visual-builder-mapping-fields"></a>
+ **Source column name** – The name of a column in the source file that represents a measure to import. Timestream for LiveAnalytics can populate this value automatically when you use **Import source columns**.
+ **Target table column name** – Optional input that indicates the column name for the measure in the target table.
+ **Timestream attribute type** – The attribute type of the data in the specified source column such as `DIMENSION`.
  + **TIMESTAMP** – Specifies when a measure was collected.
  + **MULTI** – Multiple measures are represented.
  + **DIMENSION** – Time series metadata.
  + **MEASURE\_NAME** – For single-measure records, this is the measure name.
+ **Data type** – The type of Timestream column, such as `BOOLEAN`.
  + **BIGINT** – A 64-bit integer.
  + **BOOLEAN** – The two truth values of logic—true and false.
  + **DOUBLE** – 64-bit variable-precision number.
  + **TIMESTAMP** – An instance in time that uses nanosecond precision time in UTC, and tracks the time since the Unix epoch.