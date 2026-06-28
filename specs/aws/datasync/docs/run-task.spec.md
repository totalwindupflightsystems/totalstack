---
id: "@specs/aws/datasync/docs/run-task"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Starting a task to transfer data"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Starting a task to transfer data

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/run-task
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Starting a task to transfer your data
<a name="run-task"></a>

Once you create your AWS DataSync transfer task, you can start moving data. Each run of a task is called a *task execution*. For information about what happens during a task execution, see [How DataSync transfers files, objects, and directories](how-datasync-transfer-works.md#transferring-files).

**Important**  
If you're planning to transfer data to or from an Amazon S3 location, review [how DataSync can affect your S3 request charges](create-s3-location.md#create-s3-location-s3-requests) and the [DataSync pricing page](https://aws.amazon.com/datasync/pricing/) before you begin.

## Starting your task
<a name="starting-task"></a>

Once you've created your task, you can begin moving data right away.

### Using the DataSync console
<a name="starting-task-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**.

1. Choose the task that you want to run.

   Make sure that the task has an **Available** status. You also can select multiple tasks.

1. Choose **Actions** and then choose one of the following options:
   + **Start** – Runs the task (or tasks if you selected more than one).
   + **Start with overriding options** – Allows you to modify some of your task settings before you begin moving data. When you're ready, choose **Start**.

1. Choose **See execution details** to view details about the running task execution.

### Using the AWS CLI
<a name="start-task-execution"></a>

To start your DataSync task, you just need to specify the Amazon Resource Name (ARN) of the task you want to run. Here's an example `start-task-execution` command:

```
aws datasync start-task-execution \
    --task-arn 'arn:aws:datasync:{{region}}:{{account-id}}:task/{{task-id}}'
```

The following example starts a task with a few settings that are different than the task's default settings:

```
aws datasync start-task-execution \
    --override-options VerifyMode=NONE,OverwriteMode=NEVER,PosixPermissions=NONE
```

The command returns an ARN for your task execution similar to the following example:

```
{ 
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:209870788375:task/task-08de6e6697796f026/execution/exec-04ce9d516d69bd52f"
}
```

**Note**  
Each agent can run a single task at a time.

### Using the DataSync API
<a name="starting-task-api"></a>

You can start your task by using the [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html) operation. Use the [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html) operation to get details about the running task execution.

Once started, you can [check the task execution's status](#understand-task-execution-statuses) as DataSync copies your data. You also can [throttle the task execution's bandwidth](configure-bandwidth.md#adjust-bandwidth-throttling) if needed.

## Task execution statuses
<a name="understand-task-execution-statuses"></a>

When you start a DataSync task, you might see these statuses. ([Task statuses](create-task-how-to.md#understand-task-creation-statuses) are different than task execution statuses.)


| Console status | API status | Description | 
| --- | --- | --- | 
| Queueing | `QUEUED` | Another task execution is running and using the same DataSync agent. For more information, see [Knowing when your task is queued](#queue-task-execution). | 
| Launching | `LAUNCHING` | DataSync is initializing the task execution. This status usually goes quickly but can take up to a few minutes. | 
| Launched | `LAUNCHED` | DataSync has launched the task execution. | 
| Preparing | `PREPARING` | DataSync is determining what data to transfer.<br />Preparation can take just minutes, a few hours, or even longer depending on the number of files, objects, or directories in both locations and how you configure your task. How preparation works also depends on your task mode. For more information, see [How DataSync prepares your data transfer](how-datasync-transfer-works.md#how-datasync-prepares). | 
| Transferring | `TRANSFERRING` | DataSync is performing the actual data transfer. | 
| Verifying | `VERIFYING` | DataSync is verifying the integrity of your data at the end of the transfer. | 
| Success | `SUCCESS` | The task execution succeeded. | 
| Cancelling | `CANCELLING` | The task execution is in the process of being cancelled. | 
| Error | `ERROR` | The task execution failed. | 

## Knowing when your task is queued
<a name="queue-task-execution"></a>

When running multiple tasks (for example, you're [transferring a large dataset](create-task-how-to.md#multiple-tasks-large-dataset)), DataSync might queue the tasks to run in a series (first in, first out). Some examples of when this happens include:
+ You run different tasks that use the same DataSync agent. While you can use the same agent for multiple tasks, an agent can only run one task at a time.
+ A task execution is in progress and you start additional executions of the same task using different [filters](filtering.md) or [manifests](transferring-with-manifest.md).

In each example, the queued tasks don't start until the task ahead of them finishes.

## Cancelling your task execution
<a name="cancel-running-task"></a>

 You can stop any running or queued DataSync task execution. 

**To cancel a task execution by using the console**

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**.

1. Select the **Task ID** for the running task that you want to monitor.

   The task status should be **Running**.

1. Choose **History** to view the task's executions.

1. Select the task execution that you want to stop, and then choose **Stop**.

1. In the dialog box, choose **Stop**.

To cancel a running or queued task by using the DataSync API, see [CancelTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_CancelTaskExecution.html).

### Automated cancellation of stuck tasks
<a name="auto-cancel-stuck-tasks"></a>

At times a running DataSync task execution can become stuck. 