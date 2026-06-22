---
id: "@specs/aws/kafka/docs/kafka-actions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Semantics of IAM authorization policy actions and resources"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Semantics of IAM authorization policy actions and resources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/kafka-actions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Semantics of IAM authorization policy actions and resources
<a name="kafka-actions"></a>

**Note**  
For clusters running Apache Kafka version 3.8 or later, IAM access control supports the WriteTxnMarkers API for terminating transactions. For clusters running Kafka versions earlier than 3.8, IAM access control doesn't support internal cluster actions including WriteTxnMarkers. For these earlier versions, to terminate transactions, use SCRAM or mTLS authentication with appropriate ACLs instead of IAM authentication.

This section explains the semantics of the action and resource elements that you can use in an IAM authorization policy. For an example policy, see [Create authorization policies for the IAM role](create-iam-access-control-policies.md).

## Authorization policy actions
<a name="actions"></a>

The following table lists the actions that you can include in an authorization policy when you use IAM access control for Amazon MSK. When you include in your authorization policy an action from the *Action* column of the table, you must also include the corresponding actions from the *Required actions* column. 


| Action | Description | Required actions | Required resources | Applicable to serverless clusters | 
| --- | --- | --- | --- | --- | 
| kafka-cluster:Connect | Grants permission to connect and authenticate to the cluster. | None | cluster | Yes | 
| kafka-cluster:DescribeCluster | Grants permission to describe various aspects of the cluster, equivalent to Apache Kafka's DESCRIBE CLUSTER ACL. | `kafka-cluster:Connect` | cluster | Yes | 
| kafka-cluster:AlterCluster | Grants permission to alter various aspects of the cluster, equivalent to Apache Kafka's ALTER CLUSTER ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeCluster` | cluster | No | 
| kafka-cluster:DescribeClusterDynamicConfiguration | Grants permission to describe the dynamic configuration of a cluster, equivalent to Apache Kafka's DESCRIBE\_CONFIGS CLUSTER ACL. | `kafka-cluster:Connect` | cluster | No | 
| kafka-cluster:AlterClusterDynamicConfiguration | Grants permission to alter the dynamic configuration of a cluster, equivalent to Apache Kafka's ALTER\_CONFIGS CLUSTER ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeClusterDynamicConfiguration` | cluster | No | 
| kafka-cluster:WriteDataIdempotently | Grants permission to write data idempotently on a cluster, equivalent to Apache Kafka's IDEMPOTENT\_WRITE CLUSTER ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:WriteData` | cluster | Yes | 
| kafka-cluster:CreateTopic | Grants permission to create topics on a cluster, equivalent to Apache Kafka's CREATE CLUSTER/TOPIC ACL. | `kafka-cluster:Connect` | topic | Yes | 
| kafka-cluster:DescribeTopic | Grants permission to describe topics on a cluster, equivalent to Apache Kafka's DESCRIBE TOPIC ACL. | `kafka-cluster:Connect` | topic | Yes | 
| kafka-cluster:AlterTopic | Grants permission to alter topics on a cluster, equivalent to Apache Kafka's ALTER TOPIC ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic` | topic | Yes | 
| kafka-cluster:DeleteTopic | Grants permission to delete topics on a cluster, equivalent to Apache Kafka's DELETE TOPIC ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic` | topic | Yes | 
| kafka-cluster:DescribeTopicDynamicConfiguration | Grants permission to describe the dynamic configuration of topics on a cluster, equivalent to Apache Kafka's DESCRIBE\_CONFIGS TOPIC ACL. | `kafka-cluster:Connect` | topic | Yes | 
| kafka-cluster:AlterTopicDynamicConfiguration | Grants permission to alter the dynamic configuration of topics on a cluster, equivalent to Apache Kafka's ALTER\_CONFIGS TOPIC ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopicDynamicConfiguration` | topic | Yes | 
| kafka-cluster:ReadData | Grants permission to read data from topics on a cluster, equivalent to Apache Kafka's READ TOPIC ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic`<br />`kafka-cluster:AlterGroup` | topic | Yes | 
| kafka-cluster:WriteData | Grants permission to write data to topics on a cluster, equivalent to Apache Kafka's WRITE TOPIC ACL | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic` | topic | Yes | 
| kafka-cluster:DescribeGroup | Grants permission to describe groups on a cluster, equivalent to Apache Kafka's DESCRIBE GROUP ACL. | `kafka-cluster:Connect` | group | Yes | 
| kafka-cluster:AlterGroup | Grants permission to join groups on a cluster, equivalent to Apache Kafka's READ GROUP ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeGroup` | group | Yes | 
| kafka-cluster:DeleteGroup | Grants permission to delete groups on a cluster, equivalent to Apache Kafka's DELETE GROUP ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeGroup` | group | Yes | 
| kafka-cluster:DescribeTransactionalId | Grants permission to describe transactional IDs on a cluster, equivalent to Apache Kafka's DESCRIBE TRANSACTIONAL\_ID ACL. | `kafka-cluster:Connect` | transactional-id | Yes | 
| kafka-cluster:AlterTransactionalId | Grants permission to alter transactional IDs on a cluster, equivalent to Apache Kafka's WRITE TRANSACTIONAL\_ID ACL. | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTransactionalId`<br />`kafka-cluster:WriteData` | transactional-id | Yes | 

