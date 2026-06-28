---
id: "@specs/aws/datasync/docs/creating-azure-blob-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with Microsoft Azure Blob Storage"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with Microsoft Azure Blob Storage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/creating-azure-blob-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring transfers with Microsoft Azure Blob Storage
<a name="creating-azure-blob-location"></a>

With AWS DataSync, you can transfer data between Microsoft Azure Blob Storage (including Azure Data Lake Storage Gen2 blob storage) and the following AWS storage services:
+ [Amazon S3](create-s3-location.md)
+ [Amazon EFS](create-efs-location.md)
+ [Amazon FSx for Windows File Server](create-fsx-location.md)
+ [Amazon FSx for Lustre](create-lustre-location.md)
+ [Amazon FSx for OpenZFS](create-openzfs-location.md)
+ [Amazon FSx for NetApp ONTAP](create-ontap-location.md)

To set up this kind of transfer, you create a [location](how-datasync-transfer-works.md#sync-locations) for your Azure Blob Storage. You can use this location as a transfer source or destination. A DataSync agent is required only when transferring data between Azure Blob and Amazon EFS or Amazon FSx, or when using **Basic** mode tasks. You don't need an agent to transfer data between Azure Blob and Amazon S3 using **Enhanced** mode.

## Providing DataSync access to your Azure Blob Storage
<a name="azure-blob-access"></a>

How DataSync accesses your Azure Blob Storage depends on several factors, including whether you're transferring to or from blob storage and what kind of [shared access signature (SAS) token](#azure-blob-sas-tokens) you're using. Your objects also must be in an [access tier](#azure-blob-access-tiers) that DataSync can work with.

**Topics**
+ [SAS tokens](#azure-blob-sas-tokens)
+ [Access tiers](#azure-blob-access-tiers)

### SAS tokens
<a name="azure-blob-sas-tokens"></a>

A SAS token specifies the access permissions for your blob storage. (For more information about SAS, see the [Azure Blob Storage documentation](https://learn.microsoft.com/azure/storage/common/storage-sas-overview).)

You can generate SAS tokens to provide different levels of access. DataSync supports tokens with the following access levels:
+ Account
+ Container

The access permissions that DataSync needs depends on the scope of your token. Not having the correct permissions can cause your transfer to fail. For example, your transfer won't succeed if you're moving objects with tags to Azure Blob Storage but your SAS token doesn't have tag permissions.

**Topics**
+ [SAS token permissions for account-level access](#account-sas-tokens)
+ [SAS token permissions for container-level access](#container-sas-tokens)
+ [SAS expiration policies](#azure-blob-sas-expiration-policies)

#### SAS token permissions for account-level access
<a name="account-sas-tokens"></a>

DataSync needs an account-level access token with the following permissions (depending on whether you're transferring to or from Azure Blob Storage).

------
#### [ Transfers from blob storage ]
+ **Allowed services** – Blob
+ **Allowed resource types** – Container, Object

  If you don't include these permissions, DataSync can't transfer your object metadata, including [object tags](#azure-blob-considerations-object-tags).
+ **Allowed permissions** – Read, List
+ **Allowed blob index permissions** – Read/Write (if you want DataSync to copy [object tags](#azure-blob-considerations-object-tags))

------
#### [ Transfers to blob storage ]
+ **Allowed services** – Blob
+ **Allowed resource types** – Container, Object

  If you don't include these permissions, DataSync can't transfer your object metadata, including [object tags](#azure-blob-considerations-object-tags).
+ **Allowed permissions** – Read, Write, List, Delete (if you want DataSync to remove files that aren't in your transfer source)
+ **Allowed blob index permissions** – Read/Write (if you want DataSync to copy [object tags](#azure-blob-considerations-object-tags))

------

#### SAS token permissions for container-level access
<a name="container-sas-tokens"></a>

DataSync needs a container-level access token with the following permissions (depending on whether you're transferring to or from Azure Blob Storage).

------
#### [ Transfers from blob storage ]
+ Read
+ List
+ Tag (if you want DataSync to copy [object tags](#azure-blob-considerations-object-tags))
**Note**  
You can't add the tag permission when generating a SAS token in the Azure portal. To add the tag permission, instead generate the token by using the [https://learn.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer](https://learn.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer) app or generate a [SAS token that provides account-level access](#account-sas-tokens).

------
#### [ Transfers to blob storage ]
+ Read
+ Write
+ List
+ Delete (if you want DataSync to remove files that aren't in your transfer source)
+ Tag (if you want DataSync to copy [object tags](#azure-blob-considerations-object-tags))
**Note**  
You can't add the tag permission when generating a SAS token in the Azure portal. To add the tag permission, instead generate the token by using the [https://learn.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer](https://learn.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer) app or generate a [SAS token that provides account-level access](#account-sas-tokens).

------

#### SAS expiration policies
<a name="azure-blob-sas-expiration-policies"></a>

Make sure that your SAS doesn't expire before you expect to finish your transfer. For information about configuring a SAS expiration policy, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy).

If the SAS expires during the transfer, DataSync can no longer access your Azure Blob Storage location. (You might see a Failed to open directory error.) If this happens, [update your location](#azure-blob-update-location) with a new SAS token and restart your DataSync task.

### Access tiers
<a name="azure-blob-access-tiers"></a>

When transferring from Azure Blob Storage, DataSync can copy objects in the hot and cool tiers. For objects in the archive access tier, you must rehydrate those objects to the hot or cool tier before you can copy them.

When transferring to Azure Blob Storage, DataSync can copy objects into the hot, cool, and archive access tiers. If you're copying objects into the archive access tier, DataSync can't verify the transfer if you're trying to [verify all data in the destination](configure-data-verification-options.md).

DataSync doesn't support the cold access tier. For more information about access tiers, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview?tabs=azure-portal).

## Considerations with Azure Blob Storage transfers
<a name="azure-blob-considerations"></a>

When planning to transfer data to or from Azure Blob Storage with DataSync, there are some things to keep in mind.

**Topics**
+ [Costs](#azure-blob-considerations-costs)
+ [Blob types](#blob-types)
+ [AWS Region availability](#azure-blob-considerations-regions)
+ [Copying object tags](#azure-blob-considerations-object-tags)
+ [Transferring to Amazon S3](#azure-blob-considerations-s3)
+ [Deleting directories in a transfer destination](#azure-blob-considerations-deleted-files)
+ [Limitations](#azure-blob-limitations)

### Costs
<a name="azure-blob-considerations-costs"></a>

The fees associated with moving data in or out of Azure Blob Storage can include:
+ Running an [Azure virtual machine (VM)](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/) (if you deploy a DataSync agent in Azure)
+ Running an [Amazon EC2](https://aws.amazon.com/ec2/pricing/) instance (if you deploy a DataSync agent in a VPC within AWS)
+ Transferring the data by using [DataSync](https://aws.amazon.com/datasync/pricing/), including request charges related to [https://azure.microsoft.com/en-us/pricing/details/storage/blobs/](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/) and [Amazon S3](create-s3-location.md#create-s3-location-s3-requests) (if S3 is one of your transfer locations)
+ Transferring data in or out of [https://azure.microsoft.com/en-us/pricing/details/storage/blobs/](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/)
+ Storing data in an [AWS storage service](working-with-locations.md) supported by DataSync

### Blob types
<a name="blob-types"></a>

How DataSync works with blob types depends on whether you're transferring to or from Azure Blob Storage. When you're moving data into blob storage, the objects or files that DataSync transfers can only be block blobs. When you're moving data out of blob storage, DataSync can transfer block, page, and append blobs.

For more information about blob types, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs).

### AWS Region availability
<a name="azure-blob-considerations-regions"></a>

You can create an Azure Blob Storage transfer location in any [AWS Region that's supported by DataSync](https://docs.aws.amazon.com/general/latest/gr/datasync.html#datasync-region).

### Copying object tags
<a name="azure-blob-considerations-object-tags"></a>

The ability for DataSync to preserve object tags when transferring to or from Azure Blob Storage depends on the following factors:
+ **The size of an object's tags** – DataSync can't transfer an object with tags that exceed 2 KB.
+ **Whether DataSync is configured to copy object tags** – DataSync [copies object tags](configure-metadata.md) by default.
+ **The namespace that your Azure storage account uses** – DataSync can copy object tags if your Azure storage account uses a flat namespace but not if your account uses a hierarchical namespace (a feature of Azure Data Lake Storage Gen2). Your DataSync task will fail if you try to copy object tags and your storage account uses a hierarchical namespace.
+ **Whether your SAS token authorizes tagging** – The permissions that you need to copy object tags vary depending on the level of access that your token provides. Your task will fail if you try to copy object tags and your token doesn't have the right permissions for tagging. For more information, check the permission requirements for [account-level access tokens](#account-sas-tokens) or [container-level access tokens](#container-sas-tokens).

### Transferring to Amazon S3
<a name="azure-blob-considerations-s3"></a>

When transferring to Amazon S3, DataSync won't transfer Azure Blob Storage objects larger than 5 TB or objects with metadata larger than 2 KB.

### Deleting directories in a transfer destination
<a name="azure-blob-considerations-deleted-files"></a>

When transferring to Azure Blob Storage, DataSync can [remove objects in your blob storage that aren't present in your transfer source](configure-metadata.md). (You can configure this option by clearing the **Keep deleted files** setting in the DataSync console. Your [SAS token](#azure-blob-sas-tokens) must also have delete permissions.)

When you configure your transfer this way, DataSync won't delete directories in your blob storage if your Azure storage account is using a hierarchical namespace. In this case, you must manually delete the directories (for example, by using [https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-explorer](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-explorer)).

### Limitations
<a name="azure-blob-limitations"></a>

Remember the following limitations when transferring data to or from Azure Blob Storage:
+ DataSync [creates some directories](filtering.md#directories-ignored-during-transfers) in a location to help facilitate your transfer. If Azure Blob Storage is a destination location and your storage account uses a hierarchical namespace, you might notice task-specific subdirectories (such as `task-000011112222abcde`) in the `/.aws-datasync` folder. DataSync typically deletes these subdirectories following a transfer. If that doesn't happen, you can delete these task-specific directories yourself as long as a task isn't running.
+ DataSync doesn't support using a SAS token to access only a specific folder in your Azure Blob Storage container.
+ You can't provide DataSync a user delegation SAS token for accessing your blob storage.

## Creating your DataSync agent (optional)
<a name="azure-blob-creating-agent"></a>

A DataSync agent is required only when transferring data between Azure Blob and Amazon EFS or Amazon FSx, or when using **Basic** mode tasks. You don't need an agent to transfer data between Azure Blob and Amazon S3 using **Enhanced** mode. This section describes how to deploy and activate an agent.

**Tip**  
Although you can deploy your agent on an Amazon EC2 instance, using a Microsoft Hyper-V agent might result in decreased network latency and more data compression. 

### Microsoft Hyper-V agents
<a name="azure-blob-creating-agent-hyper-v"></a>

You can deploy your DataSync agent directly in Azure with a Microsoft Hyper-V image.

**Tip**  
Before you continue, consider using a shell script that might help you deploy your Hyper-V agent in Azure quicker. You can get more information and download the code on [GitHub](https://github.com/aws-samples/aws-datasync-deploy-agent-azure).  
If you use the script, you can skip ahead to the section about [Getting your agent's activation key](#azure-blob-creating-agent-hyper-v-3).

**Topics**
+ [Prerequisites](#azure-blob-creating-agent-hyper-v-0)
+ [Downloading and preparing your agent](#azure-blob-creating-agent-hyper-v-1)
+ [Deploying your agent in Azure](#azure-blob-creating-agent-hyper-v-2)
+ [Getting your agent's activation key](#azure-blob-creating-agent-hyper-v-3)
+ [Activating your agent](#azure-blob-creating-agent-hyper-v-4)

#### Prerequisites
<a name="azure-blob-creating-agent-hyper-v-0"></a>

To prepare your DataSync agent and deploy it in Azure, you must do the following:
+ Enable Hyper-V on your local machine.
+ Install [https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.3&viewFallbackFrom=powershell-7.1](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.3&viewFallbackFrom=powershell-7.1) (including the Hyper-V Module).
+ Install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
+ Install [https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json).

#### Downloading and preparing your agent
<a name="azure-blob-creating-agent-hyper-v-1"></a>

Download an agent from the DataSync console. Before you can deploy the agent in Azure, you must convert it to a fixed-size virtual hard disk (VHD). For more information, see the [Azure documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/prepare-for-upload-vhd-image).

**To download and prepare your agent**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Agents**, and then choose **Create agent**.

1. For **Hypervisor**, choose **Microsoft Hyper-V**, and then choose **Download the image**.

   The agent downloads in a `.zip` file that contains a `.vhdx` file.

1. Extract the `.vhdx` file on your local machine.

1. Open PowerShell and do the following:

   1. Copy the following `Convert-VHD` cmdlet:

      ```
      Convert-VHD -Path .\{{local-path-to-vhdx-file}}\aws-datasync-2.0.1686143940.1-x86_64.xfs.gpt.vhdx `
      -DestinationPath .\{{local-path-to-vhdx-file}}\aws-datasync-2016861439401-x86_64.vhd -VHDType Fixed
      ```

   1. Replace each instance of `{{local-path-to-vhdx-file}}` with the location of the `.vhdx` file on your local machine.

   1. Run the command.

   Your agent is now a fixed-size VHD (with a `.vhd` file format) and ready to deploy in Azure.

#### Deploying your agent in Azure
<a name="azure-blob-creating-agent-hyper-v-2"></a>

Deploying your DataSync agent in Azure involves:
+ Creating a managed disk in Azure
+ Uploading your agent to that managed disk
+ Attaching the managed disk to a Linux virtual machine

**To deploy your agent in Azure**

1. In PowerShell, go to the directory that contains your agent's `.vhd` file.

1. Run the `ls` command and save the `Length` value (for example, `85899346432`).

   This is the size of your agent image in bytes, which you need when creating a managed disk that can hold the image.

1. Do the following to create a managed disk:

   1. Copy the following Azure CLI command:

      ```
      az disk create -n {{your-managed-disk}} `
      -g {{your-resource-group}} `
      -l {{your-azure-region}} `
      --upload-type Upload `
      --upload-size-bytes {{agent-size-bytes}} `
      --sku standard_lrs
      ```

   1. Replace `{{your-managed-disk}}` with a name for your managed disk.

   1. Replace `{{your-resource-group}}` with the name of the Azure resource group that your storage account belongs to.

   1. Replace `{{your-azure-region}}` with the Azure region where your resource group is located.

   1. Replace `{{agent-size-bytes}}` with the size of your agent image.

   1. Run the command.

   This command creates an empty managed disk with a [standard SKU](https://learn.microsoft.com/en-us/rest/api/storagerp/srp_sku_types) where you can upload your DataSync agent.

1. To generate a shared access signature (SAS) that allows write access to the managed disk, do the following:

   1. Copy the following Azure CLI command:

      ```
      az disk grant-access -n {{your-managed-disk}} `
      -g {{your-resource-group}} `
      --access-level Write `
      --duration-in-seconds 86400
      ```

   1. Replace `{{your-managed-disk}}` with the name of the managed disk that you created.

   1. Replace `{{your-resource-group}}` with the name of the Azure resource group that your storage account belongs to.

   1. Run the command.

      In the output, take note of the SAS URI. You need this URI when uploading the agent to Azure.

   The SAS allows you to write to the disk for up to an hour. This means that you have an hour to upload your agent to the managed disk.

1. To upload your agent to your managed disk in Azure, do the following:

   1. Copy the following `AzCopy` command:

      ```
      .\azcopy copy {{local-path-to-vhd-file}} {{sas-uri}} --blob-type PageBlob
      ```

   1. Replace `{{local-path-to-vhd-file}}` with the location of the agent's `.vhd` file on your local machine.

   1. Replace `{{sas-uri}}` with the SAS URI that you got when you ran the `az disk grant-access` command.

   1. Run the command.

1. When the agent upload finishes, revoke access to your managed disk. To do this, copy the following Azure CLI command:

   ```
   az disk revoke-access -n {{your-managed-disk}} -g {{your-resource-group}}
   ```

   1. Replace `{{your-resource-group}}` with the name of the Azure resource group that your storage account belongs to.

   1. Replace `{{your-managed-disk}}` with the name of the managed disk that you created.

   1. Run the command.

1. Do the following to attach your managed disk to a new Linux VM:

   1. Copy the following Azure CLI command:

      ```
      az vm create --resource-group {{your-resource-group}} `
      --location eastus `
      --name {{your-agent-vm}} `
      --size Standard_E4as_v4 `
      --os-type linux `
      --attach-os-disk {{your-managed-disk}}
      ```

   1. Replace `{{your-resource-group}}` with the name of the Azure resource group that your storage account belongs to.

   1. Replace `{{your-agent-vm}}` with a name for the VM that you can remember.

   1. Replace `{{your-managed-disk}}` with the name of the managed disk that you're attaching to the VM.

   1. Run the command.

You've deployed your agent. Before you can start configuring your data transfer, you must activate the agent.

#### Getting your agent's activation key
<a name="azure-blob-creating-agent-hyper-v-3"></a>

To manually get your DataSync agent's activation key, follow these steps. 

Alternatively, [DataSync can automatically get the activation key for you](activate-agent.md), but this approach requires some network configuration.

**To get your agent's activation key**

1. In the Azure portal, [enable boot diagnostics for the VM for your agent](https://learn.microsoft.com/en-us/azure/virtual-machines/boot-diagnostics) by choosing the **Enable with custom storage account** setting and specifying your Azure storage account.

   After you've enabled the boot diagnostics for your agent's VM, you can access your agent’s local console to get the activation key.

1. While still in the Azure portal, go to your VM and choose **Serial console**.

1. In the agent's local console, log in by using the following default credentials: 
   + **Username** – **admin**
   + **Password** – **password**

   We recommend at some point changing at least the agent's password. In the agent's local console, enter **5** on the main menu, then use the `passwd` command to change the password.

1. Enter **0** to get the agent's activation key.

1. Enter the AWS Region where you're using DataSync (for example, **us-east-1**).

1. Choose the [service endpoint](choose-service-endpoint.md) that the agent will use to connect with AWS. 

1. Save the value of the `Activation key` output. 

#### Activating your agent
<a name="azure-blob-creating-agent-hyper-v-4"></a>

After you have the activation key, you can finish creating your DataSync agent.

**To activate your agent**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Agents**, and then choose **Create agent**.

1. For **Hypervisor**, choose **Microsoft Hyper-V**.

1. For **Endpoint type**, choose the same type of service endpoint that you specified when you got your agent's activation key (for example, choose **Public service endpoints in {{Region name}}**).

1. Configure your network to work with the service endpoint type that your agent is using. For service endpoint network requirements, see the following topics:
   + [VPC endpoints](datasync-network.md#using-vpc-endpoint)
   + [Public endpoints](datasync-network.md#using-public-endpoints)
   + [Federal Information Processing Standard (FIPS) endpoints](datasync-network.md#using-public-endpoints)

1. For **Activation key**, do the following:

   1. Choose **Manually enter your agent's activation key**.

   1. Enter the activation key that you got from the agent's local console.

1. Choose **Create agent**.

Your agent is ready to connect with your Azure Blob Storage. For more information, see [Creating your Azure Blob Storage transfer location](#creating-azure-blob-location-how-to).

### Amazon EC2 agents
<a name="azure-blob-creating-agent-ec2"></a>

You can deploy your DataSync agent on an Amazon EC2 instance.

**To create an Amazon EC2 agent**

1. [Deploy an Amazon EC2 agent](deploy-agents.md#ec2-deploy-agent).

1. [Choose a service endpoint](choose-service-endpoint.md) that the agent uses to communicate with AWS.

   In this situation, we recommend using a virtual private cloud (VPC) service endpoint.

1. Configure your network to work with [VPC service endpoints](datasync-network.md#using-vpc-endpoint).

1. [Activate the agent](https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html).

## Creating your Azure Blob Storage transfer location
<a name="creating-azure-blob-location-how-to"></a>

You can configure DataSync to use your Azure Blob Storage as a transfer source or destination.

**Before you begin**  
Make sure that you know [how DataSync accesses Azure Blob Storage](#azure-blob-access) and works with [access tiers](#azure-blob-access-tiers) and [blob types](#blob-types). You also need a [DataSync agent](#azure-blob-creating-agent) that can connect to your Azure Blob Storage container.

### Using the DataSync console
<a name="creating-azure-blob-location-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Microsoft Azure Blob Storage**.

1. For **Container URL**, enter the URL of the container that's involved in your transfer.

1. (Optional) For **Access tier when used as a destination**, choose the [access tier](#azure-blob-access-tiers) that you want your objects or files transferred into.

1. For **Folder**, enter path segments if you want to limit your transfer to a virtual directory in your container (for example, `/my/images`).

1. If your transfer requires an agent, choose **Use agents**, then choose the DataSync agent that can connect with your Azure Blob Storage container.

1. For **SAS token**, provide the credentials necessary for DataSync to access your blob storage. Some public datasets on Azure Blob storage do not require credentials. You can enter a SAS token directly, or specify an AWS Secrets Manager secret that contains the token. For more information, see [Providing credentials for storage locations](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html).

   Your SAS token is part of the SAS URI string that comes after your storage resource URI and a question mark (`?`). A token looks something like this:

   ```
   sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D
   ```

1. (Optional) Enter values for the **Key** and **Value** fields to tag the location.

   Tags help you manage, filter, and search for your AWS resources. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="creating-azure-blob-location-cli"></a>

1. Copy the following `create-location-azure-blob` command:

   ```
   aws datasync create-location-azure-blob \
     --container-url "https://{{path/to/container}}" \
     --authentication-type "SAS" \
     --sas-configuration '{
         "Token": "{{your-sas-token}}"
       }' \
     --agent-arns {{my-datasync-agent-arn}} \
     --subdirectory "{{/path/to/my/data}}" \
     --access-tier "{{access-tier-for-destination}}" \
     --tags [{"Key": "{{key1}}","Value": "{{value1}}"}]
   ```

1. For the `--container-url` parameter, specify the URL of the Azure Blob Storage container that's involved in your transfer.

1. For the `--authentication-type` parameter, specify `SAS`. If you are accessing a public dataset that does not require authentication, specify `NONE`.

1. For the `--sas-configuration` parameter's `Token` option, specify the SAS token that allows DataSync to access your blob storage. 

   You can also provide additional parameters for securing your keys using AWS Secrets Manager. For more information, see [Providing credentials for storage locations](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html).

   Your SAS token is part of the SAS URI string that comes after your storage resource URI and a question mark (`?`). A token looks something like this:

   ```
   sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D
   ```

1. (Optional) For the `--agent-arns` parameter, specify the Amazon Resource Name (ARN) of the DataSync agent that can connect to your container.

   Here's an example agent ARN: `arn:aws:datasync:{{us-east-1}}:{{123456789012}}:agent/agent-{{01234567890aaabfb}}`

   You can specify more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For the `--subdirectory` parameter, specify path segments if you want to limit your transfer to a virtual directory in your container (for example, `/my/images`).

1. (Optional) For the `--access-tier` parameter, specify the [access tier](#azure-blob-access-tiers) (`HOT`, `COOL`, or `ARCHIVE`) that you want your objects or files transferred into.

   This parameter applies only when you're using this location as a transfer destination.

1. (Optional) For the `--tags` parameter, specify key-value pairs that can help you manage, filter, and search for your location.

   We recommend creating a name tag for your location.

1. Run the `create-location-azure-blob` command.

   If the command is successful, you get a response that shows you the ARN of the location that you created. For example:

   ```
   { 
       "LocationArn": "arn:aws:datasync:us-east-1:123456789012:location/loc-12345678abcdefgh" 
   }
   ```

## Viewing your Azure Blob Storage transfer location
<a name="azure-blob-view-location"></a>

You can get details about the existing DataSync transfer location for your Azure Blob Storage.

### Using the DataSync console
<a name="azure-blob-view-location-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

1. Choose your Azure Blob Storage location.

   You can see details about your location, including any DataSync transfer tasks that are using it.

### Using the AWS CLI
<a name="azure-blob-view-location-cli"></a>

1. Copy the following `describe-location-azure-blob` command:

   ```
   aws datasync describe-location-azure-blob \
     --location-arn "{{your-azure-blob-location-arn}}"
   ```

1. For the `--location-arn` parameter, specify the ARN for the Azure Blob Storage location that you created (for example, `arn:aws:datasync:{{us-east-1}}:{{123456789012}}:location/loc-{{12345678abcdefgh}}`).

1. Run the `describe-location-azure-blob` command.

   You get a response that shows you details about your location. For example:

   ```
   {
       "LocationArn": "arn:aws:datasync:us-east-1:123456789012:location/loc-12345678abcdefgh",
       "LocationUri": "azure-blob://my-user.blob.core.windows.net/container-1",
       "AuthenticationType": "SAS",
       "Subdirectory": "/my/images",
       "AgentArns": ["arn:aws:datasync:us-east-1:123456789012:agent/agent-01234567890deadfb"],
   }
   ```

## Updating your Azure Blob Storage transfer location
<a name="azure-blob-update-location"></a>

If needed, you can modify your location's configuration in the console or by using the AWS CLI.

### Using the AWS CLI
<a name="azure-blob-update-location-cli"></a>

1. Copy the following `update-location-azure-blob` command:

   ```
   aws datasync update-location-azure-blob \
     --location-arn "{{your-azure-blob-location-arn}}" \
     --authentication-type "SAS" \
     --sas-configuration '{
         "Token": "{{your-sas-token}}"
       }' \
     --agent-arns {{my-datasync-agent-arn}} \
     --subdirectory "{{/path/to/my/data}}" \
     --access-tier "{{access-tier-for-destination}}"
   ```

1. For the `--location-arn` parameter, specify the ARN for the Azure Blob Storage location that you're updating (for example, `arn:aws:datasync:{{us-east-1}}:{{123456789012}}:location/loc-{{12345678abcdefgh}}`).

1. For the `--authentication-type` parameter, specify `SAS`.

1. For the `--sas-configuration` parameter's `Token` option, specify the SAS token that allows DataSync to access your blob storage. 

   The token is part of the SAS URI string that comes after the storage resource URI and a question mark (`?`). A token looks something like this:

   ```
   sp=r&st=2022-12-20T14:54:52Z&se=2022-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=qCBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D
   ```

1. For the `--agent-arns` parameter, specify the Amazon Resource Name (ARN) of the DataSync agent that you want to connect to your container.

   Here's an example agent ARN: `arn:aws:datasync:{{us-east-1}}:{{123456789012}}:agent/agent-{{01234567890aaabfb}}`

   You can specify more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For the `--subdirectory` parameter, specify path segments if you want to limit your transfer to a virtual directory in your container (for example, `/my/images`).

1. (Optional) For the `--access-tier` parameter, specify the [access tier](#azure-blob-access-tiers) (`HOT`, `COOL`, or `ARCHIVE`) that you want your objects to be transferred into.

   This parameter applies only when you're using this location as a transfer destination.

## Next steps
<a name="create-azure-blob-location-next-steps"></a>

After you finish creating a DataSync location for your Azure Blob Storage, you can continue setting up your transfer. Here are some next steps to consider:

1. If you haven't already, [create another location](working-with-locations.md) where you plan to transfer your data to or from your Azure Blob Storage.

1. Learn how DataSync [handles metadata and special files](metadata-copied.md), particularly if your transfer locations don't have a similar metadata structure.

1. Configure how your data gets transferred. For example, you can [transfer only a subset of your data](filtering.md) or delete files in your blob storage that aren't in your source location (as long as your [SAS token](#azure-blob-sas-tokens) has delete permissions).

1. [Start your transfer](run-task.md). 