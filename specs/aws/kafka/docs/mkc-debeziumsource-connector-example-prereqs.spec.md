---
id: "@specs/aws/kafka/docs/mkc-debeziumsource-connector-example-prereqs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Complete prerequisites to use Debezium source connector"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Complete prerequisites to use Debezium source connector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mkc-debeziumsource-connector-example-prereqs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Complete prerequisites to use Debezium source connector
<a name="mkc-debeziumsource-connector-example-prereqs"></a>

Your connector must be able to access the internet so that it can interact with services such as AWS Secrets Manager that are outside of your Amazon Virtual Private Cloud. The steps in this section help you complete the following tasks to enable internet access.
+ Set up a public subnet that hosts a NAT gateway and routes traffic to an internet gateway in your VPC.
+ Create a default route that directs your private subnet traffic to your NAT gateway.

For more information, see [Enable internet access for Amazon MSK Connect](msk-connect-internet-access.md).

**Prerequisites**

Before you can enable internet access, you need the following items:
+ The ID of the Amazon Virtual Private Cloud (VPC) associated with your cluster. For example, *vpc-123456ab*.
+ The IDs of the private subnets in your VPC. For example, *subnet-a1b2c3de*, *subnet-f4g5h6ij*, etc. You must configure your connector with private subnets.

**To enable internet access for your connector**

1. Open the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Create a public subnet for your NAT gateway with a descriptive name, and note the subnet ID. For detailed instructions, see [Create a subnet in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#AddaSubnet).

1. Create an internet gateway so that your VPC can communicate with the internet, and note the gateway ID. Attach the internet gateway to your VPC. For instructions, see [Create and attach an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway).

1. Provision a public NAT gateway so that hosts in your private subnets can reach your public subnet. When you create the NAT gateway, select the public subnet that you created earlier. For instructions, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating).

1. Configure your route tables. You must have two route tables in total to complete this setup. You should already have a main route table that was automatically created at the same time as your VPC. In this step you create an additional route table for your public subnet.

   1. Use the following settings to modify your VPC's main route table so that your private subnets route traffic to your NAT gateway. For instructions, see [Work with route tables](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html) in the *Amazon Virtual Private Cloud* *User Guide*.  
**Private MSKC route table**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/msk/latest/developerguide/mkc-debeziumsource-connector-example-prereqs.html)

   1. Follow the instructions in [Create a custom route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Routing) to create a route table for your public subnet. When you create the table, enter a descriptive name in the **Name tag** field to help you identify which subnet the table is associated with. For example, **Public MSKC**.

   1. Configure your **Public MSKC** route table using the following settings.  
****    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/msk/latest/developerguide/mkc-debeziumsource-connector-example-prereqs.html)

Now that you have enabled internet access for Amazon MSK Connect you are ready to create a connector.