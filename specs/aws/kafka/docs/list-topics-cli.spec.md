---
id: "@specs/aws/kafka/docs/list-topics-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS List topics using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# List topics using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/list-topics-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# List topics using the AWS CLI
<a name="list-topics-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md).

```
aws kafka list-topics --cluster-arn {{ClusterArn}}
```

The output of this command looks like the following JSON example.

```
{
    "topics": [
        {
            "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
            "topicName": "MyTopic",
            "partitionCount": 3,
            "replicationFactor": 3,
            "outOfSyncReplicaCount": 0
        },
        {
            "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/AnotherTopic",
            "topicName": "AnotherTopic",
            "partitionCount": 6,
            "replicationFactor": 3,
            "outOfSyncReplicaCount": 1
        }
    ]
}
```

## Paginating results
<a name="list-topics-pagination"></a>

If your cluster has many topics, you can use pagination to retrieve results in smaller batches. Use the `--max-results` parameter to specify the maximum number of topics to return, and use the `--next-token` parameter to retrieve the next page of results.

```
aws kafka list-topics --cluster-arn {{ClusterArn}} --max-results 10
```

If there are more results available, the response includes a `nextToken` value. Use this token to retrieve the next page of results.

```
aws kafka list-topics --cluster-arn {{ClusterArn}} --max-results 10 --next-token {{NextToken}}
```

## Filtering topics by name
<a name="list-topics-filter"></a>

You can filter the list of topics by specifying a prefix using the `--topic-name-filter` parameter. This returns only topics whose names start with the specified prefix.

```
aws kafka list-topics --cluster-arn {{ClusterArn}} --topic-name-filter "prod-"
```

This command returns only topics whose names start with `prod-`, such as `prod-orders` or `prod-inventory`.