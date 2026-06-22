---
id: "@specs/aws/kafka/docs/msk-connect-supported-worker-config-properties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Supported worker configuration properties"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Supported worker configuration properties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-supported-worker-config-properties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Supported worker configuration properties
<a name="msk-connect-supported-worker-config-properties"></a>

MSK Connect provides a default worker configuration. You also have the option to create a custom worker configuration to use with your connectors. The following list includes information about the worker configuration properties that Amazon MSK Connect does or does not support.
+ The `key.converter` and `value.converter` properties are required.
+ MSK Connect supports the following `producer.` configuration properties.

  ```
  producer.acks
  producer.batch.size
  producer.buffer.memory
  producer.compression.type
  producer.enable.idempotence
  producer.key.serializer
  producer.linger.ms
  producer.max.request.size
  producer.metadata.max.age.ms
  producer.metadata.max.idle.ms
  producer.partitioner.class
  producer.reconnect.backoff.max.ms
  producer.reconnect.backoff.ms
  producer.request.timeout.ms
  producer.retry.backoff.ms
  producer.value.serializer
  ```
+ MSK Connect supports the following `consumer.` configuration properties.

  ```
  consumer.allow.auto.create.topics
  consumer.auto.offset.reset
  consumer.check.crcs
  consumer.fetch.max.bytes
  consumer.fetch.max.wait.ms
  consumer.fetch.min.bytes
  consumer.heartbeat.interval.ms
  consumer.key.deserializer
  consumer.max.partition.fetch.bytes
  consumer.max.poll.interval.ms
  consumer.max.poll.records
  consumer.metadata.max.age.ms
  consumer.partition.assignment.strategy
  consumer.reconnect.backoff.max.ms
  consumer.reconnect.backoff.ms
  consumer.request.timeout.ms
  consumer.retry.backoff.ms
  consumer.session.timeout.ms
  consumer.value.deserializer
  ```
+ All other configuration properties that don't start with the `producer.` or `consumer.` prefixes are supported *except* for the following properties. 

  ```
  access.control.
  admin.
  admin.listeners.https.
  client.
  connect.
  inter.worker.
  internal.
  listeners.https.
  metrics.
  metrics.context.
  rest.
  sasl.
  security.
  socket.
  ssl.
  topic.tracking.
  worker.
  bootstrap.servers
  config.storage.topic
  connections.max.idle.ms
  connector.client.config.override.policy
  group.id
  listeners
  metric.reporters
  plugin.path
  receive.buffer.bytes
  response.http.headers.config
  scheduled.rebalance.max.delay.ms
  send.buffer.bytes
  status.storage.topic
  ```

**Note**  
Worker configuration properties apply only to Kafka Connect worker-level settings. JVM and logging framework properties (such as `log4j.*` or `log4j2.*`) are not supported and have no effect when specified in a custom worker configuration.

For more information about worker configuration properties and what they represent, see [Kafka Connect Configs](https://kafka.apache.org/documentation/#connectconfigs) in the Apache Kafka documentation.