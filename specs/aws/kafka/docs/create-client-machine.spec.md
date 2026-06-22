---
id: "@specs/aws/kafka/docs/create-client-machine"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a client machine"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a client machine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-client-machine
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 3: Create a client machine
<a name="create-client-machine"></a>

In this step of [Get Started Using Amazon MSK](getting-started.md), you create a client machine. You use this client machine to create a topic that produces and consumes data. For simplicity, you'll create this client machine in the VPC that is associated with the MSK cluster so that the client can easily connect to the cluster.

**To create a client machine**Create a client machine

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the Amazon EC2 console dashboard, choose **Launch instance**.

1. Under **Name and tags**, for **Name**, enter a descriptive name for your client machine so that you can easily keep track of it. For example, **MSKTutorialClient**.

1. Under **Application and OS Images (Amazon Machine Image)**, for **Amazon Machine Image (AMI)**, choose **Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type**.

1. For **Instance type**, keep the default selection of **t2.micro**.

1. Under **Key pair (login)**, choose an existing key pair or create a new one. If you don't require a key pair to connect to your instance, you can choose **Proceed without a key pair (not recommended)**.

   To create a new key pair, do the following:

   1. Choose **Create new key pair**.

   1. For **Key pair name**, enter **MSKKeyPair**.

   1. For **Key pair type** and **Private key file format**, keep the default selections.

   1. Choose **Create key pair**.

   Alternatively, you can use an existing key pair.

1. Scroll down the page and expand the **Advanced details** section, then do the following:

   1. For **IAM instance profile**, choose an IAM role that you want the client machine to assume.

     If you don't have an IAM role, do the following:

     1. Choose **Create new IAM profile**.

     1. Perform the steps mentioned in [Step 2: Create an IAM role](create-client-iam-role.md).

1. Choose **Launch instance**.

1. Choose **View Instances**. Then, in the **Security Groups** column, choose the security group that is associated with your new instance. Copy the ID of the security group, and save it for later.

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security Groups**. Find the security group whose ID you saved in [Step 1: Create an MSK Provisioned cluster](create-cluster.md).

1. In the **Inbound Rules** tab, choose **Edit inbound rules**.

1. Choose **Add rule**.

1. In the new rule, choose **All traffic** in the **Type** column. In the second field in the **Source** column, select the security group of your client machine. This is the group whose name you saved after you launched the client machine instance.

1. Choose **Save rules**. Now the cluster's security group can accept traffic that comes from the client machine's security group.

**Next Step**

[Step 4: Create a topic in the Amazon MSK cluster](create-topic.md)