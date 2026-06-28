---
id: "@specs/aws/datasync/docs/deploy-agents"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Deploying your agent"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Deploying your agent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/deploy-agents
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Deploying your AWS DataSync agent
<a name="deploy-agents"></a>

When creating an AWS DataSync agent, the first step is to deploy the agent in your storage environment. You can deploy an agent as a virtual machine (VM) on VMware ESXi, Linux Kernel-based Virtual Machine (KVM), Nutanix AHV (using the KVM image), and Microsoft Hyper-V hypervisors. You also can deploy an agent as an Amazon EC2 instance in a virtual private cloud (VPC) within AWS.

**Tip**  
Before you begin, confirm whether you [need a DataSync agent](do-i-need-datasync-agent.md).

## Deploying your agent on VMware
<a name="create-vmw-agent"></a>

You can download an agent from the DataSync console and deploy it in your VMware environment.

**Before you begin**: Make sure that your storage environment can support a DataSync agent. For more information, see [Virtual machine requirements](agent-requirements.md#hardware).

**To deploy an agent on VMware**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Agents**, and then choose **Create agent**. 

1. For **Hypervisor**, choose **VMWare ESXi**, and then choose **Download the image**.
   + The Enhanced mode agent downloads as an `.ova` image file.
   + The Basic mode agent downloads in a `.zip` file that contains the `.ova` image file

1. To minimize network latency, deploy the agent as close as possible to the storage system that DataSync needs to access (the same local network if possible). For more information, see [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements).

   If needed, see your hypervisor's documentation on how to deploy an `.ova` file in a VMware host.

1. Power on your hypervisor, log in to the agent VM, and get the agent's IP address. You need this IP address to activate the agent.

   The agent VM's default credentials are login **admin** and password **password**. If needed, change the password through the [VM's local console](local-console-vm.md).

**Next step: [Choosing a service endpoint for your AWS DataSync agent](choose-service-endpoint.md)**

## Deploying your agent on KVM
<a name="create-kvm-agent"></a>

You can download an agent from the DataSync console and deploy it in your KVM environment.

**Before you begin**: Make sure that your storage environment can support a DataSync agent. For more information, see [Virtual machine requirements](agent-requirements.md#hardware).

**To deploy an agent on KVM**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Agents**, and then choose **Create agent**.

1. For **Hypervisor**, choose **Kernel-based Virtual Machine (KVM)**, and then choose **Download the image**.
   + The Enhanced mode agent downloads as an `.qcow2` image file.
   + The Basic mode agent downloads in a `.zip` file that contains the `.qcow2` image file

1. To minimize network latency, deploy the agent as close as possible to the storage system that DataSync needs to access (the same local network if possible). For more information, see [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements).

1. Run the following command to install your `.qcow2` image. 

   ```
   virt-install \
       --name "datasync" \
       --description "DataSync agent" \
       --os-type=generic \
       --ram=32768 \
       --vcpus=4 \
       --disk path=datasync-yyyymmdd-x86_64.qcow2,bus=virtio,size=80 \
       --network default,model=virtio \
       --graphics none \
       --virt-type kvm \
       --import
   ```

   For information about how to manage this VM and your KVM host, see your hypervisor's documentation.

1. Power on your hypervisor, log in to your VM, and get the IP address of the agent. You need this IP address to activate the agent.

   The agent VM's default credentials are login **admin** and password **password**. If needed, change the password through the [VM's local console](local-console-vm.md).

**Next step: [Choosing a service endpoint for your AWS DataSync agent](choose-service-endpoint.md)**

## Deploying your Basic mode agent on Microsoft Hyper-V
<a name="create-hyper-v-agent"></a>

You can download a Basic mode agent from the DataSync console and deploy it in your Microsoft Hyper-V environment.

