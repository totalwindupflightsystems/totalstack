---
id: "@specs/aws/kafka/docs/serverless-config-dual-stack"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure dual-stack network type"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Configure dual-stack network type

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/serverless-config-dual-stack
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure dual-stack network type
<a name="serverless-config-dual-stack"></a>

 Amazon MSK supports dual-stack network type for existing MSK Serverless clusters that use Kafka version 3.6.0 or later at no additional cost. With dual-stack networking, your clusters can use both IPv4 and IPv6 addresses. Dual-stack endpoints also support IPv4 thus maintaining backward compatibility. Amazon MSK provides IPv6 support through dual-stack network type, not as IPv6-only.

 By default, clients connect to Amazon MSK clusters using the IPv4 network type. All new clusters that you create also use IPv4 by default. To update a cluster's network type to dual-stack, make sure you’ve fulfilled the prerequisites described in the following section. Then, use the [UpdateConnectivity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html#UpdateConnectivity) API to update connectivity to dual-stack. 

**Note**  
Once you update your cluster to use the dual-stack network type, you can’t switch it back to the IPv4 network type.

**Topics**
+ [Prerequisites for using dual-stack network type](#msks-ipv6-prerequisites)
+ [IAM permissions for MSK Serverless](#msks-ipv6-iam-permissions)
+ [Use dual-stack network type for a cluster](#update-msks-network-type)
+ [Considerations for using dual-stack network type](#msks-dual-stack-considerations)

## Prerequisites for using dual-stack network type
<a name="msks-ipv6-prerequisites"></a>

Before you configure dual-stack network type for your clusters, make sure you that all subnets you provide during cluster creation must support dual-stack network type. If even one subnet in your cluster doesn’t support dual-stack, you won’t be able to update the network type for your cluster to dual-stack.

## IAM permissions for MSK Serverless
<a name="msks-ipv6-iam-permissions"></a>

You must have the following IAM permissions:
+  `ec2:DescribeSubnets` 
+  `ec2:ModifyVpcEndpoint` 

For a complete list of permissions required to perform all Amazon MSK actions, see AWS managed policy: [ AmazonMSKFullAccess.](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonMSKFullAccess)

## Use dual-stack network type for a cluster
<a name="update-msks-network-type"></a>

You can update the network type for an MSK Serverless cluster using the AWS Management Console, AWS CLI, or AWS SDK.

------
#### [ Using AWS Management Console ]

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK Serverless cluster for which you want to configure the dual-stack network type.

1. On the Cluster details page, choose **Properties**.

1. In **Network settings**, choose **Edit network type**.

1. For **Network type**, choose **Dual stack**.

1. Choose **Save changes**.

------
#### [ Using AWS CLI ]

You can use the [ update-connectivity](https://docs.aws.amazon.com/cli/latest/reference/kafka/update-connectivity.html) API to update the network type of your existing MSK Serverless cluster to dual-stack. The following example uses the ` update-connectivity` command to set the cluster’s network type to dual-stack.

In the following example, replace the sample cluster ARN, arn:aws:kafka:{{us-east-1}}:{{ 123456789012}}:cluster/{{myCluster}} /{{12345678-1234-1234-1234-123456789012 -1}}, with your actual MSK cluster ARN. To get the current cluster version, use the [describe-cluster](https://docs.aws.amazon.com/cli/latest/reference/kafka/describe-cluster.html) command.

```
aws kafka update-connectivity \
    --cluster-arn "arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{12345678-1234-1234-1234-123456789012-1}}" \
    --current-version "{{KTVPDKIKX0DER}}" \
    --connectivity-info '{
        "networkType": "DUAL"
    }
```

------
#### [ Using AWS SDK ]

The following example uses the [UpdateConnectivity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html#UpdateConnectivity) API to set the cluster’s network type to dual-stack.

In the following example, replace the sample cluster ARN, arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{12345678-1234-1234-1234-123456789012-1}}, with your actual MSK cluster ARN. To get the current cluster version use the [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) API.

```
import boto3

client = boto3.client("kafka")

response = client.update_connectivity(
    ClusterArn="arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{myCluster}}/{{12345678-1234-1234-1234-123456789012-1}}",
    CurrentVersion="{{KTVPDKIKX0DER}}",
    ConnectivityInfo={
        "NetworkType": "DUAL"
    }
)
print("Connectivity update initiated:", response)
```

------

## Considerations for using dual-stack network type
<a name="msks-dual-stack-considerations"></a>
+ IPv6 support is currently available only in dual-stack mode (IPv4 \+ IPv6), not as IPv6-only.
+ Dual-stack network type is unavailable for multi-VPC private connectivity.
+ You can change the network type from IPv4 to dual-stack for an existing cluster only if all its subnets support the dual-stack network type.
+ You can't revert to the IPv4 network type after enabling dual-stack. To switch back, you must delete and recreate the cluster.
+ You must have the following IAM permissions:
  + `ec2:DescribeSubnets` and ` ec2:ModifyVpcEndpoint`