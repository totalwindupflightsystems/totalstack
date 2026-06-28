---
id: "@specs/aws/datasync/docs/datasync-large-migration-timelines"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Estimating migration timelines"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Estimating migration timelines

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/datasync-large-migration-timelines
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Estimating migration timelines
<a name="datasync-large-migration-timelines"></a>

Using the information you've collected to this point, you can estimate how long the migration will take using AWS DataSync.

## Estimating data transfer timelines
<a name="datasync-large-migration-transfer-timelines"></a>

You can estimate how long it takes DataSync to transfer your data based on the following information you collected during migration requirements gathering and your DataSync proof of concept (POC):
+ Your [available network bandwidth](gathering-migration-requirements.md#datasync-migration-network-bandwidth)
+ Source and destination storage utilization metrics
+ Performance metrics from your [DataSync POC](datasync-large-migration-poc.md)

**To estimate a data transfer timeline**

1. Compare the data and file throughput from your POC with your available network bandwidth.

1. If your throughput is lower than your available bandwidth (such as 300 MiB/s for throughput with 10 Gbps of network bandwidth), consider partitioning your dataset into multiple tasks to maximize bandwidth usage.

   DataSync has a few options for partitioning your dataset. For more information, see [Accelerating your migration with data partitioning](datasync-large-migration-data-partitioning.md).

1. Calculate how many days a transfer takes by using the following formula, which provides a theoretical minimum transfer time:

   ```
   (DATA_SIZE * 8 bits per byte)/(CIRCUIT * NETWORK_UTILIZATION percentage * 3600 seconds per hour * AVAILABLE_HOURS) = Number of days
   ```

   When using this formula, replace the following with your own values:
   + `DATA_SIZE`: The amount of data that you're migrating (expressed in bytes).
   + `CIRCUIT`: Your available network bandwidth (expressed in bits per second).
   + `NETWORK_UTILIZATION`: What percent of your network is being used.
   + `AVAILABLE_HOURS`: The number of operational hours available in each day.

   For example, you would calculate a migration with 100 TB of data, a 1 Gbps internet connection, 80 percent network utilization, and 24 hours per day availability like this:

   `(100,000,000,000,000 bytes * 8) / (1,000,000,000 bps * 0.80 * 3600 * 24) = 11.57 days`

   In this case, the migration would take almost 12 days before accounting for real-world conditions.

1. Adjust your calculated transfer duration to account for real-world conditions:
   + Network performance fluctuations
   + Storage performance variations
   + Downtime between migration waves

## Estimating cutover timelines
<a name="datasync-large-migration-cutover-timelines"></a>

If you're migrating active datasets, you likely need cutovers so that you don't disrupt business operations.

Don't underestimate how long cutovers take. With large migrations, it's not uncommon for cutover activities to take up to 30 percent of your overall migration time.

1. Evaluate if you need to perform cutovers in waves to reduce the amount of data scanned for incremental changes.

   One strategy for doing this is cutting over datasets that you partition based on shares, folders, or storage systems.

1. Review how long it generally took DataSync to prepare, transfer, and verify your data during the POC.

   Note in particular the prepare durations of your task executions. To find this information, run the [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html) operation, then check the value of [PrepareDuration](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionResultDetail.html#DataSync-Type-TaskExecutionResultDetail-PrepareDuration) for the duration time (in milliseconds).

1. Estimate how long a cutover might take by measuring the time delta across parallel tasks.

   For more information on parallel tasks, see [Accelerating your migration with data partitioning](datasync-large-migration-data-partitioning.md).

1. Use your cutover estimation to schedule your cutovers. These essentially are maintenance windows when your source data can't be modified.

## Next steps
<a name="estimate-cutover-timelines-next-steps"></a>

After estimating your timelines, you're ready to start implementing your migration.