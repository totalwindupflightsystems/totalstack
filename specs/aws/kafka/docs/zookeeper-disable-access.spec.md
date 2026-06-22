---
id: "@specs/aws/kafka/docs/zookeeper-disable-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Disable or enable ZooKeeper access"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Disable or enable ZooKeeper access

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/zookeeper-disable-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Disable or enable direct Apache ZooKeeper client access
<a name="zookeeper-disable-access"></a>

You can disable direct Apache ZooKeeper client access on your Amazon MSK Provisioned cluster to verify that your applications do not rely on direct ZooKeeper connections. When ZooKeeper access is disabled, clients can no longer connect to the Apache ZooKeeper nodes on ports 2181 (plaintext) and 2182 (TLS). You can re-enable ZooKeeper access at any time.

**Note**  
This feature is only available for Amazon MSK Provisioned clusters that use ZooKeeper metadata mode with Standard brokers. It is not available for the following cluster types:  
Clusters running in KRaft metadata mode
Clusters using Express brokers. ZooKeeper access is managed automatically in Express clusters and cannot be configured manually.
Amazon MSK Serverless clusters

**Disabling ZooKeeper access using the console**

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the list of clusters, choose the cluster on which you want to disable ZooKeeper access.

1. Choose the **Properties** tab, then find the **Network settings** section.

1. Choose **Disable ZooKeeper access**.

**Disabling ZooKeeper access using the AWS CLI**

1. Run the following AWS CLI command, replacing {{ClusterArn}} and {{Current-Cluster-Version}} with the ARN and current version of the cluster. To find the current version of the cluster, use the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) operation or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. An example version is `KTVPDKIKX0DER`.

   ```
   aws kafka update-connectivity --cluster-arn {{ClusterArn}} --current-version {{Current-Cluster-Version}} --zookeeper-access '{"Enabled": false}'
   ```

   The output of this `update-connectivity` command looks like the following JSON example.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
       "ClusterOperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef"
   }
   ```
**Note**  
To re-enable ZooKeeper access, use a similar AWS CLI command with the following value for `--zookeeper-access` instead:  

   ```
   '{"Enabled": true}'
   ```

1. To get the result of the `update-connectivity` operation, run the following command, replacing {{ClusterOperationArn}} with the ARN that you obtained in the output of the `update-connectivity` command.

   ```
   aws kafka describe-cluster-operation --cluster-operation-arn {{ClusterOperationArn}}
   ```

   The output of this `describe-cluster-operation` command looks like the following JSON example.

   ```
   {
       "ClusterOperationInfo": {
           "ClientRequestId": "982168a3-939f-11e9-8a62-538df00285db",
           "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
           "CreationTime": "2026-01-15T21:08:57.735Z",
           "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
           "OperationState": "UPDATE_COMPLETE",
           "OperationType": "UPDATE_CONNECTIVITY",
           "SourceClusterInfo": {
               "ZookeeperAccess": {
                   "Enabled": true
               }
           },
           "TargetClusterInfo": {
               "ZookeeperAccess": {
                   "Enabled": false
               }
           }
       }
   }
   ```

   If `OperationState` has the value `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again.

**Disabling ZooKeeper access using the Amazon MSK API**
+ To use the API to disable or enable ZooKeeper access on a cluster, see [UpdateConnectivity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html).