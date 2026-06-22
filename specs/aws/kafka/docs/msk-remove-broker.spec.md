---
id: "@specs/aws/kafka/docs/msk-remove-broker"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Remove a broker"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Remove a broker

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-remove-broker
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Remove a broker from an Amazon MSK cluster
<a name="msk-remove-broker"></a>

Use this Amazon MSK operation when you want to remove brokers from Amazon Managed Streaming for Apache Kafka (MSK) provisioned clusters. You can reduce your cluster’s storage and compute capacity by removing sets of brokers, with no availability impact, data durability risk, or disruption to your data streaming applications.

You can add more brokers to your cluster to handle increase in traffic, and remove brokers when the traffic subsides. With broker addition and removal capability, you can best utilize your cluster capacity and optimize your MSK infrastructure costs. Broker removal gives you broker-level control over existing cluster capacity to fit your workload needs and avoid migration to another cluster.

Use the AWS Console, Command Line Interface (CLI), SDK, or CloudFormation to reduce broker count of your provisioned cluster. MSK picks the brokers that do not have any partitions on them (except for canary topics) and prevents applications from producing data to those brokers, while safely removing those brokers from the cluster.

You should remove one broker per Availability Zone, if you want to reduce a cluster’s storage and compute. For example, you can remove two brokers from a two Availability Zone cluster, or three brokers from a three Availability Zone cluster in a single broker removal operation.