**Before you begin**: Make sure that your storage environment can support a DataSync agent. For more information, see [Virtual machine requirements](agent-requirements.md#hardware).

**To deploy a Basic mode agent on Hyper-V**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Agents**, and then choose **Create agent**.

1. For **Hypervisor**, choose **Microsoft Hyper-V**, and then choose **Download the image**.

   The agent downloads in a `.zip` file that contains a `.vhdx` image file.

1. To minimize network latency, deploy the agent as close as possible to the storage system that DataSync needs to access (the same local network if possible). For more information, see [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements).

   If needed, see your hypervisor's documentation on how to deploy a `.vhdx` file in a Hyper-V host.
**Warning**  
You may notice poor network performance if you enable virtual machine queue (VMQ) on a Hyper-V host that's using a Broadcom network adapter. For information about a workaround, see the [Microsoft documentation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/poor-network-performance-hyper-v-host-vm).

1. Power on your hypervisor, log in to your VM, and get the IP address of the agent. You need this IP address to activate the agent.

   The agent VM's default credentials are login **admin** and password **password**. If needed, change the password through the [VM's local console](local-console-vm.md).

**Next step: [Choosing a service endpoint for your AWS DataSync agent](choose-service-endpoint.md)**

## Deploying your Amazon EC2 agent
<a name="ec2-deploy-agent"></a>

