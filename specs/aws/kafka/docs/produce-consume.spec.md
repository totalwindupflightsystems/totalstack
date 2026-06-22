---
id: "@specs/aws/kafka/docs/produce-consume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Produce and consume data"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Produce and consume data

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/produce-consume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 5: Produce and consume data
<a name="produce-consume"></a>

In this step of [Get Started Using Amazon MSK](getting-started.md), you produce and consume data.

**To produce and consume messages**Produce and consume messages

1. Run the following command to start a console producer.

   ```
   $KAFKA_ROOT/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVER --producer.config $KAFKA_ROOT/config/client.properties --topic {{MSKTutorialTopic}}
   ```

1. Enter any message that you want, and press **Enter**. Repeat this step two or three times. Every time you enter a line and press **Enter**, that line is sent to your Apache Kafka cluster as a separate message.

1. Keep the connection to the client machine open, and then open a second, separate connection to that machine in a new window. Because this is a new session, set the `KAFKA_ROOT` and `BOOTSTRAP_SERVER` environment variables again. For information about how to set these environment variables, see [Creating a topic on the client machine](create-topic.md#create-topic-client-machine).

1. Run the following command with your second connection string to the client machine to create a console consumer.

   ```
   $KAFKA_ROOT/bin/kafka-console-consumer.sh --bootstrap-server $BOOTSTRAP_SERVER --consumer.config $KAFKA_ROOT/config/client.properties --topic {{MSKTutorialTopic}} --from-beginning
   ```

   You should start seeing the messages you entered earlier when you used the console producer command.

1. Enter more messages in the producer window, and watch them appear in the consumer window.

**Next Step**

[Step 6: Use Amazon CloudWatch to view Amazon MSK metrics](view-metrics.md)