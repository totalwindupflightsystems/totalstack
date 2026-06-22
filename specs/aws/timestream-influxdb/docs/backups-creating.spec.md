---
id: "@specs/aws/timestream-influxdb/docs/backups-creating"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating backups"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Creating backups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/backups-creating
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Creating backups of Amazon Timestream tables
<a name="backups-creating"></a>

This section describes how to enable AWS Backup and create on-demand and scheduled backups for Amazon Timestream.

**Topics**
+ [Enabling AWS Backup to protect Timestream for LiveAnalytics data](#backups-enabling)
+ [Creating on-demand backups](#backups-on-demand)
+ [Scheduled backups](#backups-scheduled)

## Enabling AWS Backup to protect Timestream for LiveAnalytics data
<a name="backups-enabling"></a>

You must enable AWS Backup to use it with Timestream for LiveAnalytics.

To enable AWS Backup in the Timestream for LiveAnalytics console, perform the following steps.

1.  Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream). 

1. A pop-up banner appears at the top of your Timestream for LiveAnalytics dashboard page to enable AWS Backup to support Timestream for LiveAnalytics data. Otherwise, from the navigation pane, choose **Backups**.

1. In the **Backup** window, you will see the banner to enable AWS Backup. Choose **Enable**.

   Data Protection through AWS Backup is now available for your Timestream for LiveAnalytics tables.

To enable through AWS Backup, refer to AWS Backup documentation to enable via console and programmatically.

If you choose to disable AWS Backup from protection your Timestream for LiveAnalytics data after those have been enabled, log in through AWS Backup console and move the toggle to the left.

 If you can’t enable or disable the AWS Backup features, your AWS admin may need to perform those actions.

## Creating on-demand backups
<a name="backups-on-demand"></a>

To create an on-demand backup of a Timestream for LiveAnalytics table, follow these steps.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. Choose **Create on-demand backup**.

1. Continue to select the settings in the backup window.

1. You can either create a backup now, initiates a backup immediately, or select a backup window to start the backup.

1. Select the lifecycle management policy of your backup. You can transition your backup data into cold storage where you have to retain the backup for a minimum of 90 days. You can set the required retention period for your backup You can either select an existing vault or or select **create new backup vault** to navigate to AWS Backup console and create a new backup vault <documentation link on creating a new backup vault here>

1. Select the appropriate IAM role.

1. If you want to assign one or more tags to your on-demand backup, enter a **key** and optional **value**, and choose **Add tag**.

1. Choose to create an on-demand backup. This takes you to the **Backup** page, where you will see a list of jobs.

1. Choose the **Backup job ID** for the resource that you chose to back up to see the details of that job.

## Scheduled backups
<a name="backups-scheduled"></a>

To schedule a backup, refer to [Create a scheduled backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-a-scheduled-backup.html).