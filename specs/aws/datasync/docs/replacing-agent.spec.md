---
id: "@specs/aws/datasync/docs/replacing-agent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Replacing your agent"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Replacing your agent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/replacing-agent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Replacing your AWS DataSync agent
<a name="replacing-agent"></a>

To replace an AWS DataSync agent, you must create a new agent and update any transfer locations that are using the old agent.

## Creating a new agent
<a name="replacing-agent-create-new-agent"></a>

To create your new DataSync agent, follow the same process when you created your old agent:

1. [Deploy an agent](deploy-agents.md) in your storage environment.

1. [Choose a service endpoint](choose-service-endpoint.md) that the agent uses to communicate with AWS.

1. [Configure your network](datasync-network.md) so that the agent can communicate with your storage and AWS.

1. [Activate your agent](activate-agent.md).

1. Once activated, make note of the agent’s Amazon Resource Name (ARN).

   You need this ARN when updating your DataSync location to use the new agent.

## Updating your location with the new agent
<a name="replacing-agent-update-location"></a>

Once you create a new agent, you can update an existing DataSync location to use this agent. In most cases, you also have to re-enter access credentials to update the location. This is because DataSync stores location credentials in a way that only your agent can use them.

### Using the DataSync console
<a name="replacing-agent-update-location-console"></a>

The following instructions describe how to update locations with a new agent by using the DataSync console.

------
#### [ NFS ]

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

1. Choose the location that you want to update, then choose **Edit**.

1. For **Agents**, choose your new agent.

   You can choose more than one agent if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. Choose **Save changes**.

------
#### [ SMB ]

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

1. Choose the location that you want to update, then choose **Edit**.

1. For **Agents**, choose your new agent.

   You can choose more than one agent if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. For **Password**, enter the password of the user that can mount your SMB file server and has permission to access the files and folders involved in your transfer.

1. Choose **Save changes**.

------
#### [ HDFS ]

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

1. Choose the location that you want to update, then choose **Edit**.

1. For **Agents**, choose your new agent.

   You can choose more than one agent if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. If you're using Kerberos authentication, upload your **Keytab file** and **Kerberos configuration file**.

1. Choose **Save changes**.

------
#### [ Object storage ]

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

1. Choose the location that you want to update, then choose **Edit**.

1. For **Agents**, choose your new agent.

   You can choose more than one agent if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. If your location requires credentials, enter the **Secret key** that allows DataSync to access your object storage bucket.

1. Choose **Save changes**.

------
#### [ Azure Blob Storage ]

Do the following to update your Microsoft Azure Blob Storage location:

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

1. Choose the location that you want to update, then choose **Edit**.

