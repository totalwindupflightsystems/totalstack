---
id: "@specs/aws/kafka/docs/iam-access-control-use-cases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Common use cases for client authorization policy"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Common use cases for client authorization policy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/iam-access-control-use-cases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Common use cases for client authorization policy
<a name="iam-access-control-use-cases"></a>

The first column in the following table shows some common use cases. To authorize a client to carry out a given use case, include the required actions for that use case in the client's authorization policy, and set `Effect` to `Allow`.

For information about all the actions that are part of IAM access control for Amazon MSK, see [Semantics of IAM authorization policy actions and resources](kafka-actions.md).

**Note**  
Actions are denied by default. You must explicitly allow every action that you want to authorize the client to perform.


****  

| Use case | Required actions | 
| --- | --- | 
| Admin | `kafka-cluster:*` | 
| Create a topic | `kafka-cluster:Connect`<br />`kafka-cluster:CreateTopic` | 
| Produce data | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic`<br />`kafka-cluster:WriteData` | 
| Consume data | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic`<br />`kafka-cluster:DescribeGroup`<br />`kafka-cluster:AlterGroup`<br />`kafka-cluster:ReadData` | 
| Produce data idempotently | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic`<br />`kafka-cluster:WriteData`<br />`kafka-cluster:WriteDataIdempotently` | 
| Produce data transactionally | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic`<br />`kafka-cluster:WriteData`<br />`kafka-cluster:DescribeTransactionalId`<br />`kafka-cluster:AlterTransactionalId` | 
| Describe the configuration of a cluster | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeClusterDynamicConfiguration` | 
| Update the configuration of a cluster | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeClusterDynamicConfiguration`<br />`kafka-cluster:AlterClusterDynamicConfiguration` | 
| Describe the configuration of a topic | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopicDynamicConfiguration` | 
| Update the configuration of a topic | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopicDynamicConfiguration`<br />`kafka-cluster:AlterTopicDynamicConfiguration` | 
| Alter a topic | `kafka-cluster:Connect`<br />`kafka-cluster:DescribeTopic`<br />`kafka-cluster:AlterTopic` | 