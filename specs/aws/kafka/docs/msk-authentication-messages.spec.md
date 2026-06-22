---
id: "@specs/aws/kafka/docs/msk-authentication-messages"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Produce and consume messages using authentication"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Produce and consume messages using authentication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-authentication-messages
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Produce and consume messages using authentication
<a name="msk-authentication-messages"></a>

This process describes how to produce and consume messages using authentication.

1. Run the following command to create a topic. The file named `client.properties` is the one you created in the previous procedure.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-topics.sh --create --bootstrap-server {{BootstrapBroker-String}} --replication-factor 3 --partitions 1 --topic ExampleTopic --command-config client.properties
   ```

1. Run the following command to start a console producer. The file named `client.properties` is the one you created in the previous procedure.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-console-producer.sh --bootstrap-server {{BootstrapBroker-String}} --topic ExampleTopic --producer.config client.properties
   ```

1. In a new command window on your client machine, run the following command to start a console consumer.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-console-consumer.sh --bootstrap-server {{BootstrapBroker-String}} --topic ExampleTopic --consumer.config client.properties
   ```

1. Type messages in the producer window and watch them appear in the consumer window.