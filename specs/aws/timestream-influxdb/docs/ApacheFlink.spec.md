---
id: "@specs/aws/timestream-influxdb/docs/ApacheFlink"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Managed Service for Apache Flink"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon Managed Service for Apache Flink

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/ApacheFlink
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Managed Service for Apache Flink
<a name="ApacheFlink"></a>

You can use Apache Flink to transfer your time series data from Amazon Managed Service for Apache Flink, Amazon MSK, Apache Kafka, and other streaming technologies directly into Amazon Timestream for LiveAnalytics. We've created an Apache Flink sample data connector for Timestream. We've also created a sample application for sending data to Amazon Kinesis so that the data can flow from Kinesis to Managed Service for Apache Flink, and finally on to Amazon Timestream. All of these artifacts are available to you in GitHub. This [video tutorial ](https://youtu.be/64DSlBvN5lg) describes the setup.

**Note**  
 Java 11 is the recommended version for using the Managed Service for Apache Flink Application. If you have multiple Java versions, ensure that you export Java 11 to your JAVA\_HOME environment variable. 

**Topics**
+ [Sample application](#ApacheFlink.sample-app)
+ [Video tutorial](#ApacheFlink.video-tutorial)

## Sample application
<a name="ApacheFlink.sample-app"></a>

To get started, follow the procedure below:

1. Create a database in Timestream with the name `kdaflink` following the instructions described in [Create a database](console_timestream.md#console_timestream.db.using-console).

1. Create a table in Timestream with the name `kinesisdata1` following the instructions described in [Create a table](console_timestream.md#console_timestream.table.using-console).

1. Create an Amazon Kinesis Data Stream with the name `TimestreamTestStream` following the instructions described in [Creating a Stream](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-streams.html#how-do-i-create-a-stream).

1. Clone the GitHub repository for the [Apache Flink data connector for Timestream](https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/flink_connector) following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

1.  To compile, run and use the sample application, follow the instructions in the [ Apache Flink sample data connector README](https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/flink_connector/README.md). 

1. Compile the Managed Service for Apache Flink application following the instructions for [Compiling the Application Code](https://docs.aws.amazon.com/managed-flink/latest/java/get-started-exercise.html#get-started-exercise-5.5).

1. Upload the Managed Service for Apache Flink application binary following the instructions to [Upload the Apache Flink Streaming Code](https://docs.aws.amazon.com/managed-flink/latest/java/get-started-exercise.html#get-started-exercise-6).

   1. After clicking on Create Application, click on the link of the IAM Role for the application.

   1. Attach the IAM policies for **AmazonKinesisReadOnlyAccess** and **AmazonTimestreamFullAccess**.
**Note**  
The above IAM policies are not restricted to specific resources and are unsuitable for production use. For a production system, consider using policies that restrict access to specific resources.

1. Clone the GitHub repository for the [ sample application writing data to Kinesis](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/kinesis_ingestor) following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

1. Follow the instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/kinesis_ingestor/README.md) to run the sample application for writing data to Kinesis.

1. Run one or more queries in Timestream to ensure that data is being sent from Kinesis to Managed Service for Apache Flink to Timestream following the instructions to [Create a table](console_timestream.md#console_timestream.table.using-console).

## Video tutorial
<a name="ApacheFlink.video-tutorial"></a>

This [video](https://youtu.be/64DSlBvN5lg) explains how to use Timestream with Managed Service for Apache Flink.