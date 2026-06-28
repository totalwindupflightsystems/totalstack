---
id: "@specs/aws/datasync/docs/datasync-large-migration-poc"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Running a proof of concept"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Running a proof of concept

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/datasync-large-migration-poc
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Running a DataSync proof of concept
<a name="datasync-large-migration-poc"></a>

Running a proof of concept (POC) with AWS DataSync helps you validate the following aspects of your data migration planning:
+ Verify network connectivity between source and destination locations.
+ Validate your initial DataSync task configuration.
+ Measure data transfer performance.
+ Estimate migration timelines.
+ Define success criteria with the key stakeholders working on the migration.

## Getting started with your proof of concept
<a name="datasync-large-migration-poc-getting-started"></a>

1. Create your DataSync agent:

   1. [Deploy your agent](deploy-agents.md).

   1. [Choose a service endpoint](choose-service-endpoint.md) for your agent.

   1. [Activate your agent](activate-agent.md).

   1. [Verify your agent's network connections](test-agent-connections.md).

1. Select a small subset of data that represents the data that you're migrating.

   For example, if your source storage has a mix of large and small files, the subset of data you transfer in your POC should reflect that. This gives you a preliminary understanding of performance from the storage systems, your network, and DataSync.

1. Create a DataSync source location for your [on-premises](transferring-on-premises-storage.md) or [other cloud](transferring-other-cloud-storage.md) storage system.

1. Create a DataSync destination location for your [AWS storage service](transferring-aws-storage.md).

1. [Create a DataSync transfer task](create-task-how-to.md) with a [filter](filtering.md) that only transfers your data subset.

1. [Start your DataSync task](run-task.md).

1. Collect transfer performance metrics by monitoring the following:
   + Your task execution's data and file throughput. You can do this through the DataSync console or the [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html) operation. If you use `DescribeTaskExecution`, here's how you calculate these metrics:
     + **Data throughput**: Divide `BytesWritten` by `TransferDuration`
     + **File throughput**: Divide `FilesTransferred` by `TransferDuration`
   + Source and destination storage utilization. Work closely with your storage administrators to get this information.
   + Network usage.

1. Verify the transferred data at your destination location:
   + Review your CloudWatch logs for task execution errors.
   + Verify that permissions and metadata are preserved at the destination location.
   + Confirm that applications and users can access destination data as expected.
   + Address any issues that you encounter. For more information, see [Troubleshooting AWS DataSync issues](troubleshooting-datasync.md).

1. Run your task a few more times to get an idea how long it takes DataSync to prepare, transfer, and verify your data. (For more information, see [Task execution statuses](run-task.md#understand-task-execution-statuses).)

   If you run a task more than once, DataSync by default performs an incremental transfer and copies only the data that's changed from the previous task run.

   While the transfer time will likely be shorter for incremental transfers, DataSync will always prepare your transfer the same way by scanning and comparing your locations to identify what to transfer. You can use these preparation times to [estimate cutover timelines](datasync-large-migration-timelines.md#datasync-large-migration-cutover-timelines) for your migration.

1. If needed, update your migration plan based on what you learned during the POC.