---
id: "@specs/aws/datasync/docs/troubleshooting-tasks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting task issues"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Troubleshooting task issues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/troubleshooting-tasks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Troubleshooting issues with DataSync tasks
<a name="troubleshooting-tasks"></a>

Use the following information to help you troubleshoot issues with AWS DataSync tasks and task executions. These issues might include task setup problems, stuck task executions, and data not transferring as expected.

## Error: Invalid SyncOption value. Option: TransferMode,PreserveDeletedFiles, Value: ALL,REMOVE.
<a name="create-task-deleted-files-error"></a>

This error occurs when you're creating or editing your DataSync task and you select the **Transfer all data** option and deselect the **Keep deleted files** option.

When you transfer all data, DataSync doesn't scan your destination location and doesn't know what to delete.

## Task execution fails with an EniNotFound error
<a name="network-interfaces-not-found"></a>

This error occurs if you delete one of your task's network interfaces in your virtual private cloud (VPC). If your task is scheduled or queued, the task will fail if it's missing a [network interface required to transfer your data](required-network-interfaces.md).

**Actions to take**  
You have the following options to work around this issue:
+ Manually restart the task. When you do this, DataSync will create any missing network interfaces it needs to run the task.
+ If you need to clean up resources in your VPC, make sure that you don't delete network interfaces related to a DataSync task that you're still using.

  To see the network interfaces allocated to your task, do one of the following:
  + Use the [DescribeTask](https://docs.aws.amazon.com//datasync/latest/userguide/API_DescribeTask.html) operation. You can view the network interfaces in the `SourceNetworkInterfaceArns` and `DestinationNetworkInterfaceArns` response elements.
  + In the Amazon EC2 console, search for your task ID (such as `task-f012345678abcdef0`) to find its network interfaces.
+ Consider not running your tasks automatically. This could include disabling task queueing or scheduling (through DataSync or custom automation).

## Task execution fails with a Cannot allocate memory error
<a name="error-cannot-allocate-memory"></a>

When your DataSync task fails with a Cannot allocate memory error, it can mean a few different things.

**Action to take**  
Try the following until you no longer see the issue:
+ If your transfer involves an agent, make sure that the agent meets the [virtual machine (VM)](agent-requirements.md#hardware) or [Amazon EC2 instance](agent-requirements.md#ec2-instance-types) requirements.
+ Split your transfer into multiple tasks by using [filters](filtering.md). It's possible that you're trying to transfer more files or objects than what [one DataSync task can handle](datasync-limits.md#task-hard-limits).
+ If you still see the issue, [contact Support](https://aws.amazon.com/contact-us/).

## Task fails with `Input/Output error` for FSx for ONTAP file system
<a name="task-fails-input-output-fsxn"></a>

When your DataSync task fails with an `Input/Output error` when transferring data with an FSx for ONTAP file system, it can be due to one or more of the following issues.

**The FSx for ONTAP volume has reached its maximum file capacity**  
This error occurs when the number of available inodes, or file pointers, on a volume is exhausted.

**Actions to take**

First, view the volume's [maximum file capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/view-volume-file-capacity.html). Then, increase the volume's file capacity by either increasing the number of inodes or by increasing the storage capacity. For more information, see [Increasing a volume's maximum file capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/low-volume-capacity.html#max-file-capacity) in the *FSx for ONTAP User Guide*.

**The FSx for ONTAP volume has run out of available storage capacity**  
This error occurs when the volume doesn't have available storage capacity.

**Actions to take**

First, determine the volume's [available storage capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-volume-storage-console.html). Then, increase the volume's storage capacity. For more information, see [Increasing a volume's storage capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/low-volume-capacity.html#increase-volume-capacity) in the *FSx for ONTAP User Guide*.

**Note**  
To automatically increase the volume's storage capacity when needed, see [Using volume autosizing](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/low-volume-capacity.html#volume-autosizing) in the *FSx for ONTAP User Guide*.

**The FSx for ONTAP directory has reached the maximum number of files that can be stored in each directory**  
This error occurs when you have reached the maximum number of files that can be stored in each directory.

**Action to take**

Increase the max directory size to support larger directories. For more information, see [Best practices for using the FSx for ONTAP maximum directory size](https://docs.aws.amazon.com/prescriptive-guidance/latest/fsx-ontap-enterprise-deployment/best-practices.html#bp-max-directory-size) in *AWS Prescriptive Guidance*.

**The DataSync task execution generated too much read write concurrency, consuming a high percentage of the file system's throughput capacity**  
This error occurs when the DataSync task execution is consuming too much of your file system's available throughput capacity.

**Actions to take**

First, determine whether the task execution was consuming too much of the file system's throughput capacity using the following methods:
+ Monitor the file system’s performance using the available CloudWatch metrics. For more information, see [Monitoring file system metrics](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-throughput-cloudwatch.html#fsxn-howtomonitor-fs) in the *FSx for ONTAP User Guide*.
+ Monitor the file system for file server performance warnings in the Amazon FSx console. For more information, see [Performance warnings and recommendations](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance-insights-FSxN.html#resolve-warnings) in the *FSx for ONTAP User Guide*.

Then, make sure that the task doesn't use all of the file system's available throughput capacity by doing one of the following:
+ Set the task execution's bandwidth limit to an amount that is less than the FSx for ONTAP file system's provisioned throughput capacity. For more information, see [Setting bandwidth limits for your AWS DataSync task](configure-bandwidth.md).
+ Increase the file system’s provisioned throughput capacity. For more information, see [Updating throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/increase-throughput-capacity.html) in the *FSx for ONTAP User Guide*.

## Task fails with `Connection Reset by peer` or `Host is down` message for FSx for ONTAP file system
<a name="task-fails-connect-reset-fsxn"></a>

If your DataSync task fails with a `Connection Reset by peer` or `Host is down` message when transferring data with an FSx for ONTAP file system, it can be due to one or more of the following issues:
+ The file system’s SMB server was rebooted or otherwise disconnected during the task execution.
+ The file system failed over from the primary to secondary server (and IP address) during task execution. DataSync does not support failing over to a secondary IP address during task execution.

  FSx for ONTAP file systems failover to a secondary server and IP address during the following events:
  + The primary server becomes unavailable.
  + The primary server's Availability Zone becomes unavailable (for Multi-AZ file systems).
  + During a user-initiated throughput capacity change.
  + During the file system's regularly scheduled maintenance window.

  For more information, see [FSx for ONTAP Failover process](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html#Failover) in the FSx for ONTAP User Guide.

**Action to take**  
Restart the task.

## Task execution has a launching status but nothing seems to be happening
<a name="task-stuck-starting"></a>

Your DataSync task can get stuck with a **Launching** status typically because the agent is powered off or has lost network connectivity.

**Actions to take**  
Make sure that your agent's status is **ONLINE**. If the agent is **OFFLINE**, make sure it's powered on.

If the agent is powered on and the task is still **Launching**, then there's likely a network connection problem between your agent and AWS. For information about how to test network connectivity, see [Verifying your agent's connection to the DataSync service](test-agent-connections.md#test-network).

If you're still having this issue, see [I don't know what's going on with my agent. Can someone help me?](troubleshooting-datasync-agents.md#enable-support-access).

## Task execution seems stuck in the preparing status
<a name="Preparing-status-too-long"></a>

The amount of time your DataSync transfer task has the **Preparing** status depends on the amount of data in your transfer source and destination and the performance of those storage systems.

When a task starts, DataSync performs a recursive directory listing to discover all files, objects, directories, and metadata in your source and destination. DataSync uses these listings to identify differences between storage systems and determine what to copy. This process can take a few minutes or even a few hours.

**Action to take**  
You shouldn't have to do anything. Continue to wait for the task status to change to **Transferring**. If the status still doesn't change, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## Task execution stops before the transfer finishes
<a name="troubleshoot-unfinished-task-execution"></a>

If your DataSync task execution stops early, your task configuration might include an AWS Region that's disabled in your AWS account.

**Actions to take**  
Do the following to run your task again:

1. Check the [opt-in status](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) of your task's Regions and make sure they're enabled.

1. [Start the task](run-task.md) again.

## Task execution fails when transferring from a Google Cloud Storage bucket
<a name="troubleshoot-object-tags-google-cloud-storage"></a>

Because DataSync communicates with Google Cloud Storage by using the Amazon S3 API, there's a limitation that might cause your DataSync transfer to fail if you try to copy object tags. The following message related to the issue appears in your CloudWatch logs:

[WARN] Failed to read metadata for file /{{your-bucket}}/{{your-object}}: S3 Get Object Tagging Failed: proceeding without tagging

To prevent this, deselect the **Copy object tags** option when configuring your transfer task settings.

## There are mismatches between task execution's timestamps
<a name="troubleshoot-task-exec-times"></a>

When looking at the DataSync console or Amazon CloudWatch logs, you might notice that the start and end times for your DataSync task execution don't match the timestamps you see in other monitoring tools. This is because the console and CloudWatch logs take into account the time a task execution spends in the launching or queueing [states](run-task.md#understand-task-execution-statuses), while some other tools don’t.

You might notice this discrepancy when comparing execution timestamps between the DataSync console or CloudWatch logs and the following places:
+ Logs for the file system involved in your transfer
+ The last modified date on an Amazon S3 object that DataSync wrote to
+ Network traffic coming from the DataSync agent
+ Amazon EventBridge events

## Task execution fails with `NoMem` error
<a name="troubleshoot-nomem"></a>

The set of data you're trying to transfer may be too large for DataSync. If you see this error, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## Task execution fails with `FsNfsIdMappingEnabled` error
<a name="troubleshoot-nfsv4-idmapping"></a>

DataSync does not support NFSv4 ID mapping. To work around this, [configure your NFS location to use NFSv3](create-nfs-location.md#configure-network-nfs-location). 

## Object fails to transfer to Azure Blob Storage with `user metadata key` error
<a name="troubleshoot-azure-blob-user-metadata"></a>

When transferring from an S3 bucket to Azure Blob Storage, you might see the following error:

```
[ERROR] Failed to transfer file {{/user-metadata/file1}}: Azure Blob user metadata key must be a CSharp identifier
```

This means that `{{/user-metadata/file1}}` includes user metadata that doesn't use a valid C\# identifier. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names).

## There's an `/.aws-datasync` folder in the destination location
<a name="troubleshoot-leftover-folder"></a>

DataSync creates a folder called `/.aws-datasync` in your destination location to help facilitate your data transfer.

While DataSync typically deletes this folder following your transfer, there might be situations where this doesn't happen.

**Action to take**  
Delete this folder anytime as long as you don't have a running task execution copying to that location.

## Can't transfer symbolic links between locations using SMB
<a name="troubleshooting-smb-symbolic-links"></a>

When your task execution finishes, you see the following error:

```
Transfer and verification completed. Selected files transferred except for files skipped due to errors. If no skipped files are listed in Cloud Watch Logs, please contact AWS Support for further assistance.
```

When transferring between SMB storage systems (such as an SMB file server and Amazon FSx for Windows File Server file system), you might see the following warnings and errors in your CloudWatch logs:

```
[WARN] Failed to read metadata for file /appraiser/symlink: No data available
[ERROR] Failed to read metadata for directory /appraiser/symlink: No data available
```

**Action to take**  
DataSync doesn't support transferring symbolic links (or hard links) when transferring between these location types. For more information, see [Links and directories copied by AWS DataSync](special-files-copied.md).

## Task report errors
<a name="troubleshoot-task-report"></a>

You might run into one of the following errors while trying to monitor your DataSync transfer with a task report. 


| Error message | Workaround | 
| --- | --- | 
| File path exceeds the maximum length of 4,096 characters. Cannot write to Task Report | None. DataSync can't transfer a file with a path that exceeds 4,096 bytes.<br />For more information, see [Storage system, file, and object limits](datasync-limits.md#file-system-limits). | 
| Failed to upload Task Report(s) to S3 due to an invalid bucket or IAM role | Check that the [DataSync IAM role](creating-task-report.md#task-report-access) has the right permissions to upload a task report to your S3 bucket. | 
| Execution error occurred prior to generating any Task Reports | Check your [CloudWatch logs](monitor-datasync.md) to identify why your task execution failed. | 