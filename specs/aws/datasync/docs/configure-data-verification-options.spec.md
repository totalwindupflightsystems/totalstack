---
id: "@specs/aws/datasync/docs/configure-data-verification-options"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Verifying data integrity"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Verifying data integrity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/configure-data-verification-options
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring how AWS DataSync verifies data integrity
<a name="configure-data-verification-options"></a>

During a transfer, AWS DataSync uses checksum verification to verify the integrity of the data that you copy between locations. You also can configure DataSync to perform additional verification at the end of your transfer.

## Data verification options
<a name="data-verification-options"></a>

Use the following information to help you decide if and how you want DataSync to perform these additional checks.


| Console option | API option | Description | 
| --- | --- | --- | 
| **Verify only transferred data** (recommended) | [VerifyMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-VerifyMode) set to `ONLY_FILES_TRANSFERRED` | DataSync calculates the checksum of transferred data (including metadata) at the source location. At the end of your transfer, DataSync compares this checksum to the checksum calculated on that same data at the destination.<br />We recommend this option when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see [Storage class considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes). | 
| **Verify all data** | [VerifyMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-VerifyMode) set to `POINT_IN_TIME_CONSISTENT` | At the end of your transfer, DataSync checks the entire source and destination to verify that both locations are fully synchronized.  Not supported when your task uses [Enhanced mode](choosing-task-mode.md). <br />If you use a [manifest](transferring-with-manifest.md), DataSync only scans and verifies what's listed in the manifest.<br />You can't use this option when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see [Storage class considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes).  | 
| Don't verify data after transfer | [VerifyMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-VerifyMode) set to `NONE` | DataSync performs data integrity checks only during your transfer. Unlike other options, there's no additional verification at the end of your transfer. | 

## Configuring data verification
<a name="configure-data-verification"></a>

You can configure data verification options when creating a task, updating a task, or starting a task execution.

### Using the DataSync console
<a name="configure-data-verification-options-console"></a>

The following instructions describe how to configure data verification options when creating a task.

**To configure data verification by using the console**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For **Verification**, choose one of the following:
   + **Verify only transferred data** (recommended)
   + **Verify all data**
   + **Don't verify data after transfer**

### Using the DataSync API
<a name="configure-data-verification-options-api"></a>

You can configure how DataSync verifies data by using the `VerifyMode` parameter with any of the following operations:
+ [CreateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html)
+ [UpdateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html)
+ [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html)