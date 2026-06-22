---
id: "@specs/aws/timestream-influxdb/docs/MSK"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon MSK"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon MSK

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/MSK
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon MSK
<a name="MSK"></a>

## Using Managed Service for Apache Flink to send Amazon MSK data to Timestream for LiveAnalytics
<a name="msk-aka"></a>

You can send data from Amazon MSK to Timestream by building a data connector similar to the sample Timestream data connector for Managed Service for Apache Flink. Refer to [Amazon Managed Service for Apache Flink](ApacheFlink.md) for more information.

## Using Kafka Connect to send Amazon MSK data to Timestream for LiveAnalytics
<a name="msk-kafka-connect"></a>

You can use Kafka Connect to ingest your time series data from Amazon MSK directly into Timestream for LiveAnalytics.

We've created a sample Kafka Sink Connector for Timestream. We've also created a sample Apache jMeter test plan for publishing data to a Kafka topic, so that the data can flow from the topic through the Timestream Kafka Sink Connector, to an Timestream for LiveAnalytics table. All of these artifacts are available on GitHub. 

**Note**  
Java 11 is the recommended version for using the Timestream Kafka Sink Connector. If you have multiple Java versions, ensure that you export Java 11 to your JAVA\_HOME environment variable. 

### Creating a sample application
<a name="msk-kafka-connect-app"></a>

To get started, follow the procedure below.

1. In Timestream for LiveAnalytics, create a database with the name `kafkastream`. 

   See the procedure [Create a database](console_timestream.md#console_timestream.db.using-console) for detailed instructions.

1. In Timestream for LiveAnalytics, create a table with the name `purchase_history`.

   See the procedure [Create a table](console_timestream.md#console_timestream.table.using-console) for detailed instructions.

1. Follow the instructions shared in the to create the following: , and .
   + An Amazon MSK cluster
   + An Amazon EC2 instance that is configured as a Kafka producer client machine 
   + A Kafka topic

   See the [prerequisites](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/java/kafka_ingestor#prerequisites) of the kafka\_ingestor project for detailed instructions.

1. Clone the [Timestream Kafka Sink Connector](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector) repository. 

   See [Cloning a repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) on GitHub for detailed instructions.

1. Compile the plugin code.

    See [Connector - Build from source](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector#connector---build-from-source) on GitHub for detailed instructions.

1. Upload the following files to an S3 bucket: following the instructions described in .
   + The jar file (kafka-connector-timestream->VERSION<-jar-with-dependencies.jar) from the `/target` directory
   + The sample json schema file, `purchase_history.json`.

   See [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the *Amazon S3 User Guide* for detailed instructions.

1. Create two VPC endpoints. These endpoints would be used by the MSK Connector to access the resources using AWS PrivateLink.
   + One to access the Amazon S3 bucket
   + One to access the Timestream for LiveAnalytics table.

   See [VPC Endpoints](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector#vpc-endpoints) for detailed instructions.

1. Create a custom plugin with the uploaded jar file.

   See [Plugins](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-plugins.html) in the *Amazon MSK Developer Guide * for detailed instructions.

1. Create a custom worker configuration with the JSON content described in [Worker Configuration parameters](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector#worker-configuration-parameters). following the instructions described in 

   See [Creating a custom worker configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-workers.html#msk-connect-create-custom-worker-config) in the *Amazon MSK Developer Guide * for detailed instructions.

1. Create a service execution IAM role.

   See [IAM Service Role](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector#iam-service-role) for detailed instructions.

1. Create an Amazon MSK connector with the custom plugin, custom worker configuration, and service execution IAM role created in the previous steps and with the [Sample Connector Configuration](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector#sample-connector-configuration).

   See [Creating a connector](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html#mkc-create-connector-intro) in the *Amazon MSK Developer Guide * for detailed instructions.

   Make sure to update the values of the below configuration parameters with respective values. See [Connector Configuration parameters](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/kafka_connector#connector-configuration-parameters) for details.
   + `aws.region`
   + `timestream.schema.s3.bucket.name`
   + `timestream.ingestion.endpoint`

   The connector creation takes 5–10 minutes to complete. The pipeline is ready when its status changes to `Running`.

1. Publish a continuous stream of messages for writing data to the Kafka topic created.

   See [How to use it](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/java/kafka_ingestor#how-to-use-it) for detailed instructions.

1. Run one or more queries to ensure that the data is being sent from Amazon MSK to MSK Connect to the Timestream for LiveAnalytics table. 

   See the procedure [Run a query](console_timestream.md#console_timestream.queries.using-console) for detailed instructions.

#### Additional resources
<a name="msk-kafka-connect-more-info"></a>

The blog, [Real-time serverless data ingestion from your Kafka clusters into Timestream for LiveAnalytics using Kafka Connect](https://aws.amazon.com/blogs/database/real-time-serverless-data-ingestion-from-your-kafka-clusters-into-amazon-timestream-using-kafka-connect/) explains setting up an end-to-end pipeline using the Timestream for LiveAnalytics Kafka Sink Connector, starting from a Kafka producer client machine that uses the Apache jMeter test plan to publish thousands of sample messages to a Kafka topic to verifying the ingested records in an Timestream for LiveAnalytics table.