---
id: "@specs/aws/datasync/docs/datasync-large-migration-data-partitioning"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Accelerating your migration with partitioning"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Accelerating your migration with partitioning

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/datasync-large-migration-data-partitioning
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Accelerating your migration with data partitioning
<a name="datasync-large-migration-data-partitioning"></a>

With a large migration, we recommend partitioning your dataset with multiple DataSync tasks. Partitioning your source data across multiple tasks (and possibly agents) lets you parallelize your transfers and reduce the migration timeline.

Partitioning also helps you stay within DataSync [quotas](datasync-limits.md) and simplifies the monitoring and debugging of your tasks. 

The following diagram shows how you might use multiple DataSync tasks and agents to transfer data from the same source storage location. In this scenario, each task focuses on a specific folder in the source location. For more information and examples on these approaches, see [How to accelerate your data transfers with AWS DataSync scale out architectures](https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/).

![A diagram that shows one approach with DataSync for partitioning your source data to help accelerate a large migration.](http://docs.aws.amazon.com/datasync/latest/userguide/images/datasync-partition-by-folder.png)


## Partitioning your dataset by folder or prefix
<a name="configure-task-by-folder"></a>

When creating your DataSync source location, you can specify a folder, directory, or prefix that DataSync reads from. For example, if you're migrating a file share with top-level directories, you can create multiple locations that specify a different directory path. You can then use these locations to run multiple DataSync tasks during your migration.

## Partitioning your dataset with filters
<a name="configure-task-with-filters"></a>

You can apply [filters](filtering.md) to include or exclude data from your source location in a transfer. In the context of a large migration, filters can help you scope tasks to specific portions of your dataset.

For example, if you’re migrating archive data that’s organized by year, you can create an include filter to match for a specific year or multiple years. You also can modify the filter each time you run the task to match a different year.

## Partitioning your dataset with manifests
<a name="configure-task-with-manifest"></a>

A [manifest](transferring-with-manifest.md) is a list of files or objects that you want DataSync to transfer. With a manifest, DataSync doesn't have to read everything in a source location to determine what to transfer.

You can create manifests from inventories of your source storage or through event-driven approaches (for example, see [Implementing AWS DataSync with hundreds of millions of objects](https://aws.amazon.com/blogs/storage/implementing-aws-datasync-with-hundreds-of-millions-of-objects/)). You can also use a different manifest each time you start a task, allowing you to transfer different sets of data with the same task.