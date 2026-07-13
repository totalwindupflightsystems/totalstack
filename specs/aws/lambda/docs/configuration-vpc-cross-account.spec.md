---
id: "@specs/aws/lambda/docs/configuration-vpc-cross-account"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Attaching functions to resources in another account"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Attaching functions to resources in another account

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-vpc-cross-account
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Giving Lambda functions access to a resource in an Amazon VPC in another account
<a name="configuration-vpc-cross-account"></a>

You can give your AWS Lambda function access to a resource in a Amazon VPC in Amazon Virtual Private Cloud managed by another account, without exposing either VPC to the internet. This access pattern allows you to share data with other organizations using AWS. Using this access pattern, you can share data between VPCs with a greater level of security and performance than over the internet. Configure your Lambda function to use a Amazon VPC peering connection to access these resources.

**Warning**  
When you allow access between accounts or VPCs, check that your plan meets the security requirements of the respective organizations that manage these accounts. Following the instructions in this document will affect the security posture of your resources.

In this tutorial, you connect two accounts together with a peering connection using IPv4. You configure a Lambda function that is not already connected to a Amazon VPC. You configure DNS resolution to connect your function to resources that do not provide static IPs. To adapt these instructions to other peering scenarios, consult the [VPC Peering Guide](https://docs.aws.amazon.com//vpc/latest/peering/what-is-vpc-peering.html).

## Prerequisites
<a name="w2aac15c27c61b9"></a>

To give a Lambda function access to a resource in another acccount, you must have:
+ A Lambda function, configured to authenticate with and then read from your resource.
+ A resource in another account, such as an Amazon RDS cluster, available through Amazon VPC.
+ Credentials for your Lambda function's account and your resource's account. If you are not authorized to use your resource's account, contact an authorized user to prepare that account.
+ Permission to create and update a VPC (and supporting Amazon VPC resources) to associate with your Lambda function.
+ Permission to update the execution role and VPC configuration for your Lambda function.
+ Permission to create a VPC peering connection in your Lambda function's account.
+ Permission to accept a VPC peering connection in your resource's account.
+ Permission to update the configuration of your resource's VPC (and supporting Amazon VPC resources).
+ Permission to invoke your Lambda function.

## Create an Amazon VPC in your function's account
<a name="w2aac15c27c61c11"></a>

Create an Amazon VPC, subnets, route tables, and a security group in your Lambda function's account. 

**To create a VPC, subnets, and other VPC resources using the console**

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the dashboard, choose **Create VPC**.

1. For **IPv4 CIDR block**, provide a private CIDR block. Your CIDR block must not overlap with blocks used in your resource's VPC. Don't pick a block your resources' VPC uses to assign IPs to resources or a block already defined in the route tables in your resources VPC. For more information about defining appropriate CIDR blocks, see [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html).

1. Choose **Customize AZs**.

1. Select the same AZs as your resource.

1. For **Number of public subnets**, choose **0**.

1. For **VPC endpoints**, choose **None**.

1. Choose **Create VPC**.

## Grant VPC permissions to your function's execution role
<a name="w2aac15c27c61c13"></a>

Attach [AWSLambdaVPCAccessExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.html) to your function’s execution role to allow it to connect to VPCs. 

**To grant VPC permissions to your function's execution role**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function.

1. Choose **Configuration**.

1. Choose **Permissions**.

1. Under **Role name**, choose the execution role.

1. In the **Permissions policies** section, choose **Add permissions**.

1. In the dropdown list, choose **Attach policies**.

1. In the search box, enter `AWSLambdaVPCAccessExecutionRole`.

1. To the left of the policy name, choose the checkbox.

1. Choose **Add permissions**.

**To attach your function to your Amazon VPC**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function.

1. Choose the **Configuration** tab, then choose **VPC**.

1. Choose **Edit**.

1. Under **VPC**, select your VPC

1. Under **Subnets**, choose your subnets.

1. Under **Security groups**, choose the default security group for your VPC.

1. Choose **Save**.

## Create a VPC peering connection request
<a name="w2aac15c27c61c17"></a>

Create a VPC peering connection request from your function's VPC (the requester VPC) to your resource's VPC (the accepter VPC).

**To request a VPC peering connection from your function's VPC**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Choose **Create peering connection**.

1. For **VPC ID (Requester)**, select your function's VPC.

1. For **Account ID**, enter the ID of your resource's account.

1. For **VPC ID (Accepter)**, enter your resource's VPC.

## Prepare your resource's account
<a name="w2aac15c27c61c19"></a>

To create your peering connection and prepare your resource's VPC to use the connection, log in to your resource's account with a role that holds the permissions listed in the prerequisites. The steps to log in may be different based on how the account is secured. For more information about how to sign in to an AWS account, see the [AWS Sign-in User Guide](https://docs.aws.amazon.com//signin/latest/userguide/what-is-sign-in.html). In your resource's account, perform the following procedures.

**To accept the VPC peering connection request**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select the pending VPC peering connection (the status is pending-acceptance).

1. Choose **Actions**

1. From the dropdown list, choose **Accept request**.

1. When prompted for confirmation, choose **Accept request**.

1. Choose **Modify my route tables now** to add a route to the main route table for your VPC so that you can send and receive traffic across the peering connection.

Inspect the route tables for the resource's VPC. The route generated by Amazon VPC might not establish connectivity, based on how your resource's VPC is set up. Check for conflicts between the new route and existing configuration for the VPC. For more information about troubleshooting, see [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html) in the *Amazon Virtual Private Cloud VPC Peering Guide*.

**To update the security group for your resource**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group for your resource.

1. Choose **Actions**.

1. From the dropdown list, choose **Edit inbound rules**.

1. Choose **Add rule**.

1. For **Source** enter your function's account ID and security group ID, separated by a forward slash (for example, 111122223333/sg-1a2b3c4d).

1. Choose **Edit outbound rules**.

1. Check whether outbound traffic is restricted. Default VPC settings allow all outbound traffic. If outbound traffic is restricted, continue to the next step.

1. Choose **Add rule**.

1. For **Destination** enter your function's account ID and security group ID, separated by a forward slash (for example, 111122223333/sg-1a2b3c4d).

1. Choose **Save rules**.

**To enable DNS resolution for your peering connection**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select your peering connection.

1. Choose **Actions**.

1. Choose **Edit DNS settings**.

1. Below **Accepter DNS resolution**, select **Allow requester VPC to resolve DNS of accepter VPC hosts to private IP**.

1. Choose **Save changes**.

## Update VPC configuration in your function's account
<a name="w2aac15c27c61c21"></a>

Log in to your function's account, then update the VPC configuration.

**To add a route for your VPC peering connection**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the check box next to the name of the route table for the subnet you associated with your function.

1. Choose **Actions**.

1. Choose **Edit routes**.

1. Choose **Add route**.

1. For **Destination**, enter the CIDR block for your resource's VPC.

1. For **Target**, select your VPC peering connection.

1. Choose **Save changes**.

For more information about considerations you may encounter while updating your route tables, consult [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com//vpc/latest/peering/vpc-peering-routing.html).

**To update the security group for your Lambda function**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Choose **Actions**.

1. Choose **Edit inbound rules**.

1. Choose **Add rule**.

1. For **Source** enter your resource's account ID and security group ID, separated by a forward slash (for example, 111122223333/sg-1a2b3c4d).

1. Choose **Save rules**.

**To enable DNS resolution for your peering connection**

1. Open the [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select your peering connection.

1. Choose **Actions**.

1. Choose **Edit DNS settings**.

1. Below **Requester DNS resolution**, select **Allow accepter VPC to resolve DNS of requester VPC hosts to private IP**.

1. Choose **Save changes**.

## Test your function
<a name="w2aac15c27c61c23"></a>

**To create a test event and inspect your function's output**

1. In the **Code source** pane, choose **Test**.

1. Select **Create new event**.

1. In the **Event JSON** panel, replace the default values with an input appropriate for your Lambda function.

1. Choose **Invoke**.

1. In the **Execution results** tab, confirm that **Response** contains your expected output.

Additionally, you can check your function's logs to verify the logs are as you expect.

**To view your function's invocation records in CloudWatch Logs**

1. Choose the **Monitor** tab.

1. Choose **View CloudWatch logs**.

1. In the **Log streams** tab, choose the log stream for your function's invocation.

1. Confirm your logs are as you expect.