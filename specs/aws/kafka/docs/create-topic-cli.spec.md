---
id: "@specs/aws/kafka/docs/create-topic-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a topic using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a topic using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-topic-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a topic using the AWS CLI
<a name="create-topic-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md).

```
aws kafka create-topic --cluster-arn {{ClusterArn}} --topic-name MyTopic --partition-count 3 --replication-factor 3
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "status": "CREATING"
}
```