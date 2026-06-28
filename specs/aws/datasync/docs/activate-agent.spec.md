---
id: "@specs/aws/datasync/docs/activate-agent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Activating your agent"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Activating your agent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/activate-agent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Activating your AWS DataSync agent
<a name="activate-agent"></a>

To finish creating your AWS DataSync agent, you must activate it. This step associates the agent with your AWS account.

**Note**  
You can't activate an agent in more than one AWS account and AWS Region at a time.

## Prerequisites
<a name="activate-agent-prerequisites"></a>

To activate your DataSync agent, make sure that you have the following information:
+ The [DataSync service endpoint](choose-service-endpoint.md) that you're activating your agent with.

  If you're using a VPC service endpoint, you need these details:
  + The VPC service endpoint ID.
  + The subnet where your VPC service endpoint is located.
  + The security group that allows the traffic required for using DataSync [VPC service endpoints](datasync-network.md#using-vpc-endpoint).
+ Your agent's IP address or domain name.

  How you find this depends on the type of agent that you [deploy](deploy-agents.md). For example, if your agent is an Amazon EC2 instance, you can find its IP address by going to the instance's page on the Amazon EC2 console.

**Note**  
For FIPS VPC endpoints, use the AWS CLI or DataSync API.

## Getting an activation key
<a name="get-activation-key"></a>

You can obtain an activation key for your deployed DataSync agent a few different ways. Some options require access to your agent on port 80 (HTTP). If you use one of these options, DataSync closes the port once you activate the agent.

**Note**  
Agent activation keys expire in 30 minutes if unused.

------
#### [ DataSync console ]

When [activating your agent in the DataSync console](#activate-agent-how-to), DataSync can get the activation key for you by using the **Automatically get the activation key from your agent** option.

To use this option, your browser must be able to reach your agent on port 80.

------
#### [ Agent local console ]

Unlike the other options for getting an activation key, this option doesn't require your agent to be accessible on port 80.

1. Log in to the [local console](local-console-vm.md#local-console-login) of your agent virtual machine (VM) or Amazon EC2 instance.

1. On the **AWS DataSync Activation - Configuration** main menu, enter **0** to get an activation key.

1. Enter the AWS Region that you're activating your agent in.

1. Enter the type of service endpoint type that your agent is using.

1. Copy the activation key that displays.

   For example: `F0EFT-7FPPR-GG7MC-3I9R3-27DOH`

   You specify this key when [activating your agent](#activate-agent-how-to).

------
#### [ CLI ]

With standard Unix tools, you can run a `curl` request to your agent's IP address to get its activation key.

To use this option, your client must be able to reach your agent on port 80. You can run the following command to check:

```
nc -vz {{agent-ip-address}} 80
```

Once you confirm you can reach the agent, run one of the following commands depending on the type of service endpoint that you're using:
+ **Public service endpoints**:

  ```
  curl "http://{{agent-ip-address}}/?gatewayType=SYNC&activationRegion={{your-region}}&no_redirect"
  ```
+ **FIPS service endpoints**:

  ```
  curl "http://{{agent-ip-address}}/?gatewayType=SYNC&activationRegion={{your-region}}&endpointType=FIPS&no_redirect"
  ```
+ **VPC service endpoints**:

  ```
  curl "http://{{agent-ip-address}}/?gatewayType=SYNC&activationRegion={{your-region}}&privateLinkEndpoint={{vpc-endpoint-ip-address}}&endpointType=PRIVATE_LINK&no_redirect"
  ```
+ **FIPS VPC service endpoints**:

  ```
  curl "http://{{agent-ip-address}}/?gatewayType=SYNC&activationRegion={{your-region}}&privateLinkEndpoint={{vpc-endpoint-ip-address}}&endpointType=FIPS_PRIVATE_LINK&no_redirect"
  ```

**Note**  
To find the `{{vpc-endpoint-ip-address}}`, open the [Amazon VPC console](https://console.aws.amazon.com/vpc/), choose **Endpoints**, and select your DataSync VPC service endpoint. On the **Subnets** tab, locate the IP address for your [VPC service endpoint's subnet](choose-service-endpoint.md#datasync-in-vpc). This is the endpoint's IP address.

This command returns an activation key. For example:

`F0EFT-7FPPR-GG7MC-3I9R3-27DOH`

You specify this key when [activating your agent](#activate-agent-how-to).

------

## Activating your agent
<a name="activate-agent-how-to"></a>

You have several options for activating your DataSync agent. Once activated, AWS [manages the agent](managing-agent.md) for you.

------
#### [ DataSync console ]

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Agents**, and then choose **Create agent**.

1. In the **Service endpoint** section, do the following to specify the service endpoint for your agent:
   + For a public service endpoint, choose **Public service endpoints in {{your current AWS Region}}**.
   + For a FIPS service endpoint, choose **FIPS service endpoints in {{your current AWS Region}}**.
   + For a VPC service endpoint, do the following:
     + Choose **VPC endpoints using AWS PrivateLink**.
     + For **VPC endpoint**, choose the VPC service endpoint that you want your agent to use.
     + For **Subnet**, choose the subnet where your VPC service endpoint is located.
     + For **Security group**, choose the security group that allows the traffic required for using DataSync [VPC service endpoints](datasync-network.md#using-vpc-endpoint).

1. In the **Activation key** section, do one of the following to specify your agent's activation key:
   + Choose **Automatically get the activation key from your agent** for DataSync to get the key for you. 
     + For **Agent address**, enter your agent's IP address or domain name.
     + Choose **Get key**.

       If activation fails, [check your network configuration](datasync-network.md) based on the type of service endpoint you're using.
   + Choose **Manually enter your agent's activation key** if you don't want a connection between your browser and agent.
     +  [Get the key](#get-activation-key) from the agent local console or by using a `curl` command.
     + Back in the DataSync console, enter the key in the **Activation key** field.

1. (Recommended) For **Agent name**, give your agent a name that you can remember.

1. (Optional) For **Tags**, enter values for the **Key** and **Value** fields to tag your agent.

   Tags help you manage, filter, and search for your AWS resources. 

1. Choose **Create agent**.

1. On the **Agents** page, verify that your agent is using the correct service endpoint type.
**Note**  
At this point, you might notice that your agent is offline. This happens briefly after activating an agent.

------
#### [ AWS CLI ]

1. Once you [get your activation key](#get-activation-key), copy one of the following `create-agent` commands depending on the type of service endpoint that you're using:
   + **Public or FIPS service endpoint**:

     ```
     aws datasync create-agent \
       --activation-key {{activation-key}} \
       --agent-name {{name-for-agent}}
     ```
   + **VPC or FIPS VPC service endpoint**:

     ```
     aws datasync create-agent \
       --activation-key {{activation-key}} \
       --agent-name {{name-for-agent}} \
       --vpc-endpoint-id {{vpc-endpoint-id}} \
       --subnet-arns {{subnet-arn}} \
       --security-group-arns {{security-group-arn}}
     ```

1. For `--activation-key`, specify your [agent activation key](#get-activation-key).

1. (Recommended) For `--agent-name`, specify a name for your agent that you can remember.

1. If you're using a VPC service endpoint, specify the following options:
   + For `--vpc-endpoint-id`, specify the ID of the VPC service endpoint that you're using.
   + For `--subnet-arns`, specify the ARN of the subnet where your VPC service endpoint is located.
   + For `--security-group-arns`, specify the ARN of the security group that allows the traffic required for using DataSync [VPC service endpoints](datasync-network.md#using-vpc-endpoint).

1. Run the `create-agent` command.

   You get a response with the ARN of the agent that you just activated. For example:

   ```
   {
       "AgentArn": "arn:aws:datasync:us-east-1:111222333444:agent/agent-0b0addbeef44baca3"
   }
   ```

1. Verify that your agent is activated by running the `list-agents` command:

   ```
   aws datasync list-agents
   ```
**Note**  
At this point, you might notice that your agent `Status` is `OFFLINE`. This happens briefly after activating an agent.

------
#### [ DataSync API ]

Once you [get your activation key](#get-activation-key), activate your agent by using the [CreateAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateAgent.html) operation.

**Note**  
When you're done, you might notice that your agent is offline. This happens briefly after activating an agent.

------

## Next steps
<a name="activate-agent-next-steps"></a>
+ [Verify your agent's connection](test-agent-connections.md) to your storage system and the DataSync service.
+ If you run into issues trying to activate your agent, get help with [troubleshooting](troubleshooting-datasync-agents.md).
+ Create the DataSync location that you want to use with your agent. This might be an [on-premises](transferring-on-premises-storage.md) or [other cloud](transferring-other-cloud-storage.md) location.