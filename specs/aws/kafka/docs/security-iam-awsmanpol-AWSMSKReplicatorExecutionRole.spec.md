---
id: "@specs/aws/kafka/docs/security-iam-awsmanpol-AWSMSKReplicatorExecutionRole"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Managed policy AWSMSKReplicatorExecutionRole"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Managed policy AWSMSKReplicatorExecutionRole

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security-iam-awsmanpol-AWSMSKReplicatorExecutionRole
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policy: AWSMSKReplicatorExecutionRole
<a name="security-iam-awsmanpol-AWSMSKReplicatorExecutionRole"></a>

The `AWSMSKReplicatorExecutionRole` policy grants permissions to the Amazon MSK replicator to replicate data between MSK clusters. The permissions in this policy are grouped as follows:
+ **`cluster`** – Grants the Amazon MSK Replicator permissions to connect to the cluster using IAM authentication. Also grants permissions to describe and alter the cluster.
+ **`topic`** – Grants the Amazon MSK Replicator permissions to describe, create, and alter a topic, and to alter the topic's dynamic configuration.
+ **`consumer group`** – Grants the Amazon MSK Replicator permissions to describe and alter consumer groups, to read and write date from an MSK cluster, and to delete internal topics created by the replicator.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "ClusterPermissions",
			"Effect": "Allow",
			"Action": [
				"kafka-cluster:Connect",
				"kafka-cluster:DescribeCluster",
				"kafka-cluster:AlterCluster",
				"kafka-cluster:DescribeTopic",
				"kafka-cluster:CreateTopic",
				"kafka-cluster:AlterTopic",
				"kafka-cluster:WriteData",
				"kafka-cluster:ReadData",
				"kafka-cluster:AlterGroup",
				"kafka-cluster:DescribeGroup",
				"kafka-cluster:DescribeTopicDynamicConfiguration",
				"kafka-cluster:AlterTopicDynamicConfiguration",
				"kafka-cluster:WriteDataIdempotently"
			],
			"Resource": [
				"arn:aws:kafka:*:*:cluster/*"
			]
		},
		{
			"Sid": "TopicPermissions",
			"Effect": "Allow",
			"Action": [
				"kafka-cluster:DescribeTopic",
				"kafka-cluster:CreateTopic",
				"kafka-cluster:AlterTopic",
				"kafka-cluster:WriteData",
				"kafka-cluster:ReadData",
				"kafka-cluster:DescribeTopicDynamicConfiguration",
				"kafka-cluster:AlterTopicDynamicConfiguration",
				"kafka-cluster:AlterCluster"
			],
			"Resource": [
				"arn:aws:kafka:*:*:topic/*/*"
			]
		},
		{
			"Sid": "GroupPermissions",
			"Effect": "Allow",
			"Action": [
				"kafka-cluster:AlterGroup",
				"kafka-cluster:DescribeGroup"
			],
			"Resource": [
				"arn:aws:kafka:*:*:group/*/*"
			]
		}
	]
}
```

------