---
id: "@specs/aws/kafka/docs/version-upgrades-best-practices"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Best practices for version upgrades"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Best practices for version upgrades

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/version-upgrades-best-practices
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Best practices for version upgrades
<a name="version-upgrades-best-practices"></a>

To ensure client continuity during the rolling update that is performed as part of the Kafka version upgrade process, review the configuration of your clients and your Apache Kafka topics as follows:
+ Set the topic replication factor (RF) to a minimum value of `2` for two-AZ clusters and a minimum value of `3` for three-AZ clusters. An RF value of `2` can lead to offline partitions during patching.
+ Set minimum in-sync replicas (minISR) to a maximum value of 1 less than your Replication Factor (RF), which is `miniISR = (RF) - 1`. This makes sure that the partition replica set can tolerate one replica being offline or under-replicated.
+ Configure clients to use multiple broker connection strings. Having multiple brokers in a client’s connection string allows for failover if a specific broker supporting client I/O begins to be patched. For information about how to get a connection string with multiple brokers, see [Getting the bootstrap brokers for an Amazon MSK cluster](https://docs.aws.amazon.com//msk/latest/developerguide/msk-get-bootstrap-brokers.html).
+ We recommend that you upgrade connecting clients to the recommended version or above to benefit from the features available in the new version. Client upgrades are not subject to the end of life (EOL) dates of your MSK cluster's Kafka version, and do not need to be completed by the EOL date. Apache Kafka provides a [bi-directional client compatibility policy](https://kafka.apache.org/protocol#protocol_compatibility) that allows older clients to work with newer clusters and vice versa.
+ Kafka clients using versions 3.x.x are likely to come with the following defaults: `acks=all` and `enable.idempotence=true`. `acks=all` is different from the previous default of `acks=1` and provides extra durability by ensuring that all in-sync replicas acknowledge the produce request. Similarly, the default for `enable.idempotence` was previously `false`. The change to `enable.idempotence=true` as the default lowers the likelihood of duplicate messages. These changes are considered best practice settings and may introduce a small amount of additional latency that's within normal performance parameters.
+ Use the recommended Kafka version when creating new MSK clusters. Using the recommended Kafka version allows you to benefit from the latest Kafka and MSK features.