---
id: "@specs/aws/kafka/docs/intelligent-rebalancing-scaling-clusters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scaling Amazon MSK clusters"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Scaling Amazon MSK clusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/intelligent-rebalancing-scaling-clusters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Scaling Amazon MSK clusters up and down with a single operation
<a name="intelligent-rebalancing-scaling-clusters"></a>

With intelligent rebalancing, you can scale your clusters up or down by editing the broker count in your clusters in a single action. You can do this in the Amazon MSK console, or by using the AWS CLI, Amazon MSK APIs or AWS SDK, and AWS CloudFormation. When you change the broker count, Amazon MSK does the following:
+ Automatically distributes partitions to new brokers.
+ Moves partitions from brokers being removed.

As you scale your clusters up and down, cluster availability for clients to produce and consume data remains unaffected.

**Topics**

------
#### [ Scaling clusters using AWS Management Console ]

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. On the **Clusters** page, choose a newly created Express-based cluster. For information about creating a provisioned Express-based cluster, see [Step 1: Create an MSK Provisioned cluster](create-cluster.md).

1. On the **Actions** dropdown list, choose **Edit number of brokers**.

1. On the **Edit number of brokers per zone** page, do one of the following:
   + To add more brokers in your cluster, choose **Add brokers to each Availability Zone**, and then enter the number of brokers you want to add.
   + To remove brokers from your cluster, choose **Remove one broker from each Availability Zone**.

1. Choose **Save changes**.

------
#### [ Scaling clusters using AWS CLI ]

You can scale your clusters up or down by editing their broker count. To do this in the AWS CLI, use the [update-broker-count](https://docs.aws.amazon.com/cli/latest/reference/kafka/update-broker-count.html) command, as shown in the following example. In this command, specify the number of brokers you want in your cluster in the `target-broker-count` parameter.

```
aws msk update-broker-count --cluster-arn arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{abcd1234-5678-90ef-ghij-klmnopqrstuv-1}} --current-version {{ABCDEF1GHIJK0L}} --target-broker-count {{6}}
```

------
#### [ Scaling clusters using AWS SDK ]

You can scale your clusters up or down by programmatically editing the broker count. To do this using the AWS SDK, use the [UpdateBrokerCount](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-count.html#UpdateBrokerCount) API, as shown in the following example. For the `TargetNumberOfBrokerNodes` parameter, specify the number of brokers you want in your cluster.

```
update_broker_count_response = client.update_broker_count(
    ClusterArn='arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{abcd1234-5678-90ef-ghij-klmnopqrstuv-1}}',
    CurrentVersion='{{ABCDEF1GHIJK0L}}',
    TargetNumberOfBrokerNodes=6
)
```

------