For information about how to rebalance partitions after you remove brokers from a cluster, see [Reassign partitions](bestpractices.md#bestpractices-balance-cluster).

You can remove brokers from all M5 and M7g based MSK provisioned clusters, regardless of the instance size.

Broker removal is supported on Kafka versions 2.8.1 and above, including on KRaft mode clusters.

**Topics**
+ [Remove broker partitions](#msk-remove-broker-partitions)
+ [Remove a broker with console](#msk-remove-broker-console)
+ [Remove a broker with CLI](#msk-remove-broker-cli)
+ [Remove a broker with API](#msk-remove-broker-api)

## Prepare to remove brokers by removing all partitions
<a name="msk-remove-broker-partitions"></a>

Before you start the broker removal process, first move all partitions, except ones for topics `__amazon_msk_canary` and `__amazon_msk_canary_state` from the brokers you plan to remove. These are internal topics that Amazon MSK creates for cluster health and diagnostic metrics.

You can use Kafka admin APIs or Cruise Control to move partitions to other brokers that you intend to retain in the cluster. See [Reassign partitions](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html#bestpractices-balance-cluster).

### Example process to remove partitions
<a name="msk-remove-broker-partitions-example"></a>

This section is an example of how to remove partitions from the broker you intend to remove. Assume you have a cluster with 6 brokers, 2 brokers in each AZ, and it has four topics:
+ `__amazon_msk_canary`
+ `__consumer_offsets`
+ `__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-c657f7e4ff32-2`
+ `msk-brk-rmv`

1. Create a client machine as described in [Create a client machine](https://docs.aws.amazon.com/msk/latest/developerguide/create-client-machine.html).

1. After configuring the client machine, run the following command to list all the available topics in your cluster.

   ```
   ./bin/kafka-topics.sh --bootstrap-server “CLUSTER_BOOTSTRAP_STRING” --list
   ```

   In this example, we see four topic names, `__amazon_msk_canary`, `__consumer_offsets`, `__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-c657f7e4ff32-2`, and `msk-brk-rmv`.

1. Create a json file called `topics.json` on the client machine and add all the user topic names as in the following code example. You don’t need to include the `__amazon_msk_canary` topic name as this is a service managed topic that will be automatically moved when necessary.

   ```
   {
   "topics": [
   {"topic": "msk-brk-rmv"},
   {"topic": "__consumer_offsets"},
   {"topic": "__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-c657f7e4ff32-2"}
   ],
   "version":1
   }
   ```

1. Run the following command to generate a proposal to move partitions to only 3 brokers out of 6 brokers on the cluster.

   ```
   ./bin/kafka-reassign-partitions.sh --bootstrap-server “CLUSTER_BOOTSTRAP_STRING” --topics-to-move-json-file topics.json --broker-list 1,2,3 --generate
   ```

1. Create a file called `reassignment-file.json` and copy the `proposed partition reassignment configuration` you got from above command.

1. Run the following command to move partitions that you specified in the `reassignment-file.json`.

   ```
   ./bin/kafka-reassign-partitions.sh --bootstrap-server “CLUSTER_BOOTSTRAP_STRING” --reassignment-json-file reassignment-file.json --execute
   ```

   The output looks similar to the following:

   ```
   Successfully started partition reassignments for morpheus-test-topic-1-0,test-topic-1-0
   ```

1. Run the following command to verify all partitions have moved.

   ```
   ./bin/kafka-reassign-partitions.sh --bootstrap-server “CLUSTER_BOOTSTRAP_STRING” --reassignment-json-file reassignment-file.json --verify
   ```

   The output looks similar to the following. Monitor the status until all partitions in your requested topics have been reassignmed successfully:

   ```
   Status of partition reassignment:
   Reassignment of partition msk-brk-rmv-0 is completed.
   Reassignment of partition msk-brk-rmv-1 is completed.
   Reassignment of partition __consumer_offsets-0 is completed.
   Reassignment of partition __consumer_offsets-1 is completed.
   ```

1. When the status indicates that the partition reassignment for each partition is completed, monitor the `UserPartitionExists` metrics for 5 minutes to ensure it displays `0` for the brokers from which you moved the partitions. After confirming this, you can proceed to remove the broker from the cluster.

## Remove a broker with the AWS Management Console
<a name="msk-remove-broker-console"></a>

**To remove brokers with the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. Choose the MSK cluster that contains brokers you want to remove.

1. On the cluster details page, choose the **Actions** button and select the **Edit number of brokers** option.

1. Enter the number of brokers that you want the cluster to have per Availability Zone. The console summarizes the number of brokers across availability zones that will be removed. Make sure this what you want.

1. Choose **Save changes**.

To prevent accidental broker removal, the console asks you to confirm that you want to delete brokers.

## Remove a broker with the AWS CLI
<a name="msk-remove-broker-cli"></a>

Run the following command, replacing `ClusterArn` with the Amazon Resource Name (ARN) that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, [Listing Amazon MSK clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-list-clusters.html). Replace `Current-Cluster-Version` with the current version of the cluster. 

**Important**  
Cluster versions aren't simple integers. To find the current version of the cluster, use the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) operation or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. An example version is `KTVPDKIKX0DER`.

The {{Target-Number-of-Brokers}} parameter represents the total number of broker nodes that you want the cluster to have when this operation completes successfully. The value you specify for {{Target-Number-of-Brokers}} must be a whole number that is less than the current number of brokers in the cluster. It must also be a multiple of the number of Availability Zones.

```
aws kafka update-broker-count --cluster-arn {{ClusterArn}} --current-version {{Current-Cluster-Version}} --target-number-of-broker-nodes {{Target-Number-of-Brokers}}
```

The output of this `update-broker-count` operation looks like the following JSON.

```
{
"ClusterOperationInfo": {
"ClientRequestId": "c0b7af47-8591-45b5-9c0c-909a1a2c99ea",
        "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
        "CreationTime": "2019-09-25T23:48:04.794Z",
        "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
        "OperationState": "UPDATE_COMPLETE",
        "OperationType": "DECREASE_BROKER_COUNT",
        "SourceClusterInfo": {
"NumberOfBrokerNodes": 12
        },
        "TargetClusterInfo": {
"NumberOfBrokerNodes": 9
        }
    }
}
```

In this output, `OperationType` is `DECREASE_BROKER_COUNT`. If `OperationState` has the value `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again.

## Remove a broker with the AWS API
<a name="msk-remove-broker-api"></a>

To remove brokers in a cluster using the API, see [UpdateBrokerCount](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-count.html#clusters-clusterarn-nodes-count-url) in the *Amazon Managed Streaming for Apache Kafka API Reference*.