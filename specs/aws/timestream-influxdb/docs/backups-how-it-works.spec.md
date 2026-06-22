---
id: "@specs/aws/timestream-influxdb/docs/backups-how-it-works"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS How it works"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# How it works

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/backups-how-it-works
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Backing up and restoring Timestream tables: How it works
<a name="backups-how-it-works"></a>

You can create backups of your Amazon Timestream tables. This section provides an overview of what happens during the backup and restore process.

**Topics**
+ [Backups](#backups-backups)
+ [Restores](#backups-restores)

## Backups
<a name="backups-backups"></a>

You can use the on-demand backup feature to create full backups of your Amazon Timestream for LiveAnalytics tables. This section provides an overview of what happens during the backup and restore process.

You can create a backup of your Timestream data at a table granularity. You can initiate a backup of the selected table using either Timestream console, or AWS Backup console, SDK, or CLI. The backup is created asynchronously and all the data in the table until the backup initiation time is included in the backup. However, there is a possibility that some of the data ingested into the table while the backup is in progress might also be included in the backup. To protect your data, you can either create a one-time on-demand backup or schedule a recurring backup of your table.

While a backup is in progress, you cannot do the following.
+ Pause or cancel the backup operation.
+ Delete the source table of the backup.
+ Disable backups on a table if a backup for that table is in progress.

Once configured, AWS Backup provides automated backup schedules, retention management, and lifecycle management, removing the need for custom scripts and manual processes. For more information, see the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

All Timestream for LiveAnalytics backups are incremental in nature, implying that the first backup of a table is a full backup and every subsequent backup of the same table is an incremental backup, copying only the changes to the data since the last backup. As the data in Timestream for LiveAnalytics is stored in a collection of partitions, all the partitions that changed either due to ingesting new data or updates to the existing data since the last backup are copied during subsequent backups. 

If you are using Timestream for LiveAnalytics console, the backups created for all the resources in the account are listed in the **Backups** tab. Additionally, the backups are also listed in the **Table** details.

## Restores
<a name="backups-restores"></a>

You can restore a table from the Timestream for LiveAnalytics console, or AWS Backup console, SDK, or AWS CLI. You can either restore the entire data from your backup, or configure the table retention settings to restore select data. When you initiate a restore, you can configure the following table settings.
+ Database Name
+ Table Name
+ Memory store retention
+ Magnetic store retention
+ Enable Magnetic storage writes
+ S3 error logs location (optional)
+ IAM role that AWS Backup will assume when restoring the backup

The preceding configurations are independent of the source table. To restore all the data in your backup, we recommend that you configure the new table settings such that the sum of memory store retention period and magnetic store retention period is greater than the difference between the oldest timestamp and now. When you select a backup that is incremental to restore, all data (incremental \+ underlying full data) is restored. Upon successful restore, the table is in active state and you can perform ingestion and/or query operations on the restored table. However, you cannot perform these operations while the restore is in progress. Once restored, the table is similar to any other table in your account.

**Example Restore the all data from a backup**  
This example has the following assumptions.  

*Oldest timestamp*—`August 1, 2021 0:00:00`
+ *Now*—`November 9, 2022 0:00:00`
To restore all data from a backup, enter and compare values as follows.  

1. Enter **Memory store retention** and **Magnetic store retention**. For example, assume these values.
   + *Memory store retention*—12 hours
   + *Magnetic store retention*—500 days

1. Find the sum of **Memory store retention** and **Magnetic store retention**.

   ```
   12 hours + (500 * 24 hours) =
   12 hours + 12,000 hours =
   12,012 hours
   ```

1. Find the difference between **Oldest timestamp** and now.

   ```
   November 9, 2022 0:00:00 - August 1, 2021 0:00:00 =
   465 days =
   465 * 24 hours =
   11,160 hours
   ```

1. Ensure the sum of retention values in the second step is greater than difference of times in the third step. Adjust the retention times if necessary.

   ```
   12,012 > 11,160
   true
   ```

**Example Restore select data from a backup**  
This example has the following assumption.  
+ *Now*—`November 9, 2022 0:00:00`
To restore only select data from a backup, enter and compare values as follows.  

1. Determine the earliest timestamp required. For example, assume `December 4, 2021 0:00:00`.

1. Find the difference between the earliest timestamp required and now.

   ```
   November 9, 2022 0:00:00 - December 4, 2021 0:00:00 =
   340 days =
   340 * 24 hours =
   8,160 hours
   ```

1. Enter the desired value for **Memory store retention**. For example, enter 12 hours.

1. Subtract the value from the difference in the second step.

   ```
   8,160 hours - 12 hours =
   8148 hours
   ```

1. Enter that value for **Magnetic store retention**.

You can copy a backup of your Timestream for LiveAnalytics table data to a different AWS Region and then restore it in that new Region. You can copy and then restore backups between AWS commercial Regions, and AWS GovCloud (US) Regions. You pay only for the data you copy from the source Region and the data you restore to a new table in the destination Region.

Once the table is restored, you must manually set up the following on the restored table.
+ AWS Identity and Access Management (IAM) policies
+ Tags
+ Scheduled Queries

Restore times are directly related to the configuration of your tables. These include the size of your tables, the number of underlying partitions, the amount of data restored to memory store, and other variables. A best practice when planning for disaster recovery is to regularly document average restore completion times and establish how these times affect your overall Recovery Time Objective (RTO).

All backup and restore console and API actions are captured and recorded in AWS CloudTrail for logging, continuous monitoring, and auditing.