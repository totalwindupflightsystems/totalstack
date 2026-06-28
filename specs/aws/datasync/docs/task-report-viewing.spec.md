---
id: "@specs/aws/datasync/docs/task-report-viewing"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Viewing your task reports"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Viewing your task reports

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/task-report-viewing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Viewing your DataSync task reports
<a name="task-report-viewing"></a>

DataSync creates task reports for every task execution. When your execution completes, you can find the related task reports in your S3 bucket. Task reports are organized under prefixes that include the IDs of your tasks and their executions.

To help locate task reports in your S3 bucket, use these examples:
+ **Summary only task report** – `{{reports-prefix}}/Summary-Reports/{{task-id-folder}}/{{task-execution-id-folder}}`
+ **Standard task report** – `{{reports-prefix}}/Detailed-Reports/{{task-id-folder}}/{{task-execution-id-folder}}`

Because task reports are in JSON format, you have several options for viewing your reports:
+ View a report by using [Amazon S3 Select](https://docs.aws.amazon.com/AmazonS3/latest/userguide/selecting-content-from-objects.html).
+ Visualize reports by using AWS services such as AWS Glue, Amazon Athena, and Amazon Quick. For more information about visualizing your task reports, see the [AWS Storage Blog](https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/).