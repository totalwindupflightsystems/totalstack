---
id: "@specs/aws/kafka/docs/update-topic-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update a topic using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update a topic using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/update-topic-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update a topic using the AWS CLI
<a name="update-topic-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster and {{TopicName}} with the name of the topic you want to update.

```
aws kafka update-topic --cluster-arn {{ClusterArn}} --topic-name {{TopicName}} --partition-count 6
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "status": "UPDATING"
}
```