---
id: "@specs/aws/kafka/docs/msk-create-cluster-tiered-storage-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create tiered storage cluster with AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create tiered storage cluster with AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-create-cluster-tiered-storage-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create an Amazon MSK cluster with tiered storage with the AWS CLI
<a name="msk-create-cluster-tiered-storage-cli"></a>

To enable tiered storage on a cluster, create the cluster with the correct Apache Kafka version and attribute for tiered storage. Follow the code example below. Also, complete the steps in the next section to [Create a Kafka topic with tiered storage enabled with the AWS CLI](#msk-create-topic-tiered-storage-cli).

See [create-cluster](https://docs.aws.amazon.com//cli/latest/reference/kafka/create-cluster.html) for a complete list of supported attributes for cluster creation.

```
aws kafka create-cluster \
 —cluster-name "MessagingCluster" \
 —broker-node-group-info file://brokernodegroupinfo.json \
 —number-of-broker-nodes 3 \
--kafka-version "3.6.0" \
--storage-mode "TIERED"
```

## Create a Kafka topic with tiered storage enabled with the AWS CLI
<a name="msk-create-topic-tiered-storage-cli"></a>

To complete the process that you started when you created a cluster with the tiered storage enabled, also create a topic with tiered storage enabled with the attributes in the later code example. The attributes specifically for tiered storage are the following:
+ `local.retention.ms` (for example, 10 mins) for time-based retention settings or `local.retention.bytes` for log segment size limits.
+ `remote.storage.enable` set to `true` to enable tiered storage.

The following configuration uses local.retention.ms, but you can replace this attribute with local.retention.bytes. This attribute controls the amount of time that can pass or number of bytes that Apache Kafka can copy before Apache Kafka copies the data from primary to tiered storage. See [Topic-level configuration](https://docs.aws.amazon.com//msk/latest/developerguide/msk-configuration-properties.html#msk-topic-confinguration) for more details on supported configuration attributes.

**Note**  
You must use the Apache Kafka client version 3.0.0 and above. These versions support a setting called `remote.storage.enable` only in those client versions of `kafka-topics.sh`. To enable tiered storage on an existing topic that uses an earlier version of Apache Kafka, see the section [Enabling tiered storage on an existing Amazon MSK topic](msk-enable-disable-topic-tiered-storage-cli.md#msk-enable-topic-tiered-storage-cli).

```
bin/kafka-topics.sh --create --bootstrap-server $bs --replication-factor 2 --partitions 6 --topic MSKTutorialTopic --config remote.storage.enable=true --config local.retention.ms=100000 --config retention.ms=604800000 --config segment.bytes=134217728
```