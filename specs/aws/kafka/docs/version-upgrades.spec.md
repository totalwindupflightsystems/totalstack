---
id: "@specs/aws/kafka/docs/version-upgrades"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Upgrade the Apache Kafka version"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Upgrade the Apache Kafka version

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/version-upgrades
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Upgrade the Apache Kafka version
<a name="version-upgrades"></a>

You can upgrade an existing MSK cluster to a newer version of Apache Kafka. Before upgrading your cluster's Kafka version, verify that your client-side software's version supports the features in the new Kafka version.

For information about how to make a cluster highly available during an upgrade, see [Build highly available clusters](bestpractices.md#ensure-high-availability).

**Upgrade the Apache Kafka version using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the navigation bar, choose the Region where you created the MSK cluster.

1. Choose the MSK cluster which you want to upgrade.

1. On the **Properties** tab, choose **Upgrade** in the **Apache Kafka version** section.

1. In the **Apache Kafka version** section, do the following:

   1. In the *Choose Apache Kafka version* dropdown list, choose the target version to which you want to upgrade. For example, choose **3.9.x**.

   1. (Optional) Choose **View version compatibility** to verify compatibility between your cluster's current version and the available upgrade versions. Then, select **Choose** to proceed.
**Note**  
Amazon MSK supports in-place upgrades to most Apache Kafka versions. However, when upgrading from a ZooKeeper-based Kafka version to a KRaft-based version, you must create a new cluster. Then, copy your data to the new cluster, and switch clients to the new cluster.

   1. (Optional) Choose the **Update cluster configuration** checkbox to apply configuration updates compatible with the new version. This enables the new version’s features and improvements.

      You can skip this step if you need to maintain your existing custom configurations.
**Note**  
Server-side upgrades don't automatically update client applications.
To maintain cluster stability, version downgrades aren't supported.

   1. Choose **Upgrade** to start the process.

**Upgrade the Apache Kafka version using the AWS CLI**

1. Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md).

   ```
   aws kafka get-compatible-kafka-versions --cluster-arn {{ClusterArn}}
   ```

   The output of this command includes a list of the Apache Kafka versions to which you can upgrade the cluster. It looks like the following example.

   ```
   {
       "CompatibleKafkaVersions": [
           {
               "SourceVersion": "2.2.1",
               "TargetVersions": [
                   "2.3.1",
                   "2.4.1",
                   "2.4.1.1",
                   "2.5.1"
               ]
           }
       ]
   }
   ```

1. Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md).

   Replace {{Current-Cluster-Version}} with the current version of the cluster. For {{TargetVersion}} you can specify any of the target versions from the output of the previous command.
**Important**  
Cluster versions aren't simple integers. To find the current version of the cluster, use the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) operation or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. An example version is `KTVPDKIKX0DER`.

   ```
   aws kafka update-cluster-kafka-version --cluster-arn {{ClusterArn}} --current-version {{Current-Cluster-Version}} --target-kafka-version {{TargetVersion}}
   ```

   The output of the previous command looks like the following JSON.

   ```
   {
       
       "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
       "ClusterOperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef"
   }
   ```

1. To get the result of the `update-cluster-kafka-version` operation, run the following command, replacing {{ClusterOperationArn}} with the ARN that you obtained in the output of the `update-cluster-kafka-version` command.

   ```
   aws kafka describe-cluster-operation --cluster-operation-arn {{ClusterOperationArn}}
   ```

   The output of this `describe-cluster-operation` command looks like the following JSON example.

   ```
   {
       "ClusterOperationInfo": {
           "ClientRequestId": "62cd41d2-1206-4ebf-85a8-dbb2ba0fe259",
           "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
           "CreationTime": "2021-03-11T20:34:59.648000+00:00",
           "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
           "OperationState": "UPDATE_IN_PROGRESS",
           "OperationSteps": [
               {
                   "StepInfo": {
                       "StepStatus": "IN_PROGRESS"
                   },
                   "StepName": "INITIALIZE_UPDATE"
               },
               {
                   "StepInfo": {
                       "StepStatus": "PENDING"
                   },
                   "StepName": "UPDATE_APACHE_KAFKA_BINARIES"
               },
               {
                   "StepInfo": {
                       "StepStatus": "PENDING"
                   },
                   "StepName": "FINALIZE_UPDATE"
               }
           ],
           "OperationType": "UPDATE_CLUSTER_KAFKA_VERSION",
           "SourceClusterInfo": {
               "KafkaVersion": "2.4.1"
           },
           "TargetClusterInfo": {
               "KafkaVersion": "2.6.1"
           }
       }
   }
   ```

   If `OperationState` has the value `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again. When the operation is complete, the value of `OperationState` becomes `UPDATE_COMPLETE`. Because the time required for Amazon MSK to complete the operation varies, you might need to check repeatedly until the operation is complete. 

**Upgrade the Apache Kafka version using the API**

1. Invoke the [GetCompatibleKafkaVersions](https://docs.aws.amazon.com//msk/1.0/apireference/compatible-kafka-versions.html#GetCompatibleKafkaVersions) operation to get a list of the Apache Kafka versions to which you can upgrade the cluster.

1. Invoke the [UpdateClusterKafkaVersion](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-version.html#UpdateClusterKafkaVersion) operation to upgrade the cluster to one of the compatible Apache Kafka versions.