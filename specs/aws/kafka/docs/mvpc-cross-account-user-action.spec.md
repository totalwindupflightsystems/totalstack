---
id: "@specs/aws/kafka/docs/mvpc-cross-account-user-action"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cross-account user configures VPC connections"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Cross-account user configures VPC connections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mvpc-cross-account-user-action
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 3: Cross-account user actions to configure client-managed VPC connections
<a name="mvpc-cross-account-user-action"></a>

To set up multi-VPC private connectivity between a client in a different account from the MSK cluster, the cross-account user creates a managed VPC connection for the client. Multiple clients can be connected to the MSK cluster by repeating this procedure. For the purposes of this use case, you’ll configure just one client.

Clients can use the supported auth schemes IAM, SASL/SCRAM, or TLS. Each managed VPC connection can have only one auth scheme associated with it. The client auth scheme must be configured on the MSK cluster where the client will connect.

 For this use case, configure the client auth scheme so that the client in Account B uses the IAM auth scheme.

**Prerequisites**

This process requires the following items:
+ The previously created cluster policy that grants the client in Account B permission to perform actions on the MSK cluster in Account A.
+ An identity policy attached to the client in Account B that grants permissions for `kafka:CreateVpcConnection`, `ec2:CreateTags`, `ec2:CreateVPCEndpoint` and `ec2:DescribeVpcAttribute` action.

**Example**  
For reference, the following is an example of the JSON for a basic client identity policy.    
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
        "ec2:CreateVPCEndpoint",
        "ec2:DescribeVpcAttribute"
      ],
      "Resource": "*"
    }
  ]
}
```

**To create a managed VPC connection for a client in Account B**

1. From the cluster administrator, get the **Cluster ARN** of the MSK cluster in Account A that you want the client in Account B to connect to. Make note of the cluster ARN to use later.

1. In the MSK console for the client Account B, choose **Managed VPC connections**, and then choose **Create connection**.

1. In the **Connection settings** pane, paste the cluster ARN into the cluster ARN text field, and then choose **Verify**.

1. Select the **Authentication type** for the client in Account B. For this use case, choose IAM when creating the client VPC connection.

1. Choose the **VPC** for the client.

1. Choose at least two availability **Zones** and associated **Subnets**. You can get the availability zone IDs from the AWS Management Console cluster details or by using the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) API or the [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) AWS CLI command. The zone IDs that you specify for the client subnet must match those of the cluster subnet. If the values for a subnet are missing, first create a subnet with the same zone ID as your MSK cluster.

1. Choose a **Security group** for this VPC connection. You can use the default security group. For more information on configuring a security group, see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html).

1. Select **Create connection**.

1. To get the list of new bootstrap broker strings from the cross-account user’s MSK console (**Cluster** details > **Managed VPC connection**), see the bootstrap broker strings shown under “**Cluster connection string**.” From the client Account B, the list of bootstrap brokers can be viewed by calling the [GetBootstrapBrokers](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html#GetBootstrapBrokers) API or by viewing the list of bootstrap brokers in the console cluster details.

1. Update the security groups associated with the VPC connections as follows:

   1. Set **inbound rules** for the PrivateLink VPC to allow all traffic for the IP range from the Account B network.

   1. [Optional] Set **Outbound rules** connectivity to the MSK cluster. Choose the **Security Group** in the VPC console, **Edit Outbound Rules**, and add a rule for **Custom TCP Traffic** for port ranges 14001-14100. The multi-VPC network load balancer is listening on the 14001-14100 port ranges. See [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html).

1. Configure the client in Account B to use the new bootstrap brokers for multi-VPC private connectivity to connect to the MSK cluster in Account A. See [Produce and consume data](https://docs.aws.amazon.com/msk/latest/developerguide/produce-consume.html).

After authorization is complete, Amazon MSK creates a managed VPC connection for each specified VPC and auth scheme. The chosen security group is associated with each connection. This managed VPC connection is configured by Amazon MSK to connect privately to the brokers. You can use the new set of bootstrap brokers to connect privately to the Amazon MSK cluster.