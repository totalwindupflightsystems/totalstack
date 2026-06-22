---
id: "@specs/aws/kafka/docs/public-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Turn on public access"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Turn on public access

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/public-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Turn on public access to an MSK Provisioned cluster
<a name="public-access"></a>

Amazon MSK gives you the option to turn on public access to the brokers of MSK Provisioned clusters running Apache Kafka 2.6.0 or later versions. For security reasons, you can't turn on public access while creating an MSK cluster. However, you can update an existing cluster to make it publicly accessible. You can also create a new cluster and then update it to make it publicly accessible.

You can turn on public access to an MSK cluster at no additional cost, but standard AWS data transfer costs apply for data transfer in and out of the cluster. For information about pricing, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/).

 Amazon MSK Provisioned clusters with dual-stack network type support both IPv4 and IPv6 connectivity for public access. When public access is enabled on your cluster, the same IPv6 bootstrap strings will automatically work for both default and public access connectivity. Your existing IPv4 bootstrap strings will continue to work for IPv4 connectivity. Note that if public access is not enabled on your cluster, the IPv6 bootstrap strings will not have public access capability. For more information, see Configure dual-stack network type for an Amazon MSK cluster. 

**Note**  
If you're using the SASL/SCRAM, or mTLS access-control methods, you must first set Apache Kafka ACLs for your cluster. Then, update the cluster's configuration to set the `allow.everyone.if.no.acl.found` property to false. For information about how to update the configuration of a cluster, see [Broker configuration operations](msk-configuration-operations.md).

To turn on public access to an MSK Provisioned cluster, make sure that the cluster meets all of the following conditions:
+ The subnets that are associated with the cluster must be public. Each public subnet has a public IPv4 address associated with it and public IPv4 addresses are priced as shown in [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/). This means that the subnets must have an associated route table with an internet gateway attached. For information about how to create and attach an internet gateway, see [Enable VPC internet access using internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.
+ Unauthenticated access control must be off and at least one of the following access-control methods must be on: SASL/IAM, SASL/SCRAM, mTLS. For information about how to update the access-control method of a cluster, see [Update security settings of a Amazon MSK cluster](msk-update-security.md).
+ Encryption within the cluster must be turned on. The on setting is the default when creating a cluster. It's not possible to turn on encryption within the cluster for a cluster that was created with it turned off. It is therefore not possible to turn on public access for a cluster that was created with encryption within the cluster turned off.
+ Plaintext traffic between brokers and clients must be off. For information about how to turn it off if it's on, see [Update security settings of a Amazon MSK cluster](msk-update-security.md).
+ If you're using IAM access control and want to apply authorization policies or update your authorization policies, see [IAM access control](iam-access-control.md). For information about Apache Kafka ACLs, see [Apache Kafka ACLs](msk-acls.md).

After you ensure that an MSK cluster meets the conditions listed above, you can use the AWS Management Console, the AWS CLI, or the Amazon MSK API to turn on public access. After you turn on public access to a cluster, you can get a public bootstrap-brokers string for it. For information about getting the bootstrap brokers for a cluster, see [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).

**Important**  
In addition to turning on public access, ensure that the cluster's security groups have inbound TCP rules that allow public access from your IP address. We recommend that you make these rules as restrictive as possible. For information about security groups and inbound rules, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the Amazon VPC User Guide. For port numbers, see [Port information](port-info.md). For instructions on how to change a cluster's security group, see [Changing an Amazon MSK cluster's security group](change-security-group.md).

**Note**  
If you use the following instructions to turn on public access and then still cannot access the cluster, see [Unable to access cluster that has public access turned on](troubleshooting.md#public-access-issues).

**Turning on public access using the console**

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the list of clusters, choose the cluster to which you want to turn on public access.

1. Choose the **Properties** tab, then find the **Network settings** section.

1. Choose **Edit public access**.

**Turning on public access using the AWS CLI**

1. Run the following AWS CLI command, replacing {{ClusterArn}} and {{Current-Cluster-Version}} with the ARN and current version of the cluster. To find the current version of the cluster, use the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) operation or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. An example version is `KTVPDKIKX0DER`.

   ```
   aws kafka update-connectivity --cluster-arn {{ClusterArn}} --current-version {{Current-Cluster-Version}} --connectivity-info '{"PublicAccess": {"Type": "SERVICE_PROVIDED_EIPS"}}'
   ```

   The output of this `update-connectivity` command looks like the following JSON example.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
       "ClusterOperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef"
   }
   ```
**Note**  
To turn off public access, use a similar AWS CLI command, but with the following connectivity info instead:  

   ```
   '{"PublicAccess": {"Type": "DISABLED"}}'
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
           "CreationTime": "2019-06-20T21:08:57.735Z",
           "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
           "OperationState": "UPDATE_COMPLETE",
           "OperationType": "UPDATE_CONNECTIVITY",
           "SourceClusterInfo": {
               "ConnectivityInfo": {
                   "PublicAccess": {
                       "Type": "DISABLED"
                   }
               }
           },
           "TargetClusterInfo": {
               "ConnectivityInfo": {
                   "PublicAccess": {
                       "Type": "SERVICE_PROVIDED_EIPS"
                   }
               }
           }
       }
   }
   ```

   If `OperationState` has the value `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again.

**Turning on public access using the Amazon MSK API**
+ To use the API to turn public access to a cluster on or off, see [UpdateConnectivity](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-connectivity.html#UpdateConnectivity).

**Note**  
For security reasons, Amazon MSK doesn't allow public access to Apache ZooKeeper or KRaft controller nodes.