---
id: "@specs/aws/lambda/docs/with-eventbridge-scheduler"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Invoke using an EventBridge Scheduler"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Invoke using an EventBridge Scheduler

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-eventbridge-scheduler
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Invoke a Lambda function on a schedule
<a name="with-eventbridge-scheduler"></a>

[Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html) is a serverless scheduler that allows you to create, run, and manage tasks from one central, managed service. With EventBridge Scheduler, you can create schedules using cron and rate expressions for recurring patterns, or configure one-time invocations. You can set up flexible time windows for delivery, define retry limits, and set the maximum retention time for unprocessed events.

When you set up EventBridge Scheduler with Lambda, EventBridge Scheduler invokes your Lambda function asynchronously. This page explains how to use EventBridge Scheduler to invoke a Lambda function on a schedule.

## Set up the execution role
<a name="using-eventbridge-scheduler-execution-role"></a>

 When you create a new schedule, EventBridge Scheduler must have permission to invoke its target API operation on your behalf. You grant these permissions to EventBridge Scheduler using an *execution role*. The permission policy you attach to your schedule's execution role defines the required permissions. These permissions depend on the target API you want EventBridge Scheduler to invoke.

 When you use the EventBridge Scheduler console to create a schedule, as in the following procedure, EventBridge Scheduler automatically sets up an execution role based on your selected target. If you want to create a schedule using one of the EventBridge Scheduler SDKs, the AWS CLI, or CloudFormation, you must have an existing execution role that grants the permissions EventBridge Scheduler requires to invoke a target. For more information about manually setting up an execution role for your schedule, see [Setting up an execution role](https://docs.aws.amazon.com/scheduler/latest/UserGuide/setting-up.html#setting-up-execution-role) in the *EventBridge Scheduler User Guide*. 

## Create a schedule
<a name="using-eventbridge-scheduler-create"></a>

**To create a schedule by using the console**

1. Open the Amazon EventBridge Scheduler console at [https://console.aws.amazon.com/scheduler/home](https://console.aws.amazon.com/scheduler/home/).

1.  On the **Schedules** page, choose **Create schedule**. 

1.  On the **Specify schedule detail** page, in the **Schedule name and description** section, do the following: 

   1. For **Schedule name**, enter a name for your schedule. For example, **MyTestSchedule**. 

   1. (Optional) For **Description**, enter a description for your schedule. For example, **My first schedule**.

   1. For **Schedule group**, choose a schedule group from the dropdown list. If you don't have a group, choose **default**. To create a schedule group, choose **create your own schedule**. 

      You use schedule groups to add tags to groups of schedules. 

1. 

   1. Choose your schedule options.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html)

1. (Optional) If you chose **Recurring schedule** in the previous step, in the **Timeframe** section, do the following: 

   1. For **Timezone**, choose a timezone. 

   1. For **Start date and time**, enter a valid date in `YYYY/MM/DD` format, and then specify a timestamp in 24-hour `hh:mm` format. 

   1. For **End date and time**, enter a valid date in `YYYY/MM/DD` format, and then specify a timestamp in 24-hour `hh:mm` format. 

1. Choose **Next**. 

1. On the **Select target** page, choose the AWS API operation that EventBridge Scheduler invokes: 

   1. Choose **AWS Lambda Invoke**.

   1. In the **Invoke** section, select a function or choose **Create new Lambda function**.

   1. (Optional) Enter a JSON payload. If you don't enter a payload, EventBridge Scheduler uses an empty event to invoke the function.

1. Choose **Next**. 

1. On the **Settings** page, do the following: 

   1. To turn on the schedule, under **Schedule state**, toggle **Enable schedule**. 

   1. To configure a retry policy for your schedule, under **Retry policy and dead-letter queue (DLQ)**, do the following:
      + Toggle **Retry**.
      + For **Maximum age of event**, enter the maximum **hour(s)** and **min(s)** that EventBridge Scheduler must keep an unprocessed event.
      + The maximum time is 24 hours.
      + For **Maximum retries**, enter the maximum number of times EventBridge Scheduler retries the schedule if the target returns an error. 

         The maximum value is 185 retries. 

      With retry policies, if a schedule fails to invoke its target, EventBridge Scheduler re-runs the schedule. If configured, you must set the maximum retention time and retries for the schedule.

   1. Choose where EventBridge Scheduler stores undelivered events.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html)

   1. To use a customer managed key to encrypt your target input, under **Encryption**, choose **Customize encryption settings (advanced)**. 

      If you choose this option, enter an existing KMS key ARN or choose **Create an AWS KMS key** to navigate to the AWS KMS console. For more information about how EventBridge Scheduler encrypts your data at rest, see [Encryption at rest](https://docs.aws.amazon.com/scheduler/latest/UserGuide/encryption-rest.html) in the *Amazon EventBridge Scheduler User Guide*. 

   1. To have EventBridge Scheduler create a new execution role for you, choose **Create new role for this schedule**. Then, enter a name for **Role name**. If you choose this option, EventBridge Scheduler attaches the required permissions necessary for your templated target to the role.

1. Choose **Next**. 

1.  In the **Review and create schedule** page, review the details of your schedule. In each section, choose **Edit** to go back to that step and edit its details. 

1. Choose **Create schedule**. 

   You can view a list of your new and existing schedules on the **Schedules** page. Under the **Status** column, verify that your new schedule is **Enabled**. 

To confirm that EventBridge Scheduler invoked the function, [check the function's Amazon CloudWatch logs](monitoring-cloudwatchlogs-view.md#monitoring-cloudwatchlogs-console).

## Related resources
<a name="using-eventbridge-scheduler-related-resources"></a>

 For more information about EventBridge Scheduler, see the following: 
+ [EventBridge Scheduler User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)
+ [EventBridge Scheduler API Reference](https://docs.aws.amazon.com/scheduler/latest/APIReference/Welcome.html)
+ [EventBridge Scheduler Pricing](https://aws.amazon.com/eventbridge/pricing/#Scheduler)