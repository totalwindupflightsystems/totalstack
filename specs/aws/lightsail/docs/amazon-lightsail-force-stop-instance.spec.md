---
id: "@specs/aws/lightsail/docs/amazon-lightsail-force-stop-instance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Force stop instances"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Force stop instances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-force-stop-instance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Force stop stuck Lightsail instances
<a name="amazon-lightsail-force-stop-instance"></a>

Rarely, an instance can get stuck in the `Stopping` state. If this happens, there might be an issue with the underlying hardware that hosts your Amazon Lightsail instance. In this guide, you’ll learn how to force stop an instance that's stuck in the `stopping` state. For more information about instance states, see [Start, Stop, or Restart your Lightsail instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md). 

## How to force stop an instance
<a name="force-stop"></a>

You can use the Lightsail console to force stop your instance, but only while the instance is in the `stopping` state. Alternatively, you can use the AWS Command Line Interface (AWS CLI) to force stop an instance while the instance is in any state except `shutting-down` and `terminated`. A force stop can take a few minutes to complete. If the instance hasn’t stopped after 10 minutes, force stop it again.

When an instance is forced to stop, it doesn't have an opportunity to flush file system caches or file system metadata. After you force stop an instance, you should perform file system checks and repair procedures.

The following procedure explains the different ways that you can force stop a Lightsail instance.

**Force stop an instance in the Lightsail console**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Instances** tab.

1. Locate the instance that's stuck in the `Stopping` state. Then, choose the actions menu icon (⋮) displayed next to the instance name.  
![Lightsail instance actions menu.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-force-stop-actions-menu.png)

1. Choose **Force stop** in the dropdown list that appears.  
![Lightsail instance actions menu force stop option.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-force-stop-choose-am-option.png)

   Alternatively, you can choose the instance name to access the instance management page. Then, choose the **Force stop** button.  
![Lightsail instance management page force stop button.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-force-stop-button-instance.png)

1. Review the considerations for this operation. To proceed, choose **Force stop**.  
![Lightsail instance management page force stop button.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-force-stop-considerations-modal.png)

**Force stop an instance with the AWS CLI**

1. Before you begin, you need to install the AWS CLI. To learn more, see [Installing the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/installing.html). Be sure to [configure the AWS CLI](lightsail-how-to-set-up-and-configure-aws-cli.md) after you install it.

1. Use the [stop-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-instance.html) command and the `--force` parameter as follows:

   `aws lightsail stop-instance --instance-name {{Wordpress-1}} --force`