---
id: "@specs/aws/lambda/docs/with-msk-cluster-network"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster and network setup"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Cluster and network setup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-msk-cluster-network
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring your Amazon MSK cluster and Amazon VPC network for Lambda
<a name="with-msk-cluster-network"></a>

To connect your AWS Lambda function to your Amazon MSK cluster, you need to correctly configure your cluster and the [Amazon Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) it resides in. This page describes how to configure your cluster and VPC. If your cluster and VPC are already configured properly, see [Configuring Amazon MSK event sources for Lambda](with-msk-configure.md) to configure the event source mapping.

**Topics**
+ [Overview of network configuration requirements for Lambda and MSK integrations](#msk-network-requirements)
+ [Configuring a NAT gateway for an MSK event source](#msk-nat-gateway)
+ [Configuring AWS PrivateLink endpoints for an MSK event source](#msk-vpc-privatelink)

## Overview of network configuration requirements for Lambda and MSK integrations
<a name="msk-network-requirements"></a>

The networking configuration required for a Lambda and MSK integration depends on the network architecture of your application. There are three main resources involved in this integration: the Amazon MSK cluster, the Lambda function, and the Lambda event source mapping. Each of these resources resides in a different VPC:
+ Your Amazon MSK cluster typically resides in a private subnet of a VPC that you manage.
+ Your Lambda function resides in an AWS-managed VPC owned by Lambda.
+ Your Lambda event source mapping resides in another AWS-managed VPC owned by Lambda, separate from the VPC that contains your function.

The [event source mapping](invocation-eventsourcemapping.md) is the intermediary resource between the MSK cluster and the Lambda function. The event source mapping has two primary jobs. First, it polls your MSK cluster for new messages. Then, it invokes your Lambda function with those messages. Since these three resources are in different VPCs, both the poll and invoke operations require cross-VPC network calls.

The network configuration requirements for your event source mapping depends on whether it uses [provisioned mode](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode) or on-demand mode, as shown in the following diagram:

![Comparison of network calls for on-demand versus provisioned mode Kafka ESMs](http://docs.aws.amazon.com/lambda/latest/dg/images/MSK-esm-network-overview.png)


The way that the Lambda event source mapping polls your MSK cluster for new messages is the same in both modes. To establish a connection between your event source mapping and your MSK cluster, Lambda creates a [hyperplane ENI](configuration-vpc.md#configuration-vpc-enis) (or reuses an existing one, if available) in your private subnet to establish a secure connection. As illustrated in the diagram, this hyperplane ENI uses the subnet and security group configuration of your MSK cluster, not your Lambda function.

After polling the message from the cluster, the way Lambda invokes your function is different in each mode:
+ In provisioned mode, Lambda automatically handles the connection between the event source mapping VPC and the function VPC. So, you don’t need any additional networking components to successfully invoke your function.
+ In on-demand mode, your Lambda event source mapping invokes your function via a path through your customer-managed VPC. Because of this, you need to configure either a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the public subnet of your VPC, or [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) endpoints in the private subnet of the VPC that provide access to Lambda, [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html), and optionally, [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). Correctly configuring either one of these options allows a connection between your VPC and the Lambda-managed runtime VPC, which is necessary to invoke your function.

A NAT gateway allows resources in your private subnet to access the public internet. Using this configuration means your traffic traverses the internet before invoking the Lambda function. AWS PrivateLink endpoints allow private subnets to securely connect to AWS services or other private VPC resources without traversing the public internet. See [Configuring a NAT gateway for an MSK event source](#msk-nat-gateway) or [Configuring AWS PrivateLink endpoints for an MSK event source](#msk-vpc-privatelink) for details on how to configure these resources.

So far, we’ve assumed that your MSK cluster resides in a private subnet within your VPC, which is the more common case. However, even if your MSK cluster is in a public subnet within your VPC, you must configure AWS PrivateLink endpoints to enable a secure connection. The following table summarizes the networking configuration requirements based on how you configure your MSK cluster and Lambda event source mapping:


| MSK cluster location (in customer-managed VPC) | Lambda event source mapping scaling mode | Required networking configuration | 
| --- | --- | --- | 
| Private subnet | On-demand mode | NAT gateway (in your VPC's public subnet), or AWS PrivateLink endpoints (in your VPC's private subnet) to enable access to Lambda, AWS STS, and optionally, Secrets Manager. | 
| Public subnet | On-demand mode | AWS PrivateLink endpoints (in your VPC's public subnet) to enable access to Lambda, AWS STS, and optionally, Secrets Manager. | 
| Private subnet | Provisioned mode | None | 
| Public subnet | Provisioned mode | None | 

In addition, the security groups associated with your MSK cluster must allow traffic over the correct ports. Ensure that you have the following security group rules configured:
+ **Inbound rules** – Allow all traffic on the default broker port. The port that MSK uses depends on the type of authentication on the cluster: `9098` for IAM authentication, `9096` for SASL/SCRAM, and `9094` for TLS. Alternatively, you can use a self-referencing security group rule to allow access from instances within the same security group.
+ **Outbound rules** – Allow all traffic on port `443` for external destinations if your function needs to communicate with other AWS services. Alternatively, you can use a self-referencing security group rule to limit access to the broker if you don’t need to communicate with other AWS services.
+ **Amazon VPC endpoint inbound rules** – If you’re using an Amazon VPC endpoint, the security group associated with the endpoint must allow inbound traffic on port `443` from the cluster’s security group.

## Configuring a NAT gateway for an MSK event source
<a name="msk-nat-gateway"></a>

You can configure a NAT gateway to allow your event source mapping to poll messages from your cluster, and invoke the function via a path through your VPC. This is required only if your event source mapping uses on-demand mode, and your cluster resides within a private subnet of your VPC. If your cluster resides in a public subnet of your VPC, or your event source mapping uses provisioned mode, you don’t need to configure a NAT gateway.

A [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) allows resources in a private subnet to access the public internet. If you need private connectivity to Lambda, see [Configuring AWS PrivateLink endpoints for an MSK event source](#msk-vpc-privatelink) instead.

After you configure your NAT gateway, you must configure the appropriate route tables. This allows traffic from your private subnet to route to the public internet via the NAT gateway.

![Diagram of a customer-managed VPC using a NAT Gateway to route traffic from the private subnet to the public internet.](http://docs.aws.amazon.com/lambda/latest/dg/images/MSK-NAT-Gateway.png)


The following steps guide you through configuring a NAT gateway using the console. Repeat these steps as necessary for each Availability Zone (AZ).

**To configure a NAT gateway and proper routing (console)**

1. Follow the steps in [ Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html), noting the following:
   + NAT gateways should always reside in a public subnet. Create NAT gateways with [public connectivity](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).
   + If your MSK cluster is replicated across multiple AZs, create one NAT gateway per AZ. For example, in each AZ, your VPC should have one private subnet containing your cluster, and one public subnet containing your NAT gateway. For a setup with three AZs, you’ll have three private subnets, three public subnets, and three NAT gateways.

1. After you create your NAT gateway, open the [Amazon VPC console](https://console.aws.amazon.com/vpc/) and choose **Route tables** in the left menu.

1. Choose **Create route table**.

1. Associate this route table with the VPC that contains your MSK cluster. Optionally, enter a name for your route table.

1. Choose **Create route table**.

1. Choose the route table you just created.

1. Under the **Subnet associations** tab, choose **Edit subnet associations**.
   + Associate this route table with the private subnet that contains your MSK cluster.

1. Choose **Edit routes**.

1. Choose **Add route**:

   1. For **Destination**, choose `0.0.0.0/0`.

   1. For **Target**, choose **NAT gateway**.

   1. In the search box, choose the NAT gateway you created in step 1. This should be the NAT gateway in the same AZ as the private subnet that contains your MSK cluster (the private subnet that you associated with this route table in step 6).

1. Choose **Save changes**.

## Configuring AWS PrivateLink endpoints for an MSK event source
<a name="msk-vpc-privatelink"></a>

You can configure AWS PrivateLink endpoints to poll messages from your cluster, and invoke the function via a path through your VPC. These endpoints should allow your MSK cluster to access the following:
+ The Lambda service
+ The [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
+ Optionally, the [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) service. This is required if the secret required for cluster authentication is stored in Secrets Manager.

Configuring PrivateLink endpoints is required only if your event source mapping uses on-demand mode. If your event source mapping uses provisioned mode, Lambda establishes the required connections for you.

PrivateLink endpoints allow secure, private access to AWS services over AWS PrivateLink. Alternatively, to configure a NAT gateway to give your MSK cluster access to the public internet, see [Configuring a NAT gateway for an MSK event source](#msk-nat-gateway).

After you configure your VPC endpoints, your MSK cluster should have direct and private access to Lambda, STS, and optionally, Secrets Manager.

![Diagram of a customer-managed VPC using AWS PrivateLink endpoints to access AWS services.](http://docs.aws.amazon.com/lambda/latest/dg/images/MSK-PrivateLink-Endpoints.png)


The following steps guide you through configuring a PrivateLink endpoint using the console. Repeat these steps as necessary for each endpoint (Lambda, STS, Secrets Manager).

**To configure VPC PrivateLink endpoints (console)**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/) and choose **Endpoints** in the left menu.

1. Choose **Create endpoint**.

1. Optionally, enter a name for your endpoint.

1. For **Type**, choose **AWS services**.

1. Under **Services**, start typing the name of the service. For example, to create an endpoint to connect to Lambda, type `lambda` in the search box.

1. In the results, you should see the service endpoint in the current region. For example, in the US East (N. Virginia) region, you should see `com.amazonaws.us-east-2.lambda`. Select this service.

1. Under **Network settings**, select the VPC that contains your MSK cluster.

1. Under **Subnets**, select the AZs that your MSK cluster is in.
   + For each AZ, under **Subnet ID**, choose the private subnet that contains your MSK cluster.

1. Under **Security groups**, select the security groups associated with your MSK cluster.

1. Choose **Create endpoint**.

By default, Amazon VPC endpoints have open IAM policies that allow broad access to resources. Best practice is to restrict these policies to perform the needed actions using that endpoint. For example, for your Secrets Manager endpoint, you can modify its policy such that it allows only your function’s execution role to access the secret.

**Example VPC endpoint policy – Secrets Manager endpoint**  

```
{
    "Statement": [
        {
            "Action": "secretsmanager:GetSecretValue",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    {{"arn:aws::iam::123456789012:role/my-role"}}
                ]
            },
            "Resource": {{"arn:aws::secretsmanager:us-west-2:123456789012:secret:my-secret"}}
        }
    ]
}
```

For the AWS STS and Lambda endpoints, you can restrict the calling principal to the Lambda service principal. However, ensure that you use `"Resource": "*"` in these policies.

**Example VPC endpoint policy – AWS STS endpoint**  

```
{
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com"
                ]
            },
            "Resource": "*"
        }
    ]
}
```

**Example VPC endpoint policy – Lambda endpoint**  

```
{
    "Statement": [
        {
            "Action": "lambda:InvokeFunction",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com"
                ]
            },
            "Resource": "*"
        }
    ]
}
```