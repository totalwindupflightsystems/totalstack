---
id: "@specs/aws/datasync/docs/tagging-tasks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tagging your tasks"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Tagging your tasks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/tagging-tasks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tagging your AWS DataSync tasks
<a name="tagging-tasks"></a>

*Tags* are key-value pairs that help you manage, filter, and search for your AWS DataSync resources. You can add up to 50 tags to each DataSync task and task execution.

For example, you might create a task for a large data migration and tag the task with the key **Project** and value **Large Migration**. To further organize the migration, you could tag one run of the task with the key **Transfer Date** and value **May 2021** (subsequent task executions might be tagged **June 2021**, **July 2021**, and so on).

## Tagging your DataSync task
<a name="tagging-tasks-console"></a>

You can tag your DataSync task only when creating the task.

### Using the DataSync console
<a name="tagging-tasks-console-steps"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. On the **Configure settings** page, choose **Add new tag** to tag your task.

### Using the AWS CLI
<a name="tagging-tasks-cli-steps"></a>

1. Copy the following `create-task` command:

   ```
   aws datasync create-task \
       --source-location-arn 'arn:aws:datasync:{{region}}:{{account-id}}:location/{{source-location-id}}' \
       --destination-location-arn 'arn:aws:datasync:{{region}}:{{account-id}}:location/{{destination-location-id}}' \
       --tags Key={{tag-key}},Value={{tag-value}}
   ```

1. Specify the following parameters in the command:
   + `--source-location-arn` – Specify the Amazon Resource Name (ARN) of the source location in your transfer.
   + `--destination-location-arn` – Specify the ARN of the destination location in your transfer.
   + `--tags` – Specify the tags that you want to apply to the task.

     For more than one tag, separate each key-value pair with a space.

1. (Optional) Specify other parameters that make sense for your transfer scenario.

   For a list of `--options`, see the [create-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html) command.

1. Run the `create-task` command.

   You get a response that shows the task that you just created.

   ```
   {
       "TaskArn": "arn:aws:datasync:us-east-2:123456789012:task/task-abcdef01234567890"
   }
   ```

To view the tags you added to this task, you can use the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-tags-for-resource.html) command.

## Tagging your DataSync task execution
<a name="tagging-task-executions-console"></a>

You can tag each run of your DataSync task.

If your task already has tags, remember the following about using tags with task executions:
+ If you start your task with the console, its user-created tags are applied automatically to the task execution. However, system-created tags that begin with `aws:` are not applied.
+ If you start your task with the DataSync API or AWS CLI, its tags are not applied automatically to the task execution.

### Using the DataSync console
<a name="tagging-task-executions-console"></a>

To add, edit, or remove tags from a task execution, you must start the task with overriding options.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**.

1. Choose the task.

1. Choose **Start**, then choose one of the following options: 
   + **Start with defaults** – Applies any tags associated with your task.
   + **Start with overriding options** – Allows you to add, edit, or remove tags for this particular task execution.

### Using the AWS CLI
<a name="tagging-task-executions-cli"></a>

1. Copy the following `start-task-execution` command:

   ```
   aws datasync start-task-execution \
       --task-arn 'arn:aws:datasync:{{region}}:{{account-id}}:task/{{task-id}}' \
       --tags Key={{tag-key}},Value={{tag-value}}
   ```

1. Specify the following parameters in the command:
   + `--task-arn` – Specify the ARN of the task that you want to start.
   + `--tags` – Specify the tags that you want to apply to this specific run of the task.

     For more than one tag, separate each key-value pair with a space.

1. (Optional) Specify other parameters that make sense for your situation.

   For more information, see the [start-task-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/start-task-execution.html) command.

1. Run the `start-task-execution` command.

   You get a response that shows the task execution that you just started.

   ```
   {
       "TaskExecutionArn": "arn:aws:datasync:us-east-2:123456789012:task/task-abcdef01234567890"
   }
   ```

To view the tags you added to this task, you can use the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-tags-for-resource.html) command.