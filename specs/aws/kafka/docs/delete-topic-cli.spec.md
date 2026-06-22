---
id: "@specs/aws/kafka/docs/delete-topic-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete a topic using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Delete a topic using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/delete-topic-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete a topic using the AWS CLI
<a name="delete-topic-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster and {{TopicName}} with the name of the topic you want to delete.

```
aws kafka delete-topic --cluster-arn {{ClusterArn}} --topic-name {{TopicName}}
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "status": "DELETING"
}
```