You can use the asterisk (\*) wildcard any number of times in an action after the colon. The following are examples.
+ `kafka-cluster:*Topic` stands for `kafka-cluster:CreateTopic`, `kafka-cluster:DescribeTopic`, `kafka-cluster:AlterTopic`, and `kafka-cluster:DeleteTopic`. It doesn't include `kafka-cluster:DescribeTopicDynamicConfiguration` or `kafka-cluster:AlterTopicDynamicConfiguration`.
+ `kafka-cluster:*` stands for all permissions.

## Authorization policy resources
<a name="msk-iam-resources"></a>

The following table shows the four types of resources that you can use in an authorization policy when you use IAM access control for Amazon MSK. You can get the cluster Amazon Resource Name (ARN) from the AWS Management Console or by using the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) API or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. You can then use the cluster ARN to construct topic, group, and transactional ID ARNs. To specify a resource in an authorization policy, use that resource's ARN.


| Resource | ARN format | 
| --- | --- | 
| Cluster | arn:aws:kafka:{{region}}:{{account-id}}:cluster/{{cluster-name}}/{{cluster-uuid}} | 
| Topic | arn:aws:kafka:{{region}}:{{account-id}}:topic/{{cluster-name}}/{{cluster-uuid}}/{{topic-name}} | 
| Group | arn:aws:kafka:{{region}}:{{account-id}}:group/{{cluster-name}}/{{cluster-uuid}}/{{group-name}} | 
| Transactional ID | arn:aws:kafka:{{region}}:{{account-id}}:transactional-id/{{cluster-name}}/{{cluster-uuid}}/{{transactional-id}} | 

You can use the asterisk (\*) wildcard any number of times anywhere in the part of the ARN that comes after `:cluster/`, `:topic/`, `:group/`, and `:transactional-id/`. The following are some examples of how you can use the asterisk (\*) wildcard to refer to multiple resources:
+ `arn:aws:kafka:us-east-1:0123456789012:topic/MyTestCluster/*`: all the topics in any cluster named MyTestCluster, regardless of the cluster's UUID.
+ `arn:aws:kafka:us-east-1:0123456789012:topic/MyTestCluster/abcd1234-0123-abcd-5678-1234abcd-1/*_test`: all topics whose name ends with "\_test" in the cluster whose name is MyTestCluster and whose UUID is abcd1234-0123-abcd-5678-1234abcd-1.
+ `arn:aws:kafka:us-east-1:0123456789012:transactional-id/MyTestCluster/*/5555abcd-1111-abcd-1234-abcd1234-1`: all transactions whose transactional ID is 5555abcd-1111-abcd-1234-abcd1234-1, across all incarnations of a cluster named MyTestCluster in your account. This means that if you create a cluster named MyTestCluster, then delete it, and then create another cluster by the same name, you can use this resource ARN to represent the same transactions ID on both clusters. However, the deleted cluster isn't accessible.