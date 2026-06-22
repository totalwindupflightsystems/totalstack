---
id: "@specs/aws/kafka/docs/intelligent-rebalancing-self-balancing-paritions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Steady state rebalancing"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Steady state rebalancing

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/intelligent-rebalancing-self-balancing-paritions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Steady state rebalancing for Amazon MSK clusters
<a name="intelligent-rebalancing-self-balancing-paritions"></a>

**Note**  
Effective June 18, 2026, Intelligent Rebalancing is available for all MSK Provisioned clusters with Express brokers. This includes Express clusters created prior to the launch of intelligent rebalancing feature in November 2025. For clusters created before November 20, 2025, Intelligent Rebalancing is available with **Rebalancing Status** set to **Paused**. To enable this feature for your existing clusters, set **Rebalancing Status** to **Active** using the Amazon MSK console, AWS CLI, or SDK. For instructions, see [Steady state rebalancing](#intelligent-rebalancing-self-balancing-paritions).

Steady state rebalancing is a part of the intelligent rebalancing feature, which is turned on by default for all new MSK Provisioned clusters with Express brokers. As you scale your clusters up or down, Amazon MSK automatically handles partition management by distributing partitions to new brokers and moving partitions from brokers due for removal. To ensure optimal distribution of workload across brokers, intelligent rebalancing uses Amazon MSK best practices to determine thresholds for automatically initiating rebalancing for your brokers.

You can pause and resume steady state rebalancing when needed. Steady state rebalancing continuously monitors your cluster and does the following:
+ Tracks broker resource usage (CPU, network, storage).
+ Adjusts partition placement automatically without any impact on data availability.
+ Completes rebalancing operations up to 180x faster for Express brokers as compared to Standard brokers.
+ Maintains cluster performance.

**Topics**

------
#### [ Pause and resume steady state rebalancing in AWS Management Console ]

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. On the **Clusters** page, choose an Express-based cluster. For information about creating a provisioned Express-based cluster, see [Step 1: Create an MSK Provisioned cluster](create-cluster.md).

1. On the Cluster detail page, verify the **Intelligent rebalancing** status. If the status is **Paused**, follow steps 4–5 to enable it.

1. On the **Actions** dropdown list, choose **Edit intelligent rebalancing**.

1. On the **Edit intelligent rebalancing** page, do the following:

   1. Choose **Active**.

   1. Choose **Save changes**.

------
#### [ Pause and resume steady state rebalancing using AWS CLI ]

To set the rebalancing status of a cluster to **ACTIVE** using the AWS CLI, use the [update-rebalancing](https://docs.aws.amazon.com/cli/latest/reference/kafka/update-rebalancing.html) command, as shown in the following example. In this command, specify the status with the `rebalancing` parameter.

```
aws msk update-rebalancing --cluster-arn arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{abcd1234-5678-90ef-ghij-klmnopqrstuv-1}} --current-version {{ABCDEF1GHIJK0L}} --rebalancing "{\"Rebalancing\":{\"Status\":\"ACTIVE\"}}"
```

------
#### [ Pause and resume steady state rebalancing using AWS SDK ]

You can also set the rebalancing status of a cluster using the [UpdateRebalancingRequest](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-rebalancing.html#UpdateRebalancing) API to programmatically modify the broker count. The following examples show how to set the rebalancing status to **ACTIVE** and **PAUSED**.

```
final UpdateRebalancingRequest updateRebalancingRequest = new UpdateRebalancingRequest()
    .withClusterArn(arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{abcd1234-5678-90ef-ghij-klmnopqrstuv-1}})
    .withCurrentVersion({{ABCDEF1GHIJK0L}})
    .withRebalancing(new Rebalancing().withStatus("ACTIVE"));
```

```
final UpdateRebalancingRequest updateRebalancingRequest = new UpdateRebalancingRequest()
    .withClusterArn(arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{abcd1234-5678-90ef-ghij-klmnopqrstuv-1}})
    .withCurrentVersion({{ABCDEF1GHIJK0L}})
    .withRebalancing(new Rebalancing().withStatus("PAUSED"));
```

------