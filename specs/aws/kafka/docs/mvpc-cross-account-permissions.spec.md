---
id: "@specs/aws/kafka/docs/mvpc-cross-account-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Multi-VPC private connectivity permissions"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Multi-VPC private connectivity permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mvpc-cross-account-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Permissions for multi-VPC private connectivity
<a name="mvpc-cross-account-permissions"></a>

This section summarizes the permissions needed for clients and clusters using the multi-VPC private connectivity feature. Multi-VPC private connectivity requires the client admin to create permissions on each client that will have a managed VPC connection to the MSK cluster. It also requires the MSK cluster admin to enable PrivateLink connectivity on the MSK cluster and select authentication schemes to control access to the cluster. 

**Cluster auth type and topic access permissions**  
Turn on the multi-VPC private connectivity feature for auth schemes that are enabled for your MSK cluster. See [Requirements and limitations for multi-VPC private connectivity](aws-access-mult-vpc.md#mvpc-requirements). If you are configuring your MSK cluster to use SASL/SCRAM auth scheme, the Apache Kafka ACLs property `allow.everyone.if.no.acl.found=false` is mandatory. After you set the [Apache Kafka ACLs](msk-acls.md) for your cluster, update the cluster's configuration to have the property `allow.everyone.if.no.acl.found` set to false for the cluster. For information about how to update the configuration of a cluster, see [Broker configuration operations](msk-configuration-operations.md).

**Cross-account cluster policy permissions**  
If a Kafka client is in an AWS account that is different than the MSK cluster, attach a cluster-based policy to the MSK cluster that authorizes the client root user for cross-account connectivity. You can edit the multi-VPC cluster policy using the IAM policy editor in the MSK console (cluster **Security settings** > **Edit cluster policy**), or use the following APIs to manage the cluster policy:

**PutClusterPolicy**  
Attaches the cluster policy to the cluster. You can use this API to create or update the specified MSK cluster policy. If you’re updating the policy, the currentVersion field is required in the request payload.

**GetClusterPolicy**  
Retrieves the JSON text of the cluster policy document attached to the cluster.

**DeleteClusterPolicy**  
Deletes the cluster policy.

The following is an example of the JSON for a basic cluster policy, similar to the one shown in the MSK console IAM policy editor. The following policy grants permissions for cluster, topic, and group-level access.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "123456789012"
            ]
        },
        "Action": [
            "kafka-cluster:*",
            "kafka:CreateVpcConnection",
            "kafka:GetBootstrapBrokers",
            "kafka:DescribeCluster",
            "kafka:DescribeClusterV2"
        ],
        "Resource": [
            "arn:aws:kafka:us-east-1:123456789012:cluster/testing/de8982fa-8222-4e87-8b20-9bf3cdfa1521-2",
            "arn:aws:kafka:us-east-1:123456789012:topic/testing/*",
            "arn:aws:kafka:us-east-1:123456789012:group/testing/*"
        ]
    }]
}
```

------

**Client permissions for multi-VPC private connectivity to an MSK cluster**  
To set up multi-VPC private connectivity between a Kafka client and an MSK cluster, the client requires an attached identity policy that grants permissions for `kafka:CreateVpcConnection`, `ec2:CreateTags` and `ec2:CreateVPCEndpoint` actions on the client. For reference, the following is an example of the JSON for a basic client identity policy.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kafka:CreateVpcConnection",
        "ec2:CreateTags",
        "ec2:CreateVPCEndpoint"
      ],
      "Resource": "*"
    }
  ]
}
```

------