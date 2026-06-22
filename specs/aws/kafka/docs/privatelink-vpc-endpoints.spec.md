---
id: "@specs/aws/kafka/docs/privatelink-vpc-endpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS APIs with Interface VPC Endpoints"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# APIs with Interface VPC Endpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/privatelink-vpc-endpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use Amazon MSK APIs with Interface VPC Endpoints
<a name="privatelink-vpc-endpoints"></a>

You can use an Interface VPC Endpoint, powered by AWS PrivateLink, to prevent traffic between your Amazon VPC and Amazon MSK APIs from leaving the Amazon network. Interface VPC Endpoints don't require an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) is an AWS technology that enables private communication between AWS services using an elastic network interface with private IPs in your Amazon VPC. For more information, see [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) and [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint).

Your applications can connect with Amazon MSK Provisioned and MSK Connect APIs using AWS PrivateLink. To get started, create an Interface VPC Endpoint for your Amazon MSK API to start traffic flowing from and to your Amazon VPC resources through the Interface VPC Endpoint. FIPS-enabled Interface VPC endpoints are available for US Regions. For more information, see [Create an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint).

Using this feature, your Apache Kafka clients can dynamically fetch the connection strings to connect with MSK Provisioned or MSK Connect resources without traversing the internet to retrieve the connection strings.

When creating an Interface VPC Endpoint, choose one of the following service name endpoints:

**For MSK Provisioned:**
+ The following service name endpoints are no longer supported for new connections:
  + com.amazonaws.region.kafka
  + com.amazonaws.region.kafka-fips (FIPS-enabled)
+ Dualstack endpoint service supporting both IPv4 and IPv6 traffic are:
  + aws.api.region.kafka-api
  + aws.api.region.kafka-api-fips (FIPS-enabled)

To set up the dualstack endpoints you must follow [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) guidelines.

Where region is your region name. Choose this service name to work with MSK Provisioned-compatible APIs. For more information, see [Operations](https://docs.aws.amazon.com/msk/1.0/apireference/operations.html) in the *https://docs.aws.amazon.com/msk/1.0/apireference/*.

**For MSK Connect:**
+ com.amazonaws.region.kafkaconnect

Where region is your region name. Choose this service name to work with MSK Connect-compatible APIs. For more information, see [Actions](https://docs.aws.amazon.com/MSKC/latest/mskc/API_Operations.html) in the *Amazon MSK Connect API Reference*.

For more information, including step-by-step instructions to create an interface VPC endpoint, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

## Control access to VPC endpoints for Amazon MSK Provisioned or MSK Connect APIs
<a name="vpc-endpoints-control-access"></a>

VPC endpoint policies let you control access by either attaching a policy to a VPC endpoint or by using additional fields in a policy that is attached to an IAM user, group, or role to restrict access to occur only through the specified VPC endpoint. Use the appropriate example policy to define access permissions for either MSK Provisioned or MSK Connect service.

If you don't attach a policy when you create an endpoint, Amazon VPC attaches a default policy for you that allows full access to the service. An endpoint policy doesn't override or replace IAM identity-based policies or service-specific policies. It's a separate policy for controlling access from the endpoint to the specified service.

For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

------
#### [ MSK Provisioned — VPC policy example ]

**Read-only access**  
This sample policy can be attached to a VPC endpoint. (For more information, see Controlling Access to Amazon VPC Resources). It restricts actions to only listing and describing operations through the VPC endpoint to which it is attached.

```
{
  "Statement": [
    {
      "Sid": "MSKReadOnly",
      "Principal": "*",
      "Action": [
        "kafka:List*",
        "kafka:Describe*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

**MSK Provisioned — VPC endpoint policy example**  
Restrict access to a specific MSK cluster

This sample policy can be attached to a VPC endpoint. It restricts access to a specific Kafka cluster through the VPC endpoint to which it is attached.

```
{
  "Statement": [
    {
      "Sid": "AccessToSpecificCluster",
      "Principal": "*",
      "Action": "kafka:*",
      "Effect": "Allow",
      "Resource": "arn:aws:kafka:us-east-1:123456789012:cluster/MyCluster"
    }
  ]
}
```

------
#### [ MSK Connect — VPC endpoint policy example ]

**List connectors and create a new connector**  
The following is an example of an endpoint policy for MSK Connect. This policy allows the specified role to list connectors and create a new connector.

```
{
    "Version": "2012-10-17", 		 	 	 		 	 	 
    "Statement": [
        {
            "Sid": "MSKConnectPermissions",
            "Effect": "Allow",
            "Action": [
                "kafkaconnect:ListConnectors",
                "kafkaconnect:CreateConnector"
            ],
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{111122223333}}:role/{{MyMSKConnectExecutionRole}}"
                ]
            }
        }
    ]
}
```

**MSK Connect — VPC endpoint policy example**  
Allows only requests from a specific IP address in the specified VPC

The following example shows a policy that only allows requests coming from a specified IP address in the specified VPC to succeed. Requests from other IP addresses will fail.

```
{
    "Statement": [
        {
            "Action": "kafkaconnect:*",
            "Effect": "Allow",
            "Principal": "*",
            "Resource": "*",
            "Condition": {
                "IpAddress": {
                    "aws:VpcSourceIp": "192.0.2.123"
                },
        "StringEquals": {
                    "aws:SourceVpc": "vpc-555555555555"
                }
            }
        }
    ]
}
```

------