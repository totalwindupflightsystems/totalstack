---
id: "@specs/aws/lightsail/docs/lightsail-how-to-create-instance-from-snapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create an instance from a snapshot"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Create an instance from a snapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/lightsail-how-to-create-instance-from-snapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create Lightsail instances from snapshots
<a name="lightsail-how-to-create-instance-from-snapshot"></a>

After you create a snapshot in Lightsail, you can create a new instance from that snapshot. You can change attributes of the new instance, such as instance size and networking type – dual-stack or IPv6-only. The new instance includes the system disk and the attached block storage disks that you added.

You must have a snapshot of an instance before you can create another instance from that snapshot. For more information, see [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md) or [Create a snapshot of your Lightsail Windows Server instance](prepare-windows-based-instance-and-create-snapshot.md).

1. On the Lightsail console, choose the instance that you want to snapshot to create a new instance.

1. Choose the **Snapshots** tab.

1. In the **Manual snapshots** section, choose the actions menu icon (⋮) next to the snapshot and choose **Create new instance**.  
![The Manage snapshots menu showing the cursor choosing Create new instance.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-create-new-linux-unix-based-lightsail-instance-from-snapshot.png)

1. The **Create an instance from a snapshot** page opens. Choose the optional settings that you want to use. For example, you can change the Availability Zone, [add a launch script](lightsail-how-to-configure-server-additional-data-shell-script.md), or [change the way you connect to your instance](understanding-ssh-in-amazon-lightsail.md).

1. Choose a plan (or *bundle*) for your new instance. You can choose to create an instance that uses a dual-stack (IPv4 and IPv6) instance plan, or an IPv6-only plan. You can also choose a larger bundle size than that of the original instance. For more information about IPv6-only instance plans, see [Configure IPv6-only networking for Lightsail instances](amazon-lightsail-ipv6-only-plans.md).
**Note**  
You can't create an instance that uses a smaller bundle size than that of the original instance.  
![The Choose a new instance plan page showing dual stack and IPv6 address types.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-plan-area.png)

1. Enter a name for your instance.

   Resource names:
   + Must be unique within each AWS Region of your Lightsail account.
   + Must contain 2–255 characters.
   + Must start and end with an alphanumeric character.
   + Can include alphanumeric characters, periods, dashes, and underscores.

1. (Optional) Choose **Add new tag** to add a tag to your instance. Repeat this step as needed to add additional tags. For more information on tag usage, see [Tags](amazon-lightsail-tags.md).

   1. For **Key**, enter a tag key.  
![A tag with only the tag key specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-only-tags.png)

   1. (Optional) For **Value**, enter a tag value.  
![A tag with the tag key and tag value specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-and-value-tags.png)

1. Choose **Create instance**.

   Lightsail opens the management page, where you can manage your new instance.
**Important**  
Custom firewall rules from the original instance don't copy over to the new instance that you create from a snapshot. Only the default rules copy over to the new instance. For more information, see [Default instance firewall rules](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-firewall-and-port-mappings-in-amazon-lightsail#default-lightsail-firewall-rules).