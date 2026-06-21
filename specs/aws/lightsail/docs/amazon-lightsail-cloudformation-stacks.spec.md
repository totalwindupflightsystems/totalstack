---
id: "@specs/aws/lightsail/docs/amazon-lightsail-cloudformation-stacks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudFormation stacks"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# CloudFormation stacks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-cloudformation-stacks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View CloudFormation stacks for Lightsail instances
<a name="amazon-lightsail-cloudformation-stacks"></a>

Amazon Lightsail uses CloudFormation to create Amazon Elastic Compute Cloud (Amazon EC2) instances from exported snapshots. A CloudFormation stack is created when you request to create an Amazon EC2 instance using the Lightsail console or Lightsail API. The stack performs a series of actions in your Amazon Web Services (AWS) account to create all of the related resources for the instance, such as the Amazon EC2 instance from an Amazon Machine Image (AMI), the Elastic Block Store (EBS) system volume from an EBS snapshot, and the security group for the instance. To learn more about CloudFormation stacks, see [Working with Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the CloudFormation documentation.

You can access the CloudFormation stacks through the Lightsail console or in the CloudFormation console. This guide shows you how to access both.

**Note**  
The CloudFormation stack used to create your Amazon EC2 resources is permanently linked to your Amazon EC2 resources. If you delete the stack, then all related resources are automatically deleted. Because of this, you should not delete any of the CloudFormation stacks created by Lightsail, and instead delete your Amazon EC2 resources using the EC2 console.

## Accessing the CloudFormation stacks through the Lightsail console
<a name="accessing-the-cloud-formation-stack"></a>

After you choose to create an instance in Amazon EC2 using the Lightsail console or the Lightsail API, an CloudFormation stack is created and its status is tracked in the **Exports** section of the Lightsail console.. To learn more about **Exports**, see [Track snapshot export status in Lightsail](amazon-lightsail-task-monitor.md).

**To view your CloudFormation stacks in the Lightsail console**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose **Exports** in the left navigation pane.

1. To access a CloudFormation stack for a previously created Amazon EC2 instance, choose **View details** for a task labeled with **Created EC2 resources**.  
![The task history in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-task-manager-cloud-formation-stack.png)

1. The confirmation page that appears lists the CloudFormation stack for the task. Choose the stack name to open the stack details in the CloudFormation console.

## Accessing the stacks in the CloudFormation console
<a name="accessing-the-stacks-in-the-cloud-formation-console"></a>

You can also access your stack details through the [CloudFormation console](https://console.aws.amazon.com/cloudformation). The stacks created by Lightsail begin with “Lightsail-stack” and have a description of “CloudFormation stack used to create Amazon EC2 resources” as shown in the following screenshot.

Stacks with a **CREATE\_IN\_PROGRESS** status are in the process of creating Amazon EC2 resources from your exported Lightsail snapshots. Stacks with a **CREATE\_COMPLETED** status have completed the process of creating Amazon EC2 resources. To view the resources created by a stack, choose the checkbox next to the stack name, and then choose the **Resources** tab.

![CloudFormation stack details.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-cloud-formation-stack-details.png)
