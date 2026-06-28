---
id: "@specs/aws/datasync/docs/task-scheduling"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scheduling your task"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Scheduling your task

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/task-scheduling
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Scheduling when your AWS DataSync task runs
<a name="task-scheduling"></a>

You can set up an AWS DataSync task schedule to periodically transfer data between storage locations.

## How DataSync task scheduling works
<a name="how-task-scheduling-works"></a>

A scheduled DataSync task runs at a frequency that you specify, with a minimum interval of 1 hour. You can create a task schedule by using a cron or rate expressions.

**Important**  
You can't schedule a task to run at an interval faster than 1 hour.

**Using cron expressions**  
Use cron expressions for task schedules that run on a specific time and day. For example, here's how you can configure a task schedule in the AWS CLI that runs at 12:00 PM UTC every Sunday and Wednesday.  

```
cron(0 12 ? * SUN,WED *)
```

**Using rate expressions**  
Use rate expressions for task schedules that run on a regular interval, such as every 12 hours. For example, here's how you can configure a task schedule in the AWS CLI that runs every 12 hours:  

```
rate(12 hours)
```

**Tip**  
For more information about cron and rate expression syntax, see the [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html).

## Creating a DataSync task schedule
<a name="configure-task-schedule"></a>

You can schedule how frequently your task runs by using the DataSync console, AWS CLI, or DataSync API.

### Using the DataSync console
<a name="configure-task-schedule-console"></a>

The following instructions describe how to set up a schedule when creating a task. You can modify the schedule later when editing the task.

In the console, some scheduling options let you specify the exact time that your task runs (such as daily at 10:30 PM). If you don't include a time for these options, your task runs at the time that you create (or update) the task.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For schedule **Frequency**, do one of the following:
   + Choose **Not scheduled** if you don't want your task to run on a schedule.
   + Choose **Hourly**, then choose the minute during the hour that you want your task to run. 
   + Choose **Daily** and enter the UTC time that you want your task to run.
   + Choose **Weekly** and the day of the week and enter the UTC time that you want the task to run.
   + Choose **Days of the week**, choose a specific day or days, and enter the UTC time that the task should run in the format HH:MM.
   + Choose **Custom**, and then select **Cron expression** or **Rate expression**. Enter your task schedule with a minimum interval of 1 hour. 

### Using the AWS CLI
<a name="configure-task-schedule-api"></a>

You can create a schedule for your DataSync task by using the `--schedule` parameter with the `create-task`, `update-task`, or `start-task-execution` command.

The following instructions describe how to do this with the `create-task` command.

1. Copy the following `create-task` command:

   ```
   aws datasync create-task \
     --source-location-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:location/loc-{{12345678abcdefgh}} \
     --destination-location-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:location/loc-{{abcdefgh12345678}} \
     --schedule '{
       "ScheduleExpression": "{{cron(0 12 ? * SUN,WED *)}}"
     }'
   ```

1. For the `--source-location-arn` parameter, specify the Amazon Resource Name (ARN) of the location that you're transferring data from.

1. For the `--destination-location-arn` parameter, specify the ARN of the location that you're transferring data to.

1. For the `--schedule` parameter, specify a cron or rate expression for your schedule.

   In the example, the cron expression `{{cron(0 12 ? * SUN,WED *)}}` sets a task schedule that runs at 12:00 PM UTC every Sunday and Wednesday.

1. Run the `create-task` command to create your task with the schedule.

## Pausing a DataSync task schedule
<a name="pause-task-schedule"></a>

There can be situations where you need to pause your DataSync task schedule. For example, you might need to temporarily disable a recurring transfer to fix an issue with your task or perform maintenance on your storage system.

DataSync might disable your task schedule automatically for the following reasons:
+ Your task fails repeatedly with the same error.
+ You [disable an AWS Region](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) that your task is using.

### Using the DataSync console
<a name="pause-scheduled-task-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, and then choose **Tasks**.

1. Choose the task that you want to pause the schedule for, and then choose **Edit**.

1. For **Schedule**, turn off **Enable schedule**. Choose **Save changes**.

### Using the AWS CLI
<a name="pause-scheduled-task-cli"></a>

1. Copy the following `update-task` command:

   ```
   aws datasync update-task \
     --task-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:task/task-{{12345678abcdefgh}} \
     --schedule '{
       "ScheduleExpression": "{{cron(0 12 ? * SUN,WED *)}}",
       "Status": "DISABLED"
     }'
   ```

1. For the `--task-arn` parameter, specify the ARN of the task that you want to pause the schedule for.

1. For the `--schedule` parameter, do the following:
   + For `ScheduleExpression`, specify a cron or rate expression for your schedule.

     In the example, the expression `{{cron(0 12 ? * SUN,WED *)}}` sets a task schedule that runs at 12:00 PM UTC every Sunday and Wednesday.
   + For `Status`, specify `DISABLED` to pause the task schedule.

1. Run the `update-task` command.

1. To resume the schedule, run the same `update-task` command with `Status` set to `ENABLED`.

## Checking the status of a DataSync task schedule
<a name="check-scheduled-task"></a>

You can see whether your DataSync task schedule is enabled. 

### Using the DataSync console
<a name="check-scheduled-task-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, and then choose **Tasks**.

1. In the **Schedule** column, check whether the task's schedule is enabled or disabled.

### Using the AWS CLI
<a name="check-scheduled-task-cli"></a>

1. Copy the following `describe-task` command:

   ```
   aws datasync describe-task \
     --task-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:task/task-{{12345678abcdefgh}}
   ```

1. For the `--task-arn` parameter, specify the ARN of the task that you want information about.

1. Run the `describe-task` command.

You get a response that provides details about your task, including its schedule. (The following example focuses primarily on the task schedule configuration and doesn't show a full `describe-task` response.)

The example shows that the task's schedule is manually disabled. If the schedule is disabled by the DataSync `SERVICE`, you see an error message for `DisabledReason` to help you understand why the task keeps failing. For more information, see [Troubleshooting AWS DataSync issues](troubleshooting-datasync.md).

```
{
    "TaskArn": "arn:aws:datasync:us-east-1:123456789012:task/task-12345678abcdefgh",
    "Status": "AVAILABLE",
    "Schedule": {
        "ScheduleExpression": "cron(0 12 ? * SUN,WED *)",
        "Status": "DISABLED",
        "StatusUpdateTime": 1697736000,
        "DisabledBy": "USER",
        "DisabledReason": "Manually disabled by user."
    },
    ...
}
```