---
id: "@specs/aws/kafka/docs/msk-connect-internet-access-private-subnets-example"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up a NAT gateway"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up a NAT gateway

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-internet-access-private-subnets-example
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up a NAT gateway for Amazon MSK Connect
<a name="msk-connect-internet-access-private-subnets-example"></a>

The following steps show you how to set up a NAT gateway to enable internet access for a connector. You must complete these steps before you create a connector in a private subnet.

## Complete prerequisites for setting up a NAT gateway
<a name="msk-connect-internet-access-private-subnets-prereq"></a>

Make sure you have the following items.
+ The ID of the Amazon Virtual Private Cloud (VPC) associated with your cluster. For example, *vpc-123456ab*.
+ The IDs of the private subnets in your VPC. For example, *subnet-a1b2c3de*, *subnet-f4g5h6ij*, etc. You must configure your connector with private subnets.

## Steps to enable internet access for your connector
<a name="msk-connect-internet-access-private-subnets-steps"></a>

**To enable internet access for your connector**

1. Open the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Create a public subnet for your NAT gateway with a descriptive name, and note the subnet ID. For detailed instructions, see [Create a subnet in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#AddaSubnet).

1. Create an internet gateway so that your VPC can communicate with the internet, and note the gateway ID. Attach the internet gateway to your VPC. For instructions, see [Create and attach an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway).

1. Provision a public NAT gateway so that hosts in your private subnets can reach your public subnet. When you create the NAT gateway, select the public subnet that you created earlier. For instructions, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating).

1. Configure your route tables. You must have two route tables in total to complete this setup. You should already have a main route table that was automatically created at the same time as your VPC. In this step you create an additional route table for your public subnet.

   1. Use the following settings to modify your VPC's main route table so that your private subnets route traffic to your NAT gateway. For instructions, see [Work with route tables](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html) in the *Amazon Virtual Private Cloud* *User Guide*.  
**Private MSKC route table**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-internet-access-private-subnets-example.html)

   1. Follow the instructions in [Create a custom route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Routing) to create a route table for your public subnet. When you create the table, enter a descriptive name in the **Name tag** field to help you identify which subnet the table is associated with. For example, **Public MSKC**.

   1. Configure your **Public MSKC** route table using the following settings.  
****    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-internet-access-private-subnets-example.html)