---
id: "@specs/aws/kafka/docs/msk-update-cluster-config"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update cluster configuration"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update cluster configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-update-cluster-config
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update the configuration of an Amazon MSK cluster
<a name="msk-update-cluster-config"></a>

To update the configuration of a cluster, make sure that the cluster is in the `ACTIVE` state. You must also ensure that the number of partitions per broker on your MSK cluster is under the limits described in [Right-size your cluster: Number of partitions per Standard broker](bestpractices.md#partitions-per-broker). You can't update the configuration of a cluster that exceeds these limits.

For information about MSK configuration, including how to create a custom configuration, which properties you can update, and what happens when you update the configuration of an existing cluster, see [Amazon MSK Provisioned configuration](msk-configuration.md).

**Topics**
+ [Broker availability during configuration updates](#update-config-cluster-availability)
+ [Updating the configuration of a cluster using the AWS CLI](#update-config-cli)
+ [Update the configuration of a Amazon MSK cluster using the API](#update-config-api)

## Broker availability during configuration updates
<a name="update-config-cluster-availability"></a>

Amazon MSK maintains high availability during most cluster configuration updates. Amazon MSK performs a rolling update where it updates one broker at a time. During this process, the cluster remains available, though individual brokers will restart as their configurations are updated. However, some configuration changes might require all brokers to be updated simultaneously, which can cause a brief cluster-wide outage. For more information about broker availability impact during updates, see [Amazon MSK Provisioned configuration](msk-configuration.md).

Before updating production clusters, we recommend that you test your configuration changes in a non-production environment and schedule updates during your maintenance windows.

If you face any issues while upgrading your MSK cluster, see [How do I troubleshoot issues when I upgrade my Amazon MSK cluster?](https://repost.aws/knowledge-center/msk-upgrade-cluster-issues)

## Updating the configuration of a cluster using the AWS CLI
<a name="update-config-cli"></a>

1. Copy the following JSON and save it to a file. Name the file `configuration-info.json`. Replace {{ConfigurationArn}} with the Amazon Resource Name (ARN) of the configuration that you want to use to update the cluster. The ARN string must be in quotes in the following JSON. 

   Replace {{Configuration-Revision}} with the revision of the configuration that you want to use. Configuration revisions are integers (whole numbers) that start at `1`. This integer mustn't be in quotes in the following JSON.

   ```
   {
        "Arn": {{ConfigurationArn}},
        "Revision": {{Configuration-Revision}}
   }
   ```

    

1. Run the following command, replacing {{ClusterArn}} with the ARN that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md). 

   Replace {{Path-to-Config-Info-File}} with the path to your configuration info file. If you named the file that you created in the previous step `configuration-info.json` and saved it in the current directory, then {{Path-to-Config-Info-File}} is `configuration-info.json`.

   Replace {{Current-Cluster-Version}} with the current version of the cluster. 
**Important**  
Cluster versions aren't simple integers. To find the current version of the cluster, use the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) operation or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. An example version is `KTVPDKIKX0DER`.

   ```
   aws kafka update-cluster-configuration --cluster-arn {{ClusterArn}} --configuration-info file://{{Path-to-Config-Info-File}} --current-version {{Current-Cluster-Version}}
   ```

   The following is an example of how to use this command:

   ```
   aws kafka update-cluster-configuration --cluster-arn "arn:aws:kafka:us-east-1:0123456789012:cluster/exampleName/abcd1234-0123-abcd-5678-1234abcd-1" --configuration-info file://c:\users\tester\msk\configuration-info.json --current-version "K1X5R6FKA87"
   ```

   The output of this `update-cluster-configuration` command looks like the following JSON example.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
       "ClusterOperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef"
   }
   ```

1. To get the result of the `update-cluster-configuration` operation, run the following command, replacing {{ClusterOperationArn}} with the ARN that you obtained in the output of the `update-cluster-configuration` command.

   ```
   aws kafka describe-cluster-operation --cluster-operation-arn {{ClusterOperationArn}}
   ```

   The output of this `describe-cluster-operation` command looks like the following JSON example.

   ```
   {
       "ClusterOperationInfo": {
           "ClientRequestId": "982168a3-939f-11e9-8a62-538df00285db",
           "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
           "CreationTime": "2019-06-20T21:08:57.735Z",
           "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
           "OperationState": "UPDATE_COMPLETE",
           "OperationType": "UPDATE_CLUSTER_CONFIGURATION",
           "SourceClusterInfo": {},
           "TargetClusterInfo": {
               "ConfigurationInfo": {
                   "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/ExampleConfigurationName/abcdabcd-abcd-1234-abcd-abcd123e8e8e-1",
                   "Revision": 1
               }
           }
       }
   }
   ```

   In this output, `OperationType` is `UPDATE_CLUSTER_CONFIGURATION`. If `OperationState` has the value `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again. 

## Update the configuration of a Amazon MSK cluster using the API
<a name="update-config-api"></a>

To use the API to update the configuration of a Amazon MSK cluster, see [UpdateClusterConfiguration](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-configuration.html#UpdateClusterConfiguration).