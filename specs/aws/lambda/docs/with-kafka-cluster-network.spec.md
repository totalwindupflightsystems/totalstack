---
id: "@specs/aws/lambda/docs/with-kafka-cluster-network"
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
> **spec:id:** @specs/aws/lambda/docs/with-kafka-cluster-network
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring your self-managed Apache Kafka cluster and network for Lambda
<a name="with-kafka-cluster-network"></a>

To connect your Lambda function to your self-managed Apache Kafka cluster, you need to correctly configure your cluster and the network it resides in. This page describes how to configure your cluster and network. If your cluster and network are already configured properly, see [Configuring self-managed Apache Kafka event sources for Lambda](with-kafka-configure.md) to configure the event source mapping.

**Topics**
+ [Self-managed Apache Kafka cluster setup](#kafka-cluster-setup)
+ [Configure network security](#services-kafka-vpc-config)

## Self-managed Apache Kafka cluster setup
<a name="kafka-cluster-setup"></a>

You can host your self-managed Apache Kafka cluster with cloud providers such as [Confluent Cloud](https://www.confluent.io/confluent-cloud/) or [Redpanda](https://www.redpanda.com/), or run it on your own infrastructure. Ensure that your cluster is properly configured and accessible from the network where your Lambda event source mapping will connect.

## Configure network security
<a name="services-kafka-vpc-config"></a>

To give Lambda full access to self-managed Apache Kafka through your event source mapping, either your cluster must use a public endpoint (public IP address), or you must provide access to the Amazon VPC you created the cluster in.

When you use self-managed Apache Kafka with Lambda, create [AWS PrivateLink VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) that provide your function access to the resources in your Amazon VPC.

**Note**  
AWS PrivateLink VPC endpoints are required for functions with event source mappings that use the default (on-demand) mode for event pollers. If your event source mapping uses [ provisioned mode](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode), you don't need to configure AWS PrivateLink VPC endpoints.

Create an endpoint to provide access to the following resources:
+  Lambda — Create an endpoint for the Lambda service principal. 
+  AWS STS — Create an endpoint for the AWS STS in order for a service principal to assume a role on your behalf. 
+  Secrets Manager — If your cluster uses Secrets Manager to store credentials, create an endpoint for Secrets Manager. 

Alternatively, configure a NAT gateway on each public subnet in the Amazon VPC. For more information, see [Enable internet access for VPC-connected Lambda functions](configuration-vpc-internet.md).

When you create an event source mapping for self-managed Apache Kafka, Lambda checks whether Elastic Network Interfaces (ENIs) are already present for the subnets and security groups configured for your Amazon VPC. If Lambda finds existing ENIs, it attempts to re-use them. Otherwise, Lambda creates new ENIs to connect to the event source and invoke your function.

**Note**  
Lambda functions always run inside VPCs owned by the Lambda service. Your function's VPC configuration does not affect the event source mapping. Only the networking configuration of the event source's determines how Lambda connects to your event source.

Configure the security groups for the Amazon VPC containing your cluster. By default, self-managed Apache Kafka uses the following ports: `9092`.
+ Inbound rules – Allow all traffic on the default broker port for the security group associated with your event source. Alternatively, you can use a self-referencing security group rule to allow access from instances within the same security group.
+ Outbound rules – Allow all traffic on port `443` for external destinations if your function needs to communicate with AWS services. Alternatively, you can also use a self-referencing security group rule to limit access to the broker if you don't need to communicate with other AWS services.
+ Amazon VPC endpoint inbound rules — If you are using an Amazon VPC endpoint, the security group associated with your Amazon VPC endpoint must allow inbound traffic on port `443` from the cluster security group.

If your cluster uses authentication, you can also restrict the endpoint policy for the Secrets Manager endpoint. To call the Secrets Manager API, Lambda uses your function role, not the Lambda service principal.

**Example VPC endpoint policy — Secrets Manager endpoint**  

```
{
      "Statement": [
          {
              "Action": "secretsmanager:GetSecretValue",
              "Effect": "Allow",
              "Principal": {
                  "AWS": [
                      "arn:aws::iam::123456789012:role/{{my-role}}"
                  ]
              },
              "Resource": "arn:aws::secretsmanager:{{us-west-2}}:123456789012:secret:{{my-secret}}"
          }
      ]
  }
```

When you use Amazon VPC endpoints, AWS routes your API calls to invoke your function using the endpoint's Elastic Network Interface (ENI). The Lambda service principal needs to call `lambda:InvokeFunction` on any roles and functions that use those ENIs.

By default, Amazon VPC endpoints have open IAM policies that allow broad access to resources. Best practice is to restrict these policies to perform the needed actions using that endpoint. To ensure that your event source mapping is able to invoke your Lambda function, the VPC endpoint policy must allow the Lambda service principal to call `sts:AssumeRole` and `lambda:InvokeFunction`. Restricting your VPC endpoint policies to allow only API calls originating within your organization prevents the event source mapping from functioning properly, so `"Resource": "*"` is required in these policies.

The following example VPC endpoint policies show how to grant the required access to the Lambda service principal for the AWS STS and Lambda endpoints.

**Example VPC Endpoint policy — AWS STS endpoint**  

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

**Example VPC Endpoint policy — Lambda endpoint**  

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