You might deploy a DataSync agent as an Amazon EC2 instance when transferring data between:
+ A self-managed cloud storage system (for example, an NFS file server in AWS) and an AWS storage service.
+ A cloud storage provider (such as Microsoft Azure Blob Storage or Google Cloud Storage) and an AWS storage service using Basic mode.
+ An S3 bucket in a commercial AWS Region and an S3 bucket in an AWS GovCloud (US) Region.
+ [Amazon S3 on AWS Outposts](#outposts-agent) and an AWS storage service using Basic mode.

**Warning**  
We don't recommend using an Amazon EC2 agent with on-premises storage because of increased network latency. Instead, deploy the agent as a VMware, KVM, or Hyper-V virtual machine in your data center as close to your on-premises storage as possible. 

### Deploying your EC2 agent
<a name="ec2-deploy-agent-how-to"></a>

**To choose the agent AMI for your AWS Region**<a name="AMI-command"></a>

1. Open a terminal and copy the following AWS CLI command to get the latest DataSync Amazon Machine Image (AMI) ID for the Region where you want to deploy your Amazon EC2 agent.

**Basic mode agents**  
`aws ssm get-parameter --name /aws/service/datasync/ami --region {{your-region}}`

**Enhanced mode agents**  
`aws ssm get-parameter --name /aws/service/datasync/ami/v3 --region {{your-region}}`

1. Run the command. In the output, take note of the `"Value"` property with the DataSync AMI ID.  
**Example command and output**  

   ```
   aws ssm get-parameter --name /aws/service/datasync/ami --region us-east-1                              
   
   {
       "Parameter": {
           "Name": "/aws/service/datasync/ami",
           "Type": "String",
           "Value": "{{ami-1234567890abcdef0}}",
           "Version": 6,
           "LastModifiedDate": 1569946277.996,
           "ARN": "arn:aws:ssm:us-east-1::parameter/aws/service/datasync/ami"
       }
   }
   ```<a name="efs-efs-steps"></a>

**To deploy your Amazon EC2 agent**
**Tip**  
To avoid charges for transferring across Availability Zones, deploy your agent in a way that it doesn't require network traffic between Availability Zones. (To learn more about data transfer prices for all AWS Regions, see [Amazon EC2 Data Transfer pricing](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer).)  
For example, deploy your agent in the Availability Zone where your self-managed cloud storage system is located. 

1. Copy the following URL:

   ```
   https://console.aws.amazon.com/ec2/v2/home?region={{agent-region}}#LaunchInstanceWizard:ami={{ami-id}}
   ```
   + Replace `{{agent-region}}` with the Region where you want to deploy your agent.
   + Replace `{{ami-id}}` with the DataSync AMI ID that you obtained.

1. Paste the URL into a browser.

   The Amazon EC2 instance launch page in the AWS Management Console displays.

1. For **Instance type**, choose one of the [recommended Amazon EC2 instances](agent-requirements.md#ec2-instance-types) for DataSync.

1.  For **Key pair**, choose an existing key pair, or create a new one. 

1. For **Network settings**, choose **Edit** and then do the following:

   1. For **VPC**, choose a VPC where you want to deploy your agent.

   1. For **Auto-assign public IP**, choose whether you want your agent to be accessible from the public internet.

      You use the instance's public or private IP address later to activate your agent.

   1. For **Firewall (security groups)**, create or a select a security group that does the following:
      + If needed, allows inbound traffic to the Amazon EC2 instance on port 80 (HTTP). Some options for [getting an agent activation key](activate-agent.md#get-activation-key) require this connection.
      + Allows inbound and outbound traffic between the Amazon EC2 instance the storage system that you're transferring data to or from. For more information, see [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements).
**Note**  
There are additional ports to configure depending on the type of [service endpoint](choose-service-endpoint.md) that your agent uses.

1. (Recommended) To increase performance when transferring from a cloud-based file system, expand **Advanced details** and choose a **Placement group** value where your storage is located.

1. Choose **Launch instance** to launch your Amazon EC2 instance.

1. Once your instance status is **Running**, choose the instance.

1. If you configured your instance to be accessible from the public internet, make note of the instance's public IP address. If you didn't, make note of the private IP address.

   You need this IP address when [activating your agent](activate-agent.md).

### Examples: Deploying your EC2 agent in an AWS Region
<a name="using-ec2-agent-in-region"></a>

The following guidance can help with common scenarios if you deploy an DataSync agent in an AWS Region.

**Topics**
+ [Deploying your Basic mode agent for transfers between cloud storage and AWS storage services](#efs-efs)
+ [Deploying your Basic mode agent for transfers between Amazon S3 and AWS file systems](#s3-cloud-nfs)

#### Deploying your Basic mode agent for transfers between cloud storage and AWS storage services
<a name="efs-efs"></a>

To transfer data between AWS accounts, or between cloud storage systems, the DataSync agent must be located in the same AWS Region and AWS account where the source file system resides. This type of transfer includes the following:
+ Transfers between Amazon EFS or Amazon FSx to AWS storage in a different AWS account.
+ Transfers from self-managed file systems to AWS storage services.

**Important**  
Deploy your agent such that it doesn't require network traffic between Availability Zones (to avoid charges for such traffic).   
To access your Amazon EFS or FSx for Windows File Server file system, deploy the agent in an Availability Zone that has a mount target to your file system.
For self-managed file systems, deploy the agent in the Availability Zone where your file system resides.
To learn more about data transfer prices for all AWS Regions, see [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/). 

For example, the following diagram shows a high-level view of the DataSync architecture for transferring data from in-cloud Network File System (NFS) to in-cloud NFS or Amazon S3.

![Diagram showing data transfer between source Region containing a virtual private cloud (VPC) with an EFS file system and DataSync agent, and a destination Region with a DataSync endpoint and EFS file system.](http://docs.aws.amazon.com/datasync/latest/userguide/images/efs-efs-ec2.png)


Remember the following when transferring between AWS storage services across AWS accounts:
+ When transferring between Amazon EFS file systems or Amazon FSx file systems using the NFS protocol, configure your source file system as an [NFS location](create-nfs-location.md).
+ When transferring between Amazon FSx file systems using the SMB protocol, configure your source file system as an [SMB location](create-smb-location.md).

#### Deploying your Basic mode agent for transfers between Amazon S3 and AWS file systems
<a name="s3-cloud-nfs"></a>

The following diagram provides a high-level view of the DataSync architecture for transferring data from Amazon S3 to an AWS file system, such as Amazon EFS or Amazon FSx. You can use this architecture to transfer data from one AWS account to another, or to transfer data from Amazon S3 to a self-managed in-cloud file system. 

![Diagram showing data transfer between source Region containing an S3 bucket and DataSync endpoint, and a destination Region containing a VPC with an EFS file system and DataSync agent.](http://docs.aws.amazon.com/datasync/latest/userguide/images/s3-efs-ec2.png)


## Deploying your Basic mode agent on AWS Outposts
<a name="outposts-agent"></a>

You can launch a DataSync Amazon EC2 instance on your Outpost. To learn more about launching an AMI on AWS Outposts, see [Launch an instance on your Outpost](https://docs.aws.amazon.com/outposts/latest/userguide/launch-instance.html) in the *AWS Outposts User Guide*. 

When using DataSync to access Amazon S3 on Outposts, you must use a Basic mode agent and launch it in a VPC that's allowed to access your Amazon S3 access point, and activate the agent in the parent Region of the Outpost. The agent must also be able to route to the Amazon S3 on Outposts endpoint for the bucket. To learn more about working with Amazon S3 on Outposts endpoints, see [Working with Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WorkingWithS3Outposts.html#AccessingS3Outposts) in the *Amazon S3 User Guide*.