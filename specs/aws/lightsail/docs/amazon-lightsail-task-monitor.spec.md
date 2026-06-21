---
id: "@specs/aws/lightsail/docs/amazon-lightsail-task-monitor"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitor exports"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Monitor exports

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-task-monitor
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Track snapshot export status in Lightsail
<a name="amazon-lightsail-task-monitor"></a>

The **Exports** section on the Amazon Lightsail console, is where you can track the status of exporting Lightsail snapshots to Amazon EC2, or creating new EC2 instances from exported instance snapshots. Export tasks can take a while depending on the size and configuration of the source instance or block storage disk. **Exports** can be accessed from the left navigation pane on all pages of the Lightsail console.

![The exports section of the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-task-monitor.png)


For more information about exporting Lightsail snapshots to Amazon EC2, or creating EC2 instances from exported snapshots, see the following guides:
+ [Export snapshots to Amazon EC2](amazon-lightsail-exporting-snapshots-to-amazon-ec2.md)
+ [Create Amazon EC2 instances from exported snapshots](amazon-lightsail-creating-ec2-instances-from-exported-snapshots.md)