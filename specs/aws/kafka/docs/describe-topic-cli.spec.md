---
id: "@specs/aws/kafka/docs/describe-topic-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Describe a topic using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Describe a topic using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/describe-topic-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Describe a topic using the AWS CLI
<a name="describe-topic-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster and {{TopicName}} with the name of the topic you want to describe.

```
aws kafka describe-topic --cluster-arn {{ClusterArn}} --topic-name {{TopicName}}
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "partitionCount": 3,
    "replicationFactor": 3,
    "configs": "Y29tcHJlc3Npb24udHlwZT1wcm9kdWNlcgpyZXRlbnRpb24ubXM9NjA0ODAwMDAw",
    "status": "ACTIVE"
}
```

## Understanding topic status
<a name="describe-topic-status"></a>

The `status` field indicates the current state of the topic. The following table describes the possible status values.


**Topic status values**  

| Status | Description | 
| --- | --- | 
| CREATING | The topic is being created. | 
| ACTIVE | The topic is active and ready for use. | 
| UPDATING | The topic configuration is being updated. | 
| DELETING | The topic is being deleted. | 

## Understanding topic configurations
<a name="describe-topic-configs"></a>

The `configs` field contains the topic's Kafka configuration properties, encoded in Base64 format. To view the configuration in a readable format, you need to decode the Base64 string.

The following example shows how to decode the configuration using the `base64` command on Linux or macOS.

```
echo "Y29tcHJlc3Npb24udHlwZT1wcm9kdWNlcgpyZXRlbnRpb24ubXM9NjA0ODAwMDAw" | base64 --decode
```

The decoded output shows the topic configuration properties in key-value format.

```
compression.type=producer
retention.ms=604800000
```

For more information about topic-level configuration properties, see [Topic-level Amazon MSK configuration](msk-configuration-properties.md#msk-topic-confinguration).