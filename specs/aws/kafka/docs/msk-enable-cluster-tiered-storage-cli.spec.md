---
id: "@specs/aws/kafka/docs/msk-enable-cluster-tiered-storage-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enable tiered storage using CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Enable tiered storage using CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-enable-cluster-tiered-storage-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enable tiered storage on an existing Amazon MSK cluster using AWS CLI
<a name="msk-enable-cluster-tiered-storage-cli"></a>

**Note**  
You can enable tiered storage only if your cluster's log.cleanup.policy is set to `delete`, as compacted topics are not supported on tiered storage. Later, you can configure an individual topic's log.cleanup.policy to `compact` if tiered storage is not enabled on that particular topic. See [Topic-level configuration](https://docs.aws.amazon.com//msk/latest/developerguide/msk-configuration-properties.html#msk-topic-confinguration) for more details on supported configuration attributes.

1. **Update the Kafka version** – Cluster versions aren't simple integers. To find the current version of the cluster, use the `DescribeCluster` operation or the `describe-cluster` AWS CLI command. An example version is `KTVPDKIKX0DER`.

   ```
   aws kafka update-cluster-kafka-version --cluster-arn ClusterArn --current-version Current-Cluster-Version --target-kafka-version 3.6.0
   ```

1. Edit cluster storage mode. The following code example shows editing the cluster storage mode to `TIERED` using the [https://docs.aws.amazon.com/cli/latest/reference/kafka/update-storage.html](https://docs.aws.amazon.com/cli/latest/reference/kafka/update-storage.html) API.

   ```
   aws kafka update-storage --current-version Current-Cluster-Version --cluster-arn Cluster-arn --storage-mode TIERED
   ```