---
id: "@specs/aws/kafka/docs/describe-topic-partitions-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View partition information using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# View partition information using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/describe-topic-partitions-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View partition information using the AWS CLI
<a name="describe-topic-partitions-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) of your cluster and {{TopicName}} with the name of the topic.

```
aws kafka describe-topic-partitions --cluster-arn {{ClusterArn}} --topic-name {{TopicName}}
```

The output of this command looks like the following JSON example.

```
{
    "partitions": [
        {
            "partition": 0,
            "leader": 1,
            "replicas": [1, 2, 3],
            "isr": [1, 2, 3]
        },
        {
            "partition": 1,
            "leader": 2,
            "replicas": [2, 3, 1],
            "isr": [2, 3, 1]
        },
        {
            "partition": 2,
            "leader": 3,
            "replicas": [3, 1, 2],
            "isr": [3, 1]
        }
    ]
}
```

## Understanding partition information
<a name="describe-topic-partitions-fields"></a>

The response includes the following information for each partition:
+ **partition** — The partition number. Partitions are numbered starting from 0.
+ **leader** — The broker ID of the leader for this partition. The leader handles all read and write requests for the partition.
+ **replicas** — The list of broker IDs that have replicas of this partition. This includes both in-sync and out-of-sync replicas.
+ **isr** — The list of broker IDs that are in-sync replicas. These replicas are fully caught up with the leader and can take over as leader if needed.

In the example above, partition 2 has an out-of-sync replica. The `replicas` list includes broker 2, but the `isr` list does not. This indicates that broker 2 is not fully caught up with the leader for this partition.

## Paginating results
<a name="describe-topic-partitions-pagination"></a>

If your topic has many partitions, you can use pagination to retrieve results in smaller batches. Use the `--max-results` parameter to specify the maximum number of partitions to return, and use the `--next-token` parameter to retrieve the next page of results.

```
aws kafka describe-topic-partitions --cluster-arn {{ClusterArn}} --topic-name {{TopicName}} --max-results 10
```

If there are more results available, the response includes a `nextToken` value. Use this token to retrieve the next page of results.

```
aws kafka describe-topic-partitions --cluster-arn {{ClusterArn}} --topic-name {{TopicName}} --max-results 10 --next-token {{NextToken}}
```

## Common use cases
<a name="describe-topic-partitions-use-cases"></a>

Viewing partition information is useful for several scenarios:
+ **Identifying under-replicated partitions** — Compare the `replicas` and `isr` lists to identify partitions where some replicas are not in sync. This can indicate performance issues or broker problems.
+ **Monitoring partition distribution** — Check that partition leaders are evenly distributed across brokers to ensure balanced load.
+ **Troubleshooting replication issues** — Identify which brokers are having trouble keeping up with replication by examining the ISR list.
+ **Planning partition rebalancing** — Use this information to understand the current partition layout before performing rebalancing operations.