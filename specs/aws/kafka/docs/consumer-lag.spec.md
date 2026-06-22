---
id: "@specs/aws/kafka/docs/consumer-lag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitor consumer lags"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Monitor consumer lags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/consumer-lag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitor consumer lags
<a name="consumer-lag"></a>

Monitoring consumer lag allows you to identify slow or stuck consumers that aren't keeping up with the latest data available in a topic. When necessary, you can then take remedial actions, such as scaling or rebooting those consumers. To monitor consumer lag, you can use Amazon CloudWatch or open monitoring with Prometheus.

Consumer lag metrics quantify the difference between the latest data written to your topics and the data read by your applications. Amazon MSK provides the following consumer-lag metrics, which you can get through Amazon CloudWatch or through open monitoring with Prometheus: `EstimatedMaxTimeLag`, `EstimatedTimeLag`, `MaxOffsetLag`, `OffsetLag`, and `SumOffsetLag`. For information about these metrics, see [Amazon MSK metrics for monitoring Standard brokers with CloudWatch](metrics-details.md).

Amazon MSK supports consumer lag metrics for clusters with Apache Kafka 2.2.1 or a later version. Consider the following points when you work with Kafka and CloudWatch metrics:
+ Consumer lag metrics are emitted only if a consumer group is in a STABLE or EMPTY state. A consumer group is STABLE after the successful completion of re-balancing, ensuring that partitions are evenly distributed among the consumers.
+ Consumer lag metrics are absent in the following scenarios:
  + If the consumer group is unstable.
  + The name of the consumer group contains a colon (:).
  + You haven't set the consumer offset for the consumer group.
+ Consumer group names are used as dimensions for consumer lag metrics in CloudWatch. While Kafka supports UTF-8 characters in consumer group names, CloudWatch supports only ASCII characters for [dimension values](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Dimension.html). If you use non-ASCII characters in consumer group names, CloudWatch drops the consumer lag metrics. To make sure that your consumer lag metrics are properly captured in CloudWatch, you must use only ASCII characters in your consumer group names.