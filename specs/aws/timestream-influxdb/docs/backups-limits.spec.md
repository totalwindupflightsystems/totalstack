---
id: "@specs/aws/timestream-influxdb/docs/backups-limits"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Quotas and limits"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Quotas and limits

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/backups-limits
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Quota and limits
<a name="backups-limits"></a>

AWS Backup limits the backups to one concurrent backup per resource. Therefore, additional scheduled or on-demand backup requests for the resource are queued and will start only after the existing backup job is completed. If the backup job is not started or completed within the backup window, the request fails. For more information about AWS Backup limits, see [AWS Backup Limits](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-limits.html) in the AWS Backup Developer Guide.

When creating a backup, you can execute up to four concurrent backups per account. Similarly, you can execute one concurrent restore per account. When you initiate more than four backup jobs simultaneously, only four backup jobs are initiated and the remaining jobs will be periodically retried. Once initiated, if the backup job is not completed within the configured backup window duration, the backup job fails. If the failed backup job is an on-demand backup, you can retry the backup and for scheduled backups, the job is attempted in the following schedule.