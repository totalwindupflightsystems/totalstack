---
id: "@specs/aws/datasync/docs/agent-requirements"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Agent requirements"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Agent requirements

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/agent-requirements
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Requirements for AWS DataSync agents
<a name="agent-requirements"></a>

Before you [deploy](deploy-agents.md) an AWS DataSync agent in your storage environment, make sure that you understand the agent hypervisor and resource requirements.

## Hypervisor requirements
<a name="hosts-requirements"></a>

DataSync agents can be deployed on supported hypervisors to facilitate data transfer.

**Note**  
Enhanced mode agents only support VMware ESXi, KVM, Nutanix AHV, and EC2.

You can run a DataSync agent on the following hypervisors:
+ **VMware ESXi (version 7.0 or 8.0)**: VMware ESXi is available on the [Broadcom website](https://knowledge.broadcom.com/external/article?articleId=366685#mcetoc_1i29sq73la). You also need a VMware vSphere client to connect to the host. 
+ **Linux Kernel-based Virtual Machine (KVM)**: A free, open-source virtualization technology. KVM is included in Linux versions 2.6.20 and newer. DataSync is tested and supported for the CentOS/RHEL 7 and 8, Ubuntu 16.04 LTS, and Ubuntu 18.04 LTS distributions. Other modern Linux distribution might work, but function or performance is not guaranteed. You must enable hardware accelerated virtualization on your KVM host to deploy your DataSync agent.

  We recommend this option if you already have a KVM environment up and running and you're already familiar with how KVM works.

  Running KVM on Amazon EC2 isn't supported and can't be used for DataSync agents.
+ **Microsoft Hyper-V (version 2012 R2, 2016, or 2019)**: Basic mode agents only. For this setup, you need a Microsoft Hyper-V Manager on a Microsoft Windows client computer to connect to the host.

  The DataSync agent is a generation 1 virtual machine (VM). For more information about the differences between generation 1 and generation 2 VMs, see [Should I create a generation 1 or 2 virtual machine in Hyper-V?](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/should-i-create-a-generation-1-or-2-virtual-machine-in-hyper-v) 
+ **Amazon EC2**: DataSync provides an Amazon Machine Image (AMI) that contains the DataSync image. For the recommended instance types, see [Amazon EC2 instance requirements](#ec2-instance-types).

## Agent requirements for DataSync transfers
<a name="agent-tranfer-resource-requirements"></a>

For DataSync transfers, your agent must meet the following resource requirements.

**Important**  
Keep in mind that the Basic mode agent requirements for working with up to 20 million files, objects, or directories are general guidelines. Your agent may need more resources because of other factors, such as how many directories you have and object metadata size. For example, the m5.2xlarge instance for an Amazon EC2 agent still might not be enough for a transfer of less than 20 million files.  
Enhanced mode agents don't have file quotas.

**Contents**
+ [Virtual machine requirements](#hardware)
+ [Amazon EC2 instance requirements](#ec2-instance-types)

### Virtual machine requirements
<a name="hardware"></a>

When deploying a DataSync agent that isn't on an Amazon EC2 instance, the agent VM requires the following resources, depending upon whether you use a Basic mode agent or an Enhanced mode agent:


| Resource | Basic mode | Enhanced mode | 
| --- | --- | --- | 
| Virtual processors | Four virtual processors assigned to the VM | Eight virtual processors assigned to the VM | 
| Disk space | 80 GB of disk space for installing the VM image and system data | 80 GB of disk space for installing the VM image and system data | 
| RAM | 32 GB of RAM assigned to the VM for task executions working with up to 20 million files, objects, or directories<br />64 GB of RAM assigned to the VM for task executions working with more than 20 million files, objects, or directories | 32 GB of RAM assigned to the VM | 

### Amazon EC2 instance requirements
<a name="ec2-instance-types"></a>

When deploying a DataSync agent on an Amazon EC2 instance, the instance size must be at least 2xlarge. We recommend using one of the following instance sizes, depending upon whether you use a Basic mode agent or an Enhanced mode agent: 


| Basic mode agent | Enhanced mode agent | 
| --- | --- | 
| For task executions working with up to 20 million files, objects, or directories, use **m5.2xlarge.** <br />For task executions working with more than 20 million files, objects, or directories, use **m5.4xlarge.**  | Use **m6a.2xlarge** regardless of the number of files, objects, or directories in your dataset. | 

## Agent requirements for AWS Region partitions
<a name="agent-partition-requirements"></a>

DataSync agent images are associated with specific [AWS Region partitions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?id=docs_gateway#partition). For example, by default you can't download an agent in a commercial AWS Region and then activate it in an AWS GovCloud (US) Region.

## Agent management requirements
<a name="agent-management-requirements"></a>

Once you [activate](activate-agent.md) your DataSync agent, AWS manages the agent for you. For more information, see [Managing your AWS DataSync agent](managing-agent.md).