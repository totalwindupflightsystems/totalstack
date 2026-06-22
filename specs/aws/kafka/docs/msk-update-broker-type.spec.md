---
id: "@specs/aws/kafka/docs/msk-update-broker-type"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update cluster broker size"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update cluster broker size

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-update-broker-type
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update the Amazon MSK cluster broker size
<a name="msk-update-broker-type"></a>

You can scale your MSK cluster on demand by changing the size of your brokers without reassigning Apache Kafka partitions. Changing the size of your brokers gives you the flexibility to adjust your MSK cluster's compute capacity based on changes in your workloads, without interrupting your cluster I/O. Amazon MSK uses the same broker size for all the brokers in a given cluster.

For Standard brokers, you can update your cluster broker size from M5 or T3 to M7g, T3 to M5, or from M7g to M5.

**Note**  
You can't migrate from a larger broker size to a smaller broker size. For example, M7g.large to T3.small.

For Express brokers, you can use only M7g broker sizes.

This topic describes how to update the broker size for your MSK cluster.

Be aware that migrating to a smaller broker size can decrease performance and reduce maxiumum achievable throughput per broker. Migrating to a larger broker size can increase performance but might cost more.

The broker-size update happens in a rolling fashion while the cluster is up and running. This means that Amazon MSK takes down one broker at a time to perform the broker-size update. For information about how to make a cluster highly available during a broker-size update, see [Build highly available clusters](bestpractices.md#ensure-high-availability). To further reduce any potential impact on productivity, you can perform the broker-size update during a period of low traffic.

During a broker-size update, you can continue to produce and consume data. However, you must wait until the update is done before you can reboot brokers or invoke any of the update operations listed under [Amazon MSK operations](https://docs.aws.amazon.com/msk/1.0/apireference/operations.html).

If you want to update your cluster to a smaller broker size, we recommend that you try the update on a test cluster first to see how it affects your scenario. 

**Important**  
You can't update a cluster to a smaller broker size if the number of partitions per broker exceeds the maximum number specified in [Right-size your cluster: Number of partitions per Standard broker](bestpractices.md#partitions-per-broker).

**Topics**
+ [Update the Amazon MSK cluster broker size using the AWS Management Console](#update-broker-type-console)
+ [Update the Amazon MSK cluster broker size using the AWS CLI](#update-broker-type-cli)
+ [Updating the broker size using the API](#update-broker-type-api)

## Update the Amazon MSK cluster broker size using the AWS Management Console
<a name="update-broker-type-console"></a>

This process shows how to update the Amazon MSK cluster broker size using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK cluster for which you want to update the broker size.

1. On the details page for the cluster, find the **Brokers summary** section, and choose **Edit broker size**.

1. Choose the broker size you want from the list.

1. Save changes.

## Update the Amazon MSK cluster broker size using the AWS CLI
<a name="update-broker-type-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md). 

1. Replace {{Current-Cluster-Version}} with the current version of the cluster and {{TargetType}} with the new size that you want the brokers to be. To learn more about broker sizes, see [Amazon MSK broker types](broker-instance-types.md).

   ```
   aws kafka update-broker-type --cluster-arn {{ClusterArn}} --current-version {{Current-Cluster-Version}} --target-instance-type {{TargetType}}
   ```

   The following is an example of how to use this command:

   ```
   aws kafka update-broker-type --cluster-arn "arn:aws:kafka:us-east-1:0123456789012:cluster/exampleName/abcd1234-0123-abcd-5678-1234abcd-1" --current-version "K1X5R6FKA87" --target-instance-type kafka.m5.large 
   ```

   The output of this command looks like the following JSON example.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:0123456789012:cluster/exampleName/abcd1234-0123-abcd-5678-1234abcd-1",
       "ClusterOperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef"
   }
   ```

1. To get the result of the `update-broker-type` operation, run the following command, replacing {{ClusterOperationArn}} with the ARN that you obtained in the output of the `update-broker-type` command.

   ```
   aws kafka describe-cluster-operation --cluster-operation-arn {{ClusterOperationArn}}
   ```

   The output of this `describe-cluster-operation` command looks like the following JSON example.

   ```
   {
     "ClusterOperationInfo": {
       "ClientRequestId": "982168a3-939f-11e9-8a62-538df00285db",
       "ClusterArn": "arn:aws:kafka:us-east-1:0123456789012:cluster/exampleName/abcd1234-0123-abcd-5678-1234abcd-1",
       "CreationTime": "2021-01-09T02:24:22.198000+00:00",
       "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
       "OperationState": "UPDATE_COMPLETE",
       "OperationType": "UPDATE_BROKER_TYPE",
       "SourceClusterInfo": {
         "InstanceType": "t3.small"
       },
       "TargetClusterInfo": {
         "InstanceType": "m5.large"
       }
     }
   }
   ```

   If `OperationState` has the value `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again. 

## Updating the broker size using the API
<a name="update-broker-type-api"></a>

To update the broker size using the API, see [UpdateBrokerType](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-type.html#UpdateBrokerType).

You can use `UpdateBrokerType` to update your cluster broker size from M5 or T3 to M7g, or from M7g to M5.