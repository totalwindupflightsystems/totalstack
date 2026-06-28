---
id: "@specs/aws/datasync/docs/monitoring-task-manually"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitoring with manual tools"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Monitoring with manual tools

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/monitoring-task-manually
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitoring AWS DataSync with manual tools
<a name="monitoring-task-manually"></a>

You can track your AWS DataSync transfers from the console or the command line.

## Monitoring your transfer by using the DataSync console
<a name="monitoring-task-console"></a>

You can monitor your DataSync transfer by using the console, which provides real-time metrics such as data transferred, data and file throughput, and data compression.

**To monitor your transfer by using the DataSync console**

1. After you [start your DataSync task](run-task.md#starting-task), choose **See execution details**.

1. View metrics about your transfer.

## Monitoring your transfer by using the AWS CLI
<a name="monitor-task-execution"></a>

You can monitor your DataSync transfer by using the AWS Command Line Interface (AWS CLI). 

Copy the following `describe-task-execution` command. To use this example command, replace the `{{user input placeholders}}` with your own information. 

```
aws datasync describe-task-execution \
  --task-execution-arn 'arn:aws:datasync:{{region}}:{{account-id}}:task/{{task-id}}/execution/{{task-execution-id}}'
```

This command returns information about a task execution similar to that shown following.

```
{
    "BytesCompressed": 3500,
    "BytesTransferred": 5000,
    "BytesWritten": 5000,
    "EstimatedBytesToTransfer": 5000,
    "EstimatedFilesToDelete": 10,
    "EstimatedFilesToTransfer": 100,
    "FilesDeleted": 10,
    "FilesSkipped": 0,
    "FilesTransferred": 100,
    "FilesVerified": 100,
    "Result": {
        "ErrorCode": "??????",
        "ErrorDetail": "??????",
        "PrepareDuration": 100,
        "PrepareStatus": "SUCCESS",
        "TransferDuration": 60,
        "TransferStatus": "AVAILABLE",
        "VerifyDuration": 30,
        "VerifyStatus": "SUCCESS"
    },
    "StartTime": 1532660733.39,
    "Status": "SUCCESS",
    "OverrideOptions": {
        "Atime": "BEST_EFFORT",
        "BytesPerSecond": "1000",
        "Gid": "NONE",
        "Mtime": "PRESERVE",
        "PosixPermissions": "PRESERVE",
        "PreserveDevices": "NONE",
        "PreserveDeletedFiles": "PRESERVE",
        "Uid": "NONE",
        "VerifyMode": "POINT_IN_TIME_CONSISTENT"
    },
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:111222333444:task/task-aaaabbbbccccddddf/execution/exec-1234abcd1234abcd1",
    "TaskReportConfig": {
        "Destination": {
            "S3": {
                "BucketAccessRoleArn": "arn:aws:iam::111222333444:role/my-datasync-role",
                "S3BucketArn": "arn:aws:s3:::amzn-s3-demo-bucket/*",
                "Subdirectory": "reports"
            }
        },
        "ObjectVersionIds": "INCLUDE",
        "OutputType": "STANDARD",
        "Overrides": {
            "Deleted": {
                "ReportLevel": "ERRORS_ONLY"
            },
            "Skipped": {
                "ReportLevel": "SUCCESSES_AND_ERRORS"
            },
            "Transferred": {
                "ReportLevel": "ERRORS_ONLY"
            },
            "Verified": {
                "ReportLevel": "ERRORS_ONLY"
            }
        },
        "ReportLevel": "ERRORS_ONLY"
    }
}
```
+ If the task execution succeeds, the value of **Status** changes to **SUCCESS**. For information about what the response elements mean, see [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/apireference/API_DescribeTaskExecution.html).
+ If the task execution fails, the result sends error codes that can help you troubleshoot issues. For information about the error codes, see [TaskExecutionResultDetail](https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskExecutionResultDetail.html).

## Monitoring your transfer by using the `watch` utility
<a name="monitor-realtime"></a>

To monitor the progress of your task in real time from the command line, you can use the standard Unix `watch` utility. Task execution duration values are measured in milliseconds.

The `watch` utility doesn't recognize the DataSync alias. The following example shows how to invoke the CLI directly. To use this example command, replace the `{{user input placeholders}}` with your own information. 

```
# pass '-n 1' to update every second and '-d' to highlight differences 
        $ watch -n 1 -d \ "aws datasync describe-task-execution --task-execution-arn 'arn:aws:datasync:{{region}}:{{account-id}}:task/{{task-id}}/execution/task {{execution-id}}'"
```