---
id: "@specs/aws/datasync/docs/configure-bandwidth"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Setting bandwidth limits"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Setting bandwidth limits

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/configure-bandwidth
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Setting bandwidth limits for your AWS DataSync task
<a name="configure-bandwidth"></a>

You can configure network bandwidth limits for your AWS DataSync task and each of its executions.

## Limiting bandwidth for a task
<a name="configure-bandwidth-create"></a>

Set a bandwidth limit when creating, editing, or starting a task.

### Using the DataSync console
<a name="configure-bandwidth-create-console"></a>

The following instructions describe how to configure a bandwidth limit for your task when you're creating it.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For **Bandwidth limit**, choose one of the following:
   + Select **Use available** to use all of the available network bandwidth for each task execution.
   + Select **Set bandwidth limit (MiB/s)** and enter the maximum bandwidth that you want DataSync to use for each task execution.

### Using the DataSync API
<a name="configure-bandwidth-create-api"></a>

You can configure a task's bandwidth limit by using the `BytesPerSecond` parameter with any of the following operations:
+ [CreateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html)
+ [UpdateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html)
+ [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html)

## Throttling bandwidth for a task execution
<a name="adjust-bandwidth-throttling"></a>

You can modify the bandwidth limit for a running or queued task execution.

### Using the DataSync console
<a name="adjust-bandwidth-throttling-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the navigation pane, expand **Data transfer**. then choose **Tasks**.

1. Choose the task and then select **History** to view the task's executions.

1. Choose the task execution that you want to modify and then choose **Edit**.

1. In the dialog box, choose one of the following:
   + Select **Use available** to use all of the available network bandwidth for the task execution.
   + Select **Set bandwidth limit (MiB/s)** and enter the maximum bandwidth that you want DataSync to use for the task execution.

1. Choose **Save changes**.

   The new bandwidth limit takes effect within 60 seconds.

### Using the DataSync API
<a name="adjust-bandwidth-throttling-api"></a>

You can modify the bandwidth limit for a running or queued task execution by using the `BytesPerSecond` parameter with the [UpdateTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTaskExecution.html) operation.