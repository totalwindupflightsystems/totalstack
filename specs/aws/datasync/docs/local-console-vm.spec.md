---
id: "@specs/aws/datasync/docs/local-console-vm"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Performing maintenance on your agent"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Performing maintenance on your agent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/local-console-vm
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Performing maintenance on your agent
<a name="local-console-vm"></a>

While AWS manages your AWS DataSync agent once it's deployed and activated, there might be cases where you need to change your agent's settings or troubleshoot an issue. Here are some examples of why you'd work with your agent through its local console:
+ Manually assign an IP address to the agent.
+ Check your agent's system resources.

**Important**  
You don't need to use the agent's local console for standard DataSync functionality.

## Accessing your agent's local console
<a name="local-console-login"></a>

How you access the local console depends on the type of agent you're using. 

### Accessing the local console (VMware ESXi, Linux KVM, Nutanix AHV, or Microsoft Hyper-V)
<a name="local-console-login-agent-vm"></a>

For security reasons, you can't remotely connect to the local console of the DataSync agent virtual machine (VM). You must access the local console from your hypervisor management interface.
+ If this is your first time using the local console, log in with the temporary credentials. The initial user name is **admin** and the temporary password is **password**. You must change the password on first log in.
**Note**  
Enhanced mode agents have the following password requirements:  
Must contain a minimum of 15 characters
Must contain at least one uppercase character
Must contain at least one lowercase character
Must contain at least one numeric character
Must contain at least one special character
At least 50% of the characters must change on password update
The password cannot be a dictionary word
**Note**  
After your initial password setup, you can change your password anytime. On the console main menu, enter the number next to **Command Prompt**, then run the `passwd` command to change the password.

### Accessing the local console (Amazon EC2)
<a name="local-console-login-agent-ec2"></a>

To connect to an Amazon EC2 agent's local console, you must use SSH.

**Before you begin**: Make sure that your EC2 instance's security group allows access with SSH (TCP port 22).

1. Open a terminal and copy the following `ssh` command:

   ```
   ssh -i {{/path/key-pair-name}}.pem {{instance-user-name}}@{{instance-public-ip-address}}
   ```
   + For {{/path/key-pair-name}}, specify the path and file name (`.pem`) of the private key required to connect to your instance.
   + For {{instance-user-name}}, specify `admin`.
   + For {{instance-public-ip-address}}, specify the public IP address of your instance.

1. Run the `ssh` command to connect to the instance.

Once connected, the main menu of the agent's local console displays.

## Configuring your agent's DHCP, DNS, and IP settings
<a name="network-configration"></a>

The default network configuration for the agent is Dynamic Host Configuration Protocol (DHCP). With DHCP, your agent is automatically assigned an IP address. In some cases, you might need to manually assign your agent's IP as a static IP address, as described following.

1. Log in to your agent's local console.

1. On the **AWS DataSync Activation - Configuration** main menu, enter **1** to begin configuring your network.

1. On the ** Network Configuration** menu, choose one of the following options.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/local-console-vm.html)

## Checking your agent's system resources
<a name="system-resource-check"></a>

When you log in to your agent console, virtual CPU cores, root volume size, and RAM are automatically checked. If there are any errors or warnings, they're flagged on the console menu display with a banner that provides details about those errors or warnings.

If there are no errors or warnings when the console starts, the menu displays white text. The **View System Resource Check** option will display `(0 Errors)`.

If there are errors or warnings, the console menu displays the number of errors and warnings, in red and yellow respectively, in a banner across the top of the menu. For example, `(1 ERROR, 1 WARNING)`.

**To check your agent's system resources**

1. Log in to your agent's local console.

1. On the **AWS DataSync Activation - Configuration** main menu, enter **4** to view the results of the system resource check.

   The console displays an **[OK]**, **[WARNING]**, or **[FAIL]** message for each resource as described in the table following.

   For Amazon EC2 instances, the system resource check verifies that the instance type is one of the instances recommended for use with DataSync. If the instance type matches that list, a single result is displayed in green text, as follows.

   `[ OK ] Instance Type Check`

   If the Amazon EC2 instance is not on the recommended list, the system resource check verifies the following resources.
   + CPU cores check: At least four cores are required.
   + Disk size check: A minimum of 80 GB of available disk space is required.
   + RAM check:
     + 32 GB of RAM assigned to the instance for task executions working with up to 20 million files, objects, or directories.
     + 64 GB of RAM assigned to the instance for task executions working with more than 20 million files, objects, or directories.
   + CPU flags check: The agent VM CPU must have either SSSE3 or SSE4 instruction set flags.

   If the Amazon EC2 instance is not on the list of recommended instances for DataSync, but it has sufficient resources, the result of the system resource check displays four results, all in green text.

   The same resources are verified for agents deployed in Hyper-V, Linux Kernel-based Virtual Machine (KVM), and VMware VMs.

   VMware agents are also checked for supported version; unsupported versions cause a red banner error. Supported versions include VMware versions 6.5 and 6.7.

## View and manage agent system time server configuration
<a name="time-management"></a>

You can view and manage your agent's system time server configuration.

1. Log in to your agent's [local console](#local-console-login).

1. On the **AWS DataSync Activation - Configuration** main menu, enter the option for **System Time Management** (such as **5** for VMware agent).

1. On the **System Time Management** menu, do one of the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/local-console-vm.html)

## Running maintenance-related commands for your agent
<a name="command-prompts"></a>

In your DataSync agent's local console, you can perform some maintenance tasks and diagnose issues with your agent.

**To run a configuration or diagnostic command in your agent's local console**

1. Log in to your [agent's local console](#local-console-login).

1. On the **AWS DataSync Activation - Configuration** main menu, enter **5** (or **6** for a VMware VM) for the **Command Prompt**.

1. Use the following commands to perform the following tasks with your agent.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/local-console-vm.html)

1. Follow the onscreen instructions.