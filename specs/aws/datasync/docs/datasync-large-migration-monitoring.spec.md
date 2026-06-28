---
id: "@specs/aws/datasync/docs/datasync-large-migration-monitoring"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitoring your transfers"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Monitoring your transfers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/datasync-large-migration-monitoring
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitoring your transfers
<a name="datasync-large-migration-monitoring"></a>

AWS DataSync provides several monitoring options to help you validate and debug your transfer.

## Monitoring your transfers with CloudWatch metrics
<a name="datasync-migration-monitoring-cloudwatch-metrics"></a>

You can create custom CloudWatch dashboards with metrics from your DataSync task executions. For more information, see [Monitoring data transfers with Amazon CloudWatch metrics](monitor-datasync.md).

## Monitoring your transfers with task reports
<a name="datasync-migration-monitoring-task-reports"></a>

If you’re transferring millions of files or objects, considering using task reports. Task reports provide detailed information about what DataSync attempts to transfer, skip, verify, and delete during a task execution. For more information, see [Monitoring your data transfers with task reports](task-reports.md).

You can also visualize your task reports by using AWS services such as AWS Glue, Amazon Athena, and Amazon Quick. For more information, see the [AWS Storage Blog](https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/).

## Monitoring your transfers with CloudWatch Logs
<a name="datasync-migration-monitoring-cloudwatch-logs"></a>

At minimum, we recommend that you configure your task to log basic information and transfer errors. For more information, see [Monitoring data transfers with Amazon CloudWatch Logs](configure-logging.md).