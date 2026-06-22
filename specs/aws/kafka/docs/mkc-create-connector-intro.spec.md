---
id: "@specs/aws/kafka/docs/mkc-create-connector-intro"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a connector"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a connector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mkc-create-connector-intro
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a connector
<a name="mkc-create-connector-intro"></a>

This procedure describes how to create a connector using the AWS Management Console.

**Creating a connector using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Connectors**.

1. Choose **Create connector**.

1. You can choose between using an existing custom plugin to create the connector, or creating a new custom plugin first. For information on custom plugins and how to create them, see [Create custom plugins](msk-connect-plugins.md). In this procedure, let's assume you have a custom plugin that you want to use. In the list of custom plugins, find the one that you want to use, and select the box to its left, then choose **Next**.

1. Enter a name and, optionally, a description.

1. Choose the cluster that you want to connect to.

1. In the **Connector network settings** section, choose one of the following for network type:
   + **IPv4** (default) - For connectivity to destinations over IPv4 only
   + **Dual-stack** - For connectivity to destinations over both IPv4 and IPv6 (only available if your subnets have IPv4 and IPv6 CIDR blocks associated with them)

1. Specify the connector configuration. The configuration parameters that you need to specify depend on the type of connector that you want to create. However, some parameters are common to all connectors, for example, the `connector.class` and `tasks.max` parameters. The following is an example configuration for the [Confluent Amazon S3 Sink Connector](https://www.confluent.io/hub/confluentinc/kafka-connect-s3).

   ```
   connector.class=io.confluent.connect.s3.S3SinkConnector
   tasks.max=2
   topics=my-example-topic
   s3.region=us-east-1
   s3.bucket.name=amzn-s3-demo-bucket
   flush.size=1
   storage.class=io.confluent.connect.s3.storage.S3Storage
   format.class=io.confluent.connect.s3.format.json.JsonFormat
   partitioner.class=io.confluent.connect.storage.partitioner.DefaultPartitioner
   key.converter=org.apache.kafka.connect.storage.StringConverter
   value.converter=org.apache.kafka.connect.storage.StringConverter
   schema.compatibility=NONE
   ```

1. Next, you configure your connector capacity. You can choose between two capacity modes: provisioned and auto scaled. For information about these two options, see [Understand connector capacity](msk-connect-capacity.md).

1. (Optional) In the **Maximum Autoscaling Task Count** section, use the Maximum Autoscaling Task Count field to enter the maximum number of tasks you want to allocate to the connector during autoscaling operations. The value must be at least equal to your maximum worker count. If you don't specify a value, the connector uses the standard calculation without any limit. For more information, see [Understand maximum autoscaling task count](msk-connect-max-autoscaling-task-count.md).

1. Choose either the default worker configuration or a custom worker configuration. For information about creating custom worker configurations, see [Understand MSK Connect workers](msk-connect-workers.md).

1. Next, you specify the service execution role. This must be an IAM role that MSK Connect can assume, and that grants the connector all the permissions that it needs to access the necessary AWS resources. Those permissions depend on the logic of the connector. For information about how to create this role, see [Understand service execution role](msk-connect-service-execution-role.md).

1. Choose **Next**, review the security information, then choose **Next** again.

1. Specify the logging options that you want, then choose **Next**. For information about logging, see [Logging for MSK Connect](msk-connect-logging.md).

1. On the **Review and create** page, review your connector configuration and choose **Create connector**.

To use the MSK Connect API to create a connector, see [CreateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateConnector.html). 

You can use `UpdateConnector` API to modify the connector's configuration. For more information, see [Update a connector](mkc-update-connector.md).