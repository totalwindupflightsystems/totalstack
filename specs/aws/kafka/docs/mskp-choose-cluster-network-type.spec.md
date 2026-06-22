---
id: "@specs/aws/kafka/docs/mskp-choose-cluster-network-type"
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
> **spec:id:** @specs/aws/kafka/docs/mskp-choose-cluster-network-type
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure dual-stack network type for an Amazon MSK cluster
<a name="mskp-choose-cluster-network-type"></a>

 Amazon MSK supports dual-stack network type for existing MSK Provisioned clusters that use Kafka version 3.6.0 or later at no additional cost. With dual-stack networking, your clusters can use both IPv4 and IPv6 addresses. Dual-stack endpoints also support IPv4 thus maintaining backward compatibility. Amazon MSK provides IPv6 support through dual-stack network type, not as IPv6-only. 

 By default, clients connect to Amazon MSK clusters using the IPv4 network type. All new clusters that you create also use IPv4 by default. To update a cluster's network type to dual-stack, make sure you’ve fulfilled the prerequisites described in the following section. Then, use the [UpdateConnectivity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html#UpdateConnectivity) API to update connectivity to dual-stack. 

 When you enable dual-stack networking on your cluster, you'll receive two types of bootstrap strings - one for IPv4 and one for IPv6 connectivity. While the cluster itself supports both IPv4 and IPv6 simultaneously (dual-stack), each bootstrap string is protocol-specific - you'll need to use IPv4 bootstrap strings for IPv4 connections and IPv6 bootstrap strings for IPv6 connections. There is no single bootstrap string that supports both protocols. Your existing IPv4 bootstrap strings will continue to work as before, while the new IPv6 bootstrap strings will be identified by the 'bi6-' prefix. Note that IPv6 connectivity is only available for broker nodes - ZooKeeper nodes can only be accessed using IPv4 bootstrap strings. Make sure to configure the appropriate ports for the protocol you plan to use, as IPv4 and IPv6 connections use different ports. For more information on required ports, see [Port Information](https://docs.aws.amazon.com/msk/latest/developerguide/port-info.html). 

 All existing MSK Provisioned clusters that support dual-stack network type will use the same IPv6 bootstrap strings for both default and public access connectivity. If you have public access enabled on your cluster, the IPv6 bootstrap strings will automatically have public access capability. Note that if public access is not enabled on your cluster, these IPv6 bootstrap strings will not have public access capability. Your existing IPv4 bootstrap strings will continue to work as before for IPv4 connectivity. 

**Note**  
Once you update your cluster to use the dual-stack network type, you can’t switch it back to the IPv4 network type.

**Topics**
+ [Prerequisites for using dual-stack network type](#mskp-ipv6-prerequisites)
+ [IAM permissions to configure dual-stack network type](#mskp-ipv6-iam-permissions)
+ [Configure dual-stack network type for an existing cluster](#update-mskp-network-type)
+ [Considerations for using dual-stack network type](#mskp-dual-stack-considerations)

## Prerequisites for using dual-stack network type
<a name="mskp-ipv6-prerequisites"></a>

Before you configure dual-stack network type for your clusters, make sure you have the following:
+ Kafka version 3.6.0 or later for existing MSK Provisioned clusters.
+  All subnets you provide during cluster creation must have both IPv4 and IPv6 CIDR blocks assigned and support dual-stack network type. If even one subnet in your cluster doesn’t have IPv6 CIDR blocks assigned, you won’t be able to use the dual-stack network type for your cluster. 
+ Dual-stack connectivity is not supported on kafka.t3.small instance types. If you have a this instance type and want to use dual-stack connectivity, you need to upgrade to another supported instance type first.
+ Required ports must be open for IPv6 connectivity. For information about the required ports, see [Port information.](https://docs.aws.amazon.com/msk/latest/developerguide/port-info.html)
+  Dual-stack connectivity is not supported for ZooKeeper nodes. You can only connect to ZooKeeper nodes using IPv4. 

## IAM permissions to configure dual-stack network type
<a name="mskp-ipv6-iam-permissions"></a>

You must have the following IAM permissions:
+  `ec2:CreateTags` 
+  `ec2:DescribeSubnets` 
+  `kafka:UpdateConnectivity` 

For a complete list of permissions required to perform all Amazon MSK actions, see AWS managed policy: [ AmazonMSKFullAccess.](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonMSKFullAccess)

## Configure dual-stack network type for an existing cluster
<a name="update-mskp-network-type"></a>

You can update the network type for an existing MSK Provisioned cluster using the AWS Management Console, AWS CLI, or AWS SDK.

------
#### [ Using AWS Management Console ]

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK Provisioned cluster for which you want to configure the dual-stack network type.

1. On the Cluster details page, choose **Properties**.

1. In **Network settings**, choose **Edit**. Then, choose **Modify network type**.
**Note**  
 If your cluster isn’t using Kafka version 3.6.0 or later and its subnets don’t support dual-stack configuration, the option to modify network type will be unavailable. To change the network type, upgrade your Kafka version and use subnets that support dual-stack configuration. 

1. For **Network type**, choose **Dual stack**.

1. Choose **Save changes**.

------
#### [ Using AWS CLI ]

You can use the [ update-connectivity](https://docs.aws.amazon.com/cli/latest/reference/kafka/update-connectivity.html) API to update the network type of your existing MSK Provisioned cluster to dual-stack. The following example uses the ` update-connectivity` command to set the cluster’s network type to dual-stack.

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

The following example uses the [ UpdateConnectivity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html#UpdateConnectivity) API to set the cluster’s network type to dual-stack.

In the following example, replace the sample cluster ARN, arn:aws:kafka:{{us-east-1}}:{{ 123456789012}}:cluster/{{myCluster}} /{{12345678-1234-1234-1234-123456789012 -1}}, with your actual MSK cluster ARN. To get the current cluster version use the [ DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) API.

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
<a name="mskp-dual-stack-considerations"></a>
+ IPv6 support is currently available only in dual-stack mode (IPv4 \+ IPv6), not as IPv6-only.
+ To use dual-stack network type for your Amazon MSK Provisioned clusters, Kafka version 3.6.0 or later is required.
+ Dual-stack network type is unavailable for multi-VPC private connectivity.
+ IPv6 connectivity for Zookeeper nodes is unavailable. You can only connect to ZooKeeper nodes using IPv4.
+ You can change the network type from IPv4 to dual-stack for an existing cluster only if all its subnets support the dual-stack network type.
+ You can't revert to the IPv4 network type after enabling dual-stack. To switch back, you must delete and recreate the cluster.
+ You must have the following IAM permissions:
  + `ec2:CreateTags`, `ec2:DescribeSubnets` and `kafka:UpdateConnectivity`