---
id: "@specs/aws/datasync/docs/troubleshooting-datasync-agents"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting agent issues"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Troubleshooting agent issues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/troubleshooting-datasync-agents
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Troubleshooting issues with DataSync agents
<a name="troubleshooting-datasync-agents"></a>

Use the following information to help you troubleshoot issues with AWS DataSync agents. Some of these issues can include:
+ Trouble connecting to an Amazon EC2 agent's local console
+ Failing to retrieve an agent's activation key
+ Issues activating an agent with a VPC service endpoint
+ Discovering an agent is offline

## How do I connect to an Amazon EC2 agent's local console?
<a name="local-console-ec2"></a>

To connect to an Amazon EC2 agent's local console, you must use SSH. Make sure that your EC2 instance's security group allows access with SSH (TCP port 22).

In a terminal, run the following `ssh` command to connect to the instance:

```
ssh -i {{/path/key-pair-name}}.pem {{instance-user-name}}@{{instance-public-ip-address}}
```
+ For {{/path/key-pair-name}}, specify the path and file name (`.pem`) of the private key required to connect to your instance.
+ For {{instance-user-name}}, specify `admin`.
+ For {{instance-public-ip-address}}, specify the public IP address of your instance.

## What does the Failed to retrieve agent activation key error mean?
<a name="vpc-activation-error"></a>

When activating your DataSync agent, the agent connects to the service endpoint that you specify to request an activation key. This error likely means that your network security settings are blocking the connection.

**Action to take**  
If you're using a virtual private cloud (VPC) service endpoint, verify that your security group settings allow your agent to connect to the VPC endpoint. For information about required ports, see [Network requirements for VPC or FIPS VPC service endpoints](datasync-network.md#using-vpc-endpoint).

If you're using a public or Federal Information Processing Standard (FIPS) endpoint, check that your firewall and router settings allow your agent to connect to the endpoint. For information, see [Network requirements for public or FIPS service endpoints](datasync-network.md#using-public-endpoints).

## I still can't activate an agent by using a VPC service endpoint
<a name="vpc-activation-failed"></a>

If you're still having issues activating a DataSync agent with a VPC service endpoint, see [I don't know what's going on with my agent. Can someone help me?](#enable-support-access)

## What do I do if my agent is offline?
<a name="troubleshoot-agent-offline"></a>

Your DataSync agent can be offline for a few reasons, but you might be able to get it back online. Before you delete the agent and create a new one, go through the following checklist to help you understand what might have happened.
+ **Contact your backup team** – If your agent is offline because its virtual machine (VM) was restored from a snapshot or backup, you might need to [replace the agent](replacing-agent.md).
+ **Check if the agent's VM or Amazon EC2 instance is off** – Depending on the type of agent that you're using, try turning the VM or EC2 instance back on if it's off. Once it's on again, [test your agent's network connectivity](test-agent-connections.md#test-network) to AWS.
+ **Verify your agent meets the minimum hardware requirements** – Your agent might be offline because its VM or EC2 instance configuration was accidentally changed since the agent was activated. For example, if your VM no longer has the minimum required memory or space, the agent might appear as offline. For more information, see [Requirements for AWS DataSync agents](agent-requirements.md).
+ **Wait for agent-related software updates to finish** – Your agent might go offline briefly following [software updates provided by AWS](managing-agent.md#managing-agent-updates). If you believe this is why the agent is offline, wait a short period then check if the agent is back online.
+ **Check your VPC service endpoint settings** – If your offline agent is using a public service endpoint and also in the same VPC where you created a VPC service endpoint for DataSync, you might need to disable [private DNS support](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) for that VPC endpoint.

If none of these seem to be the reason that the agent is offline, you likely need to [replace the agent](replacing-agent.md).

## I don't know what's going on with my agent. Can someone help me?
<a name="enable-support-access"></a>

You can allow AWS Support to access your DataSync agent and help troubleshoot agent-related issues. You must enable this access through the agent's local console.

**To provide Support access to your agent**

1. [Log in to your agent's local console](local-console-vm.md#local-console-login).

1. At the prompt, enter **5** to open the command prompt (for VMware VMs, use **6**).

1. Enter **h** to open the **AVAILABLE COMMANDS** window.

1. In the **AVAILABLE COMMANDS** window, enter the following to connect to Support:

   `open-support-channel`

   If you are using the agent with VPC endpoints, you must provide a VPC endpoint IP address for your support channel, as follows: 

   `open-support-channel {{vpc-ip-address}}`

   Your firewall must allow the inbound TCP port 22 to initiate a support channel to AWS. When you connect to Support, DataSync assigns you a support number. Make a note of your support number.
**Note**  
The channel number isn't a TCP/UDP port number. Instead, it makes an SSH (TCP 22) connection to servers and provides the support channel for the connection.

1. When the support channel is established, provide your support service number to Support so that they can provide troubleshooting assistance.

1. When the support session is finished, press **Enter** to end it.

1. Enter **exit** to log out of the DataSync local console.

1. Follow the prompts to exit the local console.