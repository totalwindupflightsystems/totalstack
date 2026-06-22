---
id: "@specs/aws/timestream-influxdb/docs/backups-deleting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Deleting backups"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Deleting backups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/backups-deleting
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Deleting backups
<a name="backups-deleting"></a>

This section describes how to delete a backup of a Timestream for LiveAnalytics table.

To delete a backup from Timestream console, follow these steps.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. Choose the radio button next to the recovery point ID of the resource. In the upper-right corner of the pane, select **Actions** and choose **Delete**.

1. Select **Continue to AWS Backup** and follow the steps for deleting backups at [Deleting backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html).

**Note**  
When you delete a backup that is incremental, only the incremental backup is deleted and the underlying full backup is not deleted.