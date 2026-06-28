---
id: "@specs/aws/datasync/docs/datasync-limits"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Quotas"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Quotas

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/datasync-limits
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS DataSync quotas
<a name="datasync-limits"></a>

Find out about resource quotas and limits when working with AWS DataSync.

## Storage system, file, and object limits
<a name="file-system-limits"></a>

The following table describes the limits that DataSync has when working with storage systems, files, and objects.


| Description | Limit | 
| --- | --- | 
| Maximum total file path length | 4,096 bytes | 
| Maximum file path component (file name, directory, or subdirectory) length | 255 bytes | 
| Maximum length of Windows domain | 253 characters | 
| Maximum length of server hostname | 255 characters | 
| Maximum Amazon S3 object name length | 1,024 UTF-8 characters | 

## DataSync quotas
<a name="task-hard-limits"></a>

The following table describes the quotas for DataSync resources in a specific AWS account and Region.


| Resource | Quota | Adjustable | 
| --- | --- | --- | 
| Maximum number of tasks you can create | 100 | Yes | 
| **(Enhanced mode tasks)** Maximum number of source and destination objects that DataSync can work with per task execution<br />For more information, see [How DataSync transfers files, objects, and directories](how-datasync-transfer-works.md#transferring-files) | Virtually unlimited | N/A | 
| **(Basic mode tasks)** Maximum number of source and destination files, objects, and directories that DataSync can work with per task execution between on-premises, self-managed, or other cloud storage and AWS storage services <br />For more information, see [How DataSync transfers files, objects, and directories](how-datasync-transfer-works.md#transferring-files) | 50 million Remember the following about this quota:   If you transfer Amazon S3 objects with prefixes, the prefixes are treated as directories and count towards the quota. For example, DataSync would consider`s3://bucket/foo/bar.txt` as two directories (`./` and `./foo/`) and one object (`bar.txt`).   If your task is working with more than 20 million files, objects, or directories, make sure that you allocate a minimum of 64 GB of RAM to your DataSync agent. For more information, see [agent requirements for DataSync transfers](agent-requirements.md#agent-tranfer-resource-requirements).    | Yes Instead of requesting an increase, you can create tasks that focus on specific directories using include and exclude filters. For more information, see [filtering the data transferred by DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).  | 
| **(Basic mode tasks)** Maximum number of source and destination files, objects, and directories that DataSync can work with per task execution between AWS storage services<br />For more information, see [How DataSync transfers files, objects, and directories](how-datasync-transfer-works.md#transferring-files) | 25 million If you transfer Amazon S3 objects with prefixes, the prefixes are treated as directories and count towards the quota. For example, DataSync would consider`s3://bucket/foo/bar.txt` as two directories (`./` and `./foo/`) and one object (`bar.txt`).  | Yes Instead of requesting an increase, you can create tasks that focus on specific directories using include and exclude filters. For more information, see [filtering the data transferred by DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).  | 
| Maximum throughput per task (for transfers that use a DataSync agent) | 10 Gbps | No | 
| Maximum throughput per task (for transfers that don't use a DataSync agent) | 5 Gbps | No | 
| Maximum number of characters you can include in a task filter | 102,400 characters If you're using the DataSync console, this limit includes all the characters combined in your include and exclude patterns.  | No | 
| Maximum number of queued executions for a single task | 50 | No | 
| Maximum number of concurrent Enhanced mode task executions | 120 | No | 
| Maximum number of days a task execution's history is retained | 30 | No | 
| Maximum size for a manifest file with Enhanced mode tasks | 20 GB | No | 

## Request a quota increase
<a name="request-quota-increase"></a>

You can request an increase for some DataSync quotas. Increases aren't granted right away and might take a couple of days to take effect.

**To request a quota increase**

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services** and then choose **AWS DataSync**.

1. Choose the quota that you want to increase, then choose **Request increase at account-level**.

1. Enter the total amount that you want the quota to be, then choose **Request**.

   If you need to increase a different quota, fill out a separate request.