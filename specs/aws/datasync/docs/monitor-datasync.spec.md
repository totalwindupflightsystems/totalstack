---
id: "@specs/aws/datasync/docs/monitor-datasync"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitoring data transfers with CloudWatch metrics"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Monitoring data transfers with CloudWatch metrics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/monitor-datasync
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitoring data transfers with Amazon CloudWatch metrics
<a name="monitor-datasync"></a>

Amazon CloudWatch provides metrics to track DataSync transfer performance and troubleshoot issues with your transfer task. 

You can monitor AWS DataSync transfer performance by using Amazon CloudWatch metrics. DataSync metrics are automatically sent to CloudWatch in 5-minute intervals (regardless of how you [configure logging](configure-logging.md)). The metrics are retained for a period of 15 months.

To see CloudWatch metrics for DataSync, you can use the following tools:
+ The CloudWatch console
+ The CloudWatch CLI
+ The CloudWatch API
+ The DataSync console (on the task execution's details page)

For more information, see the [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html).

## CloudWatch metrics for DataSync
<a name="accessing-metrics"></a>

DataSync metrics use the `aws/datasync` namespace and provide metrics for the following dimensions:
+ **AgentId** – The unique ID of the agent (if your task uses an agent).
+ **TaskId** – The unique ID of the task. It takes the form of `task-{{01234567890abcdef}}`.

The `aws/datasync` namespace includes the following metrics. Some metrics aren't available with every [task mode](choosing-task-mode.md).


| CloudWatch metric | Task mode support | Description | 
| --- | --- | --- | 
| `BytesCompressed` | Basic | The number of physical bytes that DataSync transfers over the network after compression (if compression is possible). This number is typically less than `BytesTransferred` unless the data isn't compressible.<br />Unit: Bytes | 
| `BytesPreparedDestination` | Basic | The number of logical bytes that DataSync prepares at the destination location.<br />Unit: Bytes | 
| `BytesPreparedSource` | Basic | The number of logical bytes that DataSync prepares at the source location.<br />Unit: Bytes | 
| `BytesTransferred` | Basic | The number of bytes that DataSync sends to the network before compression (if compression is possible). For the number of bytes transferred over the network, see the `BytesCompressed` metric.<br />Unit: Bytes | 
| `BytesVerifiedDestination` | Basic | The number of logical bytes that DataSync verifies at the destination location.<br />Unit: Bytes | 
| `BytesVerifiedSource` | Basic | The number of logical bytes that DataSync verifies at the source location.<br />Units: Bytes | 
| `BytesWritten` | Enhanced, Basic | The number of logical bytes that DataSync writes to the destination location.<br />Unit: Bytes | 
| `FilesDeleted` | Enhanced, Basic | The number of files, objects, and directories that DataSync deletes in your destination location. If you don't configure your task to [delete data in the destination that isn't in the source](configure-metadata.md#task-option-file-object-handling), the value is always `0`.<br />Unit: Count | 
| `FilesListedSource` | Enhanced | The number of objects that DataSync finds at your source location.<br />Unit: Count | 
| `FilesPrepared` | Enhanced | The number of objects that DataSync will attempt to transfer after comparing your source and destination locations. For more information, see [How DataSync prepares your data transfer](how-datasync-transfer-works.md#how-datasync-prepares).<br />This metric isn't applicable if you configure your task to [transfer all data](configure-metadata.md#task-option-transfer-mode). In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.<br />Unit: Count | 
| `FilesPreparedDestination` | Basic | The number of files, objects, and directories that DataSync prepares at the destination location.<br />Unit: Count | 
| `FilesPreparedSource` | Basic | The number of files, objects, and directories that DataSync prepares at the source location.<br />Unit: Count | 
| `FilesSkipped` | Basic | The number of files, objects, and directories that DataSync skips during your transfer.<br />Unit: Count | 
| `FilesTransferred` | Enhanced, Basic | The number of files, objects, and directories that DataSync transfers over the network. This value is updated periodically during the [task execution](run-task.md#understand-task-execution-statuses) when something is read from the source and sent over the network. This value can be less than `EstimatedFilesToTransfer` in a [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html) response if DataSync fails to transfer something. In some cases, this value can also be greater than `EstimatedFilesToTransfer`. This metric is implementation-specific for some location types, so don't use it as an exact indication of what transferred or to monitor your task execution.  <br />Unit: Count | 
| `FilesVerified` | Enhanced | The number of objects that DataSync verifies during your transfer.<br />Unit: Count | 
| `FilesVerifiedDestination` | Basic | The number of files, objects, and directories that DataSync verifies at the destination location.<br />Unit: Count | 
| `FilesVerifiedSource` | Basic | The number of files, objects, and directories that DataSync verifies at the source location.<br />Unit: Count | 