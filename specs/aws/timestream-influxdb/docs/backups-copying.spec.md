---
id: "@specs/aws/timestream-influxdb/docs/backups-copying"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Copying backups"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Copying backups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/backups-copying
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Copying a backup of a Amazon Timestream table
<a name="backups-copying"></a>

You can make a copy of a current backup. You can copy backups to multiple AWS accounts or AWS Regions on demand or automatically as part of a scheduled backup plan. Cross-Region replication is especially valuable if you have business continuity or compliance requirements to store backups a minimum distance away from your production data.

Cross-account backups are useful for securely copying your backups to one or more AWS accounts in your organization for operational or security reasons. If your original backup is inadvertently deleted, you can copy the backup from its destination account to its source account, and then start the restore. Before you can do this, you must have two accounts that belong to the same organization in the Organizations service and required permissions for the accounts. When you copy an incremental backup into another account or Region, the associated full backup is also copied.

Copies inherit the source backup's configuration unless you specify otherwise. There is one exception. If you specify your new copy to "Never" expire. With this setting, the new copy still inherits its source expiration date. If you want your new backup copy to be permanent, either set your source backups to never expire, or specify your new copy to expire 100 years after its creation.

To copy a backup from Timestream console, follow these steps.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. Choose the radio button next to the recovery point ID of the resource. In the upper-right corner of the pane, select **Actions** and choose **Copy**.

1. Select **Continue to AWS Backup** and follow the steps for [Cross account backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html).

Copying on-demand and scheduled backups across accounts and Regions is not natively supported in the Timestream for LiveAnalytics console currently and you have to navigate to AWS Backup to perform the operation. 