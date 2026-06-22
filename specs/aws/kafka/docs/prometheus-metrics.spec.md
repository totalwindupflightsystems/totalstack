---
id: "@specs/aws/kafka/docs/prometheus-metrics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Use Prometheus metrics"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Use Prometheus metrics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/prometheus-metrics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use Prometheus metrics
<a name="prometheus-metrics"></a>

All metrics emitted by Apache Kafka to JMX are accessible using open monitoring with Prometheus. For information about Apache Kafka metrics, see [Monitoring](https://kafka.apache.org/documentation/#monitoring) in the Apache Kafka documentation. Along with Apache Kafka metrics, consumer-lag metrics are also available at port 11001 under the JMX MBean name `kafka.consumer.group:type=ConsumerLagMetrics`. You can also use the Prometheus Node Exporter to get CPU and disk metrics for your brokers at port 11002.