1. For **Agents**, choose your new agent.

   You can choose more than one agent if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. For **SAS token**, enter the [shared access signature (SAS) token](creating-azure-blob-location.md#azure-blob-sas-tokens) that allows DataSync to access your blob storage.

1. Choose **Save changes**.

------

### Using the AWS CLI
<a name="replacing-agent-update-location-cli"></a>

The following instructions describe how to update locations with a new agent by using the AWS CLI. (You can also do this by using the [DataSync API](https://docs.aws.amazon.com/datasync/latest/userguide/API_Operations.html).)

------
#### [ NFS ]

1. Copy the following [update-location-nfs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-nfs.html) command:

   ```
   aws datasync update-location-nfs \
     --location-arn {{datasync-nfs-location-arn}} \
     --on-prem-config AgentArns={{new-datasync-agent-arn}}
   ```

1. For the `--location-arn` parameter, specify the ARN of the NFS location that you're updating.

1. For the `--on-prem-config` parameter’s `AgentArns` option, specify the ARN of your new agent.

   You can specify more than one ARN if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. Run the `update-location-nfs` command to update the location.

------
#### [ SMB ]

1. Copy the following [update-location-smb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-smb.html) command:

   ```
   aws datasync update-location-smb \
     --location-arn {{datasync-smb-location-arn}} \
     --agent-arns {{new-datasync-agent-arn}} \
     --password {{smb-file-server-password}}
   ```

1. For the `--location-arn` parameter, specify the ARN of the SMB location that you're updating.

1. For the `--agent-arns` parameter, specify the ARN of your new agent.

   You can specify more than one ARN if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. For the `--password` parameter, specify the password of the user that can mount your SMB file server and has permission to access the files and folders involved in your transfer.

1. Run the `update-location-smb` command to update the location.

------
#### [ HDFS ]

1. Copy the following [update-location-hdfs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-hdfs.html) command:

   ```
   aws datasync update-location-hdfs \
     --location-arn {{datasync-hdfs-location-arn}} \
     --agent-arns {{new-datasync-agent-arn}} \
     --kerberos-keytab {{keytab-file}} \
     --kerberos-krb5-conf {{krb5-conf-file}}
   ```

1. For the `--location-arn` parameter, specify the ARN of the HDFS location that you're updating.

1. For the `--agent-arns` parameter, specify the ARN of your new agent.

   You can specify more than one ARN if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. If you're using Kerberos authentication, include the `--kerberos-keytab` and `--kerberos-krb5-conf` parameters:
   + For the `--kerberos-keytab` parameter, specify the Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and encrypted keys.

     You can specify the keytab file by providing the file's address.
   + For the `--kerberos-krb5-conf` parameter, specify the file that contains the configuration for your Kerberos realm.

     You can specify the `krb5.conf` file by providing the file's address.

   If you're using simple authentication, you don't need to include these Kerberos-related parameters in your command.

1. Run the `update-location-hdfs` command to update the location.

------
#### [ Object storage ]

1. Copy the following [update-location-object-storage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-object-storage.html) command:

   ```
   aws datasync update-location-object-storage \
     --location-arn {{datasync-object-storage-location-arn}} \
     --agent-arns {{new-datasync-agent-arn}} \
     --secret-key {{bucket-secret-key}}
   ```

1. For the `--location-arn` parameter, specify the ARN of the object storage location that you're updating.

1. For the `--agent-arns` parameter, specify the ARN of your new agent.

   You can specify more than one ARN if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. Do the following depending on if your object storage location requires access credentials:
   + **If your location requires credentials** – For the `--secret-key` parameter, specify the secret key that allows DataSync to access your object storage bucket.
   + **If your location requires credentials** – Specify empty strings for the `--access-key` and `--secret-key` parameters. Here's an example command:

     ```
     aws datasync update-location-object-storage \
       --location-arn arn:aws:datasync:{{us-east-2}}:{{111122223333}}:location/loc-{{abcdef01234567890}} \
       --agent-arns arn:aws:datasync:{{us-east-2}}:{{111122223333}}:agent/agent-{{1234567890abcdef0}} \
       --access-key "" \
       --secret-key ""
     ```

1. Run the `update-location-object-storage` command to update the location.

------
#### [ Azure Blob Storage ]

1. Copy the following [update-location-azure-blob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-azure-blob.html) command:

   ```
   aws datasync update-location-azure-blob \
     --location-arn {{datasync-azure-blob-storage-location-arn}} \
     --agent-arns {{new-datasync-agent-arn}} \
     --sas-configuration '{
         "Token": "{{sas-token-for-azure-blob-storage}}"
       }'
   ```

1. For the `--location-arn` parameter, specify the ARN of the Azure Blob Storage location that you're updating.

1. For the `--agent-arns` parameter, specify the ARN of your new agent.

   You can specify more than one ARN if you're replacing [multiple agents](do-i-need-datasync-agent.md#multiple-agents) for a location.

1. For the `--sas-configuration` parameter's `Token` option, specify the [SAS token](creating-azure-blob-location.md#azure-blob-sas-tokens) that allows DataSync to access your blob storage.

1. Run the `update-location-azure-blob` command to update the location.

------

## Next steps
<a name="replacing-agent-next-steps"></a>

1. [Delete your old agent](clean-up.md#deleting-agent). If you have any running DataSync tasks using this agent, wait until those tasks finish before deleting it.

1. If you need to replace agents for multiple locations, repeat the previous steps.

1. When you’re done, you can resume [running your tasks](run-task.md).
**Note**  
**Replacing agents for scheduled tasks** – If you replace an agent for a [scheduled task](task-scheduling.md), you must start that task manually if the new agent is using a different type of [service endpoint](choose-service-endpoint.md) than your old agent. If you don't run the task manually before its next scheduled run, the task fails.  
For example, if your old agent used a public service endpoint, but the new agent uses a VPC endpoint, start that task manually by using the console or `StartTaskExecution` operation. After that, your task will resume running on its schedule.