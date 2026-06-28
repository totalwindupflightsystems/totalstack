---
id: "@specs/aws/datasync/docs/discovery-configure-storage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Adding your on-premises storage system"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Adding your on-premises storage system

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/discovery-configure-storage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Adding your on-premises storage system to DataSync Discovery
<a name="discovery-configure-storage"></a>

Specify an on-premises storage system that you want AWS DataSync Discovery to collect information about and provide AWS storage migration recommendations for.

**Note**  
DataSync Discovery currently supports NetApp Fabric-Attached Storage (FAS) and All Flash FAS (AFF) systems that are running ONTAP 9.7 or later.

## Accessing your on-premises storage system
<a name="discovery-configure-storage-access"></a>

To collect information about your on-premises storage system, DataSync Discovery needs credentials that provide read access to your storage system's management interface. For security, DataSync Discovery stores these credentials in AWS Secrets Manager.

**Important**  
If you update these credentials on your storage system, make sure to also update them in DataSync Discovery. You can do this by using the [UpdateStorageSystem](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateStorageSystem.html) operation.

### How DataSync Discovery uses AWS Secrets Manager
<a name="how-datasync-uses-secrets-manager"></a>

AWS Secrets Manager is a secret storage service that protects database credentials, API keys, and other secret information. DataSync Discovery uses Secrets Manager to protect the credentials that you provide for accessing your on-premises storage system.

Secrets Manager encrypts secrets using AWS Key Management Service keys. For more information, see [Secret encryption and decryption](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).

You can configure Secrets Manager to automatically rotate secrets for you according to a schedule that you specify. This enables you to replace long-term secrets with short-term ones, which helps to significantly reduce the risk of compromise. For more information, see [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

You pay for credentials stored in Secrets Manager. For more information, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing).

## Adding your on-premises storage system
<a name="discovery-add-storage"></a>

You must provide some information about your storage system before DataSync Discovery can collect information about it.

### Using the AWS CLI
<a name="discovery-add-storage-cli"></a>

Using the AWS Command Line Interface (AWS CLI), configure DataSync Discovery to work with your on-premises storage system.

**Before you begin**: We recommend that you [enable logging with CloudWatch](#discovery-enable-cloudwatch).

**To add an on-premises storage system by using the AWS CLI**

1. Copy the following `add-storage-system` command:

   ```
   aws datasync add-storage-system \
     --server-configuration ServerHostname="{{domain-or-ip}}",ServerPort={{network-port}} \
     --system-type {{storage-system-type}} \
     --credentials Username="{{your-management-interface-username}}",Password="{{your-management-interface-password}}"
     --agent-arns "{{agent-arn}}"
   ```

1. Specify the following required parameters in the command:
   + `--server-configuration ServerHostname` – Specify the domain name or IP address of your storage system's management interface.
   + `--server-configuration ServerPort` – Specify the network port that's needed to connect with the system's management interface.
   + `--system-type` – Specify the type of storage system that you're adding.
   + `--credentials` – Include the following options:
     + ` Username` – Specify the user name needed to access your storage system's management interface.
     + `Password` – Specify the password needed to access your storage system's management interface.

       For more information, see [Accessing your on-premises storage system](#discovery-configure-storage-access).
   + `--agent-arns` – Specify the DataSync agent that you want to connect to your storage system's management interface.

     If you don't haven't an agent, see [Deploying your AWS DataSync agent](deploy-agents.md).

1. (Optional) Add any of the following parameters to the command:
   + `--cloud-watch-log-group-arn` – Specify the Amazon Resource Name (ARN) of the CloudWatch log group that you want to use to log DataSync Discovery activity.
   + `--tags` – Specify a `Key` and `Value` to tag the DataSync resource that's representing your storage system.

     A *tag* is a key-value pair that helps you manage, filter, and search for your DataSync resources.
   + `--name` – Specify a name for your storage system.

1. Run the `add-storage-system` command.

   You get a response that shows you the storage system ARN that you just added.

   ```
   {
       "StorageSystemArn": "arn:aws:datasync:us-east-1:123456789012:system/storage-system-abcdef01234567890"
   }
   ```

After you add the storage system, you can run a discovery job to collect information about the storage system.

## Removing your on-premises storage system
<a name="discovery-remove-storage"></a>

When you remove an on-premises storage system from DataSync Discovery, you permanently delete any associated discovery jobs, collected data, and recommendations.

### Using the AWS CLI
<a name="discovery-remove-storage-cli"></a>

1. Copy the following `remove-storage-system` command:

   ```
   aws datasync remove-storage-system --storage-system-arn "{{your-storage-system-arn}}"
   ```

1. For `--storage-system-arn`, specify the ARN of your storage system.

1. Run the `remove-storage-system` command.

   If successful, you get an HTTP 200 response with an empty HTTP body.

## Logging DataSync Discovery activity to Amazon CloudWatch
<a name="discovery-enable-cloudwatch"></a>

When you enable logging with Amazon CloudWatch, you can more easily troubleshoot issues with DataSync Discovery. For example, if your discovery job is interrupted, you can check the logs to locate the issue. If you resolve the problem within 12 hours of when it occurred, your discovery job picks up where it left off.

If you configure your system by using the AWS CLI, you must [create a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) with a resource policy that allows DataSync to log events to the log group. You can use a [log group resource policy](configure-logging.md#cloudwatchlogs) similar to one for DataSync tasks, with some differences:
+ For the service principal, use `discovery-datasync.amazonaws.com`.
+ If you're using the `ArnLike` condition, specify a storage system ARN like this:

  ```
  "ArnLike": {
    "aws:SourceArn": [
      "arn:aws:datasync:{{region}}:{{account-id}}:system/*"
     ]
  },
  ```