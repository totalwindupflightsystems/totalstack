---
id: "@specs/aws/lightsail/docs/getting-started-with-amazon-lightsail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Linux instances"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Linux instances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/getting-started-with-amazon-lightsail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create Linux/Unix instances with apps on Lightsail
<a name="getting-started-with-amazon-lightsail"></a>

**Did you know?**  
 Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable automatic snapshots for your instance. For more information, see [ Configure automatic snapshots for Lightsail instances and disks ](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html) . 

Create a Linux/Unix-based Amazon Lightsail instance (a virtual private server) running an application like WordPress or a development stack like LAMP. After your instance starts running, you can connect to it via SSH without leaving Lightsail. Here's how.

To create a Windows-based instance, see [Get started with Windows-based instances in Amazon Lightsail](get-started-with-windows-based-instances-in-lightsail.md).

## Create a Linux-based instance
<a name="getting-started-create-an-instance"></a>

1. On the home page, choose **Create instance**.

1. Select a location for your instance (an AWS Region and Availability Zone).

   Choose **Change AWS Region and Availability Zone** to create your instance in another location.

1. Optionally, you can change the Availability Zone.

   Choose **Change your Availability Zone**.

1. Choose the Linux platform.

1. Pick an application (**Apps \+ OS**) or an operating system (**OS Only**).

   To learn more about Lightsail instance images, see [Choose an Amazon Lightsail instance image](compare-options-choose-lightsail-instance-image.md).

1. Choose your instance plan.

   Choose whether your instance uses dual-stack (IPv4 and IPv6), or IPv6-only networking. Some Lightsail blueprints don't support IPv6-only networking at this time. To see which blueprints support IPv6-only networking see [Review the Lightsail instance blueprint offerings](compare-options-choose-lightsail-instance-image.md).

   You can try the $5 USD Lightsail plan free for one month (up to 750 hours). We will credit one free month to your account. Learn more on our [Lightsail pricing page](http://www.amazonlightsail.com/pricing/).
**Note**  
As part of the AWS Free Tier, you can get started with Amazon Lightsail for free on select instance bundles. For more information, see **AWS Free Tier** on the [Amazon Lightsail Pricing page](https://aws.amazon.com/lightsail/pricing).

1. Enter a name for your instance.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. (Optional) Choose **Add new tag** to add a tag to your instance. Repeat this step as needed to add additional tags. For more information on tag usage, see [Tags](amazon-lightsail-tags.md).

   1. For **Key**, enter a tag key.  
![A tag with only the tag key specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-only-tags.png)

   1. (Optional) For **Value**, enter a tag value.  
![A tag with the tag key and tag value specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-and-value-tags.png)

1. Choose **Create instance**.

   For advanced creation options, see [Use a launch script to configure your Amazon Lightsail instance when it starts up](lightsail-how-to-configure-server-additional-data-shell-script.md) or [Set up SSH for your Linux/Unix-based Lightsail instances](lightsail-how-to-set-up-ssh.md).

Within minutes, your Lightsail instance is ready and you can connect to it via SSH, without leaving Lightsail\!

## Connect to your instance
<a name="getting-started-connect-to-your-instance"></a>

1. On the Lightsail home page, choose the menu on the right of your instance's name, and then choose **Connect**.  
![Instance connect.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-connect-to-your-instance.png)

   Alternately, you can open your instance management page, choose the **Connect** tab, then choose **Connect using SSH**.  
![Instance connect.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-connect-to-your-instance-from-instance-management-page.png)
**Note**  
To connect to your instance using an SSH client such as PuTTY, you can follow this procedure: [Set up PuTTY to connect to your Lightsail instance](lightsail-how-to-set-up-putty-to-connect-using-ssh.md).

1. Now you can type commands into the terminal and manage your Lightsail instance without setting up an SSH client.  
![Browser-based SSH terminal.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-bitnami-terminal-window.png)

## Next steps
<a name="linux-unix-next-steps"></a>

Now that you can connect to your instance, what you do next depends on how you plan to use it. For example:
+ [WordPress](amazon-lightsail-wordpress.md) if you're creating a blog.
+ [Create a static IP address](lightsail-create-static-ip.md) for your instance to keep the same IP address each time you restart your Lightsail instance.
+ [Create a snapshot of your instance](lightsail-how-to-create-a-snapshot-of-your-instance.md) as a backup.