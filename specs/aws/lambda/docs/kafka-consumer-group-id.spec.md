---
id: "@specs/aws/lambda/docs/kafka-consumer-group-id"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Consumer group ID"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Consumer group ID

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kafka-consumer-group-id
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Customizable consumer group ID in Lambda
<a name="kafka-consumer-group-id"></a>

When setting up Amazon MSK or self-managed Apache Kafka as an event source, you can specify a [consumer group](https://developer.confluent.io/learn-more/kafka-on-the-go/consumer-groups/) ID. This consumer group ID is an existing identifier for the Kafka consumer group that you want your Lambda function to join. You can use this feature to seamlessly migrate any ongoing Kafka record processing setups from other consumers to Lambda.

Kafka distributes messages across all consumers in a consumer group. If you specify a consumer group ID that has other active consumers, Lambda receives only a portion of the messages from the Kafka topic. If you want Lambda to handle all messages in the topic, turn off any other consumers in that consumer group.

Additionally, if you specify a consumer group ID, and Kafka finds a valid existing consumer group with the same ID, Lambda ignores the [StartingPosition](kafka-starting-positions.md) for your event source mapping. Instead, Lambda begins processing records according to the committed offset of the consumer group. If you specify a consumer group ID, and Kafka cannot find an existing consumer group, then Lambda configures your event source with the specified `StartingPosition`.

The consumer group ID that you specify